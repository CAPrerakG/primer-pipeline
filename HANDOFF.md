# Handoff — industry primer series

## Latest state: after 084 (30 Sep 2026)

084 Bearings is published at `https://caprerakg.github.io/primer-pipeline/084.html`: 16,163 words, 86 links,
88 glossary terms, 12 questions, four glossary groups and six analytical boxes. Fifteen companies covered;
eleven-stock basket. All selected prices end 18 September. SKF pair, SNL and Benara excluded with explanations.
Primary audits cover SKF perimeters, Vishal OCI/EPS mismatch, SKP qualified review, Galaxy sanctions removal,
Menon classification and Timken GGB restatement. `verify.py 084` and `verify.py 081` exit 0. Browser search/charts
tested. Verification now also enforces the .gl glossary class and valid chart viewBox.

Next: **085, Industrial Gears & Transmission + Hydraulics & Motion Control**, the queue-suggested merge
of order 9 (six names) and order 10 (eight names). Disclose the merge. Weekly usage checked after 084 was
30% used / 70% remaining; continue until approximately 50% remaining per Prerak.

### Previous completed primer: 083

The next queued primer is **084, Bearings (15 names)**. Primer 083, Welding & Cutting Equipment, covers all eight
watchlist names and is published at `https://caprerakg.github.io/primer-pipeline/083.html`. It has 13,966 words,
91 links, 86 glossary terms, 12 questions, four headed glossary groups and six analytical `box pm` asides.
Its six-stock price basket excludes Rasandik (auto components) and Technocrats (only 20 listed price bars).
The primary source and EPS audit is in `b1/audit_083.md`; company tables are preserved in
`b1/research_083_screener.json`. `verify.py 083` passed with three warnings for GEE price gaps in 2004–06,
before the July 2011 backtest. The same fixed price date, 18 September 2026, continues to apply.

Prerak has authorized continuing successive primers until the weekly Codex allowance reaches approximately 50%
remaining. Check the current account usage after each completed primer. Do not start another when the remaining
allowance is at or below that threshold. The remainder of this file preserves the original 081→082 handoff and
contains older status statements; use `AGENTS.md`, `CHECKLIST.md` and this latest block for current status.

_Written 30 Sep 2026, after primer 081 (Metal Fabrication & Engineering) was published and pushed._
_Updated 30 Sep 2026: the series is moving to **ChatGPT Codex / agent mode**. Publishing no longer depends
on Claude._

_If you are an agent: read `AGENTS.md` first — it is the operating contract. Then this file,
`.claude/skills/industry-primer/SKILL.md` (the full pipeline spec), `CHECKLIST.md` and `FAMILY_NOTES.md`._

---

## 1. Where things stand

| | |
|---|---|
| Repo | `github.com/CAPrerakG/primer-pipeline`, branch `main` — **the only master copy** |
| Last commit | `31c0d08` "Primer 081: Metal Fabrication & Engineering" |
| Published | **81 primers**, covering **85 of 278** watchlist sections |
| Queued | 154 sections; 39 deferred to the very end (financials, insurance, pharma, healthcare, hospitals, hotels) |
| Fixed data date | **18 September 2026** — every basket, every YTD, every price. Do not move it. |
| Next primer | **082** |

### What 082 is

The lowest-numbered queued section is **order 4, Fasteners (6 names)**, and `CHECKLIST.md` carries a
standing note to **merge Fasteners + Industrial Tools (3) + Abrasives (3)** into one primer — 12 names.
That merge is Prerak's own suggestion in the source file, so take it unless the roster argues otherwise,
and **disclose the merge on the page**. Set all three sections to `"status":"done","primer":"082"`.

One thing to check while building it: **Birla Precision Technologies** (in 081) makes AT3-class tool
holders and machine-tool accessories, so it overlaps the Industrial Tools section. Cross-reference 081;
do not repeat it.

---

## 2. Publishing — resolved (30 Sep 2026)

The series no longer depends on Claude to publish.

**What changed.** `b1/publish_static.py` writes every primer to `docs/NNN.html` and a relinked
`docs/index.html`. GitHub Pages serves `/docs` on `main`, so the canonical URL becomes
`https://caprerakg.github.io/primer-pipeline/NNN.html`. The pages are fully self-contained — inline CSS
and JS, no build step, no external dependency except Google Fonts, which degrade gracefully.

**Status: the repository was made public on 30 Sep 2026**, which is what GitHub Pages requires on the
free plan. One manual step remains and only Prerak can do it: **Settings → Pages → Source: Deploy from a
branch → `main` / `/docs`**. Once set, every primer is live at
`https://caprerakg.github.io/primer-pipeline/NNN.html` and each later push republishes automatically.

The pages also work straight off disk without Pages at all — pull the repo and open `docs/index.html`.
Relative links, the charts and the glossary search all work over `file://`.

