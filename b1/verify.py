"""Mechanical pre-publish checks for a primer. Run from b1/:  python verify.py NNN

gate.py checks that the page is big enough. verify.py checks that it is TRUE.
Every check here exists because the corresponding mistake was actually made at
least once in primers 001-081. FAIL blocks publishing; WARN needs a human look.
"""
import datetime, glob, io, json, os, re, sys

B = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(B)
CUT = 1789776000                      # bars strictly before this = up to 18-Sep-2026
DATA_DATE = '2026-09-18'
NIFTY = {2012: 27.7, 2013: 6.8, 2014: 31.4, 2015: -4.1, 2016: 3.0, 2017: 28.6,
         2018: 3.2, 2019: 12.0, 2020: 14.9, 2021: 24.1, 2022: 4.3, 2023: 20.0,
         2024: 8.8, 2025: 10.5, 2026: -10.7}
MN = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

fails, warns = [], []
def fail(m): fails.append(m); print('  FAIL  ' + m)
def warn(m): warns.append(m); print('  warn  ' + m)
def ok(m):   print('  ok    ' + m)
def d(t):    return datetime.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')

no = sys.argv[1] if len(sys.argv) > 1 else sys.exit('usage: python verify.py NNN')
P = json.load(io.open(os.path.join(B, 'prices.json'), encoding='utf-8'))
R = json.load(io.open(os.path.join(B, 'roster.json'), encoding='utf-8'))[no]
D = json.load(io.open(os.path.join(B, f'data_{no}.json'), encoding='utf-8'))
U = json.load(io.open(os.path.join(B, 'urls.json'), encoding='utf-8'))
frag = io.open(os.path.join(B, f'frag_{no}.html'), encoding='utf-8').read()

print(f'\n=== verify {no}: {R["ind"]} ===')

# 1. every basket member's series ends on the project data date -------------
print('\n[1] price series end on ' + DATA_DATE)
basket = R.get('basket_syms') or []
if not basket:
    warn('no basket_syms set - compute_stats picked the basket automatically')
for s in basket:
    v = [r for r in (P.get(s) or []) if r[0] < CUT]
    if not v:
        fail(f'{s}: no price data at all')
    elif d(v[-1][0]) != DATA_DATE:
        fail(f'{s}: series ends {d(v[-1][0])}, not {DATA_DATE}')
if basket and not fails:
    ok(f'all {len(basket)} basket members end {DATA_DATE}')

# 2. the Nifty column must match the canonical calendar returns -------------
print('\n[2] Nifty calendar returns in data_%s.json' % no)
bad = [(c['y'], c['n'], NIFTY[c['y']]) for c in D.get('cy', [])
       if c['y'] in NIFTY and abs(c['n'] - NIFTY[c['y']]) > 0.15]
for y, got, exp in bad:
    fail(f'{y}: data says {got}, canonical is {exp} - windowing artefact?')
if not bad:
    ok(f'{len(D.get("cy", []))} years match')

# 3. a note for every calendar year -----------------------------------------
print('\n[3] one note per cy year')
meta = json.loads(re.search(r'<!--META(\{.*?\})-->', frag, re.S).group(1))
notes = meta.get('data_extra', {}).get('notes', {})
miss = [c['y'] for c in D.get('cy', []) if str(c['y']) not in notes]
fail(f'years without a note: {miss}') if miss else ok(f'{len(notes)} notes for {len(D.get("cy", []))} years')

# 4. cross-references point at published primers ----------------------------
print('\n[4] cross-references')
refs = set(re.findall(r'\((\d{3})\)', frag)) | set(re.findall(r'\bsee (\d{3})\b', frag))
for r in sorted(refs):
    if r == no:
        warn(f'({r}) is a self-reference')
    elif r not in U:
        fail(f'({r}) is not a published primer')
if refs and not [r for r in refs if r != no and r not in U]:
    ok(f'{len(refs)} references, all published: {", ".join(sorted(refs))}')

# 5. urls.json holds full URLs ----------------------------------------------
print('\n[5] urls.json')
bare = [k for k, v in U.items() if not str(v).startswith('https://')]
fail(f'bare artifact ids (mkchecklist will refuse): {bare}') if bare else ok(f'{len(U)} urls, all absolute')

# 6. corporate actions and trading gaps across the whole roster -------------
print('\n[6] corporate-action / gap scan (all roster members)')
hits = 0
for m in R['members']:
    v = [r for r in (P.get(m['sym']) or []) if r[0] < CUT]
    if len(v) < 2:
        continue
    for i in range(1, len(v)):
        a, b = v[i-1][1], v[i][1]
        if a > 0 and (b/a - 1 <= -0.30 or b/a - 1 >= 0.50):
            inb = ' [IN BASKET]' if m['sym'] in basket else ''
            warn(f'{m["sym"]} {d(v[i][0])}: {a:.2f} -> {b:.2f} ({(b/a-1)*100:+.0f}%){inb}')
            hits += 1
        if (v[i][0] - v[i-1][0]) / 86400 > 45:
            inb = ' [IN BASKET]' if m['sym'] in basket else ''
            warn(f'{m["sym"]}: {int((v[i][0]-v[i-1][0])/86400)}d gap {d(v[i-1][0])} -> {d(v[i][0])}{inb}')
            hits += 1
