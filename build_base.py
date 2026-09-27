import json, openpyxl
wb=openpyxl.load_workbook(r'C:/Users/sayoni.n/Desktop/Industry-wise stocks.xlsx',read_only=True)
rows=[r for r in list(wb['Industry-wise stocks'].iter_rows(values_only=True))[1:] if r[2]]
tv={d['s']:d['d'] for d in json.load(open('tv_scan.json'))['data']}
bse=json.load(open('bse_list.json'))
isin2bse={}
for b in bse:
    if b['ISIN_NUMBER']: isin2bse.setdefault(b['ISIN_NUMBER'],b)
id2bse={b['scrip_id']:b for b in bse}
base=[]
miss=0
for r in rows:
    ind,co,sym,wl=r[0].strip(),r[1],r[2].strip(),r[3]
    t=tv.get(sym)
    isin=t[7] if t else None
    b=isin2bse.get(isin) if isin else None
    if not b and sym.startswith('BSE:'): b=id2bse.get(sym[4:])
    if not t: miss+=1
    base.append({'ind':ind,'co':co,'sym':sym,'wl':wl,'tv_name':t[1] if t else None,'tv_sector':t[2] if t else None,'tv_ind':t[3] if t else None,
                 'mcap':t[5] if t else None,'isin':isin,'bse_code':b['SCRIP_CD'] if b else None})
json.dump(base,open('base.json','w'))
print(len(base),'rows; not in TV scan:',miss,'; with BSE code:',sum(1 for x in base if x['bse_code']),'; NSE-only:',sum(1 for x in base if not x['bse_code']))
