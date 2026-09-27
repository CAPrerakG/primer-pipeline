import json,sys
for no in sys.argv[1:]:
    try: d=json.load(open(f'data_{no}.json',encoding='utf-8'))
    except Exception as e: print(no,'ERR',e); continue
    if not d: print(no,'EMPTY'); continue
    print('=====',no,'basket',d.get('basket'),'start',d.get('start'))
    print(' monthly:',' '.join(f"{m['m']}:{m['rel']:+.1f}({m['hit']}/{m['n']})" for m in d['monthly']))
    print(' win:',{k:(round(v['mean'],1),round(v['median'],1),f"{v['hit']}/{v['n']}") for k,v in d['win'].items()})
    print(' cy:',' '.join(f"{c['y']}:{c['b']:+.0f}/{c['rel']:+.0f}" for c in d['cy']))
    print(' ytd:',d.get('ytd'))
    print(' dd:','; '.join(f"{x['co'][:22]} {x['fp']:+.0f} 1y{x['y1']:+.0f}" for x in d['dd'][:10]))
