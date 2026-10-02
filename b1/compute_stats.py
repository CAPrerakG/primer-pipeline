import json, sys, pandas as pd, numpy as np
CUT=1789776000  # project data date: bars up to and including 18-Sep-2026 (UTC)
P=json.load(open('b1/prices.json')); P={k:[r for r in v if r[0]<CUT] for k,v in P.items() if v}; R=json.load(open('b1/roster.json'))
def ser(s):
    v=P.get(s)
    if not v: return None
    x=pd.Series({pd.Timestamp(t,unit='s').normalize():c for t,c in v}).sort_index()
    return x[~x.index.duplicated()]
nifty=ser('NSE:NIFTY'); nm=nifty.resample('ME').last().pct_change()
comp=lambda x:(1+x).prod()-1
END=pd.Timestamp('2026-09-18')
for no,v in R.items():
    if len(sys.argv)>1 and no not in sys.argv[1:]: continue
    EXCL={'BSE:SOUTLAT'}  # shells with no operations
    mem=[m for m in v['members'] if P.get(m['sym']) and m['sym'] not in EXCL]
    # basket: mcap>=300cr and >=24 months history; fallback top by mcap
    cand=[]
    for m in mem:
        s=ser(m['sym']); 
        if s is None or len(s)<250: continue
        if v.get('start',{}).get(m['sym']): s=s[s.index>=v['start'][m['sym']]]  # documented per-member entry date (e.g. after illiquid SME gaps)
        cand.append((m,s))
    big=[(m,s) for m,s in cand if (m['mcap'] or 0)>=3e9]
    use=big if len(big)>=3 else sorted(cand,key=lambda x:-(x[0]['mcap'] or 0))[:6]
    if v.get('basket_syms'): use=[(m,s) for m,s in cand if m['sym'] in v['basket_syms']]  # manual override (misclassified or illiquid members excluded)
    if not use: print(no,'NO DATA'); json.dump({},open(f'b1/data_{no}.json','w')); continue
    mr=pd.DataFrame({m['sym']:s.resample('ME').last().pct_change(fill_method=None) for m,s in use}).clip(-0.5,0.5)
    b=mr.mean(axis=1,skipna=True); cnt=mr.notna().sum(axis=1)
    df=pd.DataFrame({'b':b,'n':nm,'c':cnt}).dropna(subset=['b','n'])
    df=df[df.c>=2] if len(use)>=4 else df
    df=df[df.index>='2011-07-31']
    full=df[df.index<'2026-09-01']; full=full.assign(rel=full.b-full.n)
    g=full.groupby(full.index.month)
    monthly=[{'m':int(m),'abs':round(g.b.mean()[m]*100,1),'rel':round(g.rel.mean()[m]*100,1),'hit':int((g.rel.apply(lambda x:(x>0).sum()))[m]),'n':int(g.rel.count()[m])} for m in range(1,13) if m in g.b.mean().index]
    cy=[]
    for y in range(max(2012,df.index[0].year+ (0 if df.index[0].month==1 else 1)),2027):
        x=df[(df.index>=f'{y}-01-01')&(df.index<=f'{y}-12-31')]
        if len(x)<6 and y<2026: continue
        cb,cn=comp(x.b)*100,comp(x.n)*100
        cy.append({'y':y,'b':round(cb,1),'n':round(cn,1),'rel':round(cb-cn,1),'partial':y==2026})
    dd=[]
    for m in sorted(mem,key=lambda x:-(x['mcap'] or 0))[:18]:
        s=ser(m['sym'])
        if s is None or len(s)<60: continue
        pk=s['2020-01-01':'2025-12-31']
        if len(pk)==0: continue
        last=s.iloc[-1]; prior=s[:s.index[-1]-pd.Timedelta(days=365)]
        y1=round((last/prior.iloc[-1]-1)*100) if len(prior) else 0
        dd.append({'co':m['co'].replace(' Limited','').replace(' Ltd.','').replace(' Ltd',''),'peak':pk.idxmax().strftime('%b %Y'),'fp':int(round((last/pk.max()-1)*100)),'y1':int(y1)})
    # window stats
    win={}; wy={}
    for a,bm,lab in [(2,3,'FebMar'),(4,7,'AprJul'),(8,9,'AugSep'),(10,12,'OctDec'),(9,11,'SepNov'),(1,3,'JanMar')]:
        vals=[]; wyv=[]
        for y in range(2012,2027):
            x=full[(full.index.year==y)&(full.index.month>=a)&(full.index.month<=bm)]
            if len(x)==bm-a+1: vals.append((comp(x.b)-comp(x.n))*100); wyv.append((y,(comp(x.b)-comp(x.n))*100))
        if vals: win[lab]={'mean':round(np.mean(vals),1),'median':round(np.median(vals),1),'hit':int(sum(v>0 for v in vals)),'n':len(vals)}
        wy[lab]=[{'y':yy,'v':round(vv,1)} for yy,vv in wyv]
    ytd=df[df.index>='2026-01-01']
    my={int(m):{int(i.year):round(r*100,1) for i,r in g2.rel.items()} for m,g2 in full.groupby(full.index.month)}
    out={'wy':wy,'my':my,'basket':[m['co'] for m,s in use],'nbasket':len(use),'start':df.index[0].strftime('%b %Y'),'monthly':monthly,'cy':cy,'dd':dd,'win':win,
         'ytd':{'b':round(comp(ytd.b)*100,1),'n':round(comp(ytd.n)*100,1)}}
    json.dump(out,open(f'b1/data_{no}.json','w'))
    best=sorted(monthly,key=lambda m:-m['rel'])[:3]; worst=sorted(monthly,key=lambda m:m['rel'])[:3]
    print(no,v['ind'],'basket',len(use),'from',out['start'],'| best',[(m['m'],m['rel'],f"{m['hit']}/{m['n']}") for m in best],'| worst',[(m['m'],m['rel'],f"{m['hit']}/{m['n']}") for m in worst],'| win',win,'| ytd',out['ytd'])
