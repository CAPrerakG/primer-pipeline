# Industry primer pipeline

Canonical home of the build pipeline for Prerak's 278-section industry primer series (moved here from a Windows
temp folder on 26 Sep 2026 so it is backed up by OneDrive).

- `CHECKLIST.md` — what is done, what is next, what is deferred. Generated; do not edit by hand.
- `FAMILY_NOTES.md` — running theses per family and data traps already found.
- `b1/` — scripts, rosters, price cache, fragments (`frag_NNN.html` is the source of each primer), built pages in `b1/out/`.
- The procedure is the `industry-primer` skill: `C:\Users\sayoni.n\.claude\skills\industry-primer\SKILL.md`.

Status of record: `b1/sections.json` (+ `b1/urls.json`). After each publish run `python mkchecklist.py` in `b1/`.
