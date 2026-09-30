# Structural repair audit: 083–088

Scope: restore presentation without changing price data, accounting figures, exclusions or research conclusions. META blocks and every glossary term/definition remain identical. No research-section numerical token was lost. Repeated methodological summaries were condensed to offset new headings; redundant URL citations were consolidated while keeping all distinct sources.

| Primer | Tables | Distinct external sources | Maximum citations per URL | Visible fragment words, before → after | Verify exit |
|---|---:|---:|---:|---:|---:|
| 083 | 8 | 33 | 4 | 12,810 → 12,790 | 0 |
| 084 | 8 | 42 | 4 | 15,090 → 15,088 | 0 |
| 085 | 8 | 44 | 4 | 15,248 → 15,244 | 0 |
| 086 | 8 | 37 | 4 | 15,014 → 15,009 | 0 |
| 087 | 8 | 39 | 4 | 15,235 → 15,211 | 0 |
| 088 | 10 | 27 | 4 | 16,809 → 16,637 | 0 |

Fragment counts exclude META comments and JavaScript-generated history notes. Gate/verify total-page counts include the history notes. Existing long primers 084–088 consequently retain the requested non-blocking >14,000-word warnings; no research was cut to force those historical pages below the future target.

## Verification

- Build, gate and verify run separately for 083, 084, 085, 086, 087 and 088; each exits 0. Regression check `verify.py 081` exits 0, with its existing gap warnings retained.
- Browser execution: no JavaScript errors; month/window/year chart bars populate in all six pages. Calendar-year and drawdown row counts equal the embedded data lengths. Glossary no-match/reset works. Mobile viewport is 390 px; tables scroll within their wrappers without widening the page.
- 083 now has 12 monthly bars, 15 window bars, 15 annual bars, 15 calendar-year rows and 7 drawdown rows. The restored figures/table markup follows 081, with 083-specific captions.
- Roster row counts for 084–088 are respectively 15, 14, 8, 8 and 7. Every listed company has business, latest reported evidence and basket treatment. Existing half-year/full-year and after-close information boundaries remain explicit.
- Negative tests run the actual verifier using in-memory altered inputs: removing each of the five hooks, reducing tables to seven, removing external sources, citing one URL over four times, or removing a players/money table each exits 1. Fake hooks inside comments do not satisfy the checks. Short and long page fixtures warn but exit 0.
- Permanent checks inspect HTML elements, not JavaScript strings or comments. Source fragments differing only by PDF page anchors count as one URL. Existing checks and final exit-code policy are retained.

Publishing remains GitHub Pages under docs/. The next new primer remains 089; its target is 11,000–14,000 words, with density over volume.