**Because the repo is public, everything in it is world-readable**, including `FAMILY_NOTES.md`,
`base.json` and the full git history. It was scanned on 30 Sep 2026: no credentials or API keys. Local
Windows paths and internal folder names were removed at that point, and two scratch files
(`b1/idx_snip.txt`, `b1/mem_tail.txt`) that contained them were deleted. The commit author email in
history predates the change and cannot be removed without rewriting public history — not worth it.

**The old artifacts.** Primers 001–081 also exist as claude.ai artifacts; their URLs are in
`b1/urls.json`. Those are owned by the original Claude account, are **private**, and cannot be updated
from anywhere else. Leave them alone — the static copies in `docs/` are now the readable set, and being
public they also fix the problem that the artifact index linked to pages nobody else could open.

From 082 onward, record the **GitHub Pages URL** in `urls.json`.

## 3. Start of every run — exact sequence

```bash
git pull
pip install websocket-client pandas numpy   # not pre-installed in most sandboxes
python b1/prices_io.py unpack               # prices.json is git-ignored; the .gz is the stored copy
cd b1 && python preflight.py                # STOP if this exits non-zero
```

`preflight.py` verifies packages, python3.12, the price cache, **live TradingView websocket access**,
Screener and BSE reachability, and git. Prices are fetched per primer, so if TradingView is blocked in
your sandbox the pipeline cannot proceed — report it and stop rather than improvising.

Then read `CHECKLIST.md` (the "Next up" table), `FAMILY_NOTES.md`, and the most recent
`b1/frag_NNN.html` as the structural and stylistic template. **`b1/frag_081.html` is the current
template** — it is the longest and most complete in the series, and it is the only one that includes
the `<p id="now-stocks"></p>` hook (see §7).

### Fresh cloud container setup

A new cloud container starts bare. These are needed and none are pre-installed:

```bash
pip install websocket-client    # required by b1/tv_fetch.py — the TradingView fetcher
pip install pandas numpy        # required by b1/compute_stats.py
pip install playwright          # only if you want to render-check the page (Chromium is pre-installed)
```

- **`mkindex.py` needs Python 3.12.** The default `python` is 3.11 and will fail on same-quote nesting
  inside an f-string. Run it as `python3.12 mkindex.py`.
- Run `pull_prices.py`, `compute_stats.py` and `splice_bse_sel.py` **from the repo root**.
  Run everything else **from `b1/`**.
- To render-check before publishing (worth doing — it caught nothing on 081 but is cheap):
  Chromium is at `/opt/pw-browsers/chromium`. Never run `playwright install`.

---

## 4. Source reachability from a cloud container (tested 30 Sep 2026)

| Host | Status | Note |
|---|---|---|
| TradingView (via `b1/tv_fetch.py`) | ✅ works | the price backbone |
| screener.in | ✅ works | but see the column-shift trap in §8 |
| **www.bseindia.com filing PDFs** | ✅ **works via `curl`** | `WebFetch` gets 403; `curl -A "Mozilla/5.0"` returns 200 |
| Company investor-presentation PDFs | ✅ works via `curl` | e.g. `aequs.com/.../Investor-Presentation-Q1-FY-27.pdf` |
| nseindia.com | ❌ 403 | genuinely blocked from cloud IPs |

**The standing brief says "nseindia and bseindia block cloud IPs". That is only half true** — BSE
corporate-filing PDFs and company IR decks are reachable, and they are the primary sources. 081 was
built from Screener plus news summaries without using them; spot-checks afterwards against Aequs's own
deck and Artson's audited release found no errors, but **082 should go to the filings first.**

To read a PDF: `curl` it down, then `pip install pypdf` and extract text. (If `pypdf` throws a
`_cffi_backend` error, run `pip install -q --force-reinstall cffi cryptography` first.)

---

## 5. The non-negotiables

- **Data correctness is a hard requirement.** Never invent a number. Every figure comes from price data
  or a cited source. Cross-check profit against **EPS × shares**, every time.
- **No compromise on depth, ever.** 001 Agrochemicals is the bar. Fix a gate failure by adding substance
  — a new sourced section, real glossary terms — never padding.
- **Order is Prerak's:** follow the `CHECKLIST.md` queue.
- **No duplication** across primers — cross-reference as "see NNN", and verify the number points at the
  right primer in `CHECKLIST.md` before writing it.
- **Nothing is written outside the repo.** No OneDrive, Drive, Dropbox.
- **Commit and push to `main` after every finished primer**, so an interrupted run loses nothing.
- Before claiming any **record or superlative** ("the strongest month in the project"), grep every
  `b1/data_*.json` and check. This has already produced one published error — see §8.

### The quality gate

