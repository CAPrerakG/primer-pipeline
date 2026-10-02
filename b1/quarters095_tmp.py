import requests,json,fitz,datetime
from bs4 import BeautifulSoup
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
x=json.load(open('b1/research_095_screener.json',encoding='utf-8'));base=Path('b1/sources_095');base.mkdir(exist_ok=True);jobs=[];headers={'User-Agent':'Mozilla/5.0'}
def run_inner(item):
 sym,v=item;n=sym.split(':')[1];p=max(v['pages'].values(),key=lambda z:datetime.datetime.strptime(z['tables']['quarters'][0][-1],'%b %Y') if z['tables'].get('quarters') and z['tables']['quarters'][0][-1] else datetime.datetime(1900,1,1));ss=BeautifulSoup(requests.get(p['url'],headers=headers,timeout=35).text,'html.parser');aa=ss.select('#quarters a[aria-label="Raw PDF"]');out=[]
 for key,a in zip(['annual','latest'],aa[-2:]):
  u=urljoin(p['url'],a['href']);r=requests.get(u,headers=headers,timeout=35,allow_redirects=False);u=r.headers.get('Location',u)
  if 'Pname=' in u:u='https://www.bseindia.com/xml-data/corpfiling/AttachHis/'+u.split('Pname=')[1]
  r=requests.get(u,headers=headers,timeout=45);r.raise_for_status();d=fitz.open(stream=r.content,filetype='pdf');t='\n'.join(f'\n--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d));k=n+'_'+key;(base/(k+'.pdf')).write_bytes(r.content);(base/(k+'.txt')).write_text(t,encoding='utf-8');out.append({'key':k,'url':u,'pages':len(d),'chars':len(t)});print(k,len(d),flush=True)
 return out
def run(item):
 try:return run_inner(item)
 except Exception as e: print(item[0],str(e),flush=True);return [{"key":item[0].split(":")[1]+"_quarter_error","error":str(e)}]
with ThreadPoolExecutor(1) as e:out=[r for rs in e.map(run,x.items()) for r in rs]
p=base/'manifest.json';m=json.loads(p.read_text()) if p.exists() else [];m+=out;p.write_text(json.dumps(m,indent=2))
