"""Read-only scoring of frozen, complete selector artifacts; never calls a model."""
from decimal import Decimal
from contextlib import closing
import hashlib
import json
import math
from pathlib import Path
import re
import sqlite3
import subprocess

from harness_metrics import (RUBRIC_VERSION, adoption_decision, empirical_p95,
                             evaluate, paired_family_bootstrap)

ROOT = Path(__file__).resolve().parents[2]
PROTOCOL = ROOT / "experiments/fixtures/harness_ablation_protocol.json"
CONTRACT = ROOT / "experiments/fixtures/harness_evaluation_contract.json"
JSON_STDIN_URL = Path(__file__).with_name("json_stdin.mjs").as_uri()


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def stable_hashes(*values):
    # Use ECMAScript serialization exactly as the artifact producers do. Python
    # JSON differs for integral floats, small exponents and negative zero.
    source = "import {readJsonStdin} from " + json.dumps(JSON_STDIN_URL) + ";\n" + """import {createHash} from 'node:crypto';
const c=v=>Array.isArray(v)?v.map(c):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,c(v[k])])):v;
console.log(JSON.stringify((await readJsonStdin()).map(v=>createHash('sha256').update(JSON.stringify(c(v))).digest('hex'))));"""
    result = subprocess.run(["node", "--input-type=module", "-e", source],
                            input=json.dumps(values, ensure_ascii=False, allow_nan=False),
                            capture_output=True, text=True, check=True, timeout=30)
    return json.loads(result.stdout)


def stable_hash(value):
    return stable_hashes(value)[0]


