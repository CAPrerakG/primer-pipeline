import json,sys,datetime
p=json.load(open('prices.json'))
def ytd(s):
    x=p.get(s)
    if not x: return None
    pre=[c for t,c in x if datetime.datetime.fromtimestamp(t).year<2026]
    if not pre: return None
    return round((x[-1][1]/pre[-1]-1)*100)
for s in sys.argv[1:]: print(s, ytd(s))
