import json, time, requests
base=json.load(open('base.json'))
out={}
s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36','Accept':'application/json,text/plain,*/*','Referer':'https://www.nseindia.com/get-quotes/equity'})
s.get('https://www.nseindia.com/',timeout=20)
todo=[x for x in base if not x['bse_code'] and x['sym'].startswith('NSE:')]
print('NSE todo',len(todo),flush=True)
for i,x in enumerate(todo):
    sym=x['sym'][4:]; res=None
    for a in range(3):
        try:
            r=s.get('https://www.nseindia.com/api/quote-equity',params={'symbol':sym},timeout=20)
            if r.status_code in (401,403):
                s.get('https://www.nseindia.com/',timeout=20); time.sleep(1.5); continue
            j=r.json(); ii=j.get('industryInfo') or {}
            res={'src':'NSE','macro':ii.get('macro'),'sector':ii.get('sector'),'industry':ii.get('industry'),'basic':ii.get('basicIndustry'),'series':(j.get('metadata') or {}).get('series'),'nse_name':(j.get('info') or {}).get('companyName')}
            break
        except Exception as e:
            time.sleep(2)
    out[x['sym']]=res
    time.sleep(0.3)
    if i%50==0: json.dump(out,open('cls_nse.json','w')); print('nse',i,flush=True)
json.dump(out,open('cls_nse.json','w'))
print('DONE',len(out),sum(1 for v in out.values() if v and v.get('basic')),flush=True)
