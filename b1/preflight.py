"""Check the environment can actually run the pipeline. Run from b1/ FIRST, every session:

    python preflight.py

Exits non-zero if anything the pipeline depends on is missing or unreachable.
Written for agent sandboxes (Codex, Claude Code cloud) where network egress may be
allowlisted and packages are not pre-installed.
"""
import importlib, io, json, os, subprocess, sys, time

B = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(B)
bad = []
def ok(m):   print('  ok    ' + m)
def fail(m): bad.append(m); print('  FAIL  ' + m)
def warn(m): print('  warn  ' + m)

print('=== preflight ===\n[1] python packages')
for mod, pipname, why in [('websocket', 'websocket-client', 'tv_fetch.py - pulling prices'),
                          ('pandas', 'pandas', 'compute_stats.py'),
                          ('numpy', 'numpy', 'compute_stats.py')]:
    try:
        importlib.import_module(mod); ok(f'{mod}')
    except ImportError:
        fail(f'{mod} missing - pip install {pipname}   ({why})')

print('\n[2] python 3.12 for mkindex.py')
try:
    r = subprocess.run(['python3.12', '-c', 'print(1)'], capture_output=True, timeout=20)
    ok('python3.12 available') if r.returncode == 0 else fail('python3.12 not runnable')
except Exception:
    v = sys.version_info
    if (v.major, v.minor) >= (3, 12):
        ok(f'default python is {v.major}.{v.minor} - mkindex.py will run as `python`')
    else:
        fail(f'no python3.12 and default is {v.major}.{v.minor} - mkindex.py will fail on f-string quoting')

print('\n[3] price cache')
gz = os.path.join(B, 'prices.json.gz'); js = os.path.join(B, 'prices.json')
if not os.path.exists(js):
    fail('prices.json missing - run `python b1/prices_io.py unpack` from the repo root') if os.path.exists(gz) \
        else fail('neither prices.json nor prices.json.gz found')
else:
    P = json.load(io.open(js, encoding='utf-8'))
    ok(f'prices.json loaded, {len(P)} symbols')

print('\n[4] TradingView websocket (needed for every new primer)')
try:
    sys.path.insert(0, B)
    from tv_fetch import fetch
    t0 = time.time()
    rows, meta = fetch('NSE:NIFTY', '1D', 20, timeout=45)
    ok(f'fetched {len(rows)} NIFTY bars in {time.time()-t0:.1f}s')
except Exception as e:
    fail(f'TradingView unreachable: {type(e).__name__}: {e}\n'
         '        wss://data.tradingview.com must be allowed. Without it you cannot\n'
         '        pull prices for a new section, and the pipeline cannot proceed.')

print('\n[5] research sources')
try:
    import urllib.request
    for url, name in [('https://www.screener.in/company/SANSERA/', 'screener.in'),
                      ('https://www.bseindia.com/', 'bseindia.com (filing PDFs)')]:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            code = urllib.request.urlopen(req, timeout=25).status
            ok(f'{name} -> HTTP {code}')
        except Exception as e:
            warn(f'{name} unreachable ({type(e).__name__}) - research will be harder')
except Exception as e:
    warn(f'could not test HTTP: {e}')

print('\n[6] git')
try:
    r = subprocess.run(['git', '-C', ROOT, 'status', '--short'], capture_output=True, text=True, timeout=30)
    if r.returncode:
        fail('not a git checkout')
    else:
        dirty = [l for l in r.stdout.splitlines() if l.strip()]
        ok('clean working tree') if not dirty else warn(f'{len(dirty)} uncommitted change(s)')
        rr = subprocess.run(['git', '-C', ROOT, 'remote', 'get-url', 'origin'], capture_output=True, text=True, timeout=30)
        ok(f'origin {rr.stdout.strip()}') if rr.returncode == 0 else fail('no origin remote')
except Exception as e:
    fail(f'git unavailable: {e}')

print(f'\n=== preflight: {len(bad)} blocking problem(s) ===')
for b_ in bad:
    print('  - ' + b_.splitlines()[0])
sys.exit(1 if bad else 0)
