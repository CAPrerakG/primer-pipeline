# Primer 090 audit — Industrial Machinery & Foundry Equipment

Snapshot: 18 September 2026. Explicit merge of 28 Industrial Machinery and one
Foundry & Metal Processing Equipment source names. 29 roster rows; nine basket members.

## Price integrity

All nine included series end on 18 September before computation. No included
series triggers the daily −30%/+50% or >45-day gap screen. The 45 verify warnings
are on excluded names: Bharat Gears, GTT, Hardcastle, Lippi, Rathi, Rex, Rolcon and
Trishakti. Full event/date detail is in price_audit_090.json and verify_090.log.
Alphalogic ends 15 September, Rex 21 August, Rolcon 7 September; never forward-filled.

DISA (ISIN INE131C01011) and Cockerill (INE515A01019) had short NSE histories from
20 April 2026. Same-ISIN BSE prehistory was scaled at first overlap by
0.9963057851239668 and 1.0003844231730288 respectively. See price_repairs_090.json.
A comparison against HEAD's compressed price cache confirmed zero changes to any
previously cached symbol, preserving the earlier085 Veljan repair.

compute_stats.py uses monthly equal weighting, available members, minimum two,
±50% constituent monthly caps, starting July2011. audit_090.py reproduces the
sensitivity cases and reconstructs ALL nine drawdown rows, avoiding the generic
18-largest-roster display cap. The high is the 2020–2025-window high, not all-time.
Published YTD −2.5%; excluding Lloyds/Cockerill −15.6%; excluding recent SME
entrants +7.7%. April13/15,+7.6pts; April–July9/15,median+12.7pts.

## Financial source hierarchy

Original financial tables take precedence over raw Screener locators. Quarterly
headers explicitly checked for June2026/June2025; EMMIL/Sona use March2026/March2025
half-years. Manugraph consolidated locator is stale March2023; current standalone
used. Systematic locator duplicates quarterly columns; no quarterly assertion used.
Cockerill current consolidated filing restates acquired global metals operations;
no fabricated bridge from old standalone quarters to its calendar2025 annual row.

annual_reconciliation_090.json is a rounded locator DIAGNOSTIC, not a certified
primary statement. Missing restated quarterly data and display rounding remain
identified. eps_reconciliation_090.json contains primary amounts, EPS/share checks,
annual other-income/revenue context and exact half-year bridges.

Key original-PDF pages (PDF page number, including covers):
- DISA June p8 (million rupees), annual group cash p196, profit/EPS p237.
- ATV June p2; annual cash p45 and weighted-share EPS p55.
- Cockerill June group p12, cash p14; current deck and August call establish scope.
- Energy-Mission March result p16 (group), cash p18; annual note29 share count.
- Lloyds June group pp10–13; annual cash pp317–318, EPS note34 p355.
- Manugraph June p4: property disposal is exceptional, not ordinary other income.
- Sona March result p9 (visually checked); annual p110 tax signs conflict with
  the detailed result. Filed PAT −346.29 lakh reconciles only with a tax credit.
- T&I June pp3–4; annual cash p69.
- Walchandnagar June pp2–3; annual cash p69, EPS note49 p125.

## Findings and unresolved disclosure exceptions

- Lloyds annual EPS1.52 ×129.9831156crore weighted shares follows GROUP PAT197.57cr;
  owners189.88cr imply about1.46 on that denominator. June EPS0.47 is retained but
  its weighted owner basis is not independently established. Do not use closing
  shares as proof. June operating bridge66.15cr excludes ordinaryOI13.08cr, while
  company EBITDA79.23cr includes it. FY26 CFO−252.90cr versus rights financing857.23cr.
- Walchandnagar annual printed weighted5.8388207crore and EPS−2.17 do NOT reconcile
  loss14.68cr; diluted6.4459595 also fails. Closing shares cannot repair an annual
  weighted count. June other income6.97cr includes asset-sale gain3.34cr.
- Manugraph June reported PAT7.4644cr includes property gain9.7825cr and employee
  charge0.2703cr; ordinaryOI only0.0247cr. Operating bridge negative2.6742cr.
- Primary EPS differs from locators: Cockerill−63.52; Energy-Mission4.87 half-year/
  10.54annual; T&I3.62. Preserve the original figures and rounding.
- DISA FY26 CFO13.21cr versus PAT53.62cr; cash absorption is material.
- Cockerill H1 CFO82.3761cr is supported by contract liabilities and payables despite
  loss; parent and group order books overlap and cannot be added.
- Sona cash7.3254cr comes with asset releases and operating weakness; capex9.8124cr.
- Lloyds associate book4830.23cr is separate from consolidated2817.42cr.
- Walchandnagar871.77cr book is at March31; DISA276cr is June standalone;
  Energy-Mission47.23cr is a FY26 deck highlight without an independently established
  point-date. None is relabelled September.
- Volteron IP is at John Cockerill SA; do not assign all parent technology to the
  listed entity. Planned acquisitions/plants remain conditional/future.
- January2026 machinery omnibus withdrawal remains the current primary policy
  finding. ATV GST appeal status updated from the July17 event in its June filing.

## Classification

Twenty exclusions are individually disclosed. Hardcastle explicitly has no
manufacturing activity; GTT is technology services, Goblin luggage, Devson
chemicals, Rathi steel, Paluck/Trishakti rental, RBM/Sonu contractors, Millworks and
Rolcon components, Sealmatic/Rex sealing, Sumax consumables/distribution,
Systematic wire, Alphalogic storage structures, Chandni trading, Lippi nil sales.
Tipco is a relevant OEM excluded for only117 price observations, not poor results.

## Structural and browser verification

13,662 words including643 history-note words; 23 sections, 54 distinct external
sources (maximum four citations per URL), 19 tables, 72 terms/four glossary groups,
six PM boxes, twelve management questions plus six self-tests. Gate PASS.
verify090 exit0 (45 excluded-name warnings); verify081 exit0 (21 existing warnings).
Browser: four charts/57 bars,15annualrows,nine drawdownrows; search/no-match/reset
works; 390px layout has no page overflow, no JavaScript errors.
No earlier primer research, figures, output pages or cached prices changed.
