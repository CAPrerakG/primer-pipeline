import os
import sys, json, time, datetime as dt
sys.path.insert(0, os.environ.get("PIPELINE_ROOT", os.path.dirname(os.path.abspath(__file__))))
from tv_fetch import fetch
syms = ["NSE:NIFTY","NSE:CNXSMALLCAP","NSE:UPL","NSE:PIIND","NSE:RALLIS","NSE:DHANUKA","NSE:BAYERCROP","NSE:SHARDACROP",
        "NSE:INSECTICID","NSE:BHARATRAS","NSE:EXCELINDUS","NSE:PUNJABCHEM","NSE:NACLIND","NSE:BHAGCHEM","NSE:SUMICHEM",
        "NSE:HERANBA","NSE:IPL","NSE:DHARMAJ","NSE:ASTEC","NSE:BESTAGRO","NSE:GSPCROP","NSE:MOL","NSE:COROMANDEL","NSE:CHAMBLFERT"]
out = {}
for s in syms:
    for attempt in range(3):
        try:
            rows, meta = fetch(s, "1D", 5000, timeout=60)
            out[s] = [[r[0], r[4]] for r in rows]
            print(s, len(rows), dt.datetime.utcfromtimestamp(rows[0][0]).date(), dt.datetime.utcfromtimestamp(rows[-1][0]).date(), rows[-1][4], flush=True)
            break
        except Exception as e:
            print("ERR", s, e, flush=True); time.sleep(2)
json.dump(out, open("agro_daily.json","w"))
