"""Synthetic completed artifacts only; no actual pilot labels or model calls."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import summarize_harness_variants as summary
from model_budget import BudgetLedger


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")


class VariantSummaryTests(unittest.TestCase):
    def test_large_unicode_hash_matches_exact_utf8_json_across_pipe_chunks(self):
        value = {"text": "é中文🙂—xy" * 20000, "sentinel": "public"}
        expected = hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
            separators=(",", ":")).encode("utf-8")).hexdigest()
        self.assertEqual(summary.stable_hash(value), expected)

    def setUp(self):
        parent = summary.ROOT / "experiments/datasets"
        parent.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="variant-summary-test-", dir=parent)
        self.addCleanup(self.temp.cleanup)
        self.run = Path(self.temp.name)
        self.cases = [{"id": f"p{i + 1:03}", "latest": f"Synthetic public task {i}"} for i in range(180)]
        self.annotations = [{"id": row["id"], "family_id": f"f{i // 2:03}", "split": "development" if i < 120 else "holdout",
                             "type": "no-skill" if i < 12 else "single", "acceptable_sets": [[]] if i < 12 else [["alpha"]], "uncertain": False}
                            for i, row in enumerate(self.cases)]
        self.policy = {"qmd": {"timeoutMs": 15000, "embedding": {"model": "text-embedding-3-small", "dimension": 1536},
                               "expansion": {"model": "gemini-3.5-flash-lite"}, "jev": {"model": "jev-latest"}},
                       "skills": {"search": {"collectionWeights": {"meta": 3, "body": 2, "references": 1}}},
                       "routing": {"skills": {"maxInjectedSkills": 6, "relevanceThreshold": 0.4, "search": {"minCandidateScore": 0.3}}}}
        self.capture_policy = {"qmdTimeoutMs": self.policy["qmd"]["timeoutMs"],
                               "collectionWeights": self.policy["skills"]["search"]["collectionWeights"], "routing": self.policy["routing"]}
        files = {"cases_sha256": self.run / "public-cases.json", "primary_annotations_sha256": self.run / "primary.json",
                 "agy_success_sha256": self.run / "agy-success.json", "source_adjudication_sha256": self.run / "adjudication.json",
                 "contract_sha256": summary.CONTRACT, "protocol_sha256": summary.PROTOCOL}
        save(files["cases_sha256"], {"schema_version": 1, "cases": self.cases})
        save(files["primary_annotations_sha256"], {"synthetic_primary": True})
        save(files["agy_success_sha256"], {"stage": "successful", "synthetic": True})
        save(files["source_adjudication_sha256"], {"synthetic_adjudication": True})
        hashes = {key: summary.file_sha(path) for key, path in files.items()}
        self.labels_path = self.run / "m1-silver-labels.json"
        save(self.labels_path, {"schema_version": 1, "status": "frozen", "variant_observations_used": False,
                               "annotation_version": "harness-public-pilot-silver-v2", "rubric_version": "harness-public-pilot-v1.1",
                               **hashes, "annotations": self.annotations})
        self.case_sha = hashes["cases_sha256"]
        save(self.run / "m1-freeze.json", {"schema_version": 1, "status": "frozen", **hashes,
             "labels_sha256": summary.file_sha(self.labels_path), "artifacts": {
                 **{str(path.relative_to(summary.ROOT)): hashes[key] for key, path in files.items()},
                 str(self.labels_path.relative_to(summary.ROOT)): summary.file_sha(self.labels_path)}})
        limits = {"request_cap": 1000, "providers": {"jev": {"requests": 1000, "tokens": 47_000_000, "usd_per_million": "0.042"}}}
        save(self.run / "budget-limits.json", limits)
        BudgetLedger(self.run / "model-budget.sqlite", limits["providers"], request_cap=1000)
        self.phase = self.run / "development"
        self.public = self.cases[:120]
        self.raw = [{"query": row["latest"], "status": "completed", "rawHitlists": [], "latency_ms": {"total": 200.0}, "float_probe": 1.0e-7} for row in self.public]
        self.raw_hashes = summary.stable_hashes(*self.raw)
        raw_binding = {"phase": "development", "casesSha256": self.case_sha, "selectedCasesSha256": summary.stable_hash(self.public), "policySha256": summary.stable_hash(self.capture_policy)}
        raw_identity = summary.stable_hash(raw_binding)
        contents = [{"status": "complete", "captureIdentitySha256": raw_identity, "input": row, "rawHitlistObservation": raw,
                     "transportObservations": [{"provider": "embedding", "source": "remote", "billedTokens": 10, "originalServiceMs": 20.0}]}
                    for row, raw in zip(self.public, self.raw)]
        checksums = summary.stable_hashes(*contents)
        entries = []
        for row, content, checksum in zip(self.public, contents, checksums):
            path = self.phase / f"raw/{row['id']}.json"
            save(path, {**content, "checkpointContentSha256": checksum})
            entries.append({"id": row["id"], "file": f"raw/{row['id']}.json", "sha256": summary.file_sha(path)})
        save(self.phase / "raw-manifest.json", {"status": "complete", "binding": raw_binding, "captureIdentitySha256": raw_identity, "cases": entries})

    def variant(self, fusion="current-max", pool=6, snippet="none", *, fix=False, service=100.0, tokens=100, source="remote", new_fp=False, reported_tokens="same", wire_usage=False):
        config = {"fusion": fusion, "poolLimit": pool, "snippet": snippet}
        name = f"{fusion}-pool{pool}-{snippet}"
        replay, stages, inputs = [], [], []
        for i, (row, raw, raw_sha) in enumerate(zip(self.public, self.raw, self.raw_hashes)):
            names = [] if i == 0 else ["alpha"]
            params = {"latest": row["latest"], "candidateSkills": [{"name": name, "description": "Public scope"} for name in names]}
            replay.append({"id": row["id"], "params": params, "rawHitlistObservation": raw})
            inputs.append({"input": row, "params": params, "rawInputSha256": raw_sha})
            stages.append({"id": row["id"], "unionCandidates": names, "semanticGatePassed": names,
                           "skillHitsAfterPool": [{"name": name, "score": 1.0, "semanticScore": 0.1 if i == 0 else 0.9} for name in (["alpha"] if i == 0 else names)], "nameCandidates": []})
        binding = {"phase": "development", "variant": name, "publicCasesSha256": self.case_sha,
                   "phaseCasesSha256": summary.stable_hash(self.public), "configSha256": summary.stable_hash(config),
                   "sourcePinsSha256": summary.stable_hash([]), "exactReplayInputsSha256": summary.stable_hash(inputs),
                   "policySha256": summary.stable_hash(self.policy), "routingSha256": summary.stable_hash(self.policy["routing"]),
                   "timeoutMs": 8000, "injectionCap": 6, "model": {"jev": "jev-latest", "jevResolved": "jev-1.14.0"},
                   "endpointSha256": summary.stable_hash("https://selector-a.invalid/v1/systemone"),
                   "rawManifestSha256": summary.file_sha(self.phase / "raw-manifest.json")}
        identity = summary.stable_hash(binding)
        contents = []
        input_hashes = summary.stable_hashes(*inputs)
        for i, (row, item, input_hash) in enumerate(zip(self.public, inputs, input_hashes)):
            empty = i == 0
            skills = [] if i < 12 or i == 12 and not fix else ["alpha"]
            if new_fp and i == 1:
                skills = ["alpha"]
            observation = {"provider": "jev", "source": source, "originalServiceMs": service, "billedTokens": tokens}
            response_tokens = (100 if tokens is None else tokens) if reported_tokens == "same" else reported_tokens
            usage = {"input_tokens" if wire_usage else "inputTokens": response_tokens,
                     "output_tokens" if wire_usage else "outputTokens": 5}
            contents.append({"status": "skipped-empty-pool" if empty else "complete", "candidate_count": 0 if empty else 1,
                "selectorIdentitySha256": identity, "inputSha256": input_hash, "input": row, "rawInputSha256": item["rawInputSha256"],
                "selection": None if empty else {"skills": skills}, "snippetProvenance": None, "evaluationWallMs": 2.0,
                "outcome": None if empty else {"status": "ok", "result": {"model": "jev-1.14.0", "usage": usage}},
                "trace": {"hostCalls": 0 if empty else 1, "fetchCalls": 0 if empty else 1, "legacyCalls": 0},
                "transportObservations": [] if empty else [observation],
                "transportCounts": {"physicalAttempts": 0 if empty else int(source == "remote"), "cacheHits": 0 if empty else int(source == "cache")}})
        content_hashes = summary.stable_hashes(*contents)
        directory = self.phase / "selectors" / name
        entries = []
        for row, content, checksum in zip(self.public, contents, content_hashes):
            path = directory / f"cases/{row['id']}.json"
            save(path, {**content, "checkpointContentSha256": checksum})
            save(path.with_name(f"{row['id']}.pending.json"), {"selectorIdentitySha256": identity, "inputSha256": content["inputSha256"]})
            entries.append({"id": row["id"], "sha256": summary.file_sha(path)})
        save(directory / "run-start.json", {"selectorIdentitySha256": identity, "binding": binding, "sourcePins": []})
        save(directory / "manifest.json", {"status": "complete", "selectorIdentitySha256": identity, "binding": binding, "cases": entries})
        artifact_binding = {"phase": "development", "variant": config, "rawManifestSha256": binding["rawManifestSha256"],
                            "policySha256": summary.stable_hash(self.capture_policy), "replayPolicySha256": summary.stable_hash(self.policy)}
        artifact_identity = summary.stable_hash(artifact_binding)
        artifact = {"status": "complete", "inputIdentitySha256": artifact_identity, "binding": artifact_binding,
                    "phase": "development", "variant": name, "config": config, "policy": self.policy,
                    "expectedCasesSha256": self.case_sha, "expectedRawManifestSha256": binding["rawManifestSha256"],
                    "cases": self.public, "replayCases": replay, "candidateStages": stages}
        save(self.phase / f"variants/{name}.json", {**artifact, "artifactContentSha256": summary.stable_hash(artifact)})
        save(self.phase / f"variants/{name}.pending.json", {"inputIdentitySha256": artifact_identity, "binding": artifact_binding})
        return name

    def summarize(self, name):
        return summary.summarize_variant(self.run, "development", name, self.labels_path)

    def test_capture_projection_and_full_producer_selector_policy_are_distinct_and_compatible(self):
        name = self.variant()
        raw_path = self.phase / "raw-manifest.json"
        original_raw_bytes = raw_path.read_bytes()
        artifact = summary.read_json(self.phase / f"variants/{name}.json")
        self.assertNotEqual(artifact["binding"]["policySha256"], artifact["binding"]["replayPolicySha256"])
        result = self.summarize(name)
        self.assertEqual(result["capture_policy_sha256"], summary.stable_hash(self.capture_policy))
        self.assertEqual(result["fixed_policy_sha256"], summary.stable_hash(self.policy))
        self.assertEqual(raw_path.read_bytes(), original_raw_bytes)
        artifact["binding"]["policySha256"] = summary.stable_hash(self.policy)
        artifact["inputIdentitySha256"] = summary.stable_hash(artifact["binding"])
        artifact["artifactContentSha256"] = summary.stable_hash({key: value for key, value in artifact.items() if key != "artifactContentSha256"})
        save(self.phase / f"variants/{name}.json", artifact)
        save(self.phase / f"variants/{name}.pending.json", {"inputIdentitySha256": artifact["inputIdentitySha256"], "binding": artifact["binding"]})
        with self.assertRaisesRegex(ValueError, "capture policy projection"):
            self.summarize(name)
        self.assertEqual(raw_path.read_bytes(), original_raw_bytes)

    def test_selector_endpoint_identity_is_exposed_and_must_match_for_latency_comparison(self):
        baseline = self.summarize(self.variant())
        left, right = copy.deepcopy(baseline), copy.deepcopy(baseline)
        endpoint = summary.stable_hash("https://selector-a.invalid/v1/systemone")
        left["selector_endpoint_sha256"] = endpoint
        right["selector_endpoint_sha256"] = summary.stable_hash("https://selector-b.invalid/v1/systemone")
        with self.assertRaisesRegex(ValueError, "endpoint"):
            summary.compare_variants(left, right)
        self.assertEqual(baseline["selector_endpoint_sha256"], endpoint)
        right["selector_endpoint_sha256"] = endpoint
        self.assertTrue(summary.compare_variants(left, right)["development_eligible"])

    def test_observed_billed_tokens_must_match_actual_host_or_wire_response_usage(self):
        for source, wire in (("remote", False), ("cache", True)):
            with self.subTest(source=source, wire_usage=wire):
                name = self.variant(tokens=1, reported_tokens=1000, source=source, wire_usage=wire)
                with self.assertRaisesRegex(ValueError, "usage"):
                    self.summarize(name)
        result = self.summarize(self.variant(source="cache", tokens=100, reported_tokens=100))
        self.assertEqual(result["records"][1]["selector_response_input_tokens"], 100)

    def test_completed_resources_retain_cache_original_observations_and_shared_query_separation(self):
        result = self.summarize(self.variant(source="cache"))
        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["metrics"]["reliability"]["failure_count"], 0)
        self.assertEqual(result["resources"]["selector_latency_p95_ms"], 100)
        self.assertEqual(result["resources"]["selector_input_tokens_p95"], 100)
        self.assertEqual(result["resources"]["service_observations"], 119)
        self.assertEqual(result["records"][0]["prediction"]["status"], "skipped-empty-pool")
        self.assertIsNone(result["records"][0]["selector_original_service_ms"])
        self.assertEqual(result["records"][0]["selector_billed_input_tokens"], 0)
        self.assertEqual(result["records"][1]["selector_transport_source"], "cache")
        self.assertEqual(result["records"][1]["reconstructed_shared_query_plus_selector_ms"], 300)
        self.assertIn("not observed cold", result["resources"]["reconstructed_pipeline_label"])
        self.assertEqual(result["stage_coverage"]["union_candidates"]["complete_set"], 1)
        self.assertEqual(result["records"][0]["candidate_stages"]["skillHitsAfterPool"][0]["name"], "alpha")
        self.assertIn("after_pool", result["records"][0]["candidate_coverage_stages"])

    def test_missing_original_metrics_are_unknown_and_block_guards(self):
        good = self.summarize(self.variant())
        unknown = self.summarize(self.variant("skill-identity-sum", fix=True, service=None, tokens=None))
        self.assertIsNone(unknown["resources"]["selector_latency_p95_ms"])
        self.assertIsNone(unknown["resources"]["selector_input_tokens_p95"])
        self.assertIsNone(unknown["resources"]["hard_timeout_ok"])
        comparison = summary.compare_variants(good, unknown)
        self.assertEqual(comparison["evidence_status"], "insufficient")
        self.assertFalse(comparison["development_eligible"])
        self.assertIsNone(comparison["adoption"])

    def test_development_uses_F1_and_original_guards_without_holdout_minimum_delta(self):
        baseline = self.summarize(self.variant())
        challenger = self.summarize(self.variant("skill-identity-sum", fix=True))
        comparison = summary.compare_variants(baseline, challenger)
        self.assertGreater(comparison["family_macro_f1_delta"], 0)
        self.assertLess(comparison["family_macro_f1_delta"], 0.03)
        self.assertFalse(comparison["adoption"]["checks"]["minimum_improvement"])
        self.assertTrue(comparison["development_eligible"])
        selected = summary.choose_development_variant([baseline, challenger], baseline)
        self.assertEqual(selected["chosen_variant"], challenger["variant"])
        # A later-stage contender may pass versus the incoming stage winner but
        # still violates the original baseline's resource cap.
        incoming = copy.deepcopy(challenger)
        incoming["resources"]["selector_latency_p95_ms"] = 120
        slower = copy.deepcopy(challenger)
        slower["variant"] = "skill-identity-sum-pool10-none"
        slower["config"]["poolLimit"] = 10
        slower["resources"]["selector_latency_p95_ms"] = 140
        decision = summary.choose_development_variant([baseline, incoming, slower], incoming)
        self.assertFalse(decision["comparisons_to_original_baseline"][slower["variant"]]["development_eligible"])
        fp = copy.deepcopy(challenger)
        fp["metrics"]["no_skill_false_positive"]["ids"] = ["p002"]
        comparison = summary.compare_variants(baseline, fp)
        self.assertEqual(comparison["new_no_skill_false_positive_ids"], ["p002"])
        self.assertFalse(comparison["development_eligible"])

    def test_ties_and_diagnostic_fallback_are_explicit(self):
        baseline = self.summarize(self.variant())
        contender = copy.deepcopy(baseline)
        contender["variant"] = "skill-identity-sum-pool6-none"
        contender["config"]["fusion"] = "skill-identity-sum"
        wider = copy.deepcopy(contender)
        wider["variant"] = "skill-identity-sum-pool10-matched-reference"
        wider["config"].update(poolLimit=10, snippet="matched-reference")
        result = summary.choose_development_variant([wider, contender, baseline], baseline)
        self.assertEqual(result["chosen_variant"], baseline["variant"])
        self.assertEqual(result["diagnostic_contender"]["variant"], contender["variant"])
        contender["resources"]["selector_latency_p95_ms"] = 200
        result = summary.choose_development_variant([contender, baseline], baseline)
        self.assertFalse(result["diagnostic_contender"]["eligible"])
        self.assertIn("not a recommended", result["diagnostic_contender"]["purpose"])
        small_matched = copy.deepcopy(baseline)
        small_matched["variant"] = "skill-identity-sum-pool6-matched-reference"
        small_matched["config"].update(fusion="skill-identity-sum", snippet="matched-reference")
        large_none = copy.deepcopy(baseline)
        large_none["variant"] = "skill-identity-sum-pool10-none"
        large_none["config"].update(fusion="skill-identity-sum", poolLimit=10)
        result = summary.choose_development_variant([baseline, large_none, small_matched], baseline)
        self.assertEqual(result["diagnostic_contender"]["variant"], small_matched["variant"])

    def test_failure_missing_and_tampered_outputs_cannot_be_scored_empty_correct(self):
        name = self.variant()
        path = self.phase / f"selectors/{name}/cases/p014.json"
        checkpoint = summary.read_json(path)
        checkpoint["selection"]["skills"] = []
        save(path, checkpoint)
        with self.assertRaisesRegex(ValueError, "hash differs"):
            self.summarize(name)
        path.unlink()
        with self.assertRaisesRegex(ValueError, "missing or unexpected"):
            self.summarize(name)
        save(self.phase / f"selectors/{name}/failed-run.json", {"status": "failed"})
        result = self.summarize(name)
        self.assertEqual(result["status"], "failed")
        self.assertIsNone(result["metrics"])
        self.assertEqual(self.summarize("never-run")["status"], "incomplete")

    def test_labels_must_be_frozen_and_all_provenance_bytes_match(self):
        name = self.variant()
        labels = summary.read_json(self.labels_path)
        labels["status"] = "pending-review"
        save(self.labels_path, labels)
        with self.assertRaisesRegex(ValueError, "frozen M1"):
            self.summarize(name)
        labels["status"] = "frozen"
        save(self.labels_path, labels)
        (self.run / "adjudication.json").write_text("tampered")
        with self.assertRaisesRegex(ValueError, "artifact hash differs"):
            self.summarize(name)


if __name__ == "__main__":
    unittest.main()
