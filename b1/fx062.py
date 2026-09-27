import io
p='frag_062.html'; s=io.open(p,encoding='utf-8').read()
SIM = """<section id="simecon" data-toc="Why simulation pays">
  <p class="eyebrow">5c · Why simulation pays</p>
  <h2>The customer's side of the business</h2>
  <p>To understand why armies keep buying simulators even when budgets are tight, look at the customer's costs. A soldier learning to shoot fires hundreds of rounds; a tank crew learning gunnery fires expensive main-gun ammunition and burns fuel; every hour on a real vehicle adds wear that must later be repaired. A simulator converts much of that recurring cost into a one-time purchase plus a maintenance fee, and it allows training at night, in bad weather and in scenarios that would be too dangerous to rehearse live.</p>
  <div class="tbl-wrap"><table><thead><tr><th>Training need</th><th>Live cost</th><th>Simulator advantage</th></tr></thead><tbody>
    <tr><td>Marksmanship</td><td>Ammunition, range time, instructors</td><td>Unlimited repetitions; every shot scored</td></tr>
    <tr><td>Vehicle driving and gunnery</td><td>Fuel, wear, main-gun rounds</td><td>Hours of practice without wear or ammunition</td></tr>
    <tr><td>Tactics and command</td><td>Moving whole units to exercise areas</td><td>Rehearse missions in a classroom</td></tr>
    <tr><td>Dangerous scenarios</td><td>Cannot be practised safely</td><td>Ambushes, casualties and failures can be simulated</td></tr>
  </tbody></table></div>
  <p>This is why simulators feature on India's indigenisation lists and why training budgets tend to survive even when equipment purchases are delayed. The weakness, from a supplier's point of view, is that simulators are bought in batches as new equipment enters service or training centres are upgraded, so demand comes in waves. The maintenance contracts that follow each batch — ₹318 cr of Zen's order book — are the steadier part of the business, and their share is worth watching as a sign of how recurring the company's revenue is becoming.</p>
</section>

<section id="rawmat" data-toc="Critical inputs">"""
GL = """<dt>UGV</dt><dd>Unmanned ground vehicle.</dd>
    <dt>Acoustic detection</dt><dd>Finding drones by the sound of their motors and propellers.</dd>
    <dt>Radar cross-section</dt><dd>How visible an object is to radar; small drones have a very small one.</dd>
    <dt>Electro-optical/infrared (EO/IR) sensor</dt><dd>Day and thermal cameras used to see and track drones.</dd>
    <dt>Geo-fencing</dt><dd>Software limits that stop drones entering defined areas.</dd>
    <dt>Virtual reality (VR)</dt><dd>A fully computer-generated environment seen through a headset.</dd>
    <dt>Augmented reality (AR)</dt><dd>Computer images overlaid on the real world.</dd>
    <dt>Digital twin</dt><dd>A virtual copy of a real system used for training or testing.</dd>"""
SRC = """<li>Partnership and market:"""
SRC_NEW = """<li>More on Zen: <a href="https://www.business-standard.com/amp/markets/news/zen-technologies-rallies-8-hits-new-high-on-pact-with-avt-simulation-124120600233_1.html">record high on the AVT pact</a>; <a href="https://www.angelone.in/news/stocks/zen-technologies-share-price-drops-10-percent-q4-fy26-results-show-pat-falls-69-percent-yoy">Q4 FY26 share reaction</a>; <a href="https://www.investywise.com/zen-technologies-investor-presentation-for-q1-fy27">Q1 FY27 investor presentation</a>; <a href="https://www.equitybulls.com/category.php?id=373556">Q1 FY27 net profit</a>; <a href="https://univest.in/blogs/zen-technologies-q4-results-fy26">Q4 FY26 order inflow</a>.</li>
    <li>Partnership and market:"""
R=[('<section id="rawmat" data-toc="Critical inputs">',SIM),("<dt>UGV</dt><dd>Unmanned ground vehicle.</dd>",GL),(SRC,SRC_NEW)]
for a,b in R:
    print(s.count(a)); s=s.replace(a,b,1)
io.open(p,'w',encoding='utf-8').write(s)
