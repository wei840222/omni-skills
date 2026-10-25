#!/usr/bin/env python3
"""Capture read-only baseline identities and a bounded local isolation check.

Configuration is extracted through explicit field allowlists. Never serialize
configuration documents, credentials, private skill names or private content.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import quote

import yaml

from audit_routing_dataset import content_hash, file_hash

ARTIFACTS = ("manifest.json", "benchmark_queries.json", "documents.json", "embedding_manifest.json", "embeddings.npz", "routing_benchmark_results.json")


def write_new(path, data):
    with path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def git_identity(path):
    def run(*args):
        return subprocess.run(["git", "-C", str(path), *args], capture_output=True, text=True, check=True).stdout
    return {"path": str(path), "head": run("rev-parse", "HEAD").strip(), "dirty_status": run("status", "--porcelain=v1", "--untracked-files=all").splitlines()}


def nested(data, *keys):
    for key in keys:
        data = data.get(key, {}) if isinstance(data, dict) else {}
    return data


def scalar_fields(data, fields):
    return {key: data[key] for key in fields if key in data and isinstance(data[key], (str, int, float, bool, type(None)))}


def endpoint_summary(data):
    if not isinstance(data, dict):
        return {}
    result = scalar_fields(data, ("model", "dimension"))
    if isinstance(data.get("baseUrl"), str):
        result["endpoint_sha256"] = hashlib.sha256(data["baseUrl"].encode()).hexdigest()
    return result


def config_summary(openclaw_path, qmd_path):
    config = json.loads(openclaw_path.read_text(encoding="utf-8"))
    plugin = nested(config, "plugins", "entries", "skill-harness", "config")
    qmd = yaml.safe_load(qmd_path.read_text(encoding="utf-8"))
    models = qmd.get("models", {})
    qmd_models = scalar_fields(models, ("embed_api_model", "embed_dimension", "generate_api_model", "rerank_api_model", "jev_api_model"))
    qmd_models["endpoint_sha256"] = {key: hashlib.sha256(models[key].encode()).hexdigest() for key in ("embed_api_url", "generate_api_url", "rerank_api_url", "jev_base_url") if isinstance(models.get(key), str)}
    # Deliberately omit all key/reference/environment/provider dictionaries.
    agent_default = nested(config, "agents", "defaults")
    main = nested(config, "agents", "entries", "main")
    default_decision = agent_default.get("decisionModel")
    main_decision = main.get("decisionModel")
    return {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "host_decision": {"agents.defaults.decisionModel": default_decision if isinstance(default_decision, str) else None, "agents.entries.main.decisionModel": main_decision if isinstance(main_decision, str) else None, "effective_main_host_model": main_decision.strip() if isinstance(main_decision, str) else default_decision.strip() if isinstance(default_decision, str) else None, "scope": "Observed allowlisted host configuration; does not prove the resident build or an actual request."},
        "plugin_qmd": {key: endpoint_summary(nested(plugin, "qmd", key)) for key in ("embedding", "expansion", "jev")},
        "plugin_legacy_decision_endpoint": endpoint_summary(plugin.get("decisionModel")),
        "plugin_policy": {"routing": scalar_fields(nested(plugin, "routing"), ("queryMode", "timeoutMs")), "skills": scalar_fields(nested(plugin, "routing", "skills"), ("maxInjectedSkills", "relevanceThreshold")), "collectionWeights": scalar_fields(nested(plugin, "skills", "search", "collectionWeights"), ("meta", "body", "references"))},
        "qmd_yaml_defaults": qmd_models,
        "interpretation": "QMD YAML defaults, plugin QMD configuration, host Decision and historical reranker are distinct identities. No live settings are changed.",
    }


def public_materialization(root, mapping_path, runtime_dir, public_names):
    started = datetime.now(timezone.utc).isoformat()
    before_bytes = mapping_path.read_bytes()
    mapping = json.loads(before_bytes)
    names = mapping.get("allowedSkillNames")
    fingerprint = mapping.get("fingerprint")
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError("Invalid runtime allowedSkillNames schema")
    if not isinstance(fingerprint, str) or not re.fullmatch(r"[a-f0-9]{64}", fingerprint):
        raise ValueError("Invalid runtime index fingerprint")
    intersection = sorted(set(names) & public_names)
    docs = runtime_dir / "indexes" / fingerprint / "docs"
    identities = []
    for name in intersection:
        source = root / "skills" / name / "SKILL.md"
        text = source.read_text(encoding="utf-8")
        match = re.match(r"\A---[^\S\n]*\n(.*?)\n---[^\S\n]*(?:\n|$)", text, re.DOTALL)
        metadata = yaml.safe_load(match.group(1)) if match else {}
        body = text[match.end():].strip() if match else text.strip()
        expected_body = body + "\n" if body else ""
        meta = f"# {metadata.get('name', name).strip()}\n\n{metadata.get('description', '').strip()}".strip()
        expected_meta = meta.rstrip() + "\n" if meta else ""
        segment = quote(name, safe="-_.~").replace(".", "%2E")
        if len(segment) > 180:
            segment = hashlib.sha256(name.strip().encode()).hexdigest()[:24]
        row = {"public_skill": name, "source_skill_sha256": file_hash(source)}
        for collection, filename, expected in [("body", "SKILL.md", expected_body), ("meta", "meta.md", expected_meta)]:
            path = docs / collection / segment / filename
            expected_hash = hashlib.sha256(expected.encode()).hexdigest()
            # Read twice to expose a refresh during the observation window.
            observed = file_hash(path) if path.is_file() else None
            observed_after = file_hash(path) if path.is_file() else None
            row[collection] = {"expected_normalized_sha256": expected_hash, "observed_sha256": observed, "matches": observed == expected_hash, "stable_during_read": observed == observed_after}
        identities.append(row)
    after_bytes = mapping_path.read_bytes()
    stable = before_bytes == after_bytes and all(row[k]["stable_during_read"] for row in identities for k in ("body", "meta"))
    return {
        "capture_started_at": started, "capture_finished_at": datetime.now(timezone.utc).isoformat(),
        "mapping": mapping_path.name, "index_fingerprint": fingerprint,
        "allowed_skill_count": len(names), "unique_allowed_skill_count": len(set(names)),
        "allowed_list_sha256": content_hash(names), "public_intersection_count": len(intersection),
        "non_public_only_count": len(set(names) - public_names),
        "public_intersection_sha256": content_hash(intersection),
        "public_body_content_matches": sum(row["body"]["matches"] for row in identities),
        "public_meta_content_matches": sum(row["meta"]["matches"] for row in identities),
        "mapping_sha256_before": hashlib.sha256(before_bytes).hexdigest(), "mapping_sha256_after": hashlib.sha256(after_bytes).hexdigest(),
        "stable_during_capture": stable,
        "identity_scope": "Normalized managed meta/body content only; raw winning source path, full entrypoint bytes and all reference identities are not established. This is an observation window, not an atomic runtime snapshot.",
        "public_content_identities": identities,
    }


def input_hashes(dataset_dir):
    return {name: file_hash(dataset_dir / name) for name in ARTIFACTS}


def controlled_fixture():
    return {"kind": "controlled_static_fixture_not_harness_replay", "candidates": [{"name": "gardening", "score": 0.75}, {"name": "writing", "score": 0.5}], "payload": {"currentUserMessage": "Help me grow basil indoors.", "candidateSkills": ["gardening", "writing"]}}


def restore_check(dataset_dir, output_dir):
    before = input_hashes(dataset_dir)
    # This validates filesystem isolation and deterministic serialization only.
    # The actual installed-harness pipeline replay is a separate M0 artifact.
    fixture = controlled_fixture()
    candidates_before = content_hash(fixture["candidates"])
    payload_before = content_hash(fixture["payload"])
    with tempfile.TemporaryDirectory(prefix="restore-fixture-", dir=output_dir) as folder:
        temporary_root = Path(folder)
        path = temporary_root / "fixture.json"
        write_new(path, fixture)
        reloaded = json.loads(path.read_text(encoding="utf-8"))
    regenerated = controlled_fixture()
    candidates_after = content_hash(regenerated["candidates"])
    payload_after = content_hash(regenerated["payload"])
    after = input_hashes(dataset_dir)
    passed = before == after and reloaded == regenerated and candidates_before == candidates_after and payload_before == payload_after and not temporary_root.exists()
    return {"schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(), "passed": passed, "scope": fixture["kind"], "baseline_inputs_before": before, "baseline_inputs_after": after, "baseline_inputs_unchanged": before == after, "candidate_sha256_before": candidates_before, "candidate_sha256_after": candidates_after, "payload_sha256_before": payload_before, "payload_sha256_after": payload_after, "own_temporary_directory_removed": not temporary_root.exists(), "limitation": "The controlled fixture checks serialization and removal of only its own temporary files; it does not establish installed-harness replay fidelity or production database rollback."}


def capture(args):
    root, dataset, output = args.root.resolve(), args.dataset_dir.resolve(), args.output_dir.resolve()
    harness = args.harness_root.resolve()
    output.mkdir(parents=True, exist_ok=True)
    for name in ("baseline-manifest.json", "dataset-audit.json", "baseline-restore-check.json"):
        if (output / name).exists():
            raise FileExistsError(output / name)
    ignored = subprocess.run(["git", "-C", str(root), "check-ignore", "--quiet", str(output / "baseline-manifest.json")], capture_output=True)
    if ignored.returncode != 0 or output == dataset:
        raise ValueError("Output must be an ignored run directory, separate from baseline inputs")
    before = input_hashes(dataset)
    # Use the reusable CLI once; it independently refuses to overwrite baseline.
    subprocess.run([sys.executable, str(root / "experiments/scripts/audit_routing_dataset.py"), "--root", str(root), "--dataset-dir", str(dataset), "--output-dir", str(output)], check=True)
    audit = json.loads((output / "dataset-audit.json").read_text(encoding="utf-8"))
    public = {path.parent.name for path in (root / "skills").glob("*/SKILL.md")}
    runtime = args.runtime_skills_dir.resolve()
    runtime_identity = [public_materialization(root, path, runtime, public) for path in sorted((runtime / "agents").glob("*.json"))]
    configuration = config_summary(args.openclaw_config, args.qmd_config)
    snapshot_embedding = json.loads((dataset / "embedding_manifest.json").read_text(encoding="utf-8"))
    results_metadata = json.loads((dataset / "routing_benchmark_results.json").read_text(encoding="utf-8"))["metadata"]
    files = {
        "workspace_uv_lock": root / "experiments/uv.lock", "workspace_pyproject": root / "experiments/pyproject.toml",
        "source_uv_lock": args.source_root / "experiments/uv.lock", "harness_package": harness / "package.json",
        "harness_pnpm_lock": harness / "pnpm-lock.yaml", "harness_entry": harness / "dist/index.js",
        "typesafe_package": args.typesafe_root / "package.json", "typesafe_pnpm_lock": args.typesafe_root / "pnpm-lock.yaml",
    }
    build_files = {str(path.relative_to(harness)): file_hash(path) for path in sorted((harness / "dist").rglob("*.js"))}
    check = restore_check(dataset, output)
    after = input_hashes(dataset)
    mismatches = []
    expected = {"model": "text-embedding-3-small", "dimension": 1536}
    if {key: snapshot_embedding.get(key) for key in expected} != expected:
        mismatches.append("Historical embedding artifact differs from the explicit experiment model/dimension requirement.")
    if configuration["plugin_qmd"]["embedding"].get("model") != configuration["qmd_yaml_defaults"].get("embed_api_model") or configuration["plugin_qmd"]["embedding"].get("dimension") != configuration["qmd_yaml_defaults"].get("embed_dimension"):
        mismatches.append("Plugin embedding configuration differs from QMD YAML defaults; use explicit experiment overrides without changing either live configuration.")
    manifest = {
        "schema_version": 1, "capture_started_at": audit["created_at"], "capture_finished_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Read-only public skill/experiment baseline with allowlisted runtime configuration and public content intersections.",
        "repositories": {"workspace": git_identity(root), "source_omni": git_identity(args.source_root), "installed_harness_source": git_identity(harness)},
        "dependency_and_build_files": {key: {"path": str(path), "sha256": file_hash(path) if path.is_file() else None} for key, path in files.items()},
        "installed_dist": {"js_file_count": len(build_files), "aggregate_sha256": content_hash(build_files), "files": build_files, "resident_build_status": "Installed disk artifacts only; running gateway build identity is not proven."},
        "baseline_input_artifacts": {key: {"path": str(dataset / key), "sha256_before": value, "sha256_after": after[key]} for key, value in before.items()},
        "baseline_inputs_unchanged": before == after,
        "public_dataset": {"skill_count": len(public), "query_count": audit["counts"]["generated_queries"], "structural_pass": audit["structural_pass"], "source_file_hash_agreement": {key: audit["counts"][key] for key in ("manifest_source_files", "current_source_files", "matching_source_files")}, "audit_artifact_sha256": file_hash(output / "dataset-audit.json"), "snapshot_source_git_commit": audit["inputs"]["snapshot_git_commit"]},
        "models": {"explicit_experiment_embedding_requirement": expected, "historical_embedding_artifact": scalar_fields(snapshot_embedding, ("model", "dimension", "config_fingerprint")), "historical_result": scalar_fields(results_metadata, ("embedding_model", "dimension", "rerank_model")), "runtime_configuration": configuration},
        "runtime_public_skill_intersections": runtime_identity,
        "mismatch_notes": mismatches,
        "restore_check_passed": check["passed"],
        "unresolved": ["No paid model or network request was made; actual host/provider request behavior is not validated.", "The running gateway build, winning source path precedence and full runtime reference content identities remain unproven.", "Runtime mappings and managed files are live and not locked; stable observations are not an atomic snapshot.", "Static isolation fixture is not installed-harness replay; separate M0 replay evidence is required."],
    }
    if before != after or not check["passed"]:
        raise RuntimeError("Baseline input or fixture isolation verification failed")
    write_new(output / "baseline-restore-check.json", check)
    write_new(output / "baseline-manifest.json", manifest)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--dataset-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--harness-root", type=Path, default=Path.home() / ".openclaw/extensions/skill-harness")
    parser.add_argument("--typesafe-root", type=Path, default=Path.home() / ".openclaw/extensions/typesafe")
    parser.add_argument("--runtime-skills-dir", type=Path, default=Path.home() / ".openclaw/plugins/skill-harness/qmd/skills")
    parser.add_argument("--openclaw-config", type=Path, default=Path.home() / ".openclaw/openclaw.json")
    parser.add_argument("--qmd-config", type=Path, default=Path.home() / ".config/qmd/index.yml")
    manifest = capture(parser.parse_args())
    print(json.dumps({"baseline_inputs_unchanged": manifest["baseline_inputs_unchanged"], "structural_pass": manifest["public_dataset"]["structural_pass"], "restore_check_passed": manifest["restore_check_passed"], "runtime_public_counts": [{key: row[key] for key in ("mapping", "allowed_skill_count", "public_intersection_count", "public_body_content_matches", "public_meta_content_matches", "stable_during_capture")} for row in manifest["runtime_public_skill_intersections"]], "mismatch_notes": manifest["mismatch_notes"]}, indent=2))


if __name__ == "__main__":
    main()
