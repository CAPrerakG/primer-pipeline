# Family notes — running theses and cross-primer context

Read this before writing any primer. Append to it when a family starts, when a primer produces a finding
that later primers should echo, or when a family closes. Keep entries short; the primers hold the detail.

## Through-lines by family

**Chemicals (001–016).** Sixteen industries from salt and caustic soda to specialty molecules, colour, scent and
fertiliser. 001 Agrochemicals is the quality benchmark for the whole series. Carbon Black was never covered
here; it is queued under Materials.

**Auto (017–027).** The vehicle chain end to end: makers, component and electronics suppliers, tyres, helmets,
dealerships.

**Oil & Gas (028–035).** Built up the chain from wellhead to lubricant shelf.

**Power & Energy (036–048).** Coal and generation through transmission, equipment, cables, solar, storage and the
EPC contractors. **Not actually complete:** ten electrical/renewable sections were missed and are queued as
"Electrical Equipment & Power — gaps". Boilers, Turbines & Power Equipment was done as 041.

**Consumer (049).** Only Apparel & Footwear Retail so far; the rest of Consumer is queued.

**Electronics & EMS (050–056).** Chips and components through contract manufacturing, power electronics, meters,
surveillance.

**Defence (057–062).** Aircraft and missiles, defence electronics, shipyards, explosives, drones and space,
training systems.

**Capital Markets (063).** Stock Exchanges & Depositories only. The rest of financials is deferred to the end.

**Metals (064–077).** Ore to the scrap heap. Through-line, stated on 077: **in metals, interchangeability is the
risk, not proximity to the commodity.** Durable returns came from what a customer cannot easily switch away from
— certified wire rope (069), total-refractory-management contracts (070), qualified superalloys (075),
integrated smelters with captive power and bauxite (072), low-cost orebodies (074). Converters, standalone
smelters on negative treatment charges and a state trading agency did badly. Also: power cost as the structural
aluminium story (AI data centres bidding $115/MWh vs smelters' $40); the first-calendar-quarter weakness that
appears in almost every metals basket (Chinese New Year + fiscal year-end destocking); October–December strength
in copper (12/14) and aluminium (11/14). **Gap closed with 079 Industrial Minerals & Mining** (27 Sep 2026): the
section is five different businesses — lignite rent (GMDC), Guinea bauxite logistics (Ashapura, ~84% of revenue),
mineral processing (20 Microns), titanium chemistry (Cochin Minerals & Rutile) and stone (ASI, Midwest). Lesson: the
word "mining" says nothing about where profit comes from; a lease is a political asset (Cochin lost captive ilmenite
to the 2019 atomic-minerals order), processing skill lasts longer. Critical-minerals/rare-earth theme is policy and
projects, not revenue, for every listed name here.

**Engineering & Capital Goods (078–).** Opening principle, stated on 078: **in engineering the question is never
what a company makes — it is who writes the specification, and whether the part wears out.** AIA Engineering
(mining consumable sold on wear life, 36% EBITDA margin) vs Alicon Castalloy (tier-one castings to a customer's
drawing, 9.5%) in the same section. Apply the same test to bearings, pumps, valves, machine tools.

## Calendar findings worth echoing

- Castings (078): April beat the Nifty in 14 of 15 years — the strongest monthly record in the project.
- Metal Recycling (076): April 13 of 15. Specialty metals (075): April 12 of 15. Small-cap fiscal-year behaviour
  is part of this — say so when an April signal comes from a small-cap basket.
- Industrial minerals (079): February–March beat the Nifty in only 3 of 15 years (median −6.9) — the weakest
  first-quarter record in the Metals family; April 13 of 15.
- Zinc (074): no usable seasonal signal at all — report that plainly rather than manufacturing a pattern.

## Data traps already found (do not repeat)

- **Corporate-action discontinuities:** Orient Ceratech 2011 demerger (070); HEG's September 2026 demerger erased its
  TV history — successor NSE:HEGAM, electrode business in unlisted HEG Graphite (071); Vedanta's 2026 demerger —
  VAML listed 15 Jun 2026, and VEDL's own series shows no ex-demerger step (072, 075); MMTC's 2013 ~92% fall with no
  single-day step >10% — record started in 2014 (077).
- **Same-group names:** Foseco India (NSE:FOSECOIND, INE519A01011, the parent) vs Foseco Crucible (BSE:FOSECOC,
  INE599F01020, the former Morganite Crucible) — conflated in 070, corrected and republished. Welcast Steels is AIA
  Engineering's 74.85% subsidiary (078). **Check the ISIN before writing about any two related names.**
- **Unusable series:** COMEX:ZNC1! prints an unchanged value for 2021–2025. No lead series exists on TV
  (COMEX/MCX). COMEX copper carries a US tariff premium in 2025–26 — say which exchange.
- **Unit misprints in sources:** NSDL Q1 PAT printed as ₹983 cr (correct ₹98.3 cr); Rajratan PAT printed as
  ₹229.6 cr (correct ₹23.0 cr); lakh-denominated filings (e.g. Pondy Oxides) — convert to crore and check against
  revenue.
- **Profit that isn't operations:** Maithan (treasury income), Welspun (PAT > EBITDA), IFGL (end of goodwill
  amortisation), MMTC (other income ₹145 cr vs ₹0.68 cr operating revenue).
  GMDC (079): trailing other income ₹945 cr vs operating profit ₹465 cr, incl. ₹522.65 cr exceptional GST credit
  in FY26; ASI Industries other income ≈ operating profit.
- **Tenfold misprint:** ScanX printed GMDC Q1 FY27 revenue ₹9,066.4 cr / PAT ₹1,634.3 cr (correct ₹906.64 cr /
  ₹163.43 cr). Check PAT against EPS × shares.
- **Name-based misclassification:** Garnet International (an NBFC, not garnet), D & H India (welding electrodes),
  International Combustion (mining equipment) sat in Industrial Minerals (079). Neelkanth Rockminerals: nil revenue
  since FY21, +226% in 2026 on a takeover.
- **Pipeline bug fixed 26 Sep 2026:** artifact URLs for 069–078 had been saved as bare ids, breaking their index
  links. urls.json must hold full https URLs; mkchecklist.py now refuses to run otherwise.
- **18-Sep cutoff not enforced (fixed 27 Sep 2026):** compute_stats.py defined END = 2026-09-18 but never applied it,
  so series pulled after 18 Sep leaked later bars into 2026 figures. 079's basket was published at −10.3% using
  closes to 25 Sep; at the 18-Sep cut it is −10.4% (republished). compute_stats.py, drivers.py, ytd.py and cyr.py now
  drop every bar after 18-Sep-2026 on load. Rerunning all sections changed only 049, 056 and 079: 056's difference is
  its hand-removed MPF Systems drawdown row (kept); **049's published 2026 figures (basket −13.8%, per-name YTDs)
  come from an earlier price vintage — the 18-Sep closes give −13.3% and several names differ by 1–5 points
  (e.g. Lux +2.3% not +7.1%). Corrected and republished 27 Sep 2026 with Prerak's approval: basket −13.3%,
  median −14%, 22 per-name figures re-cut at 18-Sep closes (verified against fresh TradingView pulls).** Never hand-edit a data_NNN.json
  without noting it here, since a rerun of compute_stats will overwrite it.
