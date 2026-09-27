import io
p='frag_067.html'; s=io.open(p,encoding='utf-8').read()
DEM = """<section id="demand" data-toc="Why demand outgrows GDP">
  <p class="eyebrow">5c · Why demand outgrows GDP</p>
  <h2>The long runway under Indian stainless</h2>
  <p>India uses far less stainless steel per person than the world average, and the gap closes as incomes rise: a household that buys a steel kitchen, a city that builds a metro, a dairy that installs stainless tanks and a refinery that orders corrosion-resistant piping all add demand that did not exist before. That is why the industry body expects 7–8% annual growth over FY26–FY28 while the wider economy grows more slowly, and why Indian capacity is planned to rise from about 7 million tonnes to 11 million.</p>
  <div class="tbl-wrap"><table><thead><tr><th>Demand source</th><th>What drives it</th><th>Grade used</th></tr></thead><tbody>
    <tr><td>Kitchenware and utensils</td><td>Household incomes and the shift from aluminium</td><td>Mostly 200 series</td></tr>
    <tr><td>Railways and metros</td><td>Vande Bharat coaches, metro cars, station fittings</td><td>400 and 300 series</td></tr>
    <tr><td>Automotive</td><td>Exhaust systems and tighter emission norms</td><td>400 series</td></tr>
    <tr><td>Process industries</td><td>Chemicals, dairy, pharma, food processing</td><td>300 series</td></tr>
    <tr><td>Construction and architecture</td><td>Railings, facades, water infrastructure</td><td>200 and 300 series</td></tr>
    <tr><td>Energy</td><td>Refineries, desalination, solar mounting</td><td>Duplex and 300 series</td></tr>
  </tbody></table></div>
  <p>Two features of this demand matter for investors. First, much of it is replacement-resistant: stainless is chosen precisely because it lasts, so growth comes from new applications rather than repeat purchases. Second, a large part of the Indian market is price-sensitive and served by small re-rollers using imported coil, which is why import duties translate quickly into domestic pricing power for an integrated producer.</p>
</section>

<section id="rawmat" data-toc="Critical inputs">"""
GL = """<dt>Scrap</dt><dd>Recycled stainless, the cheapest source of alloy units.</dd>
    <dt>2B finish</dt><dd>The standard smooth, lightly reflective cold-rolled finish.</dd>
    <dt>BA finish</dt><dd>Bright-annealed, mirror-like surface used in appliances.</dd>
    <dt>No. 4 finish</dt><dd>A brushed surface common on kitchen equipment.</dd>
    <dt>Precision strip</dt><dd>Very thin, tightly toleranced stainless for springs and blades.</dd>
    <dt>Slitting</dt><dd>Cutting wide coil into narrower strips.</dd>
    <dt>Grade mix</dt><dd>The share of 200, 300 and 400 series in sales, which drives realisations.</dd>
    <dt>Surcharge lag</dt><dd>The delay between alloy costs changing and prices adjusting.</dd>
    <dt>Melt capacity</dt><dd>How much liquid steel a plant can make in a year.</dd>
    <dt>Downstream capacity</dt><dd>Rolling and finishing capacity, which converts slabs into sellable products.</dd>
    <dt>Corrosion resistance</dt><dd>The property customers buy, set by chromium, nickel and molybdenum content.</dd>
    <dt>Molybdenum</dt><dd>An addition in 316-grade steel for resistance to salt and chemicals.</dd>
    <dt>Per-capita consumption</dt><dd>Stainless use per person — an indicator of how far a market can grow.</dd>
    <dt>Re-roller</dt><dd>A small mill that buys coil and rolls it to finished sizes.</dd>"""
SRC = """<li>Nickel:"""
SRC2 = """<li>Further reading: <a href="https://jslgc.com/stainless-steel-trading-market-outlook-2026-global-supply-shifts-and-indias-demand-engine/">the 2026 stainless trading outlook</a>; <a href="https://www.tacto.ai/en/commodities/nickel-price">nickel price tracker</a>.</li>
    <li>Nickel:"""
R=[('<section id="rawmat" data-toc="Critical inputs">',DEM),
   ("<dt>Scrap</dt><dd>Recycled stainless, the cheapest source of alloy units.</dd>",GL),
   (SRC,SRC2)]
for a,b in R:
    print(s.count(a)); s=s.replace(a,b,1)
io.open(p,'w',encoding='utf-8').write(s)
