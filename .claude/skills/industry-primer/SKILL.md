---
name: industry-primer
description: Build and publish the next industry primer in Prerak's 278-section TradingView watchlist series (Sowilo). Use when asked to continue, resume or write the next primer, when a scheduled primer run fires, or when fixing or republishing an existing primer. Covers the full pipeline — roster, prices, split scan, audit, stats, research, the 22-section page, the quality gate, publishing, the index and the checklist.
---

# Industry primer

One complete, self-contained HTML primer per industry section in Prerak's TradingView "Industry - ..." watchlists
(278 sections). Written from a senior analyst / fund-manager view for the Indian listed universe. A reader should
need no follow-up.

## Non-negotiables

- **Data correctness is a hard requirement.** Never invent a number. Every figure comes from price data or a cited
  source. When sources disagree, or a figure fails a sanity check against revenue, say so on the page.
- **No compromise on depth or quality, ever.** 001 Agrochemicals is the bar. Fix gate failures by adding
  substance — a new sourced section, real glossary terms — never padding.
- **Order is Prerak's:** follow the queue in `CHECKLIST.md`. Financials, capital markets, insurance, pharma,
  healthcare, hospitals and hotels are **deferred until every queued section is done**.
- **Usage:** call `mcp__ccd_session_mgmt__get_usage` before starting and after each primer. At **95%** of the
  5-hour or weekly window, finish the current primer, do the housekeeping, stop, and report. In a cloud session
  that tool may not exist; cloud runs draw on the cloud-session credit first, so keep going primer by primer and
  commit after each one so an interrupted run loses nothing.
- **No duplication** across primers — cross-reference as "see NNN".

## Paths (all relative to the repo root, github.com/CAPrerakG/primer-pipeline)

- Repo root (**run `b1/pull_prices.py`, `b1/compute_stats.py`, `b1/splice_bse_sel.py` from here**).
- Build folder (**run everything else from `b1/`**).
- Status of record: `CHECKLIST.md` (generated from `b1/sections.json`).
- Running theses and known data traps: `FAMILY_NOTES.md`.
- Finished pages: `b1/out/NNN.html`; `build_primer.py` also copies a named copy to `primers/`, which reaches
  Prerak's OneDrive `Industry Primers` folder when he pulls. (On his machine it copies there directly.)
- Index artifact (republish with `url`): https://claude.ai/artifact/28APxDNsNdKC2zXQmDH6dC
- The TradingView fetcher is `b1/tv_fetch.py` (needs the `websocket-client` package:
  `pip install websocket-client` if the import fails).

## Start of every run

0. **Git and prices.** `git pull`, then `python b1/prices_io.py unpack` (the price cache is stored as
   `b1/prices.json.gz`; `prices.json` itself is git-ignored).
1. Check usage.
2. Read `CHECKLIST.md` (the "Next up" table), `FAMILY_NOTES.md`, and the most recent `frag_NNN.html` as the
   structural and stylistic template.
3. Pick the lowest-order queued section. Merge small siblings when the note suggests it or when a section has
   fewer than about four usable names; disclose the merge on the page. The new primer number is one higher than the
   last published number.

## Pipeline

1. **Roster.** From `..\base.json` (fields `ind, co, sym, mcap, tv_ind, wl, isin`) add
   `roster.json["NNN"] = {"ind", "members":[{sym,co,mcap,basic,status:"in"}], "moved_out":[]}` with `basic = tv_ind`.
   Append new symbols to `syms.json`.
