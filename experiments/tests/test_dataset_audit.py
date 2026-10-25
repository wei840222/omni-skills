"""Source identity and evidence boundaries of the skill-authored benchmark."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from audit_routing_dataset import audit_dataset, content_hash, write_audit


class DatasetAuditTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.dataset = self.root / "baseline"
        self.dataset.mkdir()
        self.skill = self.root / "skills" / "garden"
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text(
            "---\nname: garden\ndescription: Care for plants\nmetadata:\n  category: outdoors\n---\nGrow plants.\n"
        )
        self.records = [{"id": 1, "prompt": "My leaves are yellow", "expected": "Diagnose plants", "actual": "Check water", "pass": True}]
        self.save_sources()
        self.queries = [{"query_id": "garden_1", "ground_truth_skill": "garden", "natural_prompt": self.records[0]["prompt"], "expected": self.records[0]["expected"]}]
        self.save_snapshot()

    def save_sources(self):
        (self.skill / "test-prompts.json").write_text(json.dumps(self.records))

    def save_snapshot(self):
        slug = self.skill.name
        documents = {"name-description": [{"id": f"{slug}/name-description", "skill": slug, "path": f"skills/{slug}/SKILL.md", "text": f"{slug}\nFixture description"}]}
        manifest = {
            "schema_version": 2, "source_git_commit": "fixture-revision",
            "skill_count": 1, "query_count": len(self.queries),
            "queries_hash": content_hash(self.queries), "corpus_hash": content_hash(documents),
            "document_count_by_collection": {"name-description": 1},
            "source_files": {str(p.relative_to(self.root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in self.skill.iterdir()},
        }
        for filename, data in [("benchmark_queries.json", self.queries), ("documents.json", documents), ("manifest.json", manifest)]:
            (self.dataset / filename).write_text(json.dumps(data))

    def audit(self):
        return audit_dataset(self.root, self.dataset)

    def codes(self, audit):
        return {issue["code"] for issue in audit["structural_errors"]}

    def test_valid_snapshot_records_denominators_and_source_assertions(self):
        result = self.audit()
        self.assertTrue(result["structural_pass"])
        self.assertEqual(result["counts"]["generated_queries"], 1)
        self.assertEqual(result["counts"]["unique_query_ids"], 1)
        self.assertEqual(result["counts"]["identity_matched_queries"], 1)
        self.assertEqual(result["source_test_evidence"]["pass_assertions"], {"true": 1})
        self.assertEqual(result["source_test_evidence"]["fields"]["evidence"]["missing"], 1)
        self.assertEqual(result["metadata_inventory"]["category_values"], {"outdoors": ["garden"]})
        self.assertEqual(result["query_audits"][0]["source_record_sha256"], content_hash(self.records[0]))

    def test_duplicate_generated_and_source_ids_are_separate_errors(self):
        self.queries.append(self.queries[0].copy())
        self.records.append(self.records[0].copy())
        self.save_sources()
        self.save_snapshot()
        result = self.audit()
        self.assertFalse(result["structural_pass"])
        self.assertTrue({"duplicate_query_id", "duplicate_source_query_id"} <= self.codes(result))
        self.assertEqual(result["counts"]["generated_queries"], 2)
        self.assertEqual(result["counts"]["unique_query_ids"], 1)

    def test_unknown_skill_does_not_hide_missing_source_case(self):
        self.queries[0]["ground_truth_skill"] = "ghost"
        self.save_snapshot()
        result = self.audit()
        self.assertIn("unknown_skill", self.codes(result))
        self.assertIn("query_source_identity_mismatch", self.codes(result))

    def test_missing_source_hash_is_structural_but_missing_evidence_is_not(self):
        manifest = json.loads((self.dataset / "manifest.json").read_text())
        del manifest["source_files"]["skills/garden/test-prompts.json"]
        (self.dataset / "manifest.json").write_text(json.dumps(manifest))
        result = self.audit()
        self.assertIn("missing_source_hash", self.codes(result))
        self.assertEqual(result["source_test_evidence"]["fields"]["evidence"]["missing"], 1)
        self.assertNotIn("missing_evidence", self.codes(result))

    def test_changed_source_content_is_detected_even_when_query_is_unchanged(self):
        self.records[0]["actual"] = "A new answer after the snapshot"
        self.save_sources()
        result = self.audit()
        self.assertIn("source_content_changed", self.codes(result))
        self.assertEqual(result["counts"]["identity_matched_queries"], 1)

    def test_changed_generated_prompt_and_snapshot_hash_are_both_reported(self):
        self.queries[0]["natural_prompt"] = "An unrelated request"
        (self.dataset / "benchmark_queries.json").write_text(json.dumps(self.queries))
        result = self.audit()
        self.assertTrue({"queries_hash_mismatch", "query_source_identity_mismatch"} <= self.codes(result))

    def test_source_case_omission_has_complete_denominator(self):
        self.queries.clear()
        self.save_snapshot()
        result = self.audit()
        self.assertIn("missing_generated_query", self.codes(result))
        self.assertEqual(result["counts"]["source_test_records"], 1)
        self.assertEqual(result["counts"]["generated_queries"], 0)

    def test_false_pass_and_empty_evidence_remain_source_assertions(self):
        self.records[0].update({"pass": False, "evidence": ""})
        self.save_sources()
        self.save_snapshot()
        result = self.audit()
        self.assertTrue(result["structural_pass"])
        self.assertEqual(result["source_test_evidence"]["pass_assertions"], {"false": 1})
        self.assertEqual(result["source_test_evidence"]["fields"]["evidence"]["empty"], 1)

    def test_known_avalanche_issue_is_semantic_and_does_not_change_labels(self):
        self.skill.rename(self.skill.parent / "avalanche")
        self.skill = self.skill.parent / "avalanche"
        (self.skill / "SKILL.md").write_text("---\nname: avalanche\ndescription: AVAX on C-Chain\n---\nAvalanche blockchain.\n")
        self.records[0]["prompt"] = "Is this backcountry ski slope safe?"
        self.save_sources()
        self.queries[0].update({"query_id": "avalanche_1", "ground_truth_skill": "avalanche", "natural_prompt": self.records[0]["prompt"]})
        self.save_snapshot()
        result = self.audit()
        self.assertTrue(result["structural_pass"])
        issue = result["manual_semantic_issues"][0]
        self.assertEqual(issue["kind"], "manual_semantic_issue")
        self.assertEqual(issue["status"], "previously_confirmed_still_present")
        self.assertEqual(issue["query_ids"], ["avalanche_1"])
        self.assertEqual(json.loads((self.dataset / "benchmark_queries.json").read_text()), self.queries)

    def test_writer_refuses_to_overwrite_an_existing_audit(self):
        output = self.root / "run"
        path = write_audit(self.audit(), output)
        original = path.read_bytes()
        with self.assertRaises(FileExistsError):
            write_audit({"changed": True}, output)
        self.assertEqual(path.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