`python gate.py NNN` requires: words ≥ 5000, links ≥ 15, glossary `<dt>` ≥ 40, questions ≥ 8, a note for
**every** cy year, and the literal word "critical" somewhere on the page. Recent actuals, for calibration:

| | 078 | 079 | 080 | 081 |
|---|---|---|---|---|
| Words | 6,589 | 9,073 | 9,256 | **13,603** |
| Links | 18 | 48 | 45 | **55** |
| Glossary terms | 44 | 50 | 47 | **63** |

If `build_primer.py` reports fewer than 21 sections, **the fragment is truncated** — write it in one go.

---

## 6. The pipeline, in order

1. **Roster.** From `base.json` (`ind, co, sym, mcap, tv_ind, wl, isin`) build
   `b1/roster.json["NNN"] = {"ind", "members":[{sym,co,mcap,basic,status:"in",isin}], "moved_out":[]}`
   with `basic = tv_ind`. Append new symbols to `b1/syms.json`.
2. **Prices.** `python b1/pull_prices.py` from the root. Then confirm **every member series ends
   18-Sep-2026** and scan each for one-day moves ≤ −30% or ≥ +50% (corporate actions) and for trading
   gaps > 45 days.
3. **Repair short series.** `python b1/splice_bse_sel.py NNN` from the root splices BSE history onto
   NSE series that start late, scaled at the first overlapping day. If a symbol no longer resolves:
   `https://symbol-search.tradingview.com/symbol_search/?text=X&exchange=NSE&type=stock&hl=false&lang=en`
   (the v3 endpoint returns 400).
4. **Audit and basket.** Set `roster["NNN"]["basket_syms"]`. Exclude — and **disclose on the page** —
   listings too recent for the backtest, corporate-action discontinuities, misclassified businesses,
   subsidiaries of another member, and shells with no price discovery. **Check ISINs whenever two names
   look related.** A one-name basket is fine when that is the truth (067, 074, 077).
   Members may join mid-record as they list (precedent: 053, 057, 058, 081) — disclose it.
5. **Stats.** `python b1/compute_stats.py NNN` from the root; `python drivers.py NNN` from `b1/`.
   **Use the cy values in `data_NNN.json`** — the Nifty figure in drivers' printout can be a windowing
   artefact. Validate the Nifty column against: 2012 27.7, 2013 6.8, 2014 31.4, 2015 −4.1, 2016 3.0,
   2017 28.6, 2018 3.2, 2019 12.0, 2020 14.9, 2021 24.1, 2022 4.3, 2023 20.0, 2024 8.8, 2025 10.5,
   2026 YTD −10.7.
6. **Optional history column.** `python series.py "EXCH:SYM"` caches a benchmark in `series.json`.
   Check the series actually trades — some continuous futures print a constant.
7. **Research.** Latest quarter for every material member (revenue, EBITDA, margin, profit, volumes,
   guidance, capex), industry structure, policy, global context. Convert lakh to crore. Separate
   operating from other income. Cite everything.
8. **Write `b1/frag_NNN.html`**, copying `frag_081.html`'s structure exactly — the `<!--META{...}-->`
   block, the hero, the section ids, the four required boxes (`kid`, `client`, `pm`, `warn`), the chart
   hooks, and **`<p id="now-stocks"></p>` inside the `now` section**.
9. **Build and gate.** `python build_primer.py NNN` then `python gate.py NNN`, both from `b1/`.
10. **Verify, then publish.** `python verify.py NNN` **must exit 0** — it checks that every basket
    series ends on the data date, the Nifty column is canonical, every year has a note, every
    cross-reference resolves, no artifact id is bare, and where this basket's months actually rank
    against all 67 baskets (so no false record is claimed). Then `python publish_static.py` writes
    `docs/NNN.html`. Record the **full** GitHub Pages URL in `b1/urls.json` — never a bare id;
    `mkchecklist.py` refuses to run otherwise.
11. **Housekeeping, every time:** set each covered section `"status":"done","primer":"NNN"` in
    `b1/sections.json`; `python mkchecklist.py`; update the family line in `mkindex.py` if the family's
    thesis moved; `python3.12 mkindex.py` then `python publish_static.py`;
    append findings to `FAMILY_NOTES.md`; then
    `python b1/prices_io.py pack && git add -A && git commit && git push`.

---

## 7. Open items inherited from the 081 run

1. ~~Pipeline bug in 070–080~~ — **FIXED 30 Sep 2026.** `build_primer.py` only inserts the `now_note`
   where the fragment has `<p id="now-stocks"></p>`; fragments 070–080 all defined a `now_note` and none
   had the hook, so eleven published primers silently dropped the basket-vs-Nifty paragraph. The hook has
   been added to all eleven, they have been rebuilt and re-gated, and the corrected pages are in `docs/`.
   `verify.py` check [8] now fails any primer missing the hook, so it cannot recur. **The claude.ai
   artifacts for 070–080 still carry the old text** — only the original account can refresh those, and
   the static pages supersede them anyway.
