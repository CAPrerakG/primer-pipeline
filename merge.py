import json, collections, os
base=json.load(open('base.json'))
cls=json.load(open('cls.json'))
scr=json.load(open('scr.json')) if os.path.exists('scr.json') else {}
rows=[]
for x in base:
    c=cls.get(x['sym']); s=scr.get(x['sym'])
    basic=ind4=None; src=None
    if c and c.get('basic'): basic,ind4,src=c['basic'],c['industry'],'BSE'
    elif s and s.get('cls') and len(s['cls'])==4: basic,ind4,src=s['cls'][3],s['cls'][2],'Screener'
    x=dict(x); x.update({'basic':basic,'ind4':ind4,'csrc':src,'about':(s or {}).get('about') if s else None})
    rows.append(x)
json.dump(rows,open('merged.json','w'))
n=len(rows); nb=sum(1 for r in rows if r['basic'])
print('rows',n,'with basic',nb)
g=collections.defaultdict(collections.Counter)
for r in rows: g[r['ind']][r['basic']]+=1
with open('basic_crosstab.txt','w',encoding='utf-8') as f:
    for k in sorted(g):
        c=g[k]; f.write(f'{k} ({sum(c.values())}): '+'; '.join(f'{a}={b}' for a,b in c.most_common())+'\n')
home=collections.defaultdict(collections.Counter)
for r in rows:
    if r['basic']: home[r['basic']][r['ind']]+=1
with open('basic_home.txt','w',encoding='utf-8') as f:
    for b in sorted(home, key=lambda b:-sum(home[b].values())):
        c=home[b]; f.write(f'{b} ({sum(c.values())}): '+'; '.join(f'{a}={n}' for a,n in c.most_common())+'\n')
