import json, sys, glob, importlib.util
from accept import A
rows=json.load(open('merged.json')); scr=json.load(open('scr.json'))
done={}
for f in sorted(glob.glob('dec*.py')):
    sp=importlib.util.spec_from_file_location(f[:-3],f); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); done.update(m.D)
sus=[r for r in rows if r['basic'] not in A[r['ind']]]
todo=[r for r in sus if r['sym'] not in done and scr.get(r['sym']) and scr[r['sym']].get('about')]
todo.sort(key=lambda r:(r['ind'],r['co']))
n=int(sys.argv[1]); out=sys.argv[2]
with open(out,'w',encoding='utf-8') as f:
    for r in todo[:n]:
        a=(scr[r['sym']]['about'] or '').replace('[1]','').replace('[2]','').replace('[3]','')
        f.write(f"{r['sym']} | {r['co']} | CUR={r['ind']} | OFF={r['basic']} | TV={r['tv_ind']} | {a[:200]}\n")
print('suspects',len(sus),'decided',len(done),'ready-with-about',len(todo),'written',min(n,len(todo)))