if not hits:
    ok('no single-day moves <=-30% or >=+50%, no gaps > 45 days')

# 7. superlative guard: rank this basket's months against every other -------
print('\n[7] month leaderboard - check before claiming any record')
allm = {}
for f in sorted(glob.glob(os.path.join(B, 'data_*.json'))):
    try:
        dd = json.load(io.open(f, encoding='utf-8'))
    except Exception:
        continue
    n2 = os.path.basename(f)[5:-5]
    for m in dd.get('monthly', []):
        if m['n'] >= 14:
            allm.setdefault(m['m'], []).append((m['hit'], m['n'], m['rel'], n2))
for m in sorted(allm):
    # Some month histories begin in 2011 and have 16 observations. Rank by hit
    # rate, and print the real denominator, rather than presenting 13/16 as 13/15.
    rows = sorted(allm[m], key=lambda x: (-x[0] / x[1], -x[2]))
    mine = [r for r in rows if r[3] == no]
    if not mine:
        continue
    rank = rows.index(mine[0]) + 1
    top = rows[0]
    tie = [r[3] for r in rows if r[0] / r[1] == mine[0][0] / mine[0][1]]
    line = (f'{MN[m-1]}: {no} is {mine[0][0]}/{mine[0][1]} at {mine[0][2]:+.1f} pts, rank {rank} of {len(rows)}'
            f'  (best: {top[3]} {top[0]}/{top[1]} at {top[2]:+.1f})')
    if rank == 1 and len(tie) == 1:
        print('  BEST  ' + line)
    elif mine[0][0] / mine[0][1] == rows[0][0] / rows[0][1]:
        print('  tied  ' + line + f'  tied with {", ".join(x for x in tie if x != no)}')
    else:
        print('        ' + line)

# 8. built page structure ----------------------------------------------------
print('\n[8] built page')
outp = os.path.join(B, 'out', f'{no}.html')
if not os.path.exists(outp):
    warn('not built yet - run build_primer.py')
else:
    h = io.open(outp, encoding='utf-8').read()
    secs = len(re.findall(r'<section id="', h))
    fail(f'only {secs} sections - fragment is truncated') if secs < 21 else ok(f'{secs} sections')
    if '<p id="now-stocks">' not in h:
        fail('no <p id="now-stocks"></p> hook - the now_note will be silently dropped')
    else:
        ok('now-stocks hook present')
    # Glossary search is optional in base.js, so a missing input otherwise
    # produces no visible error. Inspect the rendered markup, not JavaScript.
    body = re.sub(r'<(?:script|style)\b[^>]*>.*?</(?:script|style)>', '', h, flags=re.S | re.I)
    glossary = re.search(r'<section\b[^>]*id="glossary"[^>]*>.*?</section>', body, re.S)
    for element_id in ('gq', 'gcount', 'gnone'):
        if glossary is None or f'id="{element_id}"' not in glossary.group():
            fail(f'glossary search missing id="{element_id}"')
        else:
            ok(f'glossary search id="{element_id}" present')
    groups = len(re.findall(r'<h3\b[^>]*>.*?</h3>\s*<dl\b', glossary.group(), re.S)) if glossary else 0
    fail(f'glossary has only {groups} headed groups - use <h3> followed by <dl>') if groups < 2 else ok(f'glossary has {groups} headed groups')
    # base.js selects .gl dt; controls alone do not make search functional.
    glossary_tag = glossary.group().split('>', 1)[0] if glossary else ''
    glossary_class = re.search(r'\bclass="([^"]*)"', glossary_tag)
    if not glossary_class or 'gl' not in glossary_class.group(1).split():
        fail('glossary section missing class="gl" - search cannot find its terms')
    else:
        ok('glossary terms have the .gl search container')
    # chart() reads viewBox immediately; a missing value also prevents the
    # later history-table and glossary initialization from running.
    for svg in re.findall(r'<svg\b[^>]*\bdata-chart="[^"]+"[^>]*>', body):
        viewbox = re.search(r'\bviewBox="([^"]+)"', svg)
        try:
            coordinates = [float(v) for v in viewbox.group(1).split()] if viewbox else []
            valid = len(coordinates) == 4 and coordinates[2] > 0 and coordinates[3] > 0
        except ValueError:
            valid = False
        if not valid:
            fail('chart missing a valid four-number viewBox - base.js cannot render it')
    classes = re.findall(r'<(?:div|aside)\b[^>]*\bclass="([^"]+)"', body)
    pm_boxes = sum({'box', 'pm'} <= set(value.split()) for value in classes)
    fail(f'only {pm_boxes} box pm analytical boxes - need at least 4') if pm_boxes < 4 else ok(f'{pm_boxes} box pm analytical boxes')

print(f'\n=== {no}: {len(fails)} FAIL, {len(warns)} warn ===')
sys.exit(1 if fails else 0)
