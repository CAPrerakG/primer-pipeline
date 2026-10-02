import requests,json,time
from bs4 import BeautifulSoup
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
base={x['sym']:x for x in json.load(open('base.json',encoding='utf8'))}
r=json.load(open('b1/roster.json'))['095'];headers={'User-Agent':'Mozilla/5.0'}
def run(m):
 k=m['sym'].split(':')[1] if (m['sym'].startswith('NSE:') and '_' not in m['sym']) else base[m['sym']]['bse_code'];pages={}
 for suffix in ['consolidated/','']:
  url=f'https://www.screener.in/company/{k}/{suffix}';resp=requests.get(url,headers=headers,timeout=40);s=BeautifulSoup(resp.text,'html.parser');tables={}
  for id in ['quarters','profit-loss','balance-sheet','cash-flow','ratios']:
   el=s.find(id=id)
   if el:tables[id]=[[td.get_text(' ',strip=True) for td in tr.find_all(['th','td'])] for tr in el.select('table tr')]
  pages[suffix or 'standalone']={'url':url,'status':resp.status_code,'tables':tables,'about':s.get_text(' ',strip=True)[:5500],'links':[{'text':a.get_text(' ',strip=True),'url':a['href']} for a in s.select('a[href]') if any(t in a['href'] for t in ['bseindia','nseindia','.pdf'])]}
  time.sleep(1)
 print(m['sym'],[(k,v['status']) for k,v in pages.items()],flush=True);return m['sym'],{'company':m['co'],'pages':pages}
with ThreadPoolExecutor(3) as e:out=dict(e.map(run,r['members']))
Path('b1/research_095_screener.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
