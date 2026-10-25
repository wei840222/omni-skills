"""Launcher guards and stdin projection, with no real child/network calls."""

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from run_harness_stage import build_settings, normalize_endpoint, run_stage


class HarnessStageTests(unittest.TestCase):
    def setUp(self):
        parent = Path(__file__).resolve().parents[1] / "datasets" / "stage-launcher-tests"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(self.temporary.cleanup)
        self.workspace = Path(self.temporary.name)
        self.run = self.workspace / "experiments/datasets/run"
        self.fixtures = self.workspace / "experiments/fixtures"
        self.run.mkdir(parents=True)
        self.fixtures.mkdir(parents=True)
        cases = [{"id": f"c{i:03}", "latest": f"Public task {i}", "expected": "LABEL_SENTINEL"} for i in range(180)]
        cases[0]["conversation"] = [{"role": "user", "text": "Public history", "family": "LABEL_SENTINEL"}]
        self.cases = self.write(self.fixtures / "harness_pilot_cases.json", {"cases": cases})
        self.contract = self.write(self.fixtures / "harness_evaluation_contract.json", {"frozen": True})
        self.protocol = self.write(self.fixtures / "harness_ablation_protocol.json", {"frozen": True})
        self.policy = {"qmd": {"timeoutMs": 15000}, "skills": {"search": {"collectionWeights": {"meta": 3, "body": 2, "references": 1}}}, "routing": {"skills": {"maxInjectedSkills": 6, "relevanceThreshold": 0.4, "search": {"minCandidateScore": 0.3, "timeoutMs": 15000}, "nameMatch": {"genericTokens": [], "maxEditDistance": 2, "minJaccardScore": 0.4}}}}
        self.write(self.run / "m0-query-probes.json", {"raw_hitlists": {"policies": self.policy}})
        self.host_pins = [{"path": "/synthetic/public-host.js", "sha256": "a" * 64}]
        self.write(self.run / "m0-host-probes.json", {"provenance": {"sources": self.host_pins}})
        self.labels = self.write(self.run / "m1-silver-labels.json", {"schema_version": 1, "status": "frozen", "variant_observations_used": False, "cases_sha256": self.digest(self.cases), "contract_sha256": self.digest(self.contract), "protocol_sha256": self.digest(self.protocol), "annotations": [{"id": row["id"], "split": "development" if i < 120 else "holdout", "acceptable_sets": [["LABEL_SENTINEL"]], "rationale": "LABEL_SENTINEL"} for i, row in enumerate(cases)]})
        self.freeze()
        self.qmd = self.workspace / "qmd.yml"
        self.write(self.qmd, {"collections": {"DO_NOT_FORWARD": "PRIVATE_SENTINEL"}, "models": {"embed_api_url": "https://models.invalid/v1", "embed_api_key": "env:SYNTHETIC_STAGE_KEY", "embed_api_model": "voyage-4", "embed_dimension": 1024, "generate_api_url": "https://models.invalid/v1", "generate_api_key": "synthetic-generator-key", "generate_api_model": "gemini-3.5-flash-lite", "jev_base_url": "https://models.invalid/typesafe", "jev_api_key": "synthetic-jev-key", "jev_api_model": "jev-latest", "rerank_api_key": "env:UNSET_IGNORED_KEY"}})
        self.env = patch.dict(os.environ, {"SYNTHETIC_STAGE_KEY": "synthetic-embedding-key"})
        self.env.start()
        self.addCleanup(self.env.stop)

    def write(self, path, value):
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def digest(self, path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def freeze(self):
        artifacts = {str(path.relative_to(self.workspace)): self.digest(path) for path in [self.cases, self.labels, self.contract, self.protocol]}
        self.write(self.run / "m1-freeze.json", {"schema_version": 1, "status": "frozen", "cases_sha256": self.digest(self.cases), "labels_sha256": self.digest(self.labels), "contract_sha256": self.digest(self.contract), "protocol_sha256": self.digest(self.protocol), "artifacts": artifacts})

    def settings(self, stage="capture", phase="development", **kwargs):
        return build_settings(stage=stage, phase=phase, run_dir=self.run, workspace=self.workspace, qmd_config=self.qmd, **kwargs)

    def test_capture_projects_only_public_cases_and_overrides_yaml_embedding_defaults(self):
        settings = self.settings()
        self.assertEqual(len(settings["cases"]), 120)
        self.assertEqual(len(settings["casePartitions"]["holdout"]), 60)
        self.assertNotIn("LABEL_SENTINEL", json.dumps(settings))
        self.assertNotIn("PRIVATE_SENTINEL", json.dumps(settings))
        self.assertEqual(settings["models"]["embedding"], "text-embedding-3-small")
        self.assertEqual(settings["models"]["dimension"], 1536)
        self.assertEqual(settings["endpoints"]["embedding"]["url"], "https://models.invalid/v1/embeddings")
        self.assertEqual(settings["endpoints"]["jev"]["url"], "https://models.invalid/typesafe/v1/systemone")
        self.assertEqual(settings["endpoints"]["embedding"]["apiKey"], "synthetic-embedding-key")

    def test_freeze_missing_or_changed_reference_stops_before_key_loading(self):
        with patch("run_harness_stage.load_endpoints", side_effect=AssertionError("keys must not be read")):
            (self.run / "m1-freeze.json").unlink()
            with self.assertRaises(ValueError): self.settings()
            self.freeze()
            self.contract.write_text('{}')
            with self.assertRaises(ValueError): self.settings()

    def test_prepare_never_reads_qmd_settings(self):
        with patch("run_harness_stage.load_endpoints", side_effect=AssertionError("no keys")):
            settings = self.settings(stage="prepare", fusion="skill-identity-sum", pool_limit=10, snippet="matched-reference")
        self.assertNotIn("endpoints", settings)
        self.assertEqual(settings["variant"]["poolLimit"], 10)

    def test_artifact_paths_are_all_checked_before_any_artifact_bytes_or_keys(self):
        freeze_path = self.run / "m1-freeze.json"
        for unsafe in ("../private.json", "/private.json"):
            self.freeze()
            freeze = json.loads(freeze_path.read_text())
            freeze["artifacts"][unsafe] = "0" * 64
            self.write(freeze_path, freeze)
            with patch.object(Path, "read_bytes", side_effect=AssertionError("no artifact byte reads")), patch("run_harness_stage.load_endpoints", side_effect=AssertionError("no keys")):
                with self.assertRaises(ValueError): self.settings()

    def test_holdout_binds_challenger_to_final_labels_contract_and_cases(self):
        freeze = json.loads((self.run / "m1-freeze.json").read_text())
        challenger = {"schema_version": 1, "status": "frozen", "m1CasesSha256": freeze["cases_sha256"], "m1LabelsSha256": freeze["labels_sha256"], "contractSha256": freeze["contract_sha256"]}
        filename = self.write(self.run / "challenger-config.json", challenger)
        settings = self.settings(phase="holdout")
        self.assertEqual(len(settings["cases"]), 60)
        self.assertEqual(settings["challengerConfigSha256"], self.digest(filename))
        challenger["m1LabelsSha256"] = "0" * 64
        self.write(filename, challenger)
        with patch("run_harness_stage.load_endpoints", side_effect=AssertionError("no keys")):
            with self.assertRaises(ValueError): self.settings(phase="holdout")

    def test_required_freeze_hash_cannot_be_omitted_from_both_fields(self):
        filename = self.run / "m1-freeze.json"
        freeze = json.loads(filename.read_text())
        del freeze["contract_sha256"]
        del freeze["artifacts"][self.contract.relative_to(self.workspace).as_posix()]
        self.write(filename, freeze)
        with patch("run_harness_stage.load_endpoints", side_effect=AssertionError("no keys")):
            with self.assertRaises(ValueError): self.settings()

    def test_alias_shift_is_rejected_before_resolving_any_keys(self):
        data = json.loads(self.qmd.read_text())
        data["models"]["generate_api_model"] = "unapproved-generator"
        self.write(self.qmd, data)
        with patch("run_harness_stage.resolve_key", side_effect=AssertionError("no key resolution")):
            with self.assertRaises(ValueError): self.settings()

    def test_endpoint_paths_and_credential_shaped_urls_are_rejected(self):
        self.assertEqual(normalize_endpoint("https://m.invalid/typesafe/", "jev"), "https://m.invalid/typesafe/v1/systemone")
        self.assertEqual(normalize_endpoint("https://m.invalid/v1", "jev"), "https://m.invalid/v1/systemone")
        self.assertEqual(normalize_endpoint("https://m.invalid/v1/systemone", "jev"), "https://m.invalid/v1/systemone")
        for value in ["https://user:secret@m.invalid", "https://m.invalid?key=secret", "https://m.invalid#secret", "https://m.invalid?"]:
            with self.assertRaises(ValueError): normalize_endpoint(value, "embedding")

    def test_select_loads_existing_variant_and_never_forwards_label_fields(self):
        variant = "current-max-pool6-none"
        folder = self.run / "development/variants"; folder.mkdir(parents=True)
        public = [{"id": f"c{i:03}", "latest": f"Public task {i}"} for i in range(120)]
        public[0]["conversation"] = [{"role": "user", "text": "Public history"}]
        self.write(folder / f"{variant}.json", {"status": "complete", "variant": variant, "phase": "development", "config": {"fusion": "current-max", "poolLimit": 6, "snippet": "none"}, "policy": self.policy, "timeoutMs": 8000, "expectedCasesSha256": self.digest(self.cases), "expectedRawManifestSha256": "b" * 64, "cases": public, "replayCases": [{"id": row["id"], "params": {"latest": row["latest"], "candidateSkills": [], "candidateSources": {}, "candidateExperiences": [], "relationEvidence": []}, "rawHitlistObservation": {"query": row["latest"], "rawHitlists": []}} for row in public], "annotations": ["LABEL_SENTINEL"]})
        settings = self.settings(stage="select", variant=variant)
        self.assertEqual(settings["hostSourcePins"], self.host_pins)
        self.assertEqual(settings["timeoutMs"], 8000)
        self.assertEqual(settings["policy"], self.policy)
        self.assertNotIn("LABEL_SENTINEL", json.dumps(settings))
        self.assertEqual(set(settings["endpoints"]), {"jev"})

    def test_fake_fresh_child_receives_stdin_secrets_but_summary_never_prints_them(self):
        observed = []
        def runner(command, **kwargs):
            observed.append((command, json.loads(kwargs["input"])))
            return SimpleNamespace(returncode=0, stdout=json.dumps({"status": "complete", "cases": 120, "currentInvocationTransport": {"physicalAttempts": 3, "cacheHits": 2, "observations": ["DO_NOT_PRINT"]}}), stderr="DO_NOT_PRINT")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            summary = run_stage(stage="capture", phase="development", run_dir=self.run, workspace=self.workspace, qmd_config=self.qmd, runner=runner)
        self.assertEqual(summary["physicalAttempts"], 3)
        self.assertEqual(summary["cacheHits"], 2)
        self.assertEqual(observed[0][0][-1], str(self.workspace / "experiments/scripts/capture_harness_pilot.mjs"))
        self.assertEqual(observed[0][1]["endpoints"]["jev"]["apiKey"], "synthetic-jev-key")
        self.assertNotIn("synthetic-jev-key", output.getvalue())
        self.assertNotIn("DO_NOT_PRINT", json.dumps(summary))

    def test_child_failure_details_and_provider_body_are_suppressed(self):
        def runner(*args, **kwargs):
            return SimpleNamespace(returncode=1, stdout="synthetic-jev-key", stderr="provider body synthetic-jev-key")
        with self.assertRaises(RuntimeError) as error:
            run_stage(stage="capture", phase="development", run_dir=self.run, workspace=self.workspace, qmd_config=self.qmd, runner=runner)
        self.assertNotIn("synthetic-jev-key", str(error.exception))

    def test_missing_freeze_never_launches_child_or_resolves_credentials(self):
        (self.run / "m1-freeze.json").unlink()
        with patch("run_harness_stage.load_endpoints", side_effect=AssertionError("no keys")):
            with self.assertRaises(RuntimeError):
                run_stage(stage="capture", phase="development", run_dir=self.run, workspace=self.workspace, qmd_config=self.qmd, runner=lambda *args, **kwargs: self.fail("no child"))


if __name__ == "__main__":
    unittest.main()
