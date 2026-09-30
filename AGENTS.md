# AGENTS.md — operating contract for this repository

This repo builds Prerak's industry primer series: one self-contained HTML primer per industry
section in his TradingView watchlists (278 sections, Indian listed universe). **088 is published;
the next queued primer is 089, Machine Tools (16 names).**

Read in this order before doing anything: this file → `HANDOFF.md` →
`.claude/skills/industry-primer/SKILL.md` (the full pipeline spec) → `CHECKLIST.md` (what is done
and what is next) → `FAMILY_NOTES.md` (accumulated judgment and every data trap already found).

---

## Start every session with exactly this

```bash
git pull
pip install websocket-client pandas numpy      # not pre-installed in most sandboxes
python b1/prices_io.py unpack                  # prices.json is git-ignored; the .gz is the stored copy
cd b1 && python preflight.py                   # STOP if this exits non-zero
```

`preflight.py` checks packages, python3.12, the price cache, **live TradingView websocket access**,
Screener and BSE reachability, and git. If TradingView is unreachable you cannot pull prices for a new
section and the pipeline cannot proceed — say so and stop rather than working around it.

## Finish every primer with exactly this

```bash
cd b1
python build_primer.py NNN
python gate.py NNN                 # size floor: 5000 words, 15 links, 40 glossary terms, 8 questions
python verify.py NNN               # truth checks - MUST exit 0
python publish_static.py           # rebuilds docs/ for GitHub Pages
python mkchecklist.py
python3.12 mkindex.py && python publish_static.py
cd .. && python b1/prices_io.py pack
git add -A && git commit -m "Primer NNN: <name>" && git push
```

`gate.py` checks the page is big enough. **`verify.py` checks it is true** — series end on the data
date, the Nifty column matches canonical calendar returns, every year has a note, every cross-reference
points at a published primer, no bare artifact ids, corporate-action and gap scan, and a month-by-month
leaderboard so no false record is ever claimed. Every check in it exists because that mistake was
actually made at least once. **Do not publish on a FAIL.**

---

## Publishing: GitHub Pages, not Claude artifacts

Primers 001–081 were published as claude.ai artifacts and `b1/urls.json` still holds those URLs. They
are owned by the original Claude account and **cannot be updated from anywhere else** — leave them alone.

From 082 onward the canonical output is the static site in `docs/`:

- `python publish_static.py` writes every primer to `docs/NNN.html` plus a relinked `docs/index.html`.
- GitHub Pages serves `/docs` on `main` → `https://caprerakg.github.io/primer-pipeline/NNN.html`
  (the repository was made public on 30 Sep 2026, which is what Pages on the free plan requires).
- Record that full `https://…` URL in `b1/urls.json`. `mkchecklist.py` rejects bare ids.
- The pages also work straight off disk: open `docs/index.html` over `file://`. Relative links and the
  inline charts all work, so the site is readable without Pages at all.

If a primer's page does not appear at its URL within a couple of minutes of pushing, check
**Settings → Pages** is still set to source `main`, folder `/docs`. `publish_static.py` writes
`.nojekyll`, which Pages needs so it does not try to run Jekyll over the files.

---

## Non-negotiables

- **Data correctness is a hard requirement.** Never invent a number. Every figure comes from price data
  or a cited source. **Cross-check every profit against EPS × shares** — three million-vs-crore
  misprints have already been caught that way.
- **The data date is fixed at 18 September 2026.** Every basket, every YTD, every quoted price. The
  stats scripts drop later bars automatically; confirm each member series ends on that date before
  computing. Never move it.
- **No compromise on depth.** 001 Agrochemicals is the bar. Fix a gate failure by adding substance — a
  new sourced section, real glossary terms — never padding. Recent word counts: 078 6,589 · 080 9,256 ·
  081 13,603.
- **Keep the series' reading tools and analytical voice.** Every primer carries the glossary search
  block (`gq`, `gcount`, `gnone`) and at least four `box pm` analytical boxes. Group glossary terms under
  `<h3>` headings with a separate `<dl>` for each group, rather than one flat list. `verify.py` checks
  these structures in the built page. Keep `class="gl"` on the glossary section and a valid
  `viewBox` on each chart SVG: the shared JavaScript requires both, and verification checks them.
- **Order is Prerak's.** Follow the `CHECKLIST.md` queue. Financials, insurance, pharma, healthcare,
  hospitals and hotels are deferred until every other section is done.
- **No duplication.** Cross-reference as "see NNN" and check the number against `CHECKLIST.md`
  (`verify.py` check [4] does this).
- **Nothing is written outside this repo.** No OneDrive, Drive, Dropbox.
- **Commit and push to `main` after every finished primer**, so an interrupted run loses nothing.
- **Never claim a record without checking.** `verify.py` check [7] ranks every month against all 67
  baskets. A false superlative has already been published once.
- **Go to primary sources first.** BSE filing PDFs (`www.bseindia.com/xml-data/corpfiling/AttachHis/…`)
  and company investor decks are reachable with `curl -A "Mozilla/5.0"`; `nseindia.com` is not. Screener
  is fine for tables but see the column-shift trap below.

---

## Two traps that will bite you specifically

1. **Screener column drift.** Asking a page-summarising tool for "the last N quarters" has returned
   columns shifted by one or two. Ask explicitly for **the rightmost column's header date** and the same
   quarter a year earlier, then reconcile the four quarters against the annual row. Uncaught, this
   published "profit up 51%" instead of "profit down 51%".
2. **Other income.** In low-margin industries it routinely decides the sign of the bottom line. Read
   Screener's "Other Income" line before the profit line, every time.

## The Engineering family's three tests (carry these into subsequent Engineering primers)

- **078 Castings:** who writes the specification, and does the part wear out?
- **080 Forgings:** margin follows the weight class and the depth of machining, not the tonnes.
- **081 Metal Fabrication:** who carries the price of steel between the quote and the delivery?

082 is **Fasteners + Industrial Tools + Abrasives merged** (12 names; the merge is Prerak's own note in
`CHECKLIST.md` — disclose it on the page). Abrasives invert the 078 test: a grinding wheel is a
consumable that wears out and is often specified by its maker. Birla Precision (in 081) makes tool
holders, so it overlaps Industrial Tools — cross-reference 081, do not repeat it.

---

## Scripts

| Script | Run from | Purpose |
|---|---|---|
| `b1/preflight.py` | `b1/` | environment and network check — run first, every session |
| `b1/pull_prices.py` | repo root | pull daily closes for everything in `syms.json` |
| `b1/splice_bse_sel.py NNN` | repo root | splice BSE history onto NSE series that start late |
| `b1/compute_stats.py NNN` | repo root | basket, seasonality, calendar years → `data_NNN.json` |
| `b1/drivers.py NNN` | `b1/` | per-year movers and window hit rates |
| `b1/build_primer.py NNN` | `b1/` | fragment + data → `out/NNN.html` |
| `b1/gate.py NNN` | `b1/` | size floor |
| `b1/verify.py NNN` | `b1/` | **truth checks — must exit 0** |
| `b1/publish_static.py` | `b1/` | build `docs/` for GitHub Pages |
| `b1/mkchecklist.py` | `b1/` | regenerate `CHECKLIST.md` from `sections.json` |
| `b1/mkindex.py` | `b1/` | regenerate the index — **needs python3.12** |
| `b1/prices_io.py pack\|unpack` | repo root | the git-stored price cache |

`prices.json` is git-ignored. Always `unpack` at the start and `pack` before committing.
