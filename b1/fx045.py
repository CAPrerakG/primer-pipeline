import io
p='frag_045.html'; s=io.open(p,encoding='utf-8').read()
R=[
("<dt>Solar module</dt><dd>Cells connected and sealed into a panel.</dd>\n    ",""),
("<dt>Degradation</dt><dd>The gradual loss of output over a module's life.</dd>\n    ",""),
("<dt>DCR</dt><dd>Domestic content requirement — modules made with Indian cells, required for subsidised schemes.</dd>\n    ",""),
("<dt>Capacity factor, curtailment, PPA</dt><dd>See 038.</dd>","<dt>Module, inverter, degradation, DCR, CUF, curtailment, PPA, LCOE</dt><dd>See 038.</dd>"),
("<dt>Yield</dt>","<dt>Standard test conditions (STC)</dt><dd>The laboratory conditions — 1,000 W/m² of light at 25°C — at which watt-peak is measured.</dd>\n    <dt>Temperature coefficient</dt><dd>How much output falls per degree of heat; lower is better in hot Indian conditions, one advantage of heterojunction.</dd>\n    <dt>Yield</dt>"),
("<td>Rooftop kits and inverters</td><td>High teens</td>","<td>Rooftop kits and inverters</td><td>Double digits (Fujiyama's net margin about 12%)</td>"),
("<td>Single digits (Vikram 8%; Saatvik near zero)</td>","<td>Single digits (Vikram's EBITDA margin 8%; Saatvik's net margin about 1%)</td>"),
("<td>Domestic makers protected by anti-dumping duty on imports</td>","<td>Domestic makers protected by anti-dumping duties on imports</td>"),
("<td>Aluminium prices up about 26% in 2026 (see 044)</td>","<td>2026 average about 26% above 2025's (see 044)</td>"),
('"2020":"+25.2% against +22.7%. Websol +105% as ALMM was announced and imports disrupted; Aerpace −20%."','"2020":"+25.2% against +22.7%. Websol +105% as Covid disrupted Chinese supply chains and India moved toward protecting domestic manufacturing; Aerpace −20%."'),
("2015 is missing because the basket lacked two members with full-year data.","2015 is omitted because Aerpace traded on only 21 days that year, leaving gaps in the monthly series."),
("<p>The market expects Emmvee's cell-driven profits to shrink as capacity arrives, while Vikram's depressed profits are expected to recover when its own cells start.</p>","<p>The market expects Emmvee's cell-driven profits to shrink as cell capacity arrives, and it values Vikram on a depressed profit (₹20 cr in the quarter), so a small denominator produces a high multiple.</p>"),
]
for a,b in R:
    n=s.count(a)
    if n!=1: print('MISS',n,a[:70])
    s=s.replace(a,b)
io.open(p,'w',encoding='utf-8').write(s)
