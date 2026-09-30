# 084 Bearings — source and price audit

Price cutoff: 18 September 2026. Research uses filings and announcements available by that date. All amounts below are crore rupees unless stated. Rightmost Screener headers were read directly from HTML, not a page summary; see `research_084_screener.json` and `reconciliation_084.json`.

## Price eligibility and reproducibility

- Fifteen watchlist names reviewed; fourteen trimmed series end 18 September. Benara ends 11 September and has a 98-day gap in 2026. No price was forward-filled to manufacture the required endpoint. Benara is excluded.
- All eleven selected basket members were separately asserted to end 18 September **before** `compute_stats.py 084` ran. `price_audit_084.json` records each endpoint, all threshold moves and gaps.
- Austin: BSE history spliced onto its August 2026 NSE listing; scale about 1.041. Menon: BSE history spliced onto March 2015 NSE history; scale 0.998240655. The generic script skips an NSE series beginning before 2019, so Menon required a manual splice using its BSE symbol and overlapping first NSE close. Both are the same ISIN, not new IPOs.
- SNL (INE568F01017) excluded: NRB Bearings (INE349A01021) owns 73.45%, confirmed in SNL FY26 report. NRB Industrial (INE047O01014) is a separate demerged operating company, not that subsidiary.
- SKF India (INE640A01023) excluded because a price-only predecessor series across its October 2025 industrial demerger is not a verified combined shareholder return. The feed has no large one-day step, which alone does not prove the economic adjustment is correct. SKF Industrial (INE2J8701016) has only 195 bars, below the pipeline's 250-bar eligibility threshold; excluded from long-history basket. Both still receive full company analysis.
- No scanned one-day move below -30% or above +50%. Galaxy has four gaps in 2015–16; Vishal has seven in 2016–21; SNL one pre-backtest gap in 2008. These are disclosed, not suppressed.
- Base 11-stock basket: YTD +29.7%, April 13/15, average excess +5.6 points. Omitting Galaxy and Vishal: YTD +29.3%, April 12/15, +5.7 points. Omitting Menon: YTD +18.5%, April 11/15, +5.4 points. See `sensitivity_084.json`.
- The fragment's `data_extra.dd` will omit the four excluded names so a stale Benara quote and SKF predecessor peak are not displayed as comparable drawdowns. Raw computed data remains unchanged; the presentation filter is explicit here.

## Primary-source accounting findings

Sources are mapped by key to full filing URLs in `sources_084/manifest.json`.

### SKF pair

SKFINDIA_latest pp3–4: continuing standalone June revenue 587.79 versus 462.50; other income 12.37 versus 4.79; PAT 61.84 versus 46.74. Share count 4.9437963 crore; printed EPS 12.5 × shares = 61.7975, within one-decimal EPS rounding. Prior continuing EPS 9.5 × shares ≈46.966, also within rounding. Consolidated June PAT61.92 includes associate0.08; June2025 consolidated revenue1283.15/PAT118.21 includes the old industrial perimeter and is expressly not comparable. FY26 consolidated PAT265.94 is not an automotive-only recurring annual base. March tax includes the BAPA adjustment; FY26 continuing PAT117.22 is distorted by tax and exceptional charges.

SKFINDUS_latest: June revenue970.77, other income9.55, PAT61.92 (EPS12.52 ×4.9437963=61.8963, close to stated precision); prior June revenue820.63, other income10.34, PAT71.87, reconstructed industrial undertaking. FY26 revenue3440.36, ordinary other income59.12, exceptional expenses196.10, PAT217.67. March PAT118.97 includes a29.00 tax credit; note9 identifies55.66 adjustment of tax on pre-demerger profits. Do not annualise this quarter. FY EPS44.03 ×4.9437963=217.6754. Historic summary EPS71870 is a denominator artefact and is not used. Effective date1 October2025, one-for-one allotment, listed5 December2025. Land transfer costs163.92 disclosed separately.

### Schaeffler

SCHAEFFLER_latest: June is Q2CY26, not Q1FY27 for its reporting calendar. Group revenue2760.55, other income36.71, PAT325.78 versus287.11. EPS20.84 ×15.63 crore shares=325.7292; prior18.37 ×15.63=287.1231. Parent revenue2681.41 and PAT336.73 are a different perimeter. CY25 group PAT1150.35; EPS73.60 ×15.63=1150.368. Group H1 CFO389.35 versus711.90; inventory cash absorption489.21 and receivables161.58 explain pressure despite profit641.85 (half-year EPS41.07 ×15.63≈641.92). KRSV June subsidiary loss17.42 and negative net assets127.59 are disclosed by the review report; these are subsidiary figures and not given a listed-share EPS.

### Harsha

