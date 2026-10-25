"""Pre-results contracts for alternatives, family weighting and uncertainty."""
import sys
import hashlib
import json
from collections import Counter
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from harness_metrics import adoption_decision, best_set_score, empirical_p95, evaluate, paired_family_bootstrap


class HarnessMetricsTests(unittest.TestCase):
    def test_alternatives_are_complete_sets_not_their_union(self):
        result = best_set_score(["a"], [["a"], ["b"]])
        self.assertEqual(result["f1"], 1)
        self.assertEqual(result["exact"], 1)
        self.assertAlmostEqual(best_set_score(["a", "b"], [["a"], ["b"]])["f1"], 2 / 3)

    def test_multi_requires_complete_set_and_empty_rules_are_explicit(self):
        self.assertAlmostEqual(best_set_score(["a"], [["a", "b"]])["f1"], 2 / 3)
        self.assertEqual(best_set_score([], [[]])["f1"], 1)
        self.assertEqual(best_set_score(["x"], [[]])["recall"], 0)
        self.assertEqual(best_set_score([], [["a"]])["precision"], 0)

    def test_family_weighting_uncertainty_bounds_and_candidates(self):
        cases = [{"id": x} for x in ["one", "two", "three", "four"]]
        annotations = [
            {"id": "one", "family_id": "f1", "type": "single", "split": "development", "acceptable_sets": [["a"]], "uncertain": False},
            {"id": "two", "family_id": "f1", "type": "single", "split": "development", "acceptable_sets": [["a"]], "uncertain": False},
            {"id": "three", "family_id": "f2", "type": "multi", "split": "development", "acceptable_sets": [["b", "c"]], "uncertain": False},
            {"id": "four", "family_id": "f3", "type": "single", "split": "development", "acceptable_sets": [["d"]], "uncertain": True},
        ]
        result = evaluate(cases, annotations, {"one": ["a"], "two": ["a"], "three": [], "four": ["d"]},
                          candidates={"one": ["a"], "two": ["a"], "three": ["b"], "four": []}, require_status=False)
        self.assertEqual(result["family_macro"]["f1"], 0.5)
        self.assertAlmostEqual(result["case_mean"]["f1"], 2 / 3)
        self.assertEqual(result["coverage"]["resolved_cases"], 3)
        self.assertEqual(result["binary_success_bounds"]["case"], {"lower": 0.5, "upper": 0.75})
        self.assertEqual(result["binary_success_bounds"]["family"], {"lower": 1 / 3, "upper": 2 / 3})
        self.assertEqual(result["candidate_coverage"]["any_relevant"], 1)
        self.assertEqual(result["candidate_coverage"]["complete_set"], 0.5)

    def test_no_skill_ids_and_missing_predictions(self):
        cases = [{"id": "none"}]
        annotations = [{"id": "none", "family_id": "f", "type": "no-skill", "split": "development", "acceptable_sets": [[]], "uncertain": False}]
        result = evaluate(cases, annotations, {"none": ["unnecessary"]}, candidates={"none": []}, require_status=False)
        self.assertEqual(result["no_skill_false_positive"]["ids"], ["none"])
        self.assertIsNone(result["candidate_coverage"]["complete_set"])
        with self.assertRaises(ValueError):
            evaluate(cases, annotations, {})

    def test_bootstrap_is_paired_seeded_and_family_level(self):
        baseline = {"f1": 0.1, "f2": 0.4, "f3": 0.7}
        variant = {key: value + 0.1 for key, value in baseline.items()}
        result = paired_family_bootstrap(baseline, variant, replicates=200, seed=17)
        self.assertAlmostEqual(result["delta"], 0.1)
        self.assertAlmostEqual(result["lower"], 0.1)
        self.assertAlmostEqual(result["upper"], 0.1)
        self.assertEqual(result, paired_family_bootstrap(baseline, variant, replicates=200, seed=17))
        with self.assertRaises(ValueError):
            paired_family_bootstrap(baseline, {"f1": 1})
        opposite = paired_family_bootstrap({"a": 0, "b": 1}, {"a": 1, "b": 0}, replicates=1000, seed=17)
        self.assertEqual((opposite["delta"], opposite["lower"], opposite["upper"]), (0, -1, 1))

    def test_adoption_requires_all_predeclared_conditions(self):
        reliable = {"complete": True, "explicit_statuses": True, "case_ids": ["one"], "failure_count": 0}
        common = dict(delta=0.04, ci_lower=0.01, baseline_no_skill_fp_ids={"old"},
                      variant_no_skill_fp_ids={"old"}, baseline_latency_p95=10, variant_latency_p95=12,
                      baseline_cost_p95=1, variant_cost_p95=1.2, budget_ok=True, hard_timeout_ok=True,
                      baseline_reliability=reliable, variant_reliability=reliable)
        self.assertTrue(adoption_decision(**common)["adopt"])
        for change in [dict(delta=0.029), dict(ci_lower=0), dict(variant_no_skill_fp_ids={"new"}),
                       dict(variant_latency_p95=12.6), dict(variant_cost_p95=1.26), dict(budget_ok=False), dict(hard_timeout_ok=False)]:
            self.assertFalse(adoption_decision(**(common | change))["adopt"])
        for change in [
            dict(variant_reliability={**reliable, "failure_count": 1}),
            dict(baseline_reliability={**reliable, "failure_count": 1}),
            dict(baseline_reliability={**reliable, "complete": False}),
            dict(variant_reliability={**reliable, "explicit_statuses": False}),
            dict(variant_reliability={**reliable, "case_ids": ["another"]}),
        ]:
            self.assertFalse(adoption_decision(**(common | change))["adopt"])

    def test_failed_empty_is_not_correct_but_legal_empty_pool_skip_is(self):
        cases = [{"id": "none"}]
        labels = [{"id": "none", "family_id": "f", "type": "no-skill", "split": "development", "acceptable_sets": [[]], "uncertain": False}]
        for status in ["unavailable", "timeout", "error"]:
            result = evaluate(cases, labels, {"none": {"status": status, "skills": []}})
            self.assertEqual(result["family_macro"]["f1"], 0)
            self.assertEqual(result["family_macro"]["exact"], 0)
            self.assertEqual(result["reliability"]["failure_count"], 1)
            self.assertEqual(result["reliability"]["successful_fraction"], 0)
            self.assertEqual(result["no_skill_false_positive"]["correct_empty_count"], 0)
            self.assertEqual(result["no_skill_false_positive"]["failure_ids"], ["none"])
        for successful in [{"status": "completed", "skills": []},
                           {"status": "skipped-empty-pool", "skills": [], "candidate_count": 0}]:
            result = evaluate(cases, labels, {"none": successful}, candidates={"none": []})
            self.assertEqual(result["family_macro"]["f1"], 1)
            self.assertEqual(result["reliability"]["failure_count"], 0)
            self.assertEqual(result["no_skill_false_positive"]["correct_empty_count"], 1)
        with self.assertRaises(ValueError):
            evaluate(cases, labels, {"none": []})
        with self.assertRaises(ValueError):
            evaluate(cases, labels, {"none": {"status": "skipped-empty-pool", "skills": [], "candidate_count": 1}})
        with self.assertRaises(ValueError):
            evaluate(cases, labels, {"none": {"status": "skipped-empty-pool", "skills": [], "candidate_count": 0}}, candidates={"none": ["present"]})

    def test_failures_remain_in_quality_denominator_and_bound_uncertain_success(self):
        cases = [{"id": "good"}, {"id": "failed"}, {"id": "unknown"}]
        labels = [{"id": name, "family_id": "f", "type": "single", "split": "development", "acceptable_sets": [["a"]], "uncertain": name == "unknown"}
                  for name in ["good", "failed", "unknown"]]
        result = evaluate(cases, labels, {
            "good": {"status": "completed", "skills": ["a"]},
            "failed": {"status": "error", "skills": []},
            "unknown": {"status": "timeout", "skills": []},
        })
        self.assertEqual(result["family_macro"]["f1"], 0.5)
        self.assertEqual(result["coverage"]["resolved_cases"], 2)
        self.assertEqual(result["reliability"]["failure_count"], 2)
        self.assertEqual(result["binary_success_bounds"]["case"], {"lower": 1 / 3, "upper": 1 / 3})

    def test_observed_p95_has_a_fixed_interpolation_rule(self):
        self.assertEqual(empirical_p95([100, 0]), 95)
        self.assertEqual(empirical_p95([0]), 0)
        with self.assertRaises(ValueError):
            empirical_p95([])
        with self.assertRaises(ValueError):
            empirical_p95([float("nan")])


class PublicPilotFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.fixture = cls.root / "experiments/fixtures"
        cls.cases_doc = json.loads((cls.fixture / "harness_pilot_cases.json").read_text())
        cls.annotation_doc = json.loads((cls.fixture / "harness_primary_annotations.json").read_text())
        cls.contract = json.loads((cls.fixture / "harness_evaluation_contract.json").read_text())
        cls.cases = cls.cases_doc["cases"]
        cls.annotations = cls.annotation_doc["annotations"]

    def test_exact_sampling_counts_and_opaque_input_projection(self):
        self.assertEqual([row["id"] for row in self.cases], [f"p{i:03}" for i in range(1, 181)])
        self.assertEqual([row["id"] for row in self.annotations], [row["id"] for row in self.cases])
        self.assertEqual(Counter(row["type"] for row in self.annotations),
                         {"single": 60, "alternatives": 40, "multi": 30, "no-skill": 30, "followup": 20})
        self.assertEqual(Counter(row["split"] for row in self.annotations), {"development": 120, "holdout": 60})
        self.assertEqual(Counter(row["family_id"] for row in self.annotations), {f"f{i:02}": 5 for i in range(1, 37)})
        for case in self.cases:
            self.assertLessEqual(set(case), {"id", "latest", "conversation"})
            self.assertNotRegex(case["latest"].lower(), r"\b(?:use|load|invoke|enable) (?:the )?skills?\b")
        self.assertEqual(len({case["latest"] for case in self.cases}), 180)

    def test_split_identities_families_and_label_contract(self):
        identities = {split: set() for split in ["development", "holdout"]}
        family_splits = {}
        for row, case in zip(self.annotations, self.cases):
            family_splits.setdefault(row["family_id"], row["split"])
            self.assertEqual(family_splits[row["family_id"]], row["split"])
            targets = row["acceptable_sets"]
            identities[row["split"]].update(skill for target in targets for skill in target)
            self.assertIs(type(row["uncertain"]), bool)
            self.assertTrue(row["rationale"] and row["source_refs"])
            if row["uncertain"]:
                self.assertTrue(row["uncertainty_reason"])
            if row["type"] == "no-skill":
                self.assertEqual(targets, [[]])
            elif row["type"] == "multi":
                self.assertTrue(all(len(set(target)) >= 2 for target in targets))
            elif row["type"] == "alternatives":
                self.assertGreaterEqual(len({tuple(sorted(target)) for target in targets}), 2)
                self.assertTrue(all(targets))
            else:
                self.assertEqual(len(targets), 1)
                self.assertEqual(len(targets[0]), 1)
            if row["type"] == "followup":
                self.assertGreaterEqual(len(case["conversation"]), 2)
                self.assertLessEqual(len(case["latest"]), 60)
        self.assertFalse(identities["development"] & identities["holdout"])
        self.assertFalse(identities["holdout"] & {"typescript", "nginx", "sqlite", "markdown", "git"})

    def test_literal_skill_name_mentions_are_negative_in_each_split(self):
        cases = {row["id"]: row for row in self.cases}
        annotations = {row["id"]: row for row in self.annotations}
        for start, family, split, names in [
            (146, "f30", "development", ["git", "nginx", "sqlite", "markdown", "typescript"]),
            (151, "f31", "holdout", ["rust", "go", "mysql", "mongodb", "svelte"]),
        ]:
            for index, name in enumerate(names, start):
                case_id = f"p{index:03}"
                self.assertRegex(cases[case_id]["latest"], rf"\b{name}\b")
                row = annotations[case_id]
                self.assertEqual((row["family_id"], row["split"], row["type"]), (family, split, "no-skill"))
                self.assertEqual(row["acceptable_sets"], [[]])
                self.assertIn("literal", row["rationale"].lower())
                self.assertTrue(any(ref["path"] == f"skills/{name}/SKILL.md" for ref in row["source_refs"]))

    def test_source_evidence_and_frozen_hashes_match(self):
        source_hashes = {}
        for source in self.annotation_doc["evidence_sources"]:
            filename = self.root / source["path"]
            self.assertTrue(filename.is_file())
            self.assertEqual(hashlib.sha256(filename.read_bytes()).hexdigest(), source["sha256"])
            source_hashes[source["path"]] = source["sha256"]
        for row in self.annotations:
            for ref in row["source_refs"]:
                lines = (self.root / ref["path"]).read_text().splitlines()
                self.assertTrue(1 <= ref["line_start"] <= ref["line_end"] <= len(lines))
                self.assertEqual(ref["sha256"], source_hashes[ref["path"]])
        freeze = self.contract["freeze"]
        self.assertIsNotNone(freeze)
        for source in freeze["artifacts"]:
            self.assertEqual(hashlib.sha256((self.root / source["path"]).read_bytes()).hexdigest(), source["sha256"])
        for doc in [self.cases_doc, self.annotation_doc]:
            self.assertEqual(doc["rubric_sha256"], freeze["rubric_sha256"])
            self.assertEqual(doc["source_head"], self.contract["source_head"])
        catalog = sorted((self.root / "skills").glob("*/SKILL.md"))
        material = [(str(filename.relative_to(self.root)), hashlib.sha256(filename.read_bytes()).hexdigest()) for filename in catalog]
        canonical = json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        self.assertEqual(hashlib.sha256(canonical).hexdigest(), freeze["public_catalog_sha256"])
        self.assertEqual(len(catalog), self.cases_doc["public_catalog_skill_count"])


if __name__ == "__main__":
    unittest.main()
