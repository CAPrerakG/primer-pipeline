import io
p='frag_044.html'; s=io.open(p,encoding='utf-8').read()
R=[
("profit ₹31 cr against about ₹1 cr a year earlier","profit ₹30.7 cr against about ₹1.4 cr a year earlier"),
("Finolex +64%, while the telecom-cable names fell about 30% (Vindhya, Birla Cable, Paramount) as fibre spending paused.","Finolex +64%, while the telecom-cable names each fell about 30% (Vindhya, Birla Cable, Paramount)."),
("<td>Wires and cables from Gujarat; up from the SME platform.</td>","<td>Wires and cables from Gujarat.</td>"),
("<td>Hindalco and Adani's Kutch Copper are the domestic sources (see 036)</td>","<td>Hindalco and Adani's Kutch Copper are the domestic sources</td>"),
("<li><b>Metals and mining</b> (036 and later primers): copper and aluminium supply.</li>","<li><b>Non-ferrous metals</b> (a later primer): copper and aluminium supply.</li>"),
("<dt>LT, HT and EHV cable</dt><dd>Low-tension (up to 1.1 kV), high-tension (up to about 66 kV) and extra-high-voltage (110–400 kV) cables.</dd>","<dt>LT, HT and EHV cable</dt><dd>Low-tension (up to 1.1 kV), high-tension (about 3.3–33 kV) and extra-high-voltage (66–400 kV) cables.</dd>"),
("₹150 cr raised for Silvassa capacity;","board approval to raise ₹150 cr through convertible debentures for Silvassa capacity;"),
]
for a,b in R:
    n=s.count(a)
    if n!=1: print('MISS',n,a[:70])
    s=s.replace(a,b)
io.open(p,'w',encoding='utf-8').write(s)
