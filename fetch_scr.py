import json, time, os, re, requests, threading, html
from concurrent.futures import ThreadPoolExecutor
base=json.load(open('base.json'))
out=json.load(open('scr.json')) if os.path.exists('scr.json') else {}
lock=threading.Lock()
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}
def parse(t):
    m=re.findall(r'<a href="/market/[^"]+"[^>]*>([^<]+)</a>',t)
    about=re.search(r'class="sub show-more-box about"[^>]*>(.*?)</div>',t,re.S)
    kp=re.search(r'<div class="commentary always-show-more"[^>]*>(.*?)</div>',t,re.S)
    h1=re.search(r'<h1[^>]*>(.*?)</h1>',t,re.S)
    clean=lambda s: html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',s))).strip()
    return {'cls':[html.unescape(x) for x in m[:4]],'about':clean(about.group(1))[:600] if about else None,
            'keypoints':clean(kp.group(1))[:900] if kp else None,'name':clean(h1.group(1)) if h1 else None}
def get(slug):
    for a in range(5):
        try:
            r=requests.get(f'https://www.screener.in/company/{slug}/',headers=H,timeout=25)
            if r.status_code==429: time.sleep(10*(a+1)); continue
            if r.status_code==404: return 404
            if r.status_code!=200: time.sleep(3); continue
            return parse(r.text)
        except Exception: time.sleep(3*(a+1))
    return None
def job(x):
    sym=x['sym']; ex,tk=sym.split(':')
    slugs=[]
    if ex=='NSE': slugs.append(tk)
    if x.get('bse_code'): slugs.append(x['bse_code'])
    if ex=='BSE': slugs.append(tk)
    res=None
    for sl in slugs:
        r=get(sl)
        if isinstance(r,dict) and (r['cls'] or r['about']): res=r; res['slug']=sl; break
        time.sleep(0.4)
    with lock:
        out[sym]=res
        if len(out)%50==0:
            json.dump(out,open('scr.json','w')); print(len(out),time.strftime('%H:%M:%S'),flush=True)
    time.sleep(0.3)
import sys
only=set(json.load(open(sys.argv[1]))) if len(sys.argv)>1 else None
todo=[x for x in base if (only is None or x['sym'] in only) and not (out.get(x['sym']) and out[x['sym']].get('about'))]
print('todo',len(todo),flush=True)
with ThreadPoolExecutor(5) as ex: list(ex.map(job,todo))
json.dump(out,open('scr.json','w'))
print('DONE',len(out),sum(1 for v in out.values() if v),flush=True)