HARSHA_latest: group revenue457.43, other income5.13 plus JV profit0.03, PAT37.38 versus37.93. EPS4.11 ×9.104 crore shares=37.4174 (prior4.17 ×9.104=37.9637). FY26 PAT155.20 vs EPS17.05 ×9.104=155.2232. Engineering revenue421.08 is not consolidated total457.43; solar is36.35. Engineering EBITDA69.79 includes other income because company defines EBITDA as PBT plus finance and depreciation. Deck margin16.6% versus18.7% prior is not Screener operating margin. Call working capital116 days, not115 in a search summary. Raw material increase6–8%, not68%. Advantek/foreign subsidiary loss figures are subsidiary measures and have no listed-share EPS denominator.

### NRB Bearings and SNL

NRBBEARING_latest: group revenue369.53, ordinary other income5.47, separate insurance exceptional gain2.65. PAT37.76 includes0.92 minority; owner PAT36.84 reconciles to EPS3.80 ×9.69=36.822. Prior group32.81 less0.72 minority=32.09; EPS3.31 ×9.69=32.0739. FY26 group145.63 less2.88 minority=142.75; EPS14.73 ×9.69=142.7337. EPS-before-exceptionals3.60 is also separately printed. Insurance proceeds are not bearing operating margin. The filing flags25.12 of overdue foreign receivables.

SNL_latest: June sales15.25, other income1.24, PAT3.46; EPS9.58 ×0.361154≈3.460. FY26 PAT10.85; annual filing EPS30.05×0.361154≈10.8527. Rounded quarterly PAT sum10.86 differs by0.01; summary annual EPS30.04 and some quarterly EPS differ by0.01–0.02 from filings. Not an independent second exposure alongside its parent.

### Menon

MENONBE_latest image pp5–6 visually read: sales91.7888, other income2.5137, PBT18.5112, PAT14.1067 versus8.4295; EPS2.52 ×5.604=14.1221 (prior1.50 ×5.604=8.406), within rounding. FY26 sales293.8086, other income6.4349, PAT38.2513; EPS6.83 ×5.604=38.2753. Screener annual sales299 and other income1 do not match this classification; quarterly sales sum294 supports primary293.81. Do not silently use299. Company headline EBITDA22.3783 includes other income; PBT+finance1.3650+depreciation2.7624=22.6386, a0.2603 difference from its headline. Avoid claiming an exact operating EBITDA from that headline; derive operating result20.1249 by excluding other income. FY26 includes Alkop aluminium castings and Brakes, not pure bearing revenue.

### Rolex

ROLEXRINGS_latest: June sales304.337, other income19.836, PAT60.140, EPS2.21 ×27.233312=60.1856. Prior PAT49.156 vs1.81 ×27.233312=49.293 within EPS rounding. FY26 PAT141.098 vs5.18 ×27.233312=141.0686. March near-zero PAT was affected by50.40 right-of-recompense expense, partly offset by labour provision reversal1.205; annual exceptional51.641. The stock split is10-for1 with face value₹1 and restated EPS. One-crore-share buyback completed after June; do not use later shares for June EPS.

### Galaxy

GALXBRG_latest p7 visually read: revenue15.9492, other income2.9303, PBT3.9751, PAT2.9877; EPS9.40 ×0.318=2.9892. Prior PAT2.5921 vs8.15 ×0.318=2.5917. FY26 PAT3.3099 vs10.41 ×0.318=3.3104. FY26 revenue67.5111. A ScanX search headline says33.1 crore; that is tenfold too high. Ordinary quarterly bearing profit is materially less than reported PBT because other income is large. June legal costs0.969 crore identified in note4. OFAC designation30 October2024 was removed30 June2026, independently confirmed at https://ofac.treasury.gov/recent-actions/20260630 . The review paragraph discussing restrictions must be read with the subsequent removal note; do not call it currently sanctioned at the cutoff.

### Austin and NIBL

AUSTENG_latest: group June PAT0.9396 (owner0.9395), EPS2.70 ×0.34778=0.9390; other income about0.48, sales32.28. Primary prior EPS4.41 and annual13.93 differ slightly from summary4.40/13.92; use primary. FY26 group PAT4.8444 vs13.93 ×0.34778=4.8446. Its NSE admission is not a new business listing history.

NIBL_latest: sales18.9030, other income0.8567, loss before associate6.7227; associate profit0.1283 leaves loss6.5944. EPS−2.72 ×2.42305=−6.5907. Prior loss5.0888 vs−2.10 ×2.42305=−5.0884. FY26 loss29.4603 vs−12.16 ×2.42305=−29.4643. Negative net worth62.1535; promoter support letter underpins going-concern assumption. Unrecognised associate losses6.1808. Operating relevance does not imply financial health.

### SKP, Vishal and Benara — unresolved source problems disclosed

