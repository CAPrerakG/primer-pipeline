import io
p='frag_043.html'; s=io.open(p,encoding='utf-8').read()
R=[
("−37.3% against the Nifty's +3.0%, on a small basket of GE's then T&amp;D business, Salzer and the newly listed HPL Electric.","−37.3% against the Nifty's +3.0%, on a two-stock basket: GE's then T&amp;D arm −37% and Salzer −28% (HPL Electric listed only in October)."),
('"2017":"+47.7% versus +28.6%. A small-cap rally with some recovery in utility tenders."','"2017":"+47.7% versus +28.6%. GE\'s T&amp;D arm +48%, HPL +46%, Salzer +38% in a broad small-cap rally."'),
('"2018":"−44.6% versus +3.2%. The small-cap collapse, and a weak order environment for grid equipment."','"2018":"−44.6% versus +3.2%. HPL −59%, Salzer −42%, GE\'s T&amp;D arm −34%: the small-cap collapse on top of weak grid ordering."'),
('"2020":"−19.8% versus +14.9%, median +14%. Hitachi Energy India, demerged from ABB, joined the market in March; GE\'s T&amp;D arm fell another 20%."','"2020":"−19.8% versus +14.9%, but the median member rose 14% (Salzer +17%, HPL +14%, GE\'s T&amp;D arm −20%); the basket figure is dragged down by monthly rebalancing and the ±50% cap through the March crash and rebound, so the median is the better guide. Hitachi Energy India, demerged from ABB India, listed in March."'),
("Returns: equal-weighted basket of GE Vernova T&amp;D India, HPL Electric and Salzer from 2016, adding Hitachi Energy India and S&amp;S Power Switchgear from 2020. Monthly returns capped at ±50%, price only; 2026 to 18 September. The record starts in 2016 because the basket needs three members with history.","Returns: equal-weighted basket of GE Vernova T&amp;D India and Salzer in 2016, HPL Electric from 2017, and Hitachi Energy India and S&amp;S Power Switchgear from 2021 (their TradingView series begin in March 2020). Monthly returns capped at ±50%, price only; 2026 to 18 September. The record starts in 2016 because that is when two members first have full-year history."),
("<li><b>Small caps overshoot in both directions:</b> S&amp;S +712% in 2023; Kaycee and Shivalic now 83–84% below their peaks.</li>","<li><b>Small caps overshoot in both directions:</b> S&amp;S +712% in 2023; Kaycee and Shivalic are each 83% below their peaks.</li>"),
("<td>−10.0% and −84% from its October 2024 peak.</td>","<td>−10.0% in 2026 and −83% from its October 2024 peak.</td>"),
("Several small caps also peaked in late 2024 and are 58–84% below those levels.","Several small caps also peaked in mid-to-late 2024 and are 58–83% below those levels."),
("<td>123,577 km of circuits planned in 2022–27 (see 039)</td>","<td>The national transmission build-out (see 039)</td>"),
("<li><b>Transmission and substation capex:</b> the national grid plan (see 039).</li>","<li><b>Transmission and substation capex:</b> the national transmission plan and inter-state build-out (see 039).</li>"),
("Exports 33.6% of non-HVDC orders, from Europe, North America and South Asia.","Exports 33.6% of orders, from Europe, North America and South Asia."),
("Revenue ₹2,494 cr (+68.6%), profit ₹294 cr (more than double), pre-tax profit +120% and EBITDA margin +450 bps.","Revenue ₹2,493.7 cr (+68.6%), pre-tax profit ₹389.5 cr (+120.2%), net profit ₹294.2 cr (+123.5%) and EBITDA margin +450 bps."),
("<dt>HVDC</dt><dd>High-voltage direct current: long-distance transmission with lower losses than AC.</dd>\n    ",""),
("<dt>Smart meter</dt><dd>A communicating electricity meter, often prepaid (see 039).</dd>\n    ",""),
("<dt>Substation, TBCB, capitalisation</dt><dd>See 039.</dd>","<dt>HVDC, substation, smart meter, bay, TBCB, capitalisation</dt><dd>See 039.</dd>"),
("<dt>Drawdown from peak</dt><dd>See 001.</dd>","<dt>Drawdown from peak</dt><dd>See 029.</dd>"),
("<dt>Order book and book-to-bill</dt><dd>See 029, 041.</dd>","<dt>Book-to-bill</dt><dd>See 029.</dd>"),
("<dt>Wiring devices</dt>","""<dt>Vacuum circuit breaker (VCB)</dt><dd>A medium-voltage breaker that interrupts the arc inside a vacuum bottle; the workhorse of distribution switchgear.</dd>
    <dt>Moulded case circuit breaker (MCCB)</dt><dd>A larger low-voltage breaker for commercial and industrial feeders.</dd>
    <dt>Residual current device (RCCB)</dt><dd>A breaker that trips on earth leakage to protect people from shock.</dd>
    <dt>Disconnector (isolator)</dt><dd>A switch that visibly separates equipment for maintenance; it is not designed to break fault current.</dd>
    <dt>Earthing switch</dt><dd>Connects isolated equipment to earth so it is safe to work on.</dd>
    <dt>Ring main unit (RMU)</dt><dd>A compact, sealed medium-voltage switchgear unit used in city distribution networks.</dd>
    <dt>Busbar</dt><dd>The thick conductor inside switchgear and substations that distributes power between circuits.</dd>
    <dt>Instrument transformer</dt><dd>Current and voltage transformers that step values down so meters and relays can measure them.</dd>
    <dt>Surge arrester</dt><dd>Diverts lightning and switching surges to earth to protect equipment.</dd>
    <dt>Breaking capacity</dt><dd>The largest fault current a breaker can safely interrupt, in kiloamperes.</dd>
    <dt>Fault clearing time</dt><dd>How quickly protection detects and removes a fault, typically a few cycles — tens of milliseconds.</dd>
    <dt>Arc</dt><dd>The plasma that forms when current is interrupted; quenching it is the core engineering problem in a breaker.</dd>
    <dt>Thyristor valve</dt><dd>The switching building block of classic LCC HVDC converters.</dd>
    <dt>Back-to-back and multi-terminal HVDC</dt><dd>A converter pair at one site linking two unsynchronised grids, versus a DC network with three or more converter stations.</dd>
    <dt>FACTS</dt><dd>Flexible AC transmission systems — SVCs, STATCOMs and series compensation that raise the capacity and stability of AC lines.</dd>
    <dt>Synchronous condenser</dt><dd>A spinning machine that supplies inertia and reactive power without generating energy, increasingly used where renewables dominate.</dd>
    <dt>Contactor and control relay</dt><dd>Industrial switching devices for motors and machines — Salzer's and Kaycee's core products.</dd>
    <dt>Reed switch</dt><dd>A tiny magnetically operated switch sealed in glass; Switching Technologies Gunther's product.</dd>
    <dt>Control panel</dt><dd>A cabinet of breakers, relays and meters assembled for a specific plant or substation; Shivalic's business.</dd>
    <dt>Wiring devices</dt>"""),
("<dt>Grid integration</dt>","""<dt>Price variation clause (PVC)</dt><dd>A contract term that passes changes in copper, steel or other input costs to the customer.</dd>
    <dt>Voltage classes</dt><dd>Low voltage up to 1 kV, medium voltage 1–36 kV, high voltage above that, and extra- and ultra-high voltage at 400 kV, 765 kV and ±800 kV DC.</dd>
    <dt>Consortium bid</dt><dd>A joint bid by several suppliers, such as Hitachi Energy with BHEL for Khavda–Nagpur.</dd>
    <dt>Related-party transactions</dt><dd>Purchases, sales and fees between the Indian arm and its parent group; shareholders must approve the material ones.</dd>
    <dt>Grid integration</dt>"""),
]
for a,b in R:
    n=s.count(a)
    if n!=1: print('MISS',n,a[:70])
    s=s.replace(a,b)
io.open(p,'w',encoding='utf-8').write(s)
