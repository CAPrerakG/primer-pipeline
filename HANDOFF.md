# Handoff — resuming the industry primer series at 082

_Written 30 Sep 2026, after primer 081 (Metal Fabrication & Engineering) was published and pushed._
_This file is for a fresh Claude session, possibly on a different Claude account. Read it, then read
`CLAUDE.md`, `.claude/skills/industry-primer/SKILL.md`, `CHECKLIST.md` and `FAMILY_NOTES.md`._

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

## 2. ⚠️ If you are on a DIFFERENT Claude account, read this first

Everything in git transfers cleanly. **The published artifacts do not.**

1. **All 81 primer artifacts and the index are owned by the original account**
   (`sowiloconcallbot@gmail.com`). A different account **cannot republish to those URLs.**
2. The skill says every run must republish the index to
   `https://claude.ai/artifact/28APxDNsNdKC2zXQmDH6dC`. **From a new account that will fail.**
   You must instead publish `b1/out/index.html` as a **new artifact**, then:
   - update the index URL in `.claude/skills/industry-primer/SKILL.md` (the "Index artifact" line), and
   - tell Prerak the new index URL so he can replace his bookmark.
3. The 81 existing primer URLs in `b1/urls.json` still work as **links** — leave them alone. They stay
   readable; they just cannot be edited from the new account. If primer 081 or any earlier one ever needs
   a correction, it has to be done from the original account, or republished as a new artifact with a new
   URL recorded in `urls.json`.
4. **The individual primers are currently PRIVATE**; only the index is shared "anyone with the link".
   So the index's links open for Prerak but not for anyone he sends the index to. If the series is meant
   to be shareable, each primer's sharing has to be changed from its own Share menu — Claude cannot do
   this, only the owner can, and it is 81 manual changes. Worth raising with him before going further.

---

## 3. Start of every run — exact sequence

```bash
cd <repo root>
git pull
python b1/prices_io.py unpack        # prices.json is git-ignored; the .gz is the stored copy
```

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
10. **Publish** `b1/out/NNN.html` with a title, a one-word generic icon and a one-sentence description.
    Save the **full `https://claude.ai/artifact/...` URL** in `b1/urls.json` — never a bare id;
    `mkchecklist.py` refuses to run otherwise.
11. **Housekeeping, every time:** set each covered section `"status":"done","primer":"NNN"` in
    `b1/sections.json`; `python mkchecklist.py`; update the family line in `mkindex.py` if the family's
    thesis moved; `python3.12 mkindex.py`; republish `b1/out/index.html` (see §2 if on a new account);
    append findings to `FAMILY_NOTES.md`; then
    `python b1/prices_io.py pack && git add -A && git commit && git push`.

---

## 7. Open items inherited from the 081 run

1. **Pipeline bug, not fixed — Prerak's call.** `build_primer.py` only inserts the `now_note` where the
   fragment contains `<p id="now-stocks"></p>`. **Fragments 070–080 all define a `now_note` and none has
   the hook**, so eleven published primers silently dropped that paragraph (the basket-vs-Nifty line).
   081 has the hook. Fixing 070–080 = add one line to each fragment, rebuild, republish to the same URLs
   — **which requires the original account.**
2. **An enrichment to 081, offered and not applied.** Artson's audited FY26 release states the
   going-concern opinion rests on Tata Projects' support. That sharpens the page's existing
   "parentage is not a balance sheet" line. One sentence; needs the original account to republish.
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
> Read `HANDOFF.md` in the repo root first, then `CLAUDE.md`, the `industry-primer` skill,
> `CHECKLIST.md` and `FAMILY_NOTES.md`.
>
> The data date is fixed at 18-Sep-2026. Confirm every member series ends on 18-Sep before computing.
> Apply the Engineering family's three tests (078, 080, 081) and cross-reference them; do not repeat
> their content. Check every cross-reference number against `CHECKLIST.md`.
>
> If you are on a different Claude account from the one that published 001–081, read §2 of `HANDOFF.md`
> before publishing anything.
>
> When 082 is done, report its URL, word count, key audit findings and any corrections, then stop.
