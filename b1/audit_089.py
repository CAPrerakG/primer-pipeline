"""Reproduce 089 price sensitivities and restrict its drawdown panel to the basket.

Run after compute_stats.py 089. No prices are invented or filled forward.
"""
import json
from pathlib import Path
import pandas as pd

B = Path(__file__).resolve().parent
P = json.loads((B / 'prices.json').read_text())
R = json.loads((B / 'roster.json').read_text())['089']
CUT = 1789776000

def series(symbol):
    return pd.Series({pd.Timestamp(t, unit='s').normalize(): c
                      for t, c in P[symbol] if t < CUT}).sort_index()

for symbol in R['basket_syms']:
    assert series(symbol).index[-1] == pd.Timestamp('2026-09-18'), symbol

mr = pd.DataFrame({s: series(s).resample('ME').last().pct_change(fill_method=None)
                   for s in R['basket_syms']}).clip(-.5, .5)
nifty = series('NSE:NIFTY').resample('ME').last().pct_change()
cases = {
    'published basket': R['basket_syms'],
    'without HMT and Sharp': [s for s in R['basket_syms'] if s not in ['NSE:HMT', 'NSE:SCML']],
    'CNC OEM trio': ['NSE:JYOTICNC', 'NSE:MACPOWER', 'NSE:LOKESHMACH'],
}
result = {}
for label, symbols in cases.items():
    df = pd.DataFrame({'b': mr[symbols].mean(axis=1), 'n': nifty,
                       'count': mr[symbols].notna().sum(axis=1)}).dropna()
    df = df[(df.index >= '2011-07-31') & (df['count'] >= 2)]
    full = df[df.index < '2026-09-01']
    april = full[full.index.month == 4]
    ytd = df[df.index >= '2026-01-01']
    result[label] = {'symbols': symbols, 'first_month': str(df.index[0].date()),
                     'april_hit': int((april.b > april.n).sum()), 'april_n': len(april),
                     'april_mean_relative': round((april.b-april.n).mean()*100, 1),
                     'ytd': round(((1+ytd.b).prod()-1)*100, 1)}

member_returns = {}
for symbol in R['basket_syms']:
    s = series(symbol)
    annual = {}
    for year in range(2012, 2027):
        previous = s[s.index < f'{year}-01-01']
        current = s[(s.index >= f'{year}-01-01') & (s.index <= f'{year}-12-31')]
        if len(previous) and len(current):
            annual[str(year)] = round((current.iloc[-1]/previous.iloc[-1]-1)*100, 1)
    member_returns[symbol] = annual

data_path = B / 'data_089.json'
data = json.loads(data_path.read_text())
names = {m['co'].replace(' Limited', '').replace(' Ltd.', '').replace(' Ltd', '')
         for m in R['members'] if m['sym'] in R['basket_syms']}
data['dd'] = [row for row in data['dd'] if row['co'] in names]
data['drawdown_scope'] = 'Eight basket members only; excludes stale quotes and demerger returns.'
data_path.write_text(json.dumps(data), encoding='utf-8')
(B / 'sensitivity_089.json').write_text(json.dumps(
    {'data_date': '2026-09-18', 'method': 'same monthly clipping and equal weighting as compute_stats; at least two available names',
     'cases': result, 'member_calendar_returns': member_returns}, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
