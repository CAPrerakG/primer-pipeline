import requests,json,re,fitz,time
from pathlib import Path
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
x=json.load(open('b1/research_095_screener.json',encoding='utf-8'));base=Path('b1/sources_095');base.mkdir(exist_ok=True);jobs=[]
def normalize(u):
 if 'AnnPdfOpen.aspx?Pname=' in u:return 'https://www.bseindia.com/xml-data/corpfiling/AttachHis/'+u.split('Pname=')[1]
 return u
for sym,v in x.items():
 n=sym.split(':')[1];p=v['pages']['consolidated/'];p=p if len(p['tables'].get('quarters',[[]])[0])>2 else v['pages']['standalone']
 for label,key in [('Annual Report 2026','AR'),('PPT','deck'),('Transcript','call')]:
  ls=[l for l in p['links'] if l['text']==label]
  if ls:jobs.append((n+'_'+key,normalize(ls[0]['url'])))
 s=BeautifulSoup(requests.get(p['url'],headers={'User-Agent':'Mozilla/5.0'},timeout=30).text,'html.parser');sec=s.find(id='quarters');a=sec.select('a[href]') if sec else []
 # quarterly PDF anchors contain linked icons rather than visible text
 aa=[z['href'] for z in a if 'bseindia' in z['href'] or 'nseindia' in z['href']]
 if aa:
  jobs.extend([(n+'_latest',normalize(aa[-1])),(n+'_annual',normalize(aa[-2]))])
 print(n,'quarter PDFs',len(aa),flush=True)
def run(job):
 k,u=job
 try:
  r=requests.get(u,headers={'User-Agent':'Mozilla/5.0'},timeout=50);r.raise_for_status();d=fitz.open(stream=r.content,filetype='pdf');t='\n'.join(f'\n--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d));(base/(k+'.pdf')).write_bytes(r.content);(base/(k+'.txt')).write_text(t,encoding='utf-8');print(k,len(d),flush=True);return {'key':k,'url':u,'pages':len(d),'chars':len(t)}
 except Exception as e:print(k,str(e),flush=True);return {'key':k,'url':u,'error':str(e)}
with ThreadPoolExecutor(3) as e:out=list(e.map(run,jobs))
(base/'manifest.json').write_text(json.dumps(out,indent=2))
