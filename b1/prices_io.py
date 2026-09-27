# prices.json (~68 MB) is kept in git as prices.json.gz.
#   python prices_io.py unpack   -> before any work (creates/refreshes prices.json)
#   python prices_io.py pack     -> before committing (refreshes prices.json.gz)
import gzip, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW, GZ = os.path.join(HERE, 'prices.json'), os.path.join(HERE, 'prices.json.gz')

def unpack():
    if not os.path.exists(GZ):
        sys.exit('prices.json.gz missing')
    if os.path.exists(RAW) and os.path.getmtime(RAW) >= os.path.getmtime(GZ):
        print('prices.json is current'); return
    with gzip.open(GZ, 'rb') as f, open(RAW, 'wb') as g:
        shutil.copyfileobj(f, g)
    print('unpacked', os.path.getsize(RAW) // 1048576, 'MB')

def pack():
    with open(RAW, 'rb') as f, gzip.open(GZ, 'wb', compresslevel=9) as g:
        shutil.copyfileobj(f, g)
    print('packed', os.path.getsize(GZ) // 1048576, 'MB')

{'unpack': unpack, 'pack': pack}[sys.argv[1] if len(sys.argv) > 1 else 'unpack']()
