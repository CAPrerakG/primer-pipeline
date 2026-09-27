import io
p='frag_055.html'; s=io.open(p,encoding='utf-8').read()
GROUND = """<section id="ground" data-toc="How a roll-out works">
  <p class="eyebrow">5b · A closer look</p>
  <h2>How a smart-meter roll-out works on the ground</h2>
  <div class="tbl-wrap"><table><thead><tr><th>Step</th><th>What happens</th><th>Where it goes wrong</th></tr></thead><tbody>
    <tr><td>1 · Survey and consumer indexing</td><td>Every consumer is mapped to a transformer and feeder, and records are cleaned</td><td>Poor discom records; missing addresses</td></tr>
    <tr><td>2 · Installation</td><td>Old meters are replaced house by house</td><td>Access to homes, consumer objections, monsoon</td></tr>
    <tr><td>3 · Communication commissioning</td><td>Each meter is connected to the network and head-end</td><td>Weak signal in rural or dense urban areas</td></tr>
    <tr><td>4 · Migration to prepaid</td><td>Accounts switched to prepaid mode with recharge options</td><td>Consumer resistance, political sensitivity</td></tr>
    <tr><td>5 · Operation and maintenance</td><td>The AMISP keeps meters and systems running for the contract life</td><td>Service levels, replacement of faulty meters</td></tr>
    <tr><td>6 · Payment</td><td>The discom pays monthly fees against service levels</td><td>Delays of 90–180 days at some discoms</td></tr>
  </tbody></table></div>
  <p>The table explains why national targets slip. Manufacturing capacity is not the constraint — Genus alone can make over 1.8 crore meters a year. The constraints are on the ground: indexing millions of consumers, reaching homes, maintaining communication coverage and persuading households to accept prepaid billing. Installation speed therefore depends on each discom's administration and on state politics as much as on the contractor.</p>
  <h3>AMISP economics, in one illustration</h3>
  <p>The broad shape of an AMISP contract can be understood without company-specific numbers. The provider spends heavily at the start — meters, communication equipment, software and installation labour — funded by equity and debt in a project company, plus the portion of the central grant passed through during roll-out. It then receives a fixed fee per meter per month for the contract life. The return depends on four things: the fee won in the tender, the cost of each installed meter, the cost of financing, and whether the discom pays on time. A small rise in meter costs or a few months' delay in payments can erode a meaningful share of the return, because the fee is fixed for years. That is why rising component prices and slow-paying discoms matter so much to the listed company's valuation, even while its revenue grows.</p>
  <h3>Order-book arithmetic</h3>
  <p>Genus's order book of about ₹24,020 cr is roughly four years of revenue at its FY27 guidance of ₹6,000–6,500 cr. But part of it is long-dated service income spread over 7–10 years, which will be recognised slowly and depends on discom payments; the manufacturing and installation part converts faster. Separating the two is the most useful thing an analyst can do with the headline number.</p>
</section>

<section id="politics" data-toc="Consumer acceptance">
  <p class="eyebrow">5c · The human factor</p>
  <h2>Consumer acceptance and state politics</h2>
  <p>Prepaid smart meters change the relationship between households and the electricity company. Consumers who were used to paying late, or not at all, now face disconnection when their balance runs out; others worry about faster-running meters or unfamiliar recharge systems. In several states these concerns have produced protests, slowed installations or led governments to pause prepaid conversion, particularly ahead of elections. The programme's success therefore depends on communication, grievance handling and gradual migration as much as on technology. For investors, the practical implication is that installation pace can vary sharply by state and can change with political circumstances — a risk that sits outside any contractor's control.</p>
</section>

<section id="rawmat" data-toc="Critical inputs">"""
GLOSS = """<dt>Consumer indexing</dt><dd>Mapping each consumer to a transformer and feeder so losses can be traced.</dd>
    <dt>Communication success rate</dt><dd>The share of meters reporting data successfully — a key service level.</dd>
    <dt>Prepaid migration</dt><dd>Switching installed smart meters to prepaid billing.</dd>
    <dt>Service-level agreement</dt><dd>Performance standards an AMISP must meet to be paid in full.</dd>
    <dt>Energy audit</dt><dd>A check of where energy is lost between supply and billing.</dd>
    <dt>O&amp;M period</dt><dd>The operation and maintenance years of an AMISP contract.</dd>
    <dt>Gross budgetary support</dt><dd>The central government's grant share of RDSS project costs.</dd>
    <dt>Class of accuracy</dt>"""
SRC = """<li>Further reading: <a href="https://www.ibef.org/research/case-study/smart-metering-deployment-in-india-policy-framework-institutional-structure-and-national-implementation-status">IBEF on the national roll-out</a>; <a href="https://www.icra.in/CommonService/OpenMedia?Key=e26d0f4d-31fb-4a27-b835-c41a7e3865be">ICRA on installations</a>; <a href="https://thesecretariat.in/article/india-s-ambitious-smart-meter-plan-falters-with-just-25-4-completion">the pace of completion</a>.</li>
    <li>Advance Metering Technology: <a"""
R=[("<li><b>February–March was positive only in 2012, 2021 and 2022</b>;","<li><b>February–March was positive only in 2021 (+31.5), 2012 (+7.1) and 2022 (+4.2)</b>;"),
   ('<section id="rawmat" data-toc="Critical inputs">', GROUND),
   ("<dt>Class of accuracy</dt>", GLOSS),
   ("<li>Advance Metering Technology: <a", SRC)]
for a,b in R:
    n=s.count(a)
    if n!=1: print('MISS',n,a[:60])
    s=s.replace(a,b)
io.open(p,'w',encoding='utf-8').write(s)
print('ok')
