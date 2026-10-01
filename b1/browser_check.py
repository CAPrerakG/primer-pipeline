"""Render a built primer and check its data displays and glossary in a real browser.

Usage: python b1/browser_check.py 090 [--channel msedge]
Reports/screenshots go to b1/.pipeline-cache/checks, never published automatically.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent

def check(number, channel='msedge'):
    if not re.fullmatch(r'\d{3}', number):
        raise ValueError('primer number must contain three digits')
    path = B / 'out' / f'{number}.html'
    markup = path.read_text(encoding='utf-8')
    match = re.search(r'window.PRIMER_DATA=(\{.*?\});</script>', markup, re.S)
    if not match:
        raise ValueError('missing PRIMER_DATA')
    data = json.loads(match.group(1))
    output = B / '.pipeline-cache' / 'checks' / number
    output.mkdir(parents=True, exist_ok=True)
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel=channel, headless=True)
        try:
            page = browser.new_page(viewport={'width': 1440, 'height': 1000})
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(path.as_uri(), wait_until='load')
            result = page.evaluate('''() => ({
              charts: [...document.querySelectorAll('svg[data-chart]')].map(e => ({
                kind:e.dataset.chart, window:e.dataset.win || null,
                bars:e.querySelectorAll('rect').length})),
              annualRows:document.querySelectorAll('[data-table="cy"] tr').length,
              drawdownRows:document.querySelectorAll('[data-table="dd"] tr').length,
              terms:document.querySelectorAll('.gl dt').length,
              tables:document.querySelectorAll('main table').length,
              sections:document.querySelectorAll('main section[id]').length
            })''')
            failures = []
            def require(condition, message):
                if not condition:
                    failures.append(message)
            kinds = {x['kind'] for x in result['charts']}
            require({'month', 'year', 'win'} <= kinds, 'missing chart type')
            for chart in result['charts']:
                expected = (len(data.get('monthly', [])) if chart['kind'] == 'month'
                            else len(data.get('cy', [])) if chart['kind'] == 'year'
                            else len(data.get('wy', {}).get(chart['window'], [])))
                require(expected > 0 and chart['bars'] == expected,
                        f"{chart['kind']} {chart['window']}: expected {expected} bars, got {chart['bars']}")
            require(result['annualRows'] == len(data.get('cy', [])) > 0, 'annual table row mismatch')
            require(result['drawdownRows'] == len(data.get('dd', [])) > 0, 'drawdown table row mismatch')
            require(result['terms'] >= 40, 'too few glossary terms')
            require(result['tables'] >= 8, 'too few tables')
            term = page.locator('.gl dt').first.inner_text()
            page.locator('#gq').fill(term)
            require(page.locator('.gl dt:visible').count() >= 1, 'search hid its own term')
            require(not page.locator('#gnone').is_visible(), 'no-match shown for a matching term')
            result['matchedTerm'] = term
            result['matchedCount'] = page.locator('#gcount').inner_text()
            page.locator('#gq').fill('zzq-no-such-glossary-term-91637')
            require(page.locator('.gl dt:visible').count() == 0, 'nonmatching search leaves terms visible')
            require(page.locator('#gnone').is_visible(), 'no-match message missing')
            page.locator('#gq').fill('')
            require(page.locator('.gl dt:visible').count() == result['terms'], 'reset lost terms')
            page.locator('header.hero').scroll_into_view_if_needed()
            page.screenshot(path=str(output / 'desktop.png'))
            page.locator('#season').scroll_into_view_if_needed()
            page.screenshot(path=str(output / 'charts.png'))
            page.set_viewport_size({'width': 390, 'height': 844})
            page.goto(path.as_uri(), wait_until='load')
            result['mobileOverflow'] = page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
            require(not result['mobileOverflow'], 'mobile page overflows viewport')
            page.locator('header.hero').scroll_into_view_if_needed()
            page.screenshot(path=str(output / 'mobile.png'))
            require(not errors, 'JavaScript errors: ' + '; '.join(errors))
            result.update(errors=errors, failures=failures, passed=not failures)
            (output / 'browser.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
            return result
        finally:
            browser.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('number')
    parser.add_argument('--channel', default='msedge')
    args = parser.parse_args()
    try:
        result = check(args.number, args.channel)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result['passed'] else 1)
    except Exception as error:
        print(f'BROWSER FAIL: {error}', file=sys.stderr)
        sys.exit(1)
