"""Build and validate one primer; stop immediately when a required check fails.

This command does not publish, edit the queue, commit, or push. Financial/source
review is still required. Run from any directory: python b1/check_primer.py 091
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

B = Path(__file__).resolve().parent

def run_steps(steps, cwd, output):
    output.mkdir(parents=True, exist_ok=True)
    report = {'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'steps': [], 'passed': False}
    for label, command in steps:
        started = time.monotonic()
        process = subprocess.run(command, cwd=cwd, capture_output=True, text=True,
                                 env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
                                 encoding='utf-8', errors='replace')
        (output / f'{label}.log').write_text(process.stdout + process.stderr, encoding='utf-8')
        report['steps'].append({'name': label, 'exit_code': process.returncode,
                                'seconds': round(time.monotonic() - started, 2)})
        print(f'{label}: exit {process.returncode}', flush=True)
        if process.returncode:
            print(process.stdout[-2500:] + process.stderr[-1000:])
            break
    else:
        report['passed'] = True
    (output / 'checks.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    return report

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('number')
    parser.add_argument('--baseline', default='081')
    parser.add_argument('--channel', default='msedge')
    args = parser.parse_args()
    if not all(re.fullmatch(r'\d{3}', x) for x in [args.number, args.baseline]):
        parser.error('primer numbers must contain three digits')
    steps = [
        ('build', [sys.executable, 'build_primer.py', args.number]),
        ('gate', [sys.executable, 'gate.py', args.number]),
        ('verify', [sys.executable, 'verify.py', args.number]),
        ('baseline', [sys.executable, 'verify.py', args.baseline]),
        ('browser', [sys.executable, 'browser_check.py', args.number, '--channel', args.channel]),
    ]
    report = run_steps(steps, B, B / '.pipeline-cache' / 'checks' / args.number)
    print('CHECKS PASS; source/financial review remains required.' if report['passed']
          else 'CHECKS FAIL; do not publish.')
    return 0 if report['passed'] else 1

if __name__ == '__main__':
    sys.exit(main())
