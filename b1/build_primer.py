import sys, re, json, os, html
B=os.path.dirname(os.path.abspath(__file__))
def build(no):
    frag=open(os.path.join(B,f'frag_{no}.html'),encoding='utf-8').read()
    meta=json.loads(re.search(r'<!--META(.*?)-->',frag,re.S).group(1))
    frag=re.sub(r'<!--META.*?-->','',frag,flags=re.S)
    data=json.load(open(os.path.join(B,f'data_{no}.json'))) if os.path.exists(os.path.join(B,f'data_{no}.json')) else {}
    data.update(meta.get('data_extra',{}))
    MN=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    def sg(x): return ("+" if x>0 else "")+(f"{x:.1f}")
    if '<!--SEASON-->' in frag:
        if data.get('monthly'):
            mo=data['monthly']; best=sorted(mo,key=lambda m:-m['rel'])[:3]; worst=sorted(mo,key=lambda m:m['rel'])[:3]
            one=data.get('nbasket',0)==1
            h=f"<p><b>Basket:</b> {'the single listed company' if one else str(data['nbasket'])+' names'} ({html.escape(', '.join(data['basket']))}), {'' if one else 'equal-weighted, '}monthly from {data['start']}, compared with the Nifty 50.{' With one stock, these statistics describe that company, not an industry.' if one else ''}</p><ul>"
            h+="<li><b>Strongest months vs the Nifty:</b> "+"; ".join(f"{MN[m['m']-1]} {sg(m['rel'])} pts (beat in {m['hit']} of {m['n']} years)" for m in best)+".</li>"
            h+="<li><b>Weakest months:</b> "+"; ".join(f"{MN[m['m']-1]} {sg(m['rel'])} pts (beat in {m['hit']} of {m['n']} years)" for m in worst)+".</li>"
            W=data.get('win',{}); lab={'JanMar':'Jan–Mar','FebMar':'Feb–Mar','AprJul':'Apr–Jul','AugSep':'Aug–Sep','SepNov':'Sep–Nov','OctDec':'Oct–Dec'}
            h+="<li><b>Windows:</b> "+"; ".join(f"{lab[k]} beat the Nifty in {v['hit']} of {v['n']} years (median {sg(v['median'])} pts)" for k,v in W.items() if k in lab)+".</li></ul>"
            apr=next((m for m in mo if m['m']==4),None)
            if meta.get('control_note'):
                h+=meta['control_note']
            elif apr and not one:
                ex=round(apr['rel']-3.0,1)
                h+=f"<p><b>Control:</b> small caps as a whole (Nifty Smallcap 100) beat the Nifty in April in 11 of 15 years, by an average of 3.0 points, and lag in January–February. Part of any April strength is this market-wide effect. After removing it, this industry's own April edge is about {sg(ex)} points.</p>"
            h+=meta.get('season_note','')
            h+='<p class="note">A tendency, not a rule: small samples, survivorship bias (only names still listed) and equal weighting. Use it for timing context, not as a signal.</p>'
        else:
            h='<p>There is not enough listed price history for a seasonality test in this industry.</p>'+meta.get('season_note','')
        frag=frag.replace('<!--SEASON-->',h)
    if data.get('ytd'):
        frag=frag.replace('<p id="now-stocks"></p>',f'<p id="now-stocks">Stocks: the basket is {sg(data["ytd"]["b"])}% this year vs {sg(data["ytd"]["n"])}% for the Nifty (to 18 Sep 2026). {meta.get("now_note","")}</p>')
    css=open(os.path.join(B,'base.css'),encoding='utf-8').read()
    js=open(os.path.join(B,'base.js'),encoding='utf-8').read()
    toc=re.findall(r'<section id="([^"]+)" data-toc="([^"]+)"',frag)
    tocli='\n'.join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i,t in toc)
    page=f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta["title"]}</title>
<meta name="description" content="{html.escape(meta["desc"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..110,500..800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{css}</style>
<div class="wrap">
<nav class="toc" aria-label="Contents"><details open><summary>Contents</summary><p class="toc-h">{html.escape(meta["short"])} · reading order</p><ol>
{tocli}
</ol></details></nav>
<main>
{frag}
</main></div>
<script>window.PRIMER_DATA={json.dumps(data)};</script>
<script>{js}</script>
'''
    os.makedirs(os.path.join(B,'out'),exist_ok=True)
    fn=os.path.join(B,'out',no+'.html')
    open(fn,'w',encoding='utf-8').write(page)
    print(fn,len(page),'sections',len(toc))
    import shutil
    # named copy inside the repo; nothing is written outside it
    os.makedirs('../primers', exist_ok=True)
    shutil.copy(fn, os.path.join('../primers', meta['file']))
if __name__=='__main__':
    for no in sys.argv[1:]: build(no)