2. **An enrichment to 081, offered and not applied.** Artson's audited FY26 release states the
   going-concern opinion rests on Tata Projects' support, which sharpens the page's existing
   "parentage is not a balance sheet" line. One sentence — now applyable by anyone, since the static
   page rebuilds from the fragment.
3. **Reclassifications worth making in Prerak's source file**, found in 081:
   Brady & Morris (material-handling equipment, not fabrication) · Ameya Precision (pump/valve
   components) · Misquita (filed under electronics distribution) · and **Omax Autos**, still sitting in
   Forgings when it belongs in Metal Fabrication.

---

## 8. Carry-forward knowledge

`FAMILY_NOTES.md` is the full record — read it. The parts that bear directly on 082:

### The Engineering family's three tests (078 → 080 → 081)
- **078 Castings:** in engineering the question is never what a company makes — it is **who writes the
  specification, and does the part wear out?**
- **080 Forgings:** **margin follows the weight class of the part and the depth of machining, not the
  tonnes.**
- **081 Metal Fabrication:** **who carries the price of steel between the quote and the delivery?**
  Where the customer fixes price first, margins are 3–11%; where the customer must qualify the supplier
  first, 19–29%.

**Apply all three to fasteners, tools and abrasives.** Abrasives should be interesting: a grinding wheel
is a *consumable that wears out* and is often specified by the abrasive maker — which is the 078 test
answering the other way for once. Fasteners are the opposite: catalogue parts, price-led, thin.

### Calendar findings
- **April is the family signal.** Three baskets share the project record of **14 of 15**: specialty
  chemicals (008, +8.7 pts), castings (078, +5.4), metal fabrication (081, +8.3). Forgings (080) is
  13 of 15. **No basket has ever managed 15 of 15.**
- When an April signal comes from a small-cap basket, say so — part of it is the market-wide small-cap
  April, and `build_primer.py` already prints a control line that strips out ~3 points.
- 081: March 2 of 15; Jan–Mar median −13.8 (weakest multi-company first quarter except salt, 015).

### Traps that have already cost something
- **Million-vs-crore misprints.** Three occurrences now, all from ScanX: Balu Forge, GMDC, and Sansera
  (Q1 FY27 profit printed as "₹866 crore"; correct ₹86.6 cr). **Always check profit against EPS × shares.**
- **Screener column labels drift in fetched summaries.** Asking a page summariser for "the last N
  quarters" returned columns shifted by one or two for MTAR, Aequs and ACGL in the 081 run. Caught on
  ACGL only because the arithmetic didn't reconcile — uncaught, it would have published "profit up 51%"
  instead of "profit down 51%". **Ask explicitly for the rightmost column's header date** and the same
  quarter a year earlier, then reconcile the four quarters against the annual row.
- **Profit that isn't operations.** Read Screener's "Other Income" line first, every time. 081 found four
  cases; IST Ltd had ₹87 cr of other income against ₹35 cr of revenue.
- **A basket choice can move a headline.** Excluding IST Ltd from 081 changed April from 15 of 15 to
  14 of 15. When an exclusion changes a headline number, **state the excluded alternative on the page.**
- **Check the ISIN before writing about any two related names.** 081 found Pritika Engineering
  (INE0MJQ01020) is a subsidiary of Pritika Auto (INE583R01029, filed in Castings), and Brady & Morris
  (INE856A01017) is 72.7% owned by W H Brady (INE855A01019) — one character apart.
- **A low price is not automatically a data error.** Salasar trades at ₹4.89 because its face value is ₹1.
  Check `shares = mcap / price` before assuming a bad feed.
- **Never hand-edit a `data_NNN.json`** without noting it in `FAMILY_NOTES.md` — a rerun of
  `compute_stats.py` overwrites it.

---

## 9. The prompt to open the next session with

> Resume the industry primer pipeline and build the next primer: 082 Fasteners, Industrial Tools &
> Abrasives (merged).
>
> Read `AGENTS.md` first, then `HANDOFF.md`, the `industry-primer` skill in
> `.claude/skills/industry-primer/SKILL.md`, `CHECKLIST.md` and `FAMILY_NOTES.md`.
>
> Run `python b1/preflight.py` before anything else and stop if it fails. Before publishing,
> `python b1/verify.py 082` must exit 0.
>
> The data date is fixed at 18-Sep-2026. Confirm every member series ends on 18-Sep before computing.
> Apply the Engineering family's three tests (078, 080, 081) and cross-reference them; do not repeat
> their content. Check every cross-reference number against `CHECKLIST.md`.
>
> When 082 is done, report its URL, word count, key audit findings and any corrections, then stop.
