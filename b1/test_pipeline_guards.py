"""Regression tests for failures that must stop automated primer processing."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from gate import assess, main
from check_primer import run_steps

class StopOnFailureTests(unittest.TestCase):
    def test_content_failure_has_nonzero_exit(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent / '.pipeline-cache') as tmp:
            root = Path(tmp)
            (root / 'out').mkdir()
            (root / 'out' / '999.html').write_text(
                '<p>critical but truncated</p><script>window.PRIMER_DATA={"cy":[],"notes":{}};</script>')
            with patch('gate.B', root):
                self.assertEqual(main(['999']), 1)

    def test_missing_year_note_is_a_failure_even_with_enough_content(self):
        body = '<p>critical ' + 'word ' * 5100 + '</p>'
        body += '<a href="https://example.com">source</a>' * 15
        body += '<dt>term</dt>' * 40 + '<details class="q">question</details>' * 8
        body += '<script>window.PRIMER_DATA=' + json.dumps({'cy': [{'y': 2026}], 'notes': {}}) + ';</script>'
        result = assess(body)
        self.assertFalse(result['passed'])
        self.assertEqual(result['missing'], [2026])

    def test_runner_does_not_execute_steps_after_failure(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent / '.pipeline-cache') as tmp:
            root = Path(tmp)
            marker = root / 'should_not_exist.txt'
            report = run_steps([
                ('fail', [sys.executable, '-c', 'raise SystemExit(7)']),
                ('later', [sys.executable, '-c', 'from pathlib import Path; Path("should_not_exist.txt").write_text("bad")']),
            ], root, root / 'report')
            self.assertFalse(report['passed'])
            self.assertEqual(len(report['steps']), 1)
            self.assertFalse(marker.exists())

if __name__ == '__main__':
    (Path(__file__).parent / '.pipeline-cache').mkdir(exist_ok=True)
    unittest.main()
