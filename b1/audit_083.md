# Primer 083 source and arithmetic audit

Cut-off: 18 September 2026. All eight trimmed price series end on that date. The six basket series are ADOR, CLASSICEIL, DIFFNKG, ESABINDIA, GEE and RASIELEC. RASANDIK is an automotive stamping and vehicle maker despite using welding in production; TECHNOCRAT is a relevant equipment maker but has only 20 price observations after its 21 August listing.

## Reporting-period and annual reconciliation

Screener rightmost quarterly header was checked explicitly as **Jun 2026**, with **Jun 2025** as the year-earlier comparison. Classic's rightmost header is **Mar 2026**, but its SME columns are **half-years**, compared with Mar 2025. Technocrats uses its FY26 audited year. The downloaded table rows and URLs are retained in `research_083_screener.json`.

| Issuer | FY26 sum of four quarterly sales | FY26 annual sales | Four-quarter PAT | FY26 annual PAT | Interpretation |
|---|---:|---:|---:|---:|---|
| Ador consolidated | ₹1,140 cr | ₹1,140 cr | ₹82 cr | ₹82 cr | Exact |
| Diffusion consolidated | ₹408 cr | ₹407 cr | ₹50 cr | ₹50 cr | Whole-crore sales rounding |
| ESAB standalone | ₹1,509 cr | ₹1,508 cr | ₹207 cr | ₹207 cr | Whole-crore sales rounding |
| GEE standalone | ₹369.14 cr | ₹369 cr | ₹13.00 cr | ₹13 cr | Annual sales rounding |
| Rasi standalone | ₹72.01 cr | ₹72.02 cr | ₹3.52 cr | ₹3.52 cr | Hundredth-crore rounding |
| Rasandik standalone | ₹67.68 cr | ₹67.44 cr | −₹6.68 cr | −₹6.69 cr | ₹0.24 cr sales difference unresolved; excluded for product mismatch |

## Profit and EPS checks

| Issuer | Reported profit | EPS × share check | Source and caution |
|---|---:|---|---|
| Ador consolidated Q1 FY27 | ₹27.60 cr PAT | ₹15.86 × 1.74 cr shares = ₹27.60 cr | [Q1 filing](https://adorwelding.com/wp-content/uploads/2026/07/OutcomeBM21072026.pdf), figures in lakh |
| Classic H2 FY26 | ₹6.2046 cr PAT | ₹3.45 × about 1.80 cr shares ≈ ₹6.21 cr | [Company FY26 release](https://nsearchives.nseindia.com/corporate/CLASSICELECTRODES_19052026153746_Classic_press_release_final.pdf), SME half-year basis |
| Diffusion consolidated Q1 FY27 | ₹16.677 cr group PAT | Company diluted EPS ₹4.47 × 3.7426 cr **issued** shares ≈ ₹16.73 cr, ₹0.05 cr / 0.3% higher. Exact weighted denominator and owner-profit bridge required; summary EPS ₹4.44 is on a different basis. | [Company Q1 release](https://diffusionengineers.com/wp-content/uploads/2026/08/Press-Release-Q1-FY-2026-27.pdf), [FY26 capital](https://diffusionengineers.com/wp-content/uploads/2026/08/Diffusion_Annual-Report_2025_26.pdf). Do not force an exact reconciliation using issued shares. |
| ESAB standalone Q1 FY27 | ₹56.14 cr PAT | ₹36.47 × about 1.539 cr shares ≈ ₹56.14 cr | [Exchange filing](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_185478_11082026212944_iXBRL_WEB.html) |
| GEE standalone Q1 FY27 | ₹6.8455 cr PAT | ₹1.32 × 5.1977 cr shares ≈ ₹6.86 cr, EPS rounded | [Q1 filing](https://www.geelimited.com/uploads/gee_reports/5cbfb30e88babba1b41bdf7920d1903c.pdf), ₹1,039.54 lakh paid-up capital at ₹2 face |
| Rasi standalone Q1 FY27 | ₹1.33 cr PAT | ₹0.43 × about 3.11 cr shares ≈ ₹1.34 cr | [Quarter table](https://www.screener.in/company/531233/), [FY26 audited report](https://www.bseindia.com/xml-data/corpfiling/AttachHis/4e598704-c710-4137-9b37-88e15310834d.pdf); rounded EPS |
| Rasandik standalone Q1 FY27 | −₹0.71 cr PAT | −₹1.19 × about 0.598 cr shares ≈ −₹0.71 cr | [Quarter table](https://www.screener.in/company/522207/); outside basket |
| Technocrats FY26 | ₹14.936 cr PAT | ₹11.63 × 1.2841 cr weighted shares ≈ ₹14.93 cr | [FY26 audited annual report](https://www.technocratplasma.com/wp-content/uploads/2026/09/Annual-Report_05.09.2026_Final_V1.pdf), statement in ₹ thousands; FY25 EPS denominator formatting is inconsistent |

## Adjustments that change the reading

- **GEE:** The [Q1 filing](https://www.geelimited.com/uploads/gee_reports/5cbfb30e88babba1b41bdf7920d1903c.pdf) shows ordinary Other Income ₹0.3089 cr and a separate ₹3.6955 cr gain on sale of two properties. Screener's expanded “Other Income” rounds the sum to ₹4.00 cr. Reported PAT ₹6.8455 cr. The [deck](https://geelimited.com/uploads/gee_reports/15e843c0db6b7583935ff30f7a18b64a.pdf) calls ₹3.15 cr “adjusted PAT” by directly subtracting the pre-tax gain from after-tax PAT; it does not provide a tax-adjusted normalized result. Thane development-rights realization of ₹400-plus cr over five years is a company scenario, not received cash.
- **Diffusion:** Actual consolidated Other Income was about ₹4.10 cr, with another ₹4.46 cr share of associates. The [Q1 release](https://diffusionengineers.com/wp-content/uploads/2026/08/Press-Release-Q1-FY-2026-27.pdf) says prior-year standalone PAT included a ₹5.067 cr subsidiary dividend; the current parent PAT decline alone does not prove operating deterioration. Of ₹209.66 cr order book, ₹159.02 cr was heavy engineering, ₹26.42 cr wear products and ₹24.22 cr welding consumables. Its order book is chiefly project work, not repeat wire.
- **ESAB:** The [December 2025 exchange filing](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_141801_10022026220048_iXBRL_WEB.html) describes a ₹30.91 cr September land gain and ₹13.65 cr December labour-code gratuity charge. Screener folds these separately disclosed exceptional items into its expanded Other Income line. June 2026 ordinary Other Income was only ₹1.78 cr.
- **Ador:** [FY26 deck](https://adorwelding.com/wp-content/uploads/2026/07/Invtpptv1.pdf) identifies ₹24.8 cr onerous cost and potential liquidated damages on a delayed process-equipment job, and a ₹14.1 cr reversal of an old Kuwait receivable provision after cash collection. These are not normal electrode-factory margins.
- **Classic:** FY26 total income +18.5%, EBITDA +7.1%. H2 income +20.7%, EBITDA +2.7%; implied H2 EBITDA margin fell from about 11.57% to 9.85%.
- **Rasi:** FY26 operating sales fell from ₹81.44 cr to ₹72.02 cr, while Other Income increased from about ₹0.87 cr to ₹1.79 cr and PAT increased from ₹2.74 cr to ₹3.52 cr. Operating cash of about ₹6.43 cr exceeded PAT with a working-capital release.

The price calculation is in `data_083.json`. Three GEE price gaps of 339, 195 and 218 days occur in 2004–06, before the July 2011 backtest. `verify.py 083` should report these as warnings and no failures.