SKP_latest images pp6–7: group revenue22.1118, other income0.8282, PAT0.0398; EPS0.02 ×1.66=0.0332, difference0.0066 is within rounded EPS half-cent bound0.0083 crore. FY26 PAT0.8757 vsEPS0.53 ×1.66=0.8798. Quarterly summary PATsum0.93 exceeds0.8757 by0.0543; EPSsum0.57 differs fromannual0.53. Do not claim exact reconciliation. French subsidiary revenue7.2408 and loss2.4649 based on management-certified unreviewed statements; group auditor's review qualified. FY26 CFO0.9312; cashflow's closing29.56 lakh differs from components33.77 lakh, so no unqualified cash-balance inference. Listed SME uses Accounting Standards, not Ind AS.

VISHALBL_latest: revenue22.6504, other income0.0319, net loss0.8123 and OCI gain0.3286 produce total comprehensive loss0.4837. Printed EPS−0.45 ×1.0791=−0.4856 matches comprehensive loss, not PAT. Correct PAT/share arithmetic is−0.75276 (Screener−0.75). FY26 PAT loss0.7087 and OCI loss0.0713 produce comprehensive loss0.7800; printed/summary annual EPS−0.72 corresponds to comprehensive loss. Annual report text defines EPS excluding OCI but its table contradicts that policy. Flag source inconsistency; do not treat−0.45 as verified profit EPS. Four rounded quarter PATs sum−0.70, reconciling actual−0.7087 within rounding, not summary annual−0.78.

BENARA: summary rightmostMar2026 has semiannual figures; its Raw PDF link retrieved aSeptember2025 document. FY26 AR used instead. Parent revenue4.1155, other income0.9153, loss16.1025 vsEPS−9.09 ×1.77073=−16.0959 (rounding). Group loss16.1069 would round EPS−9.10, while group P&L repeats−9.09 and some pre-tax totals from parent; cashflow gives groupPBT−16.4976. Stock writeoff9.1007 and bad debts5.2385 are disclosed. Auditor cannot obtain sufficient evidence for going concern. Annual group EPS/summary classification remains inconsistent; no fine growth claim is made and it is excluded from basket.

## Annual reconciliation conclusion

Direct HTML reconciliation records the rightmost date, corresponding year-earlier date, four FY26 quarters (CY25 for Schaeffler), Other Income before PAT, and annual values. Large rounded tables can differ by1–2 crore. Menon classification, SKP quarterly sum, Vishal OCI/EPS and Benara source link/perimeter are real exceptions and are disclosed. NRB owner-profit differences are minority interests, not unit errors. No global claim that every source reconciled is made.

## Additional source/interpretation notes

- DPIIT Bearings QCO2025 PDF has a blank Gazette date and notification number: it is a draft, not evidence of a live blanket import restriction. Cite the draft as a policy proposal only.
- Engineering tests078/080/081 are cross-referenced and applied;082 tools/abrasives and083 welding are links for maintenance context, not duplicated company descriptions.
- An eleven-member price basket is neither eleven members in2011 nor a value-weighted industry index. Thin historic trading, survivorship, monthly±50% return clipping and price-only dividends exclusion are disclosed.
- No earlier primer figures or content were changed during084 research.

## Final Timken and supplementary EPS checks

Timken June consolidated results are in millions: sales943.320, Other Income10.733, PAT119.659 crore. EPS15.91 x7.5219 crore shares=119.6734. Prior PAT108.425 checks with primary EPS14.41 x7.5219=108.3906 (summary14.42 differs); FY26 PAT414.885 checks with55.16 x7.5219=414.9080. GGB acquired for128.8 crore, paid1Dec2025; common-control comparatives restated from1Apr2024. Prior subsidiary comparatives management-compiled, not independently reviewed to same extent. June tax reversal3.373 versus8.254 prior affects PAT comparison.

SKF India prior consolidated PAT118.21: EPS23.9 x4.9437963=118.1567. FY26 consolidated265.94: EPS53.8 x4.9437963=265.9762. Continuing standalone FY26117.22 corresponds to the filing's continuing EPS23.7 x4.9437963=117.1680, within one-decimal rounding. Current consolidated61.92 similarly checks with one-decimal EPS12.5. The61.48 BAPA amount includes7.28 interest separately presented as exceptional expense: do not add that interest twice. Schaeffler parent336.73 uses primary parent EPS21.54 x15.63=336.6702 within rounding.

## Page verification

Browser execution in headless Edge confirmed 88 glossary terms, live search, no-match state, 15 rendered annual rows and all three populated charts, with no JavaScript errors at desktop or mobile width. During draft inspection, missing chart viewBox and glossary .gl class were corrected before publication; verify.py now guards these dependencies as well as the existing search controls and analytical-box requirements. No earlier primer content or figures were changed.
