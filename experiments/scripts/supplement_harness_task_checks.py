"""Supplement four fixed artifacts for reviewed public-API compatibility only.

Primary grader, cases, artifacts and scores remain immutable. This does not
change routing adoption or count as another model-generation attempt.
"""
import argparse
import ast
import importlib.util
from pathlib import Path

from prepare_harness_task_packets import ROOT, read, write_new
from summarize_harness_variants import file_sha
from harness_task_checks import public_task_input


def supplement(run_dir):
    run_dir = Path(run_dir).resolve()
    if not run_dir.is_relative_to(ROOT / "experiments/datasets"):
        raise ValueError("Run outside experiments")
    primary_path = run_dir / "task-results.json"
    primary_hash = file_sha(primary_path)
    primary = read(primary_path)
    freeze = read(run_dir / "m1-freeze.json")
    original = ROOT / "experiments/scripts/harness_task_checks.py"
    original_hash = file_sha(original)
    if original_hash != freeze["artifacts"][original.relative_to(ROOT).as_posix()]:
        raise ValueError("Frozen primary grader changed")
    selected = []
    for pair in primary["pairs"]:
        if pair["id"] not in {"t05", "t12"}:
            continue
        for arm in ["baseline", "challenger"]:
            row = pair[arm]
            artifact = run_dir / row["artifact"]
            if artifact.name != public_task_input(pair["id"])["artifact_contract"]["filename"]:
                raise ValueError("Reviewed artifact differs from contract filename")
            if row["success"] is not False or row["checks"] != [{"name": "bounded-execution-or-contract", "passed": False}] or artifact.is_symlink() or file_sha(artifact) != row["artifact_sha256"]:
                raise ValueError("Only the four unchanged reviewed primary rejections are eligible")
            if pair["id"] == "t12":
                for node in ast.walk(ast.parse(artifact.read_text())):
                    if isinstance(node, ast.Attribute) and node.attr == "split":
                        if not (isinstance(node.value, ast.Name) and node.value.id == "text"):
                            raise ValueError("Only reviewed text.split is allowed")
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "split":
                        if len(node.args) != 1 or not isinstance(node.args[0], ast.Constant) or node.args[0].value != "\n" or node.keywords:
                            raise ValueError("Only reviewed text.split(newline) is allowed")
            selected.append((pair["id"], arm, row, artifact))
    if len(selected) != 4:
        raise ValueError("Exactly four fixed artifacts required")
    source = original.read_text()
    replacements = {
        'ROOT = Path(__file__).resolve().parents[2]': f"ROOT = Path({str(ROOT)!r})",
        '"splitlines", "strip"': '"splitlines", "split", "strip"',
        '"ValueError", "Exception"]': '"ValueError", "Exception", "RecursionError"]',
        '"coalesce", "ifnull"}': '"coalesce", "ifnull", "typeof"}',
    }
    for before, after in replacements.items():
        if source.count(before) != 1:
            raise ValueError("Unexpected primary source; compatibility patch refused")
        source = source.replace(before, after)
    output = run_dir / "task-generation/supplementary"
    output.mkdir()
    copied = output / "public_api_compat_grader.py"
    with copied.open("x") as stream:
        stream.write(source)
    spec = importlib.util.spec_from_file_location("public_api_compat_grader", copied)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    results = []
    for task_id, arm, row, artifact in selected:
        observed = module.run_task_check(task_id, artifact.parent)
        results.append({"id": task_id, "arm": arm, "artifact_sha256": row["artifact_sha256"], **observed})
    if file_sha(primary_path) != primary_hash or file_sha(original) != original_hash:
        raise ValueError("Primary artifacts changed")
    record = {"schema_version": 1, "status": "complete", "method": "public-api-compatibility-supplement-v1",
              "primary_results_sha256": primary_hash, "primary_grader_sha256": original_hash,
              "supplementary_grader_sha256": file_sha(copied),
              "exact_source_replacements": replacements, "results": results,
              "limitations": ["Original primary result remains10/12per arm; four primary rejections did not reach semantic checks.",
                              "Only SQL typeof, reviewed text.split(newline), and RecursionError are added. Same semantic cases and resource limits.",
                              "Post-observation supplementary execution; cannot replace primary scores or support adoption. No model or artifact retries."]}
    write_new(run_dir / "task-results-supplement.json", record)
    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    report = supplement(parser.parse_args().run_dir)
    print({"status": report["status"], "supplementary_artifacts": len(report["results"]), "passed": sum(row["passed"] for row in report["results"]), "primary_scores_unchanged": True})
