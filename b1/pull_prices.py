import sys, json, os, time, threading
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from tv_fetch import fetch
syms=json.load(open('b1/syms.json'))+["NSE:NIFTY","NSE:CNXAUTO","NSE:CNXSMALLCAP"]
out=json.load(open('b1/prices.json')) if os.path.exists('b1/prices.json') else {}
lock=threading.Lock()
def job(s):
    if s in out: return
    for a in range(3):
        try:
            rows,meta=fetch(s,"1D",5000,timeout=60)
            with lock:
                out[s]=[[r[0],r[4]] for r in rows]
                if len(out)%25==0:
                    json.dump(out,open('b1/prices.json','w')); print(len(out),time.strftime('%H:%M:%S'),flush=True)
            return
        except Exception as e:
            time.sleep(2)
    with lock: out[s]=None
with ThreadPoolExecutor(4) as ex: list(ex.map(job,syms))
json.dump(out,open('b1/prices.json','w'))
print('DONE',len(out),sum(1 for v in out.values() if v),flush=True)
