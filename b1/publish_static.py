"""Build docs/ as a self-contained static site of every published primer.

Removes the dependency on claude.ai artifacts: after running this and enabling
GitHub Pages (Settings > Pages > Source: main, folder /docs), every primer has a
stable public URL at https://caprerakg.github.io/primer-pipeline/NNN.html

Run from b1/:  python publish_static.py
"""
import io, json, os, re, shutil, sys

B = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(B)
DOCS = os.path.join(ROOT, 'docs')
BASE_URL = 'https://caprerakg.github.io/primer-pipeline'

U = json.load(io.open(os.path.join(B, 'urls.json'), encoding='utf-8'))
os.makedirs(DOCS, exist_ok=True)

# 1. copy each primer page to docs/NNN.html
copied, missing = [], []
for no in sorted(U):
    src = os.path.join(B, 'out', f'{no}.html')
    if not os.path.exists(src):
        # 001 predates the pipeline and lives at the repo root
        alt = os.path.join(ROOT, '001_Agrochemicals.html')
        if no == '001' and os.path.exists(alt):
            src = alt
        else:
            missing.append(no)
            continue
    shutil.copy(src, os.path.join(DOCS, f'{no}.html'))
    copied.append(no)

# 2. index with relative links instead of artifact URLs
idx = io.open(os.path.join(B, 'out', 'index.html'), encoding='utf-8').read()
by_url = {}
for no, url in U.items():
    by_url[url] = no
    by_url[url.rstrip('/')] = no

def relink(m):
    url = m.group(1)
    no = by_url.get(url) or by_url.get(url.rstrip('/'))
    return f'href="{no}.html"' if no else m.group(0)

idx, n_rel = re.subn(r'href="(https://claude\.ai/artifact/[^"]+)"', relink, idx)
idx = idx.replace('<title>Industry Primer Library</title>',
                  '<title>Industry Primer Library</title>')
io.open(os.path.join(DOCS, 'index.html'), 'w', encoding='utf-8').write(idx)

# 3. GitHub Pages must not run Jekyll over these files
io.open(os.path.join(DOCS, '.nojekyll'), 'w', encoding='utf-8').write('')

left = len(re.findall(r'href="https://claude\.ai/artifact/', idx))
print(f'docs/: {len(copied)} primers copied, index relinked ({n_rel} links)')
if missing:
    print('  MISSING built page for:', missing)
if left:
    print(f'  WARNING: {left} artifact links still in index (url not in urls.json)')
print(f'  public URL once Pages is on: {BASE_URL}/index.html')
