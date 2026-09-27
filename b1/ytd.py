import json,sys,datetime
CUT=1789776000  # project data date: bars up to and including 18-Sep-2026 (UTC)
p=json.load(open('prices.json')); p={k:[r for r in v if r[0]<CUT] for k,v in p.items() if v}
def ytd(s):
    x=p.get(s)
    if not x: return None
    pre=[c for t,c in x if datetime.datetime.fromtimestamp(t).year<2026]
    if not pre: return None
    return round((x[-1][1]/pre[-1]-1)*100)
for s in sys.argv[1:]: print(s, ytd(s))
