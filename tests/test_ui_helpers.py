"""Synthetic filesystem-only checks; no browser, provider or client systems."""
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1] / "ui"


class UiHelpers(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)

    def run_helper(self, skill, script, *args, success=True):
        result = subprocess.run(
            [sys.executable, "-B", str(ROOT / skill / "scripts" / script), *map(str, args)],
            cwd=self.work, capture_output=True, text=True, timeout=15,
        )
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def scaffold(self, *args, **kwargs):
        return self.run_helper("ui-frontend-implementation", "component_scaffold.py", *args, **kwargs)

    def manifest(self, *args, **kwargs):
        return self.run_helper("ui-asset-visual-automation", "asset_manifest.py", *args, **kwargs)

    def checklist(self, *args, **kwargs):
        return self.run_helper("ui-tooling-workflow", "ui_release_checklist.py", *args, **kwargs)

    def perf(self, *args, **kwargs):
        return self.run_helper("ui-performance-optimisation", "web_perf_snapshot.py", *args, **kwargs)

    def report(self, filename, audits):
        path = self.work / filename
        path.write_text(json.dumps({"audits": audits}), encoding="utf-8")
        return path

    def test_scaffold_valid_name_and_existing_file_protection(self):
        self.scaffold("review-card")
        target = self.work / "ReviewCard.tsx"
        self.assertIn("export function ReviewCard", target.read_text())
        target.write_text("existing user work", encoding="utf-8")
        self.scaffold("review-card", success=False)
        self.assertEqual(target.read_text(), "existing user work")
        self.scaffold("review-card", "--force")
        self.assertIn("export function ReviewCard", target.read_text())

    def test_scaffold_rejects_invalid_identifiers_before_creating_directory(self):
        for name in ["123card", "../escape", "bad name", "a/b", "", "bad--name", 'x"y']:
            with self.subTest(name=name):
                self.scaffold(name, "--out", "not-created", success=False)
                self.assertFalse((self.work / "not-created").exists())

    def test_checklist_preserves_existing_work_until_explicit_force(self):
        self.checklist("Synthetic release")
        target = self.work / "ui-release-checklist.md"
        self.assertIn("- [ ]", target.read_text())
        target.write_text("review notes", encoding="utf-8")
        self.checklist("New release", success=False)
        self.assertEqual(target.read_text(), "review notes")
        self.checklist("New release", "--force")
        self.assertIn("New release", target.read_text())

    def test_manifest_hashes_bytes_and_excludes_itself_on_repeat(self):
        assets = self.work / "assets"
        assets.mkdir()
        (assets / "icon.svg").write_bytes(b"<svg/>")
        target = assets / "manifest.json"
        self.manifest(assets, "--out", target)
        first = target.read_bytes()
        entries = json.loads(first)["files"]
        self.assertEqual(entries, [{
            "path": "icon.svg", "bytes": 6,
            "sha256": hashlib.sha256(b"<svg/>").hexdigest(),
        }])
        self.manifest(assets, "--out", target, success=False)
        self.assertEqual(target.read_bytes(), first)
        self.manifest(assets, "--out", target, "--force")
        self.assertEqual(target.read_bytes(), first)

    def test_manifest_missing_input_does_not_create_false_empty_result(self):
        self.manifest("missing", success=False)
        self.assertFalse((self.work / "asset-manifest.json").exists())

    def test_perf_units_deltas_and_missing_metrics(self):
        baseline = self.report("base.json", {
            "largest-contentful-paint": {"numericValue": 1500},
            "cumulative-layout-shift": {"numericValue": 0.12},
        })
        candidate = self.report("candidate.json", {
            "largest-contentful-paint": {"numericValue": 1200},
            "cumulative-layout-shift": {"numericValue": 0.02},
        })
        result = self.perf(baseline, "--candidate", candidate)
        rows = {r["Metric"]: r for r in csv.DictReader(io.StringIO(result.stdout))}
        self.assertEqual(rows["LCP"]["Unit"], "ms")
        self.assertEqual(rows["LCP"]["Delta"], "-300.00")
        self.assertEqual(rows["CLS"]["Unit"], "unitless")
        self.assertEqual(rows["CLS"]["Delta"], "-0.10")
        self.assertEqual(rows["TTI"]["Baseline"], "n/a")
        self.assertEqual(rows["TTI"]["Delta"], "n/a")

    def test_perf_baseline_only_does_not_invent_candidate(self):
        baseline = self.report("base.json", {})
        result = self.perf(baseline)
        rows = list(csv.DictReader(io.StringIO(result.stdout)))
        self.assertTrue(rows)
        self.assertTrue(all(r["Baseline"] == "n/a" and r["Candidate"] == "" for r in rows))

    def test_perf_rejects_malformed_or_non_numeric_reports(self):
        target = self.work / "invalid.json"
        for document in ["not json", "[]", '{"audits":[]}',
                         '{"audits":{"largest-contentful-paint":{"numericValue":"fast"}}}',
                         '{"audits":{"largest-contentful-paint":{"numericValue":true}}}',
                         '{"audits":{"largest-contentful-paint":{"numericValue":NaN}}}']:
            with self.subTest(document=document):
                target.write_text(document, encoding="utf-8")
                result = self.perf(target, success=False)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
