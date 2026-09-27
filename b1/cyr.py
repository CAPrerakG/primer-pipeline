import json,sys,datetime
p=json.load(open('prices.json',encoding='utf-8'))
def cy(sym):
    s=p[sym]; last={}
    for t,c in s:
        y=datetime.datetime.utcfromtimestamp(t).year; last[y]=c
    ys=sorted(last); out=[]
    for i in range(1,len(ys)):
        out.append(f"{ys[i]}:{(last[ys[i]]/last[ys[i-1]]-1)*100:+.0f}")
    return ' '.join(out[-13:])
for s in sys.argv[1:]: print(s, cy(s))
