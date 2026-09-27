# Per-year and per-month driver attribution for an industry basket.
import json,sys,datetime,statistics
P=json.load(open('prices.json')); R=json.load(open('roster.json',encoding='utf-8'))
no=sys.argv[1]; D=json.load(open(f'data_{no}.json'))
names={m['co']:m['sym'] for m in R[no]['members']}
syms=[(c,names[c]) for c in D['basket'] if c in names]
def yearly(sym):
    last={}
    for t,c in P[sym]:
        y=datetime.datetime.fromtimestamp(t).year; last[y]=c
    return {y:(last[y]/last[y-1]-1)*100 for y in last if y-1 in last}
def monthly(sym):
    last={}
    for t,c in P[sym]:
        d=datetime.datetime.fromtimestamp(t); last[(d.year,d.month)]=c
    ks=sorted(last); return {ks[i]:(last[ks[i]]/last[ks[i-1]]-1)*100 for i in range(1,len(ks))}
Y={c:yearly(s) for c,s in syms}; M={c:monthly(s) for c,s in syms}
print('BASKET',len(syms),'names')
for c in D['cy']:
    y=c['y']; r=sorted([(Y[n][y],n) for n in Y if y in Y[n]],reverse=True)
    top=', '.join(f"{n[:18]} {v:+.0f}" for v,n in r[:3]); bot=', '.join(f"{n[:18]} {v:+.0f}" for v,n in r[-3:]) if len(r)>3 else ''
    print(f"{y}: basket {c['b']:+.0f} nifty {c['n']:+.0f} rel {c['rel']:+.0f} | n={len(r)} median {statistics.median([v for v,_ in r]) if r else 0:+.0f} | TOP {top} | BOTTOM {bot}")
mo=sorted(D['monthly'],key=lambda m:-m['rel'])
for m in [mo[0],mo[1],mo[-1]]:
    k=str(m['m']); vals=D['my'][k]
    ex=sorted(vals.items(),key=lambda kv:kv[1])
    print(f"MONTH {m['m']} avg {m['rel']:+.1f} ({m['hit']}/{m['n']}): worst years {ex[:3]} best years {ex[-3:]}")
for w,v in D['win'].items():
    ys=D['wy'][w]; neg=[(x['y'],x['v']) for x in ys if x['v']<0]; big=sorted(ys,key=lambda x:-x['v'])[:2]
    print(f"WIN {w}: hit {v['hit']}/{v['n']} median {v['median']:+} | negative years {neg} | biggest {[(x['y'],x['v']) for x in big]}")
