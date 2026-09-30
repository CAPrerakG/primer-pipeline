# Primer 089 — Machine Tools: completion audit

Data cutoff: 18 September 2026. Canonical page: https://caprerakg.github.io/primer-pipeline/089.html

## Content and rendering

- 16 source companies; eight included in the monthly basket.
- Built page: 13,967 words, 90 links, 43 distinct external source URLs, 66 glossary terms, 20 tables and five analytical boxes.
- All four charts render; calendar-year and drawdown tables contain 15 and eight rows respectively.
- Grouped glossary search, match count and no-results message work. The 390-pixel mobile viewport has no horizontal overflow. No browser JavaScript errors were observed.
- Browser results are recorded in `browser_audit_089.json`.

## Data and financial audit

- Every included member series ends on 18 September 2026. Emkay and Solitaire end on 17 September and are excluded; no prices were carried forward.
- Batliboi and Kennametal incomplete NSE histories were replaced with continuous BSE histories for the same securities, scaled using recent overlapping prices. The repair method and overlaps are recorded in `price_repairs_089.json`.
- None of the previously cached price series changed; 16 new series were added. No earlier primer's research or figures were rewritten.
- Corporate events, stale quotes and business-perimeter exclusions are disclosed. Emkay's transferred tools undertaking is not treated as the continuing listed business.
- Profit was checked against EPS and share counts. Owner-versus-group profit inconsistencies at Batliboi and Sunita, Sharp's half-year and annual reconciliation differences, and weighted-share limitations at Lokesh and Jainex are disclosed instead of silently repaired.
- Order books are distinguished from bids and capacity plans. Jyoti, Macpower and Kennametal cash conversion is examined alongside reported profit.
- The January 2026 rescission of the machinery safety omnibus technical regulation is reflected using the official Gazette; the withdrawn timetable is not presented as a catalyst.
- Raw financial tables, source inventory, annual bridges, EPS checks and basket sensitivity are retained in the accompanying `089` JSON audit files.

## Release checks

- `build_primer.py 089`: passed.
- `gate.py 089`: passed.
- `verify.py 089`: exit 0; zero failures, 58 historical gap/action warnings reviewed and disclosed.
- `verify.py 081`: exit 0; zero failures, 21 existing warnings.
- Static pages, checklist and index regenerated; price cache packed.

Prerak instructed the pipeline to stop after primer 089. Primer 090 must not be started until he resumes it.
