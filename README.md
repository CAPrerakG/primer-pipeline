# Industry primer pipeline

Build pipeline for Prerak's 278-section industry primer series. The GitHub repo is the source of truth;
there is a local clone on Prerak's Desktop. Nothing is stored on OneDrive.

- `CHECKLIST.md` — what is done, what is next, what is deferred. Generated; do not edit by hand.
- `FAMILY_NOTES.md` — running theses per family and data traps already found.
- `b1/` — scripts, rosters, price cache, fragments (`frag_NNN.html` is the source of each primer), built pages in `b1/out/`.
- The procedure is the `industry-primer` skill, checked in at `.claude/skills/industry-primer/SKILL.md`.

Status of record: `b1/sections.json` (+ `b1/urls.json`). After each publish run `python mkchecklist.py` in `b1/`.
