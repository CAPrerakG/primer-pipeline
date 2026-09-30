# Primer 082 audit — fixed 18 September 2026

## Scope and price cut

The primer merges FASTENERS (six names), INDUSTRIAL TOOLS (three) and ABRASIVES (three). Every symbol was fetched into `prices.json` and explicitly trimmed to bars with timestamp below `1789776000` before `compute_stats.py 082` and `drivers.py 082` ran. UTC date of the last retained bar is **2026-09-18 for all twelve**:

| Symbol | Retained observations | Last price (₹) | Basket |
|---|---:|---:|---|
| NSE:SUNDRMFAST | 4,992 | 1,228.20 | yes |
| NSE:GALAPREC | 504 | 1,011.20 | yes, after listing |
| NSE:STERTOOLS | 4,855 | 213.21 | yes |
| BSE:SIMMOND | 4,992 | 238.20 | yes |
| NSE:LAKPRE | 4,266 | 4.90 | no: stale operating accounts / insolvency |
| BSE:AUTOPINS | 812 | 177.00 | no: mainly suspension springs, large trading gaps |
| NSE:DENEERS | 798 | 172.25 | yes, after listing |
| BSE:TAPARIA | 146 | 14.03 | no: discontinuous trading, dividend steps |
| BSE:SPAR | 1,065 | 4.39 | no: virtually no current sales |
| NSE:GRINDWELL | 4,945 | 1,895.60 | yes |
| NSE:CARBORUNIV | 4,992 | 1,124.40 | yes |
| NSE:WENDT | 4,703 | 8,767.50 | yes |

`verify.py 082` exits 0. Its gap warnings are deliberate disclosures. Wendt's only flagged 116-day gap was in 2010, before the July 2011 basket start. Taparia has repeated months-to-years gaps and price discontinuities on dividend dates; Auto Pins has a 47-day 2026 gap.

## Financial checks

The Screener extraction is stored in `research_082_screener.json`. The **rightmost header** was read explicitly for each company and compared with the same period a year earlier: June 2026 / June 2025 for the quarterly reporters; March 2026 / March 2025 half-years for De Neers. Other Income was read before PAT. Statutory filings and company decks cited in the primer were used as the primary sources where available.

| Company | Profit basis and check | Issue resolved |
|---|---|---|
| Sundram | Consolidated owner PAT ₹168.69 cr; EPS ₹8.01 × ~21.1 cr shares ≈ ₹169 cr | Standalone parent revenue and exports kept separate from consolidated figures |
| Sterling | Group PAT ₹5.9 cr; EPS ₹1.61 × ~3.60 cr ≈ ₹5.80 cr (deck rounded) | Fastener parent PAT ₹16.4 cr is far higher than consolidated group PAT; EV subsidiaries dilute earnings |
| Gala | PAT ₹8.2 cr; basic EPS ~₹6.40 × ~1.28 cr ≈ ₹8.19 cr | Diluted EPS ₹6.25 has a different share denominator |
| Simmonds | PAT ₹3.84 cr; EPS ₹3.43 × ~1.12 cr ≈ ₹3.84 cr | Other Income fell from ₹0.39 cr to ₹0.11 cr, so profit gain is operating |
| De Neers | FY26 owner PAT ₹25.236 cr; EPS ₹29.32 × ~0.861 cr ≈ ₹25.24 cr | SME half-year reporting, audited trading segment, CFO ₹11.49 cr versus PAT ₹25.29 cr |
| Taparia | PAT ₹47.7576 cr; EPS ₹31.46 × 1.51788 cr shares ≈ ₹47.75 cr | Lakh-to-crore conversion validated; sparse quoted price cannot support ordinary P/E |
| Grindwell | PAT ₹115 cr; EPS ₹10.43 × ~11.07 cr ≈ ₹115.46 cr | Whole-crore table rounding; Other Income ₹25 cr versus ₹24 cr |
| CUMI | Group net profit ₹80.34 cr less non-controlling ₹3.94 cr = owner PAT ₹76.40 cr; EPS ~₹4.01 × 19.05 cr shares ≈ ₹76.39 cr | Abrasives PBIT ₹39.61 cr contains ₹25.18 cr leasehold-property gain; normalised for identified gain ≈ ₹14.43 cr |
| Wendt | Consolidated PAT ₹6.18 cr; EPS ₹30.90 × 0.20 cr shares = ₹6.18 cr | Parent PAT ₹8.00 cr differs; CUMI 37.5% owner after Wendt GmbH exit |

Four-quarter FY26 sales reconcile to annual rows: CUMI ₹5,206 cr, Grindwell ₹3,073 cr, Gala ₹314.30 cr, Sterling approximately ₹827.81 cr versus ₹828 cr rounded, Wendt ₹236.32 cr versus ₹236 cr rounded. CUMI quarterly PAT totals approximately ₹167 cr versus annual ₹168 cr after display rounding/scope. No figure from a summarised fetch was used without checking its header.

## Method boundaries

- The basket has six long-history operating names; De Neers and Gala join only after their listings. It is price-only and equal weighted monthly, with neither dividends nor trading costs.
- April is 11/15 at +4.6 points versus Nifty; August is 13/16 at +2.8 points. The run exposed a `verify.py` display bug that printed `/15` for every month. The verifier now uses each month's actual denominator and ranks by hit rate; the primer makes no project-record claim.
- The four excluded names remain in the page and drawdown roster. Taparia's displayed drawdown is expressly unreliable because of trading gaps and dividends.
- No earlier primer was modified in this run. References to 078, 080 and 081 apply their three analytical tests, with their previously published pages left intact.
