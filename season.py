import json, pandas as pd, numpy as np
d = json.load(open("agro_daily.json"))
s = {k: pd.Series({pd.Timestamp(t, unit='s').normalize(): c for t, c in v}) for k, v in d.items()}
px = pd.DataFrame(s).sort_index()
m = px.resample('ME').last()
r = m.pct_change(fill_method=None)
core = ["NSE:UPL","NSE:PIIND","NSE:RALLIS","NSE:DHANUKA","NSE:BAYERCROP","NSE:INSECTICID","NSE:BHARATRAS","NSE:EXCELINDUS","NSE:PUNJABCHEM","NSE:ASTEC","NSE:SHARDACROP","NSE:NACLIND","NSE:SUMICHEM","NSE:HERANBA","NSE:IPL","NSE:BHAGCHEM","NSE:DHARMAJ","NSE:BESTAGRO","NSE:MOL"]
# equal-weight basket monthly return (rebalanced monthly), using names with data both months
bask = r[core].mean(axis=1, skipna=True)
cnt = r[core].notna().sum(axis=1)
nifty = r["NSE:NIFTY"]; small = r["NSE:CNXSMALLCAP"]
df = pd.DataFrame({"agro":bask,"n":cnt,"nifty":nifty,"small":small}).dropna(subset=["agro","nifty"])
df = df[df.index >= "2011-07-31"]
df["rel"] = df.agro - df.nifty
df["rel_s"] = df.agro - df.small
print("months", len(df), df.index[0].date(), df.index[-1].date())
print("constituents per month min/median/max", df.n.min(), df.n.median(), df.n.max())
full = df[df.index < "2026-09-01"]
g = full.groupby(full.index.month)
tab = pd.DataFrame({"agro_avg%":g.agro.mean()*100,"agro_med%":g.agro.median()*100,"rel_nifty_avg%":g.rel.mean()*100,
                    "hit_rel>0":g.rel.apply(lambda x:(x>0).mean()),"rel_small_avg%":g.rel_s.mean()*100,"yrs":g.agro.count()})
print(tab.round(2))
# window by year: Apr-Sep vs Oct-Mar (fiscal), compounded
def comp(x): return (1+x).prod()-1
rows=[]
for y in range(2012, 2027):
    w1 = full[(full.index>=f"{y}-04-01")&(full.index<=f"{y}-09-30")]
    w0 = full[(full.index>=f"{y-1}-10-01")&(full.index<=f"{y}-03-31")]
    if len(w1)==0: continue
    rows.append({"yr":y,"AprSep_agro%":comp(w1.agro)*100,"AprSep_nifty%":comp(w1.nifty)*100,"AprSep_small%":comp(w1.small)*100,
                 "prevOctMar_agro%":comp(w0.agro)*100 if len(w0) else np.nan,"prevOctMar_nifty%":comp(w0.nifty)*100 if len(w0) else np.nan, "m":len(w1)})
W = pd.DataFrame(rows).set_index("yr")
W["AprSep_rel"] = W["AprSep_agro%"]-W["AprSep_nifty%"]
W["AprSep_rel_small"] = W["AprSep_agro%"]-W["AprSep_small%"]
print(W.round(1))
# calendar/fiscal year returns
yr=[]
for y in range(2012, 2027):
    x = full[(full.index>=f"{y}-01-01")&(full.index<=f"{y}-12-31")]
    yr.append({"cy":y,"agro%":comp(x.agro)*100,"nifty%":comp(x.nifty)*100,"small%":comp(x.small)*100,"m":len(x)})
Y=pd.DataFrame(yr).set_index("cy"); Y["rel"]=Y["agro%"]-Y["nifty%"]; print(Y.round(1))
# individual stock drawdowns from 2021-22 peak
for k in core+["NSE:COROMANDEL","NSE:CHAMBLFERT","NSE:NIFTY"]:
    p = px[k].dropna()
    if p.index[0] > pd.Timestamp("2021-06-01"): 
        pk = p[:"2023-12-31"]
    else: pk = p["2020-01-01":"2023-12-31"]
    if len(pk)==0: continue
    pkd = pk.idxmax(); tr = p[pkd:].min(); trd = p[pkd:].idxmin()
    print(f"{k:16s} peak {pkd.date()} {pk.max():9.1f} trough {trd.date()} {tr:9.1f} dd {100*(tr/pk.max()-1):6.1f}% last {p.iloc[-1]:9.1f} vs peak {100*(p.iloc[-1]/pk.max()-1):6.1f}%  1y {100*(p.iloc[-1]/p[:p.index[-1]-pd.Timedelta(days=365)].iloc[-1]-1):6.1f}%")
df.to_csv("agro_monthly.csv")
