import re,html,json,sys
def wc(s): return len(html.unescape(re.sub(r'<[^>]+>',' ',s)).split())
for no in sys.argv[1:]:
    h=open(f'out/{no}.html',encoding='utf-8').read()
    body=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S)
    m=re.search(r'window.PRIMER_DATA=(\{.*?\});</script>',h,flags=re.S); D=json.loads(m.group(1))
    notes=D.get('notes',{}); nw=sum(len(v.split()) for v in notes.values())
    words=wc(body)+nw  # notes render via JS
    links=len(re.findall(r'<a href="http',body)); gl=len(re.findall(r'<dt>',body)); qs=len(re.findall(r'<details class="q"',body))
    yrs=[c['y'] for c in D.get('cy',[])]; miss=[y for y in yrs if str(y) not in notes]
    ok=words>=5000 and links>=15 and gl>=40 and qs>=8 and not miss and 'critical' in body.lower()
    print(f"{no}: words {words} (notes {nw}) links {links} glossary {gl} questions {qs} | years without note {miss} | GATE {'PASS' if ok else 'FAIL'}")