def finite(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def checked_content(value, key):
    content = {name: item for name, item in value.items() if name != key}
    if value.get(key) != stable_hash(content):
        raise ValueError(f"Invalid {key}")
    return content


def frozen_inputs(run_dir, labels_path):
    freeze = read_json(run_dir / "m1-freeze.json")
    labels = read_json(labels_path)
    if freeze.get("schema_version") != 1 or labels.get("schema_version") != 1 or freeze.get("status") != "frozen" or labels.get("status") != "frozen" or labels.get("variant_observations_used") is not False:
        raise ValueError("Scoring requires frozen M1 labels created before variant observations")
    if labels.get("annotation_version") != "harness-public-pilot-silver-v2" or labels.get("rubric_version") != RUBRIC_VERSION:
        raise ValueError("Unexpected frozen label/rubric version")
    if freeze.get("labels_sha256") != file_sha(labels_path):
        raise ValueError("Frozen labels file hash differs")
    fields = ["cases_sha256", "contract_sha256", "protocol_sha256", "primary_annotations_sha256",
              "agy_success_sha256", "source_adjudication_sha256"]
    if any(not re.fullmatch(r"[a-f0-9]{64}", str(freeze.get(key, ""))) or labels.get(key) != freeze[key] for key in fields):
        raise ValueError("Frozen M1 provenance hashes differ")
    artifacts = {}
    for relative, expected in freeze.get("artifacts", {}).items():
        path = ROOT / relative
        if Path(relative).is_absolute() or ".." in Path(relative).parts or not path.resolve().is_relative_to(ROOT) or path.is_symlink() or path.resolve() == (run_dir / "m1-freeze.json").resolve():
            raise ValueError("Unsafe or self-referential frozen artifact")
        if file_sha(path) != expected:
            raise ValueError(f"Frozen artifact hash differs: {relative}")
        artifacts.setdefault(expected, []).append(path)
    if any(freeze[key] not in artifacts for key in [*fields, "labels_sha256"]):
        raise ValueError("M1 freeze must pin every provenance artifact by file bytes")
    if freeze["contract_sha256"] != file_sha(CONTRACT) or freeze["protocol_sha256"] != file_sha(PROTOCOL):
        raise ValueError("Current contract/protocol differs from M1 freeze")
    contract, protocol = read_json(CONTRACT), read_json(PROTOCOL)
    adoption, inference = contract["adoption"], contract["inference"]
    if (adoption["minimum_family_macro_f1_improvement"], adoption["maximum_latency_p95_ratio"], adoption["maximum_cost_p95_ratio"], adoption["hard_timeout_ms"], inference["replicates"], inference["seed"], inference["confidence"]) != (0.03, 1.25, 1.25, 8000, 10000, 20261025, 0.95):
        raise ValueError("Contract differs from installed metric implementation")
    if protocol.get("status") != "frozen-before-variant-observations" or protocol.get("variant_observations_used") is not False:
        raise ValueError("A pre-observation ablation protocol is required")
    cases_file = artifacts[freeze["cases_sha256"]][0]
    public = read_json(cases_file)
    cases = public.get("cases") if isinstance(public, dict) else public
    annotations = labels.get("annotations")
    if not isinstance(cases, list) or not isinstance(annotations, list) or len(cases) != 180 or len(annotations) != 180:
        raise ValueError("Frozen cases and annotations must each contain180 records")
    ids = [row["id"] for row in cases]
    if len(set(ids)) != 180 or {row["id"] for row in annotations} != set(ids) or len({row["id"] for row in annotations}) != 180:
        raise ValueError("Frozen cases and labels must match exactly once")
    if any(type(row.get("uncertain")) is not bool or not isinstance(row.get("family_id"), str) or row.get("split") not in {"development", "holdout"} for row in annotations):
        raise ValueError("Frozen annotation status/family/split is invalid")
    if sum(row["split"] == "development" for row in annotations) != 120 or sum(row["split"] == "holdout" for row in annotations) != 60:
        raise ValueError("Frozen annotation partitions must be120/60")
    return freeze, cases, annotations, contract, protocol


def budget_snapshot(run_dir):
    """Inspect the existing ledger in SQLite read-only mode; never initialize it."""
    result = {"ok": None, "ledgers": {}, "jev_usd_per_million": None, "unit_prices_usd_per_million": {}}
    checks = []
    for prefix in ("model", "probe"):
        ledger = run_dir / f"{prefix}-budget.sqlite"
        limits = run_dir / ("budget-limits.json" if prefix == "model" else "probe-budget-limits.json")
        if not ledger.exists() or not limits.exists():
            if prefix == "model" or ledger.exists() or limits.exists():
                checks.append(None)
            continue
        spec = read_json(limits)
        with closing(sqlite3.connect(ledger.resolve().as_uri() + "?mode=ro", uri=True)) as db:
            db.execute("PRAGMA query_only=ON")
            persisted = db.execute("SELECT value FROM settings WHERE key='spec'").fetchone()
            tripped = db.execute("SELECT value FROM settings WHERE key='tripped'").fetchone()
            rows = db.execute("SELECT provider,COUNT(*),SUM(COALESCE(billed,reserved)),SUM(COALESCE(billed,0)),SUM(billed IS NULL) FROM requests GROUP BY provider").fetchall()
        same = persisted is not None and json.loads(persisted[0]) == {"providers": spec["providers"], "request_cap": spec.get("request_cap")}
        okay = same and not tripped and (spec.get("request_cap") is None or sum(row[1] for row in rows) <= spec["request_cap"])
        providers = {}
        for provider, count, reserved, billed, unknown in rows:
            limit = spec["providers"].get(provider)
            okay = okay and limit is not None and count <= limit["requests"] and reserved <= limit["tokens"]
            providers[provider] = {"attempts": count, "reserved_or_billed_tokens": reserved,
                                   "observed_billed_tokens": billed, "unknown_usage_attempts": unknown}
        result["ledgers"][prefix] = {"ok": bool(okay), "providers": providers,
                                     "limits_sha256": file_sha(limits), "tripped": bool(tripped)}
        checks.append(bool(okay))
        if prefix == "model":
            result["jev_usd_per_million"] = spec["providers"].get("jev", {}).get("usd_per_million")
            result["unit_prices_usd_per_million"] = {provider: value.get("usd_per_million") for provider, value in spec["providers"].items()}
    result["ok"] = False if False in checks else None if not checks or None in checks else True
    return result


def candidate_coverage(cases, annotations, pools, split=None):
    # Availability of an upstream pool is independent of the final selector's
    # no-dispatch skip. Reuse only evaluate's coverage output; these placeholders
    # never supply quality, reliability or adoption observations.
    placeholders = {case_id: {"status": "completed", "skills": []} for case_id in pools}
    return evaluate(cases, annotations, placeholders, candidates=pools, split=split)["candidate_coverage"]


def capture_policy_projection(policy):
    """Exact capturePilot settings.policy projection of the resolved M0 policy."""
    try:
        return {"qmdTimeoutMs": policy["qmd"]["timeoutMs"],
                "collectionWeights": policy["skills"]["search"]["collectionWeights"],
                "routing": policy["routing"]}
    except (KeyError, TypeError) as error:
        raise ValueError("Full M0 policy cannot supply the frozen capture projection") from error


def response_input_tokens(checkpoint):
    # Installed TypeSafe maps wire input_tokens to host inputTokens. Accept the
    # wire spelling for retained envelopes, but never accept conflicting aliases.
    usage = checkpoint.get("outcome", {}).get("result", {}).get("usage")
    if usage is None:
        return None
    if not isinstance(usage, dict):
        raise ValueError("Invalid selector response usage")
    known = []
    for key in ("inputTokens", "input_tokens"):
        value = usage.get(key)
        if value is None:
            continue
        if type(value) is not int or value < 0:
            raise ValueError("Invalid selector response input usage")
        known.append(value)
    if len(set(known)) > 1:
        raise ValueError("Conflicting selector response input usage aliases")
    return known[0] if known else None


def summarize_variant(run_dir, phase, variant, labels_path):
    run_dir, labels_path = Path(run_dir).resolve(), Path(labels_path).resolve()
    if not run_dir.is_relative_to(ROOT / "experiments/datasets") or not labels_path.is_relative_to(run_dir):
        raise ValueError("Summary inputs must be explicit frozen artifacts inside the experiment run")
    if phase not in {"development", "holdout"} or not re.fullmatch(r"[A-Za-z0-9_-]+", variant):
        raise ValueError("Invalid phase/variant")
    freeze, cases, annotations, contract, protocol = frozen_inputs(run_dir, labels_path)
    selected = [row["id"] for row in annotations if row["split"] == phase]
    base = {"phase": phase, "variant": variant, "labels_sha256": freeze["labels_sha256"],
            "contract_sha256": freeze["contract_sha256"], "protocol_sha256": freeze["protocol_sha256"],
            "cases_sha256": freeze["cases_sha256"], "expected_case_ids": sorted(selected)}
    named = re.fullmatch(r"(current-max|skill-identity-sum)-pool(6|10|20)-(none|matched-reference)", variant)
    if named:
        base["config"] = {"fusion": named[1], "poolLimit": int(named[2]), "snippet": named[3]}
    phase_dir = run_dir / phase
    selector_dir = phase_dir / "selectors" / variant
    variant_path = phase_dir / "variants" / f"{variant}.json"
    manifest_path = selector_dir / "manifest.json"
    failures = [path for path in [phase_dir / "failed-run.json", phase_dir / "variants" / f"{variant}.failed.json", selector_dir / "failed-run.json"] if path.exists()]
    if failures or not all(path.is_file() for path in [variant_path, manifest_path, phase_dir / "raw-manifest.json"]):
        return {**base, "status": "failed" if failures else "incomplete", "evidence_status": "insufficient", "metrics": None,
                "records": [], "reason": "Failed or incomplete outputs are not scored", "failure_artifacts": [str(path) for path in failures]}
    artifact, manifest, raw_manifest = read_json(variant_path), read_json(manifest_path), read_json(phase_dir / "raw-manifest.json")
    checked_content(artifact, "artifactContentSha256")
    if any(value.get("status") != "complete" for value in (artifact, manifest, raw_manifest)):
        return {**base, "status": "incomplete", "evidence_status": "insufficient", "metrics": None, "records": [], "reason": "Every stage must be complete"}
    config = artifact["config"]
    binding = manifest["binding"]
    endpoint_sha = binding.get("endpointSha256")
    if not isinstance(endpoint_sha, str) or not re.fullmatch(r"[a-f0-9]{64}", endpoint_sha):
        raise ValueError("Selector endpoint identity is missing or invalid")
    identities = stable_hashes(artifact["binding"], binding, raw_manifest["binding"], config)
    if identities[:3] != [artifact["inputIdentitySha256"], manifest["selectorIdentitySha256"], raw_manifest["captureIdentitySha256"]] or identities[3] != binding["configSha256"]:
        raise ValueError("Variant/selector/raw manifest identity mismatch")
    artifact_pending = read_json(phase_dir / "variants" / f"{variant}.pending.json")
    start = read_json(selector_dir / "run-start.json")
    if artifact_pending["inputIdentitySha256"] != artifact["inputIdentitySha256"] or stable_hash(artifact_pending["binding"]) != identities[0] or start["selectorIdentitySha256"] != manifest["selectorIdentitySha256"] or stable_hash(start["binding"]) != identities[1] or stable_hash(start["sourcePins"]) != binding["sourcePinsSha256"]:
        raise ValueError("Start/pending artifact identity differs")
    if artifact["phase"] != phase or artifact["variant"] != variant or binding["phase"] != phase or binding["variant"] != variant or artifact["expectedCasesSha256"] != freeze["cases_sha256"] or binding["publicCasesSha256"] != freeze["cases_sha256"]:
        raise ValueError("Phase/public case provenance mismatch")
    raw_sha = file_sha(phase_dir / "raw-manifest.json")
    if artifact["expectedRawManifestSha256"] != raw_sha or artifact["binding"]["rawManifestSha256"] != raw_sha or binding["rawManifestSha256"] != raw_sha:
        raise ValueError("Frozen raw manifest hash differs")
    if phase == "holdout":
        frozen_challenger = read_json(run_dir / "challenger-config.json")
        if frozen_challenger.get("status") != "frozen" or frozen_challenger.get("m1LabelsSha256") != freeze["labels_sha256"] or frozen_challenger.get("contractSha256") != freeze["contract_sha256"] or binding.get("challengerConfigSha256") != file_sha(run_dir / "challenger-config.json"):
            raise ValueError("Holdout comparison is not bound to the final frozen challenger/labels")
    sequences = [[row["id"] for row in value] for value in [artifact["cases"], artifact["replayCases"], artifact["candidateStages"], manifest["cases"], raw_manifest["cases"]]]
    order = sequences[0]
    if any(sequence != order for sequence in sequences) or len(order) != len(set(order)) or set(order) != set(selected):
        raise ValueError("Every stage must match exact frozen phase case IDs and order")
    full_policy_sha, capture_policy_sha, routing_sha = stable_hashes(artifact["policy"], capture_policy_projection(artifact["policy"]), artifact["policy"]["routing"])
    if stable_hash(artifact["cases"]) != binding["phaseCasesSha256"] or full_policy_sha != binding["policySha256"] or routing_sha != binding["routingSha256"] or artifact["binding"].get("replayPolicySha256") != full_policy_sha:
        raise ValueError("Frozen phase cases/routing policy hash differs")
    if raw_manifest["binding"].get("policySha256") != capture_policy_sha or artifact["binding"].get("policySha256") != capture_policy_sha:
        raise ValueError("Frozen raw/producer capture policy projection hashes differ")
    skills_policy = artifact["policy"]["routing"]["skills"]
    if binding.get("timeoutMs") != 8000 or binding.get("injectionCap") != 6 or skills_policy.get("maxInjectedSkills") != 6 or skills_policy.get("relevanceThreshold") != 0.4 or skills_policy.get("search", {}).get("minCandidateScore") != 0.3 or binding.get("model") != {"jev": "jev-latest", "jevResolved": "jev-1.14.0"}:
        raise ValueError("Selector changed a fixed frozen experiment condition")
    known = {f"{case_id}{suffix}" for case_id in order for suffix in (".json", ".pending.json")}
    if {path.name for path in (selector_dir / "cases").iterdir()} != known:
        raise ValueError("Selector case files are missing or unexpected")
    predictions, candidates, records, replay_inputs = {}, {}, [], []
    stage_pools = {name: {} for name in ("after_pool", "semantic_gate", "name_candidates", "union_candidates")}
    public = {row["id"]: row for row in cases}
    for index, case_id in enumerate(order):
        checkpoint_path = selector_dir / "cases" / f"{case_id}.json"
        checkpoint, pending = read_json(checkpoint_path), read_json(selector_dir / "cases" / f"{case_id}.pending.json")
        if file_sha(checkpoint_path) != manifest["cases"][index]["sha256"] or checkpoint["selectorIdentitySha256"] != manifest["selectorIdentitySha256"] or pending["selectorIdentitySha256"] != manifest["selectorIdentitySha256"] or pending["inputSha256"] != checkpoint["inputSha256"]:
            raise ValueError("Selector checkpoint/pending/manifest hash differs")
        raw_entry = raw_manifest["cases"][index]
        if raw_entry["file"] != f"raw/{case_id}.json":
            raise ValueError("Unsafe raw checkpoint path")
        raw_path = phase_dir / raw_entry["file"]
        raw = read_json(raw_path)
        if file_sha(raw_path) != raw_entry["sha256"] or raw["status"] != "complete" or raw["captureIdentitySha256"] != raw_manifest["captureIdentitySha256"]:
            raise ValueError("Raw checkpoint is incomplete or differs from manifest")
        replay, stage = artifact["replayCases"][index], artifact["candidateStages"][index]
        item = {"input": checkpoint["input"], "params": replay["params"], "rawInputSha256": checkpoint["rawInputSha256"]}
        if checkpoint.get("snippetProvenance") is not None:
            item["snippets"] = checkpoint["snippetProvenance"]
        checkpoint_hash, raw_content_hash, raw_hash, replay_raw_hash, public_hash, case_hash, item_hash = stable_hashes(
            {key: value for key, value in checkpoint.items() if key != "checkpointContentSha256"},
            {key: value for key, value in raw.items() if key != "checkpointContentSha256"},
            raw["rawHitlistObservation"], replay["rawHitlistObservation"], public[case_id], checkpoint["input"], item)
        if checkpoint_hash != checkpoint["checkpointContentSha256"] or raw_content_hash != raw["checkpointContentSha256"]:
            raise ValueError("Selector/raw checkpoint content hash differs")
        if raw_hash != replay_raw_hash or raw_hash != checkpoint["rawInputSha256"] or public_hash != case_hash or item_hash != checkpoint["inputSha256"]:
            raise ValueError("Exact selector input is not the frozen public raw case")
        replay_inputs.append(item)
        pool = [row["name"] for row in replay["params"]["candidateSkills"]]
        if pool != stage["unionCandidates"] or type(checkpoint["candidate_count"]) is not int or checkpoint["candidate_count"] != len(pool):
            raise ValueError("Candidate count/stage/replay mismatch")
        observations = checkpoint.get("transportObservations", [])
        if checkpoint["status"] == "skipped-empty-pool":
            if pool or checkpoint.get("selection") not in (None, {"skills": []}) or observations or checkpoint.get("trace", {}) != {"hostCalls": 0, "fetchCalls": 0, "legacyCalls": 0}:
                raise ValueError("Illegal empty-pool skip")
            skills, service, tokens, source = [], None, 0, "no-dispatch"
            response_tokens = None
            prediction = {"status": "skipped-empty-pool", "skills": [], "candidate_count": 0}
        elif checkpoint["status"] == "complete":
            if not pool or checkpoint.get("outcome", {}).get("status") != "ok" or len(observations) != 1 or observations[0].get("provider") != "jev":
                raise ValueError("Nonempty selector needs one successful original Jev observation")
            observation = observations[0]
            source = observation.get("source")
            if source not in {"remote", "cache"}:
                raise ValueError("Unverifiable selector observation source")
            expected_counts = {"physicalAttempts": int(source == "remote"), "cacheHits": int(source == "cache")}
            trace = checkpoint.get("trace", {})
            if checkpoint.get("transportCounts") != expected_counts or any(trace.get(key) != value for key, value in {"hostCalls": 1, "fetchCalls": 1, "legacyCalls": 0}.items()) or checkpoint.get("outcome", {}).get("result", {}).get("model") != "jev-1.14.0":
                raise ValueError("Selector transport/model provenance differs")
            service = observation.get("originalServiceMs")
            service = service if finite(service) else None
            tokens = observation.get("billedTokens")
            tokens = tokens if type(tokens) is int and tokens >= 0 else None
            response_tokens = response_input_tokens(checkpoint)
            if tokens is not None and response_tokens is not None and tokens != response_tokens:
                raise ValueError("Selector billed input usage differs from host response usage")
            skills = checkpoint["selection"]["skills"]
            if not isinstance(skills, list) or any(not isinstance(skill, str) for skill in skills) or len(set(skills)) != len(skills) or any(skill not in pool for skill in skills):
                raise ValueError("Invalid selected skill identities")
            prediction = {"status": "completed", "skills": skills}
        else:
            raise ValueError("Failed selector terminal status cannot be scored as an empty selection")
        predictions[case_id], candidates[case_id] = prediction, pool
        stage_pools["after_pool"][case_id] = [row["name"] for row in stage["skillHitsAfterPool"]]
        stage_pools["semantic_gate"][case_id] = stage["semanticGatePassed"]
        stage_pools["name_candidates"][case_id] = stage["nameCandidates"]
        stage_pools["union_candidates"][case_id] = pool
        query_ms = raw["rawHitlistObservation"].get("latency_ms", {}).get("total")
        query_ms = query_ms if finite(query_ms) else None
        selector_work = 0 if prediction["status"] == "skipped-empty-pool" else service
        records.append({"id": case_id, "prediction": prediction, "candidate_count": len(pool), "candidates": pool,
                        "candidate_stages": stage, "shared_query_latency_ms": query_ms,
                        "shared_query_transport_observations": raw.get("transportObservations", []),
                        "selector_original_service_ms": service, "selector_billed_input_tokens": tokens,
                        "selector_response_input_tokens": response_tokens,
                        "selector_transport_source": source, "selector_local_wall_ms": checkpoint.get("evaluationWallMs"),
                        "selector_transport_counts": checkpoint.get("transportCounts"),
                        "reconstructed_shared_query_plus_selector_ms": query_ms + selector_work if query_ms is not None and selector_work is not None else None})
    if stable_hash(replay_inputs) != binding["exactReplayInputsSha256"]:
        raise ValueError("Aggregate exact replay input identity differs")
    metrics = evaluate(cases, annotations, predictions, candidates=candidates, split=phase)
    stage_coverage = {name: candidate_coverage(cases, annotations, pools, split=phase) for name, pools in stage_pools.items()}
    annotation_by_id = {row["id"]: row for row in annotations}
    for row in records:
        case_id = row["id"]
        row["candidate_coverage_stages"] = {name: candidate_coverage([public[case_id]], [annotation_by_id[case_id]], {case_id: pools[case_id]}) for name, pools in stage_pools.items()}
    nonempty = [row for row in records if row["candidate_count"]]
    services = [row["selector_original_service_ms"] for row in nonempty if row["selector_original_service_ms"] is not None]
    tokens = [row["selector_billed_input_tokens"] for row in records if row["selector_billed_input_tokens"] is not None]
    budgets = budget_snapshot(run_dir)
    rate = budgets["jev_usd_per_million"]
    for row in records:
        row["selector_equivalent_usd"] = str(Decimal(row["selector_billed_input_tokens"]) * Decimal(rate) / 1_000_000) if row["selector_billed_input_tokens"] is not None and rate is not None else None
    shared_query = {}
    for row in records:
        for observation in row["shared_query_transport_observations"]:
            provider = observation.get("provider")
            if not isinstance(provider, str):
                raise ValueError("Shared query observation requires a provider")
            group = shared_query.setdefault(provider, {"observations": 0, "known_billed_tokens": 0, "unknown_usage_observations": 0})
            group["observations"] += 1
            billed = observation.get("billedTokens")
            if type(billed) is int and billed >= 0:
                group["known_billed_tokens"] += billed
            else:
                group["unknown_usage_observations"] += 1
    for provider, group in shared_query.items():
        price = budgets["unit_prices_usd_per_million"].get(provider)
        group["equivalent_usd"] = str(Decimal(group["known_billed_tokens"]) * Decimal(price) / 1_000_000) if price is not None and not group["unknown_usage_observations"] else None
    query_times = [row["shared_query_latency_ms"] for row in records if row["shared_query_latency_ms"] is not None]
    new_tokens = [row["selector_billed_input_tokens"] for row in records if row["selector_transport_source"] == "remote"]
    resource = {"selector_latency_p95_ms": empirical_p95(services) if services and len(services) == len(nonempty) else None,
                "selector_input_tokens_p95": empirical_p95(tokens) if len(tokens) == len(records) else None,
                "service_observations": len(services), "service_required": len(nonempty), "cost_observations": len(tokens),
                "skipped_empty_pools": len(records) - len(nonempty), "jev_usd_per_million": rate,
                "hard_timeout_ok": False if binding.get("timeoutMs") != 8000 else None if len(services) != len(nonempty) else all(value <= 8000 for value in services),
                "budget": budgets,
                "selector_actual_new_billed_input_tokens": sum(new_tokens) if all(value is not None for value in new_tokens) else None,
                "actual_new_selector_spend_scope": "Physical original selector requests in these checkpoints; this read-only summary issues no requests",
                "shared_query_latency_p95_ms": empirical_p95(query_times) if len(query_times) == len(records) else None,
                "shared_query_by_provider": shared_query,
                "reconstructed_pipeline_label": "Reconstructed shared-query-plus-selector time; not observed cold end-to-end gateway latency",
                "shared_query_cost_scope": "Frozen shared query observations are reported per case, excluded from selector-only cost gates"}
    return {**base, "status": "complete", "fixed_policy_sha256": binding["policySha256"],
            "capture_policy_sha256": capture_policy_sha, "shared_raw_manifest_sha256": raw_sha,
            "selector_endpoint_sha256": endpoint_sha,
            "selector_source_pins_sha256": binding["sourcePinsSha256"], "selector_implementation_sha256": stable_hash(binding.get("implementation", [])),
            "evidence_status": "sufficient" if resource["selector_latency_p95_ms"] is not None and resource["selector_input_tokens_p95"] is not None and rate is not None and budgets["ok"] is not None else "insufficient",
            "config": config, "metrics": metrics, "stage_coverage": stage_coverage, "resources": resource, "records": records,
            "artifact_hashes": {"variant": file_sha(variant_path), "selector_manifest": file_sha(manifest_path), "raw_manifest": raw_sha, "m1_freeze": file_sha(run_dir / "m1-freeze.json")}}


def compare_variants(baseline, challenger):
    result = {"baseline": baseline["variant"], "challenger": challenger["variant"], "evidence_status": "insufficient", "adoption": None, "development_eligible": False}
    if baseline.get("status") != "complete" or challenger.get("status") != "complete":
        return {**result, "reason": "Both full phase outputs are required"}
    for key in ("phase", "labels_sha256", "contract_sha256", "protocol_sha256", "cases_sha256", "expected_case_ids", "fixed_policy_sha256", "capture_policy_sha256", "shared_raw_manifest_sha256", "selector_endpoint_sha256", "selector_source_pins_sha256", "selector_implementation_sha256"):
        if baseline[key] != challenger[key]:
            raise ValueError(f"Variants are not paired on {key}")
    left, right = baseline["metrics"], challenger["metrics"]
    if not left["family_scores"]["f1"] or set(left["family_scores"]["f1"]) != set(right["family_scores"]["f1"]):
        return {**result, "reason": "Matched resolved intent families are required"}
    interval = paired_family_bootstrap(left["family_scores"]["f1"], right["family_scores"]["f1"], replicates=10000, seed=20261025, confidence=0.95)
    added_fp = sorted(set(right["no_skill_false_positive"]["ids"]) - set(left["no_skill_false_positive"]["ids"]))
    a, b = baseline["resources"], challenger["resources"]
    measured = all(finite(value[key]) for value in (a, b) for key in ("selector_latency_p95_ms", "selector_input_tokens_p95"))
    shared_price = a["jev_usd_per_million"] is not None and a["jev_usd_per_million"] == b["jev_usd_per_million"]
    reliability = all(value["reliability"]["complete"] and value["reliability"]["explicit_statuses"] and value["reliability"]["failure_count"] == 0 for value in (left, right))
    checks = {"complete_reliable_paired_outputs": reliability,
              "no_new_no_skill_false_positives": not added_fp, "original_selector_measurements": measured,
              "shared_declared_jev_unit_price": shared_price,
              "latency_p95": measured and b["selector_latency_p95_ms"] <= 1.25 * a["selector_latency_p95_ms"],
              "cost_p95": measured and b["selector_input_tokens_p95"] <= 1.25 * a["selector_input_tokens_p95"],
              "budget": a["budget"]["ok"] is True and b["budget"]["ok"] is True,
              "hard_timeout": a["hard_timeout_ok"] is True and b["hard_timeout_ok"] is True}
    if measured and shared_price:
        result["adoption"] = adoption_decision(delta=interval["delta"], ci_lower=interval["lower"],
            baseline_no_skill_fp_ids=left["no_skill_false_positive"]["ids"], variant_no_skill_fp_ids=right["no_skill_false_positive"]["ids"],
            baseline_latency_p95=a["selector_latency_p95_ms"], variant_latency_p95=b["selector_latency_p95_ms"],
            baseline_cost_p95=a["selector_input_tokens_p95"], variant_cost_p95=b["selector_input_tokens_p95"],
            budget_ok=checks["budget"], hard_timeout_ok=checks["hard_timeout"], baseline_reliability=left["reliability"], variant_reliability=right["reliability"])
    return {**result, "evidence_status": "sufficient" if measured and shared_price and reliability and all(value["budget"]["ok"] is not None for value in (a, b)) else "insufficient",
            "family_macro_f1_delta": interval["delta"], "paired_family_bootstrap": interval,
            "resource_comparison": {"baseline": {key: a[key] for key in ("selector_latency_p95_ms", "selector_input_tokens_p95")},
                                    "challenger": {key: b[key] for key in ("selector_latency_p95_ms", "selector_input_tokens_p95")}, "maximum_ratio": 1.25},
            "new_no_skill_false_positive_ids": added_fp, "checks": checks, "development_eligible": all(checks.values())}


def choose_development_variant(summaries, incoming_baseline):
    protocol = read_json(PROTOCOL)
    summaries = list(summaries)
    if isinstance(incoming_baseline, str):
        incoming_baseline = next(row for row in summaries if row["variant"] == incoming_baseline)
    if incoming_baseline["variant"] not in {row["variant"] for row in summaries}:
        summaries.append(incoming_baseline)
    if len({row["variant"] for row in summaries}) != len(summaries):
        raise ValueError("Development variant summaries must be unique")
    original = next((row for row in summaries if row.get("config") and all(row["config"].get(key) == value for key, value in protocol["baseline"].items())), None)
    if original is None or any(row["phase"] != "development" for row in summaries):
        raise ValueError("Development selection requires the original baseline and development-only summaries")
    comparisons = {row["variant"]: compare_variants(original, row) for row in summaries}

    def order(row):
        config = row["config"]
        return (-row["metrics"]["family_macro"]["f1"], config["poolLimit"], config["snippet"] != "none", config["fusion"] != "current-max", row["variant"])

    eligible = [row for row in summaries if comparisons[row["variant"]]["development_eligible"]]
    chosen = min(eligible, key=order) if eligible else incoming_baseline
    diagnostic = None
    if all(chosen.get("config", {}).get(key) == value for key, value in protocol["baseline"].items()):
        contenders = [row for row in summaries if row.get("status") == "complete" and row.get("metrics", {}).get("family_macro", {}).get("f1") is not None and any(row["config"].get(key) != value for key, value in protocol["baseline"].items())]
        if contenders:
            contender = min(contenders, key=lambda row: (not comparisons[row["variant"]]["development_eligible"], *order(row)))
            diagnostic = {"variant": contender["variant"], "config": contender["config"], "eligible": comparisons[contender["variant"]]["development_eligible"], "purpose": "diagnostic holdout contender, not a recommended change"}
    return {"chosen_variant": chosen["variant"], "chosen_config": chosen.get("config"),
            "decision": "retain-incoming-baseline" if chosen["variant"] == incoming_baseline["variant"] else "choose-development-variant",
            "comparisons_to_original_baseline": comparisons, "diagnostic_contender": diagnostic,
            "evidence_status": "sufficient" if comparisons[chosen["variant"]]["development_eligible"] else "insufficient",
            "selection_rule": "Highest eligible development family-macro F1; pool/none/current-max exact tie order; no holdout3% improvement gate"}
