"""Content floor for built primers; a failed page returns a nonzero exit code."""
import html
import json
import re
import sys
from pathlib import Path

B = Path(__file__).resolve().parent

def assess(page):
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', page, flags=re.S)
    match = re.search(r'window.PRIMER_DATA=(\{.*?\});</script>', page, flags=re.S)
    if not match:
        raise ValueError('built page is missing PRIMER_DATA')
    data = json.loads(match.group(1))
    notes = data.get('notes', {})
    note_words = sum(len(value.split()) for value in notes.values())
    words = len(html.unescape(re.sub(r'<[^>]+>', ' ', body)).split()) + note_words
    links = len(re.findall(r'<a href="http', body))
    glossary = len(re.findall(r'<dt>', body))
    questions = len(re.findall(r'<details class="q"', body))
    missing = [row['y'] for row in data.get('cy', []) if str(row['y']) not in notes]
    passed = (words >= 5000 and links >= 15 and glossary >= 40
              and questions >= 8 and not missing and 'critical' in body.lower())
    return dict(words=words, note_words=note_words, links=links, glossary=glossary,
                questions=questions, missing=missing, passed=passed)

def main(numbers):
    if not numbers:
        print('Usage: python gate.py NNN [NNN ...]', file=sys.stderr)
        return 2
    failed = False
    for number in numbers:
        try:
            if not re.fullmatch(r'\d{3}', number):
                raise ValueError('primer number must contain three digits')
            metrics = assess((B / 'out' / f'{number}.html').read_text(encoding='utf-8'))
            print(f"{number}: words {metrics['words']} (notes {metrics['note_words']}) "
                  f"links {metrics['links']} glossary {metrics['glossary']} "
                  f"questions {metrics['questions']} | years without note {metrics['missing']} "
                  f"| GATE {'PASS' if metrics['passed'] else 'FAIL'}")
            failed |= not metrics['passed']
        except (OSError, ValueError, KeyError, TypeError) as error:
            print(f'{number}: GATE FAIL: {error}')
            failed = True
    return int(failed)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
