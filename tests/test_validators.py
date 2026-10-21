"""Validator regressions; no skill/model behavior is scored here."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        shutil.copytree(ROOT / 'skills', self.root / 'skills')
        for name in ('tests/validate.py', 'evals/run.py', 'evals/cases.jsonl'):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, target)

    def assert_rejected(self, name, success_marker):
        for flags in ([], ['-O']):
            with self.subTest(flags=flags):
                result = subprocess.run([sys.executable, *flags, str(self.root / name)],
                                        capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertNotIn(success_marker, result.stdout)

    def test_missing_skill_section_fails_with_or_without_optimization(self):
        path = self.root / 'skills/meeting-to-actions/SKILL.md'
        path.write_text(path.read_text().replace('## Purpose', '## Missing Purpose'), encoding='utf-8')
        self.assert_rejected('tests/validate.py', 'SKILL_CONTRACT_PASS')

    def test_false_provenance_fails_with_or_without_optimization(self):
        path = self.root / 'evals/cases.jsonl'
        cases = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        cases[0]['ground_truth_status'] = 'human_verified'
        path.write_text('\n'.join(json.dumps(case) for case in cases), encoding='utf-8')
        self.assert_rejected('evals/run.py', 'FIXTURE_SCHEMA_PASS')


if __name__ == '__main__':
    unittest.main()
