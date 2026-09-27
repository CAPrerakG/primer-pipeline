import io,json,re,os,html
U=json.load(io.open('urls.json',encoding='utf-8'))
meta={'001':('Agrochemicals','Pesticides, herbicides and fungicides: the technical-to-formulation chain, the China factor, the monsoon, and 39 listed companies. The benchmark primer for this series.')}
for no in sorted(U):
    f=f'frag_{no}.html'
    if not os.path.exists(f): continue
    d=json.loads(re.search(r'<!--META(\{.*?\})-->',io.open(f,encoding='utf-8').read(),re.S).group(1))
    desc=re.sub(r'^Industry \d+ of 278(,? and the first of the [^:]+)?(, closing the [^:]+)?(, opening the [^:]+)?:\s*','',d['desc'])
    meta[no]=(d['short'],desc)
POWER_BLURB=os.environ.get('POWER_BLURB','Core complete: from coal and generation through transmission, equipment, cables, solar, storage and the contractors who build the grid. Ten related electrical and renewable sections are still to come.')
fam=[('Chemicals','001–016','Sixteen industries from salt and caustic soda to specialty molecules, colour, scent and fertiliser.',[f'{i:03d}' for i in range(1,17)]),
     ('Auto','017–027','The vehicle chain end to end: makers, the component and electronics suppliers beneath them, tyres, helmets and the showroom.',[f'{i:03d}' for i in range(17,28)]),
     ('Oil & Gas','028–035','Complete: built up the value chain from the wellhead to the lubricant shelf.',[f'{i:03d}' for i in range(28,36)]),
     ('Power & Energy','036–048',POWER_BLURB,[f'{i:03d}' for i in range(36,49)]),
     ('Consumer','049','Started: apparel and footwear retail; the rest of the consumer theme follows later.',['049']),
     ('Electronics & EMS','050–056','Complete: from chips and components through contract manufacturing to power electronics, meters and surveillance equipment.',[f'{i:03d}' for i in range(50,57)]),
     ('Defence','057–062','Complete: aircraft and missiles, defence electronics, shipyards, explosives, drones and space, and training systems.',[f'{i:03d}' for i in range(57,63)]),
     ('Capital Markets','063','Paused at his instruction: the financialisation theme resumes after the industrial sectors are done.',['063']),
     ('Metals','064–077, 079','Complete: the whole chain, from ore to the scrap heap — mining, ferro alloys, steel and its conversions, the furnace consumables, the non-ferrous metals, recycling and trading — with Industrial Minerals & Mining (079) closing the gap. The through-line: in metals, interchangeability is the risk, not proximity to the commodity.',[f'{i:03d}' for i in range(64,78)]+['079']),
    ('Engineering','078–','Started: up the chain from basic metalworking to finished machinery — castings and forgings first, then fabrication, bearings, pumps, valves, machine tools and the capital-goods businesses. The opening principle: in engineering, what matters is who writes the specification.',[f'{i:03d}' for i in range(78,100) if i!=79])]
CARD=[]
for name,rng,blurb,nums in fam:
    items=[f'<li><a class="row" href="{U[n] if U[n].startswith('http') else 'https://claude.ai/artifact/'+U[n]}"><span class="no">{n}</span><span class="tx"><b>{html.escape(html.unescape(meta[n][0]))}</b><em>{html.escape(html.unescape(meta[n][1]))}</em></span><span class="go">→</span></a></li>' for n in nums if n in U and n in meta]
    if items: CARD.append(f'<section class="fam"><header><h2>{html.escape(name)}</h2><span class="rng">{rng} · {len(items)} published</span></header><p class="blurb">{html.escape(blurb)}</p><ul class="list">{"".join(items)}</ul></section>')
done=len(U)
src=io.open('out/index.html',encoding='utf-8').read()
new=re.sub(r'<div class="kpi">.*?</div>\s*(?=<section class="fam">)', f'<div class="kpi"><div><b>{done}</b><span>published</span></div><div><b>278</b><span>industries in total</span></div><div><b>18 Sep 2026</b><span>price data through</span></div></div>\n', src, flags=re.S)
new=re.sub(r'<section class="fam">.*</section>\s*(?=<footer>)', ''.join(CARD)+'\n', new, flags=re.S)
new=re.sub(r'content="Index of the completed industry primers: \d+ of 278 published', f'content="Index of the completed industry primers: {done} of 278 published', new)
io.open('out/index.html','w',encoding='utf-8').write(new)
print('urls',done,'index rebuilt')
