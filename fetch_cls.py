import json, time, os, requests, threading
from concurrent.futures import ThreadPoolExecutor
base=json.load(open('base.json'))
out=json.load(open('cls.json')) if os.path.exists('cls.json') else {}
lock=threading.Lock()
HB={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36','Referer':'https://www.bseindia.com/','Origin':'https://www.bseindia.com'}
def bse(code):
    for a in range(4):
        try:
            r=requests.get(f'https://api.bseindia.com/BseIndiaAPI/api/ComHeadernew/w?quotetype=EQ&scripcode={code}&seriesid=',headers=HB,timeout=20)
            j=r.json(); return {'src':'BSE','macro':j.get('Sector'),'sector':j.get('IndustryNew'),'industry':j.get('IGroup'),'basic':j.get('ISubGroup')}
        except Exception as e: time.sleep(1.5*(a+1))
    return None
todo=[x for x in base if x['bse_code'] and x['sym'] not in out]
print('BSE todo',len(todo),flush=True)
def job(x):
    res=bse(x['bse_code'])
    with lock:
        out[x['sym']]=res
        if len(out)%250==0:
            json.dump(out,open('cls.json','w')); print(len(out),flush=True)
with ThreadPoolExecutor(6) as ex: list(ex.map(job,todo))
json.dump(out,open('cls.json','w'))
# NSE-only
s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36','Accept':'application/json,text/plain,*/*','Referer':'https://www.nseindia.com/'})
s.get('https://www.nseindia.com/',timeout=20)
todo=[x for x in base if not x['bse_code'] and x['sym'].startswith('NSE:') and x['sym'] not in out]
print('NSE todo',len(todo),flush=True)
for i,x in enumerate(todo):
    sym=x['sym'][4:]
    res=None
    for a in range(3):
        try:
            r=s.get('https://www.nseindia.com/api/quote-equity',params={'symbol':sym},timeout=20)
            if r.status_code==401 or r.status_code==403:
                s.get('https://www.nseindia.com/',timeout=20); time.sleep(1); continue
            j=r.json(); ii=j.get('industryInfo') or {}
            res={'src':'NSE','macro':ii.get('macro'),'sector':ii.get('sector'),'industry':ii.get('industry'),'basic':ii.get('basicIndustry'),'series':(j.get('metadata') or {}).get('series')}
            break
        except Exception as e: time.sleep(2)
    out[x['sym']]=res
    time.sleep(0.35)
    if i%50==0: json.dump(out,open('cls.json','w')); print('nse',i,flush=True)
json.dump(out,open('cls.json','w'))
print('DONE',len(out),sum(1 for v in out.values() if v and v.get('basic')))
