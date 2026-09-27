# Fetch driver series from TradingView and compute calendar-year averages.
import sys,json,os,datetime
sys.path.insert(0, r"C:/Users/sayoni.n/OneDrive - SOWILO INVESTMENT MANAGERS LLP/Info's files - Research/Research Stocks & Sectors-Prerak/Claude-Backtest")
from tv_fetch import fetch
f='series.json'; S=json.load(open(f)) if os.path.exists(f) else {}
for sym in sys.argv[1:]:
    if sym not in S:
        try:
            rows,meta=fetch(sym,"1D",5000,timeout=60); S[sym]=[[r[0],r[4]] for r in rows]
        except Exception as e: print(sym,'ERR',e); continue
    ys={}
    for t,c in S[sym]:
        ys.setdefault(datetime.datetime.fromtimestamp(t).year,[]).append(c)
    print(sym, len(S[sym]), ' '.join(f"{y}:{sum(v)/len(v):.1f}" for y,v in sorted(ys.items()) if y>=2012), '| last', S[sym][-1][1], datetime.datetime.fromtimestamp(S[sym][-1][0]).date())
json.dump(S,open(f,'w'))
