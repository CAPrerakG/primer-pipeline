import sys, json, datetime, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from tv_fetch import fetch
from concurrent.futures import ThreadPoolExecutor
P=json.load(open('b1/prices.json')); R=json.load(open('b1/roster.json'))
bl={x['ISIN_NUMBER']:x for x in json.load(open('bse_list.json',encoding='utf-8'))}
base={x['sym']:x for x in json.load(open('base.json',encoding='utf-8'))}
todo=[]
SEL=set(sys.argv[1:])
for no,v in R.items():
    if SEL and no not in SEL: continue
    for m in v['members']:
        s=m['sym']; x=P.get(s)
        if not s.startswith('NSE:'): continue
        st=datetime.datetime.fromtimestamp(x[0][0]) if x else None
        if x and st.year<2019: continue
        isin=(base.get(s) or {}).get('isin')
        b=bl.get(isin)
        if b and b.get('scrip_id'): todo.append((s,'BSE:'+b['scrip_id']))
print('todo',len(todo))
res={}
def job(t):
    s,b=t
    for a in range(3):
        try:
            rows,meta=fetch(b,"1D",5000,timeout=60); res[s]=(b,[[r[0],r[4]] for r in rows]); return
        except Exception as e: time.sleep(2)
    res[s]=(b,None)
with ThreadPoolExecutor(4) as ex: list(ex.map(job,todo))
json.dump(res,open('b1/bse_raw.json','w'))
log=[]
for s,(b,rows) in res.items():
    x=P.get(s)
    if not rows: log.append((s,b,'no BSE data')); continue
    if not x: P[s]=rows; log.append((s,b,'NSE missing -> BSE only',len(rows))); continue
    n0=x[0][0]; b0=rows[0][0]
    if b0 < n0-60*86400:
        # scale BSE to NSE on first NSE day
        bmap={int(r[0]//86400):r[1] for r in rows}
        d0=int(n0//86400); ref=None
        for k in range(0,6):
            if d0-k in bmap: ref=bmap[d0-k]; break
        f=x[0][1]/ref if ref else 1.0
        pre=[[r[0],r[1]*f] for r in rows if r[0]<n0]
        P[s]=pre+x
        log.append((s,b,'spliced',datetime.datetime.fromtimestamp(b0).date().isoformat(),round(f,3)))
    else: log.append((s,b,'BSE not longer'))
json.dump(P,open('b1/prices.json','w'))
for l in log: print(l)
