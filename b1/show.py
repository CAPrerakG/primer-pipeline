import json,sys
r=json.load(open('roster.json',encoding='utf-8'))
s=json.load(open('../scr.json',encoding='utf-8'))
for no in sys.argv[1:]:
    x=r[no]
    print('=====',no,x.get('name') or x.get('ind'), {k:v for k,v in x.items() if k not in('members','moved_out')})
    for m in x['members']:
        sc=s.get(m['sym'],{}) or {}
        ab=(sc.get('about') or '')[:260]
        print(f"  {m['sym']:<14} {m['co'][:38]:<38} {m.get('mcap') and round(m['mcap']/1e7) or 0:>8}cr {m.get('status','')} | {ab}")
    print('  moved_out:',x.get('moved_out'))
