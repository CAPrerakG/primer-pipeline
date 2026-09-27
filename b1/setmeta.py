import sys, json, re
def setmeta(no, **kw):
    fn=f'frag_{no}.html'; s=open(fn,encoding='utf-8').read()
    m=re.search(r'<!--META(.*?)-->',s,re.S); meta=json.loads(m.group(1)); meta.update(kw)
    s=s[:m.start()]+'<!--META'+json.dumps(meta,ensure_ascii=False)+'-->'+s[m.end():]
    open(fn,'w',encoding='utf-8').write(s)