2. **Prices.** From the pipeline root: `python b1/pull_prices.py`. Then trim every series to **18-Sep-2026**
   (the project's fixed data date) and scan each member for one-day moves ≤ −30% or ≥ +50%.
3. **Repair short series.** If an NSE series starts late, splice BSE history (`python b1/splice_bse_sel.py NNN`
   from the root, or manually via `tv_fetch` scaled at the first overlapping day). If a symbol no longer resolves,
   find the successor with
   `https://symbol-search.tradingview.com/symbol_search/?text=X&exchange=NSE&type=stock&hl=false&lang=en`
   (the v3 endpoint returns 400).
4. **Audit and basket.** Set `roster["NNN"]["basket_syms"]`. Exclude and **disclose on the page**: listings too
   recent for the backtest, corporate-action discontinuities, misclassified businesses, subsidiaries of another
   member, and shells with no price discovery (typically 80–98% below an old high). **Check ISINs whenever two names
   look related.** A one-name basket is acceptable when that is the truth (067, 074, 077).
5. **Stats.** From the root: `python b1/compute_stats.py NNN`. From b1: `python drivers.py NNN` for per-year movers and
   window hit rates. **Use the cy values in `data_NNN.json`** — the Nifty figure in drivers' printout can be a
   windowing artefact. Validate against Nifty calendar returns: 2012 27.7, 2013 6.8, 2014 31.4, 2015 −4.1,
   2016 3.0, 2017 28.6, 2018 3.2, 2019 12.0, 2020 14.9, 2021 24.1, 2022 4.3, 2023 20.0, 2024 8.8, 2025 10.5,
   2026 YTD −10.7.
6. **Optional history column.** `python series.py "EXCH:SYM"` caches a benchmark series in `series.json`. Use
   year-end values trimmed to 18-Sep-2026 for 2026. Check that the series actually trades — some continuous
   futures print a constant value.
7. **Research.** Latest quarterly results for every material member (revenue, EBITDA, margin, profit, volumes,
   guidance, capex), industry structure, policy, and global context. Convert lakh to crore. Cross-check profit
   against revenue and EBITDA. Separate operating from other income. Cite everything.
8. **Write `frag_NNN.html`**, copying the structure of the latest fragment exactly:
   - A `<!--META{...}-->` block with keys `title, short, file, desc, season_note, now_note, data_extra`.
     `data_extra.notes` needs **one note for every cy year**; `data_extra.hx = {label, v:{year:value}}` is optional.
     With hx, the history table header order is **Year, hx, What happened, Basket, Nifty, Diff**.
   - `header.hero` (series line, h1, lede, meta spans, four stat tiles), then sections with ids: `brief`,
     `products`, `chain`, `players`, `money`, one or two special sections (5b, 5c), `rawmat`, `calendar`, `season`,
     `drivers`, `history`, `world`, `tech`, `policy`, `now`, `watch`, `proxies`, `ask`, `debates`, `glossary`,
     `test`, `sources`.
   - Required boxes: `box kid` (explain to a 10-year-old), `box client` (one-minute client pitch), `box pm`
     (fund-manager lens / how to use this / honest read), `box warn` (**The audit** — every exclusion and data
     problem).
   - Chart hooks: `svg[data-chart=month]`, `svg[data-chart=win][data-win=...]`, `svg[data-chart=year]`,
     `<div><!--SEASON--></div>`, and `tbody[data-table=cy]`.
   - Explain the value chain to a 10-year-old with an analogy; place every listed company on the chain; cover
     cycles and why outliers happened; seasonality with the exceptions explained; terminology; critical inputs;
     technology and country-leadership shifts; policy; proxies; concall questions; myths and debates.
9. **Build and gate.** From b1: `python build_primer.py NNN` then `python gate.py NNN`. The gate needs
   words ≥ 5000, links ≥ 15, glossary `<dt>` ≥ 40, questions ≥ 8, a note for every cy year, and the literal word
   "critical". Write the file in one go — a partial write has happened before; if the build shows fewer than 21
   sections, the file is truncated.
10. **Publish.** Artifact publish `b1/out/NNN.html` with a title, a one-word generic icon and a one-sentence
    description. **Save the full `https://claude.ai/artifact/...` URL** in `urls.json` (never a bare id).
11. **Housekeeping, every time:**
    - In `sections.json`, set each covered section to `"status": "done", "primer": "NNN"`.
    - `python mkchecklist.py` (it refuses to run if any URL is bare).
    - When a family starts or closes, edit its line in `mkindex.py`; then `python mkindex.py` and republish
      `b1/out/index.html` to the index URL above with `url` set.
    - Append any new through-line or data trap to `FAMILY_NOTES.md`.
    - **Commit and push after every primer**, so nothing is lost if the session ends:
      `python b1/prices_io.py pack`, then `git add -A && git commit -m "Primer NNN: <name>" && git push`.
      Commit directly to `main` — this repo is a working store, not a code-review project.

## Fixing a published primer

Edit its fragment, rebuild, re-gate, and republish to the **same URL** (from `urls.json`) with a short label. Record
the correction in `FAMILY_NOTES.md` and tell Prerak what changed and why.

## End of run

Report each primer's URL and word count, the most important audit findings, any corrections to earlier work,
classification errors worth fixing in his source file, and where the queue stands.
