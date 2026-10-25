#!/usr/bin/env python3
"""Launch one frozen harness stage in a fresh Node process; never log settings."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit, urlunsplit

import yaml

WORKSPACE = Path(__file__).resolve().parents[2]
SCRIPTS = {"capture": "capture_harness_pilot.mjs", "prepare": "prepare_harness_variants.mjs", "select": "select_harness_candidates.mjs"}
MODELS = {"embedding": "text-embedding-3-small", "dimension": 1536, "expansion": "gemini-3.5-flash-lite", "expansionResolved": "gemini-3.5-flash-lite", "jev": "jev-latest", "jevResolved": "jev-1.14.0"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def project_case(row):
    if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not re.fullmatch(r"[A-Za-z0-9_-]+", row["id"]) or not isinstance(row.get("latest"), str) or not row["latest"].strip():
        raise ValueError("Invalid frozen public case")
    result = {"id": row["id"], "latest": row["latest"]}
    if "conversation" in row:
        if not isinstance(row["conversation"], list):
            raise ValueError("Invalid public conversation")
        turns = []
        for turn in row["conversation"]:
            text = turn.get("text", turn.get("content"))
            if turn.get("role") not in {"user", "assistant"} or not isinstance(text, str):
                raise ValueError("Invalid public conversation turn")
            turns.append({"role": turn["role"], "text": text})
        result["conversation"] = turns
    return result


def frozen_inputs(workspace, run_dir):
    """Read final labels only for id/split bookkeeping, after all byte checks."""
    try:
        freeze = read_json(run_dir / "m1-freeze.json")
        paths = {"cases": workspace / "experiments/fixtures/harness_pilot_cases.json", "labels": run_dir / "m1-silver-labels.json", "contract": workspace / "experiments/fixtures/harness_evaluation_contract.json", "protocol": workspace / "experiments/fixtures/harness_ablation_protocol.json"}
        if freeze.get("schema_version") != 1 or freeze.get("status") != "frozen" or not isinstance(freeze.get("artifacts"), dict):
            raise ValueError("Final M1 freeze is required")
        for key, filename in paths.items():
            expected = freeze.get(key + "_sha256")
            if not isinstance(expected, str) or not re.fullmatch(r"[a-f0-9]{64}", expected) or freeze["artifacts"].get(filename.relative_to(workspace).as_posix()) != expected:
                raise ValueError("Required frozen M1 artifact/hash is missing")
        artifact_paths = {}
        for relative, expected in freeze["artifacts"].items():
            if not isinstance(relative, str) or not relative or "\\" in relative or Path(relative).is_absolute() or ".." in Path(relative).parts or not isinstance(expected, str) or not re.fullmatch(r"[a-f0-9]{64}", expected):
                raise ValueError("Invalid frozen workspace artifact path/hash")
            filename = (workspace / relative).resolve()
            if not filename.is_relative_to(workspace):
                raise ValueError("Frozen workspace artifact escaped")
            artifact_paths[relative] = filename
        # Validate every path, including extra budget/review artifacts, before
        # opening any artifact bytes. The manifest itself is the sole prior read.
        artifact_bytes = {relative: filename.read_bytes() for relative, filename in artifact_paths.items()}
        actual = {relative: hashlib.sha256(value).hexdigest() for relative, value in artifact_bytes.items()}
        if any(actual[key] != expected for key, expected in freeze["artifacts"].items()):
            raise ValueError("Frozen workspace artifact changed")
        for key, filename in paths.items():
            relative = filename.relative_to(workspace).as_posix()
            if actual.get(relative) != freeze.get(key + "_sha256"):
                raise ValueError("Frozen M1 artifact/reference changed")
        labels = json.loads(artifact_bytes[paths["labels"].relative_to(workspace).as_posix()])
        if labels.get("schema_version") != 1 or labels.get("status") != "frozen" or labels.get("variant_observations_used") is not False or any(labels.get(key + "_sha256") != freeze[key + "_sha256"] for key in ("cases", "contract", "protocol")):
            raise ValueError("Final silver-label freeze/reference mismatch")
        parsed = json.loads(artifact_bytes[paths["cases"].relative_to(workspace).as_posix()])
        cases = [project_case(row) for row in (parsed["cases"] if isinstance(parsed, dict) else parsed)]
        by_id = {row["id"]: row for row in cases}
        splits = {}
        for annotation in labels["annotations"]:
            identity, split = annotation.get("id"), annotation.get("split")
            if identity not in by_id or identity in splits or split not in {"development", "holdout"}:
                raise ValueError("Invalid final split bookkeeping")
            splits[identity] = split
        partitions = {phase: [row["id"] for row in cases if splits.get(row["id"]) == phase] for phase in ("development", "holdout")}
        if len(cases) != 180 or len(by_id) != 180 or len(splits) != 180 or len(partitions["development"]) != 120 or len(partitions["holdout"]) != 60:
            raise ValueError("Final splits must cover all180 cases as120/60")
        return cases, partitions, freeze["cases_sha256"]
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as error:
        raise ValueError("Final frozen artifacts are missing or invalid") from None


def normalize_endpoint(value, provider):
    if not isinstance(value, str) or "?" in value or "#" in value or any(ord(character) < 32 for character in value):
        raise ValueError("Model URL must not contain query/fragment")
    parts = urlsplit(value.strip())
    if parts.scheme not in {"http", "https"} or not parts.hostname or parts.username is not None or parts.password is not None or "@" in parts.netloc:
        raise ValueError("Model URL must be explicit HTTP(S) without userinfo")
    if parts.port is not None and parts.port < 1:
        raise ValueError("Invalid model URL port")
    base = urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/"), "", ""))
    suffix = {"embedding": "/embeddings", "expansion": "/chat/completions", "jev": "/systemone"}[provider]
    if base.endswith(suffix):
        return base
    return base + (("/v1" if not parts.path.rstrip("/").endswith("/v1") else "") + suffix if provider == "jev" else suffix)


def resolve_key(value):
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ValueError("Model key reference must be a string")
    if value.startswith("env:"):
        if value[4:] not in os.environ:
            raise ValueError("Model key environment reference is unset")
        return os.environ[value[4:]]
    expanded = os.path.expandvars(value)
    if "$" in expanded:
        raise ValueError("Model key environment reference is unset")
    return expanded


def load_endpoints(config, stage):
    models = yaml.safe_load(config.expanduser().read_text(encoding="utf-8")).get("models", {})
    if models.get("generate_api_model") != MODELS["expansion"] or models.get("jev_api_model") != MODELS["jev"]:
        raise ValueError("Configured model aliases differ from frozen identities")
    fields = {"embedding": ("embed_api_url", "embed_api_key"), "expansion": ("generate_api_url", "generate_api_key"), "jev": ("jev_base_url", "jev_api_key")}
    providers = fields if stage == "capture" else {"jev": fields["jev"]}
    urls = {provider: normalize_endpoint(models.get(url), provider) for provider, (url, _) in providers.items()}
    return {provider: {"url": urls[provider], "apiKey": resolve_key(models.get(key))} for provider, (_, key) in providers.items()}


def selector_replays(rows, cases):
    if not isinstance(rows, list) or [row.get("id") for row in rows] != [row["id"] for row in cases]:
        raise ValueError("Prepared selector cases/order mismatch")
    result = []
    for replay, source in zip(rows, cases):
        original = replay["params"]
        if original.get("candidateExperiences", []) or original.get("relationEvidence", []):
            raise ValueError("Private/additional candidate sources are unavailable")
        skills = [{key: row[key] for key in ("name", "description")} for row in original["candidateSkills"]]
        if any(not all(isinstance(row[key], str) for key in row) for row in skills):
            raise ValueError("Invalid prepared skill metadata")
        params = {"latest": source["latest"], **({"conversation": source["conversation"]} if "conversation" in source else {}), "candidateSkills": skills, "candidateSources": {row["name"]: original.get("candidateSources", {}).get(row["name"], []) for row in skills}, "candidateExperiences": [], "relationEvidence": []}
        raw = replay["rawHitlistObservation"]
        if raw.get("query") != source["latest"] or any(key in raw for key in ("annotations", "expected", "acceptable_sets", "family", "kind", "labels")):
            raise ValueError("Prepared raw query contains mismatched/label fields")
        item = {"id": source["id"], "params": params, "rawHitlistObservation": raw}
        if "matchedSnippets" in replay:
            item["matchedSnippets"] = [{key: row[key] for key in ("skill", "collection", "path", "text", "chunkSha256", "score")} for row in replay["matchedSnippets"]]
        result.append(item)
    return result


def build_settings(*, stage, phase, run_dir, workspace=WORKSPACE, qmd_config=None, fusion=None, pool_limit=None, snippet=None, variant=None):
    workspace, run_dir = Path(workspace).resolve(), Path(run_dir).resolve()
    if stage not in SCRIPTS or phase not in {"development", "holdout"} or run_dir == workspace / "experiments/datasets" or not run_dir.is_relative_to(workspace / "experiments/datasets"):
        raise ValueError("Invalid stage, phase or run directory")
    cases, partitions, cases_sha = frozen_inputs(workspace, run_dir)
    selected = [row for row in cases if row["id"] in set(partitions[phase])]
    settings = {"runDir": str(run_dir), "phase": phase, "expectedCasesSha256": cases_sha}
    if phase == "holdout":
        challenger = run_dir / "challenger-config.json"
        frozen = read_json(challenger)
        freeze = read_json(run_dir / "m1-freeze.json")
        if frozen.get("schema_version") != 1 or frozen.get("status") != "frozen" or frozen.get("m1CasesSha256") != cases_sha or frozen.get("m1LabelsSha256") != freeze["labels_sha256"] or frozen.get("contractSha256") != freeze["contract_sha256"] or ("protocolSha256" in frozen and frozen["protocolSha256"] != freeze["protocol_sha256"]):
            raise ValueError("Holdout needs a frozen matching challenger")
        settings["challengerConfigSha256"] = digest(challenger)
    policy = read_json(run_dir / "m0-query-probes.json")["raw_hitlists"]["policies"]
    if stage == "prepare":
        if fusion not in {"current-max", "skill-identity-sum"} or pool_limit not in {6, 10, 20} or snippet not in {"none", "matched-reference"} or variant is not None:
            raise ValueError("Prepare requires explicit fusion/pool/snippet flags")
        settings["variant"] = {"fusion": fusion, "poolLimit": pool_limit, "snippet": snippet}
        return settings
    settings.update({"cases": selected, "casePartitions": partitions, "models": dict(MODELS)})
    if stage == "capture":
        if variant is not None or any(value is not None for value in (fusion, pool_limit, snippet)):
            raise ValueError("Capture accepts no variant options")
        settings["policy"] = {"qmdTimeoutMs": policy["qmd"]["timeoutMs"], "collectionWeights": policy["skills"]["search"]["collectionWeights"], "routing": policy["routing"]}
    else:
        if not isinstance(variant, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", variant) or any(value is not None for value in (fusion, pool_limit, snippet)):
            raise ValueError("Select requires one existing safe variant name")
        artifact = read_json(run_dir / phase / "variants" / (variant + ".json"))
        if artifact.get("status") != "complete" or artifact.get("variant") != variant or artifact.get("phase") != phase or artifact.get("expectedCasesSha256") != cases_sha or artifact.get("policy") != policy or artifact.get("timeoutMs") != 8000 or [project_case(row) for row in artifact["cases"]] != selected:
            raise ValueError("Prepared variant differs from frozen phase/policy")
        if phase == "holdout" and artifact.get("challengerConfigSha256") != settings["challengerConfigSha256"]:
            raise ValueError("Prepared variant uses another challenger freeze")
        settings.update({"variant": variant, "config": artifact["config"], "policy": policy, "timeoutMs": 8000, "expectedRawManifestSha256": artifact["expectedRawManifestSha256"], "replayCases": selector_replays(artifact["replayCases"], selected), "hostSourcePins": read_json(run_dir / "m0-host-probes.json")["provenance"]["sources"]})
    settings["endpoints"] = load_endpoints(Path(qmd_config) if qmd_config else Path.home() / ".config/qmd/index.yml", stage)
    return settings


def run_stage(*, runner=subprocess.run, **arguments):
    try:
        settings = build_settings(**arguments)
        stage = arguments["stage"]; workspace = Path(arguments.get("workspace", WORKSPACE))
        child = runner(["node", str(workspace / "experiments/scripts" / SCRIPTS[stage])], input=json.dumps(settings, ensure_ascii=False, allow_nan=False), capture_output=True, text=True, check=False)
        if child.returncode:
            raise ValueError("Child stage failed")
        result = json.loads(child.stdout.strip().splitlines()[-1])
        stats = result.get("currentInvocationTransport", {})
        summary = {"stage": stage, "phase": arguments["phase"], "status": result["status"], "cases": result["cases"], "physicalAttempts": stats.get("physicalAttempts", 0), "cacheHits": stats.get("cacheHits", 0)}
        if summary["status"] not in {"complete", "cached-complete", "cached-artifact"} or type(summary["cases"]) is not int or summary["cases"] != (120 if arguments["phase"] == "development" else 60) or any(type(summary[key]) is not int or summary[key] < 0 for key in ("physicalAttempts", "cacheHits")):
            raise ValueError("Child summary is invalid")
        return summary
    except Exception:
        raise RuntimeError("Stage failed; child diagnostics and settings are suppressed") from None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=SCRIPTS, required=True)
    parser.add_argument("--phase", choices=("development", "holdout"), required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--qmd-config", type=Path)
    parser.add_argument("--fusion", choices=("current-max", "skill-identity-sum"))
    parser.add_argument("--pool-limit", type=int, choices=(6, 10, 20))
    parser.add_argument("--snippet", choices=("none", "matched-reference"))
    parser.add_argument("--variant")
    try:
        print(json.dumps(run_stage(**vars(parser.parse_args()))))
    except Exception:
        print("Stage launch stopped; inspect frozen inputs/run artifacts. Settings and child diagnostics omitted.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
