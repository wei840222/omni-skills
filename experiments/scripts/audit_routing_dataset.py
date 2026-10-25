#!/usr/bin/env python3
"""Audit skill-authored query/source identities without changing labels or data.

This checks structural provenance, not routing correctness. Existing pass values
are author assertions; evidence coverage and known semantic issues stay separate.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

import yaml


def content_hash(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_dataset(root: Path, dataset_dir: Path):
    root, dataset_dir = root.resolve(), dataset_dir.resolve()
    queries = json.loads((dataset_dir / "benchmark_queries.json").read_text(encoding="utf-8"))
    documents = json.loads((dataset_dir / "documents.json").read_text(encoding="utf-8"))
    manifest = json.loads((dataset_dir / "manifest.json").read_text(encoding="utf-8"))
    if not isinstance(queries, list) or not isinstance(documents, dict) or not isinstance(manifest, dict):
        raise ValueError("Expected query list, document collections object and manifest object")
    errors = []

    def error(code, **details):
        errors.append({"code": code, **details})

    if content_hash(queries) != manifest.get("queries_hash"):
        error("queries_hash_mismatch")
    if content_hash(documents) != manifest.get("corpus_hash"):
        error("corpus_hash_mismatch")
    skill_files = sorted((root / "skills").glob("*/SKILL.md"))
    skills = {path.parent.name: path for path in skill_files}
    if not skills:
        error("empty_skill_catalog")
    for field, actual in [("skill_count", len(skills)), ("query_count", len(queries))]:
        if manifest.get(field) != actual:
            error("manifest_count_mismatch", field=field, manifest=manifest.get(field), actual=actual)

    source_hashes = manifest.get("source_files", {})
    if not isinstance(source_hashes, dict):
        error("invalid_source_files_manifest")
        source_hashes = {}
    current_sources = {}
    for path in skill_files:
        for source in [path, path.parent / "test-prompts.json", *sorted((path.parent / "references").rglob("*.md"))]:
            if source.exists():
                current_sources[str(source.relative_to(root))] = source
    source_audits = []
    for relative in sorted(set(source_hashes) | set(current_sources)):
        path = current_sources.get(relative)
        actual = file_hash(path) if path else None
        recorded = source_hashes.get(relative)
        source_audits.append({"path": relative, "recorded_sha256": recorded, "current_sha256": actual, "matches": actual is not None and recorded == actual})
        if actual is None:
            error("missing_current_source", path=relative)
        elif recorded is None:
            error("missing_source_hash", path=relative)
        elif recorded != actual:
            error("source_content_changed", path=relative)

    frontmatter_fields, metadata_fields, source_fields = Counter(), Counter(), Counter()
    category_values = defaultdict(list)
    metadata_types = defaultdict(Counter)
    source_records = defaultdict(list)
    evidence_fields = ("expected", "actual", "pass", "evidence")
    evidence = {field: Counter() for field in evidence_fields}
    pass_assertions = Counter()
    source_count = 0
    source_skills = 0
    related_skills_count = 0
    for slug, path in skills.items():
        text = path.read_text(encoding="utf-8")
        try:
            sections = text.split("---", 2)
            metadata = yaml.safe_load(sections[1]) if text.startswith("---") and len(sections) == 3 else None
        except yaml.YAMLError:
            metadata = None
        if not isinstance(metadata, dict):
            error("invalid_skill_frontmatter", skill=slug)
        else:
            frontmatter_fields.update(metadata.keys())
            nested = metadata.get("metadata", {})
            if isinstance(nested, dict):
                metadata_fields.update(nested.keys())
                for field, value in nested.items():
                    metadata_types[field][type(value).__name__] += 1
                if "category" in nested:
                    category_values[json.dumps(nested["category"], ensure_ascii=False) if not isinstance(nested["category"], str) else nested["category"]].append(slug)
                related_skills_count += int(bool(nested.get("related-skills")))
        test_path = path.parent / "test-prompts.json"
        if not test_path.exists():
            error("missing_test_source", skill=slug)
            continue
        try:
            records = json.loads(test_path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError):
            error("invalid_test_source_json", skill=slug)
            continue
        if not isinstance(records, list) or not records:
            error("invalid_test_source_list", skill=slug)
            continue
        source_skills += 1
        for index, record in enumerate(records, 1):
            source_count += 1
            if not isinstance(record, dict):
                error("invalid_source_record", skill=slug, index=index)
                continue
            source_fields.update(record.keys())
            query_id = f"{slug}_{record.get('id', index)}"
            if not isinstance(record.get("prompt"), str) or not record["prompt"].strip():
                error("invalid_source_prompt", query_id=query_id)
            for field in evidence_fields:
                evidence[field]["present" if field in record else "missing"] += 1
                if field in record:
                    evidence[field]["nonempty" if record[field] not in (None, "", [], {}) else "empty"] += 1
            assertion = record.get("pass")
            pass_assertions["true" if assertion is True else "false" if assertion is False else "missing" if "pass" not in record else "other"] += 1
            identity = {"query_id": query_id, "ground_truth_skill": slug, "natural_prompt": record.get("prompt"), "expected": record.get("expected", "")}
            source_records[query_id].append({"identity": identity, "record": record, "index": index, "path": str(test_path.relative_to(root))})
    for query_id, records in source_records.items():
        if len(records) > 1:
            error("duplicate_source_query_id", query_id=query_id, count=len(records))

    ids = Counter()
    matched = 0
    query_audits = []
    for index, query in enumerate(queries, 1):
        if not isinstance(query, dict):
            error("invalid_query_record", index=index)
            continue
        query_id = query.get("query_id")
        if not isinstance(query_id, str) or not query_id:
            error("invalid_query_id", index=index)
            continue
        ids[query_id] += 1
        slug = query.get("ground_truth_skill")
        if not isinstance(slug, str) or slug not in skills:
            error("unknown_skill", query_id=query_id, skill=slug)
        if not isinstance(query.get("natural_prompt"), str) or not query["natural_prompt"].strip():
            error("invalid_query_prompt", query_id=query_id)
        sources = source_records.get(query_id, [])
        source = sources[0] if len(sources) == 1 else None
        identity_matches = source is not None and query == source["identity"]
        if not identity_matches:
            error("query_source_identity_mismatch", query_id=query_id, source_matches=len(sources))
        matched += int(identity_matches)
        record = source["record"] if source else {}
        query_audits.append({
            "index": index, "query_id": query_id, "owning_skill": slug,
            "query_sha256": content_hash(query), "source_path": source["path"] if source else None,
            "source_index": source["index"] if source else None,
            "source_record_sha256": content_hash(record) if source else None,
            "source_identity_sha256": content_hash(source["identity"]) if source else None,
            "identity_matches": identity_matches,
            "source_evidence": {field: {"present": field in record, "type": type(record[field]).__name__ if field in record else None, "sha256": content_hash(record[field]) if field in record else None} for field in evidence_fields},
            "source_pass_assertion": record.get("pass"),
        })
    for query_id, count in ids.items():
        if count > 1:
            error("duplicate_query_id", query_id=query_id, count=count)
    for query_id in sorted(set(source_records) - set(ids)):
        error("missing_generated_query", query_id=query_id)
    for collection, rows in documents.items():
        if not isinstance(rows, list):
            error("invalid_document_collection", collection=collection)
            continue
        if len(rows) != manifest.get("document_count_by_collection", {}).get(collection):
            error("document_count_mismatch", collection=collection, actual=len(rows))
        collection_skills = {row.get("skill") for row in rows if isinstance(row, dict) and isinstance(row.get("skill"), str)}
        if collection_skills != set(skills):
            error("document_skill_inventory_mismatch", collection=collection, missing=sorted(set(skills) - collection_skills), unknown=sorted(collection_skills - set(skills)))

    # This is a previously inspected issue, not a keyword-based label inference.
    semantic_issues = []
    avalanche_cases = [item for item in query_audits if item["owning_skill"] == "avalanche"]
    if avalanche_cases:
        skill_text = skills["avalanche"].read_text(encoding="utf-8") if "avalanche" in skills else ""
        source_prompts = [record["record"].get("prompt", "") for values in source_records.values() for record in values if record["identity"]["ground_truth_skill"] == "avalanche"]
        confirmed = "C-Chain" in skill_text and "AVAX" in skill_text and any("ski" in prompt.lower() or "backcountry" in prompt.lower() for prompt in source_prompts if isinstance(prompt, str))
        semantic_issues.append({
            "code": "avalanche_domain_mismatch", "kind": "manual_semantic_issue",
            "status": "previously_confirmed_still_present" if confirmed else "requires_revalidation",
            "query_ids": [item["query_id"] for item in avalanche_cases],
            "skill_path": "skills/avalanche/SKILL.md", "test_path": "skills/avalanche/test-prompts.json",
            "skill_sha256": file_hash(skills["avalanche"]) if "avalanche" in skills else None,
            "finding": ("The skill covers Avalanche blockchain operations; its authored cases concern snow avalanches, skiing and rescue."
                        if confirmed else "Previously identified snow/blockchain mismatch; the current source requires manual semantic revalidation before treating the issue as still present or resolved."),
            "action": "Manual semantic adjudication required; labels and baseline data remain unchanged.",
        })

    revision = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True)
    return {
        "schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Structural/source identity audit of skill-authored single-owning-skill labels; no independent semantic accuracy claim.",
        "inputs": {"root": str(root), "dataset_dir": str(dataset_dir), "current_git_commit": revision.stdout.strip() if revision.returncode == 0 else None, "snapshot_git_commit": manifest.get("source_git_commit"), "files": {name: file_hash(dataset_dir / name) for name in ("manifest.json", "benchmark_queries.json", "documents.json")}},
        "fingerprints": {"current_queries_sha256": content_hash(queries), "snapshot_queries_sha256": manifest.get("queries_hash"), "current_corpus_sha256": content_hash(documents), "snapshot_corpus_sha256": manifest.get("corpus_hash"), "current_source_files_sha256": content_hash({item["path"]: item["current_sha256"] for item in source_audits})},
        "counts": {"current_skills": len(skills), "skills_with_test_sources": source_skills, "source_test_records": source_count, "unique_source_query_ids": len(source_records), "generated_queries": len(queries), "unique_query_ids": len(ids), "identity_matched_queries": matched, "manifest_source_files": len(source_hashes), "current_source_files": len(current_sources), "matching_source_files": sum(item["matches"] for item in source_audits), "structural_errors": len(errors), "manual_semantic_issues": len(semantic_issues)},
        "structural_pass": not errors, "structural_errors": errors,
        "source_test_evidence": {"denominator": source_count, "fields": {field: {key: counts[key] for key in ("present", "missing", "nonempty", "empty")} for field, counts in evidence.items()}, "pass_assertions": dict(pass_assertions), "interpretation": "pass/actual/evidence are existing author-provided records, not independently reproduced or validated by this audit."},
        "metadata_inventory": {"skill_denominator": len(skills), "frontmatter_fields": dict(frontmatter_fields), "metadata_fields": dict(metadata_fields), "metadata_field_types": {key: dict(value) for key, value in metadata_types.items()}, "test_record_fields": dict(source_fields), "category_values": dict(category_values), "skills_with_related_skills": related_skills_count, "taxonomy_limit": "Only explicit metadata.category values are inventoried; no taxonomy or family assignments are inferred."},
        "manual_semantic_issues": semantic_issues,
        "unresolved": ["All remaining query/skill semantic compatibility is unreviewed.", "Source pass assertions and supplied evidence have not been independently reproduced.", "No accepted alternate, multiple-skill or no-skill labels are inferred."],
        "query_audits": query_audits, "source_file_audits": source_audits,
    }


def write_audit(audit, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "dataset-audit.json"
    with path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--dataset-dir", type=Path, required=True, help="Read-only existing snapshot directory")
    parser.add_argument("--output-dir", type=Path, required=True, help="New run directory under an ignored path")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    ignored = subprocess.run(["git", "-C", str(args.root), "check-ignore", "--quiet", str(output / "dataset-audit.json")], capture_output=True, text=True)
    if ignored.returncode != 0:
        parser.error("--output-dir must be inside a Git-ignored run directory under --root")
    if output == args.dataset_dir.resolve():
        parser.error("--output-dir must differ from the baseline dataset directory")
    audit = audit_dataset(args.root, args.dataset_dir)
    path = write_audit(audit, output)
    print(json.dumps({"output": str(path), "structural_pass": audit["structural_pass"], "counts": audit["counts"]}, indent=2))
    return 0 if audit["structural_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
