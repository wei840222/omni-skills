"""Execute frozen graders only after primary-agent artifact inspection."""
import argparse
import datetime
import json
from pathlib import Path

from harness_task_checks import public_task_input, run_task_check
from prepare_harness_task_packets import ROOT, read, write_new
from summarize_harness_variants import file_sha


def collect(run_dir):
    run_dir = Path(run_dir).resolve()
    if not run_dir.is_relative_to(ROOT / "experiments/datasets"):
        raise ValueError("Run outside experiments")
    generation = run_dir / "task-generation"
    assignments = read(generation / "assignments.json")
    review = read(generation / "source-review.json")
    if review.get("reviewer") != "primary-agent" or review.get("allow_execution") is not True:
        raise ValueError("Primary source inspection required before execution")
    freeze = read(run_dir / "m1-freeze.json")
    for name in ["experiments/fixtures/harness_task_checks.json", "experiments/scripts/harness_task_checks.py"]:
        if file_sha(ROOT / name) != freeze["artifacts"][name]:
            raise ValueError("Frozen grader changed")
    dispatched = [json.loads(line) for line in (generation / "dispatches.jsonl").read_text().splitlines()]
    if len(dispatched) != 24 or len({d["agent"] for d in dispatched}) != 24 or any(d["attempt"] != 1 or d["fresh_context"] is not True or d["model_override"] is not None for d in dispatched):
        raise ValueError("Require24 fresh single-attempt native worker dispatches")
    if len(assignments["assignments"]) != 24 or {d["opaque_id"] for d in dispatched} != {d["opaque_id"] for d in assignments["assignments"]}:
        raise ValueError("Dispatch/assignment mismatch")
    reviewed = {r["artifact"]: r["sha256"] for r in review["artifacts"]}
    pairs = {}
    for row in assignments["assignments"]:
        artifact = run_dir / row["artifact"]
        if artifact.name != public_task_input(row["task_id"])["artifact_contract"]["filename"]:
            raise ValueError("Reviewed artifact differs from contract filename")
        if not artifact.resolve().is_relative_to(generation) or artifact.is_symlink() or file_sha(artifact) != reviewed.get(row["artifact"]):
            raise ValueError("Unreviewed or changed task artifact")
        if file_sha(run_dir / row["packet"]) != row["packet_sha256"]:
            raise ValueError("Solver packet changed")
        pair = pairs.setdefault(row["task_id"], {"id": row["task_id"], "task": public_task_input(row["task_id"])["request"]})
        result = run_task_check(row["task_id"], artifact.parent)
        pair[row["arm"]] = {"status": "completed", "success": result["passed"], "artifact": row["artifact"],
                            "artifact_sha256": file_sha(artifact), "packet_sha256": row["packet_sha256"],
                            "selected_skills": row["selected_skills"], "checks": result["checks"], "failures": result["failures"],
                            "native_model": None, "native_usage": None, "attempts": 1}
    values = [pairs[key] for key in sorted(pairs)]
    if len(values) != 12 or any(not {"baseline", "challenger"}.issubset(pair) for pair in values):
        raise ValueError("Incomplete paired tasks")
    record = {"schema_version": 1, "status": "complete", "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "pairs": values, "actual_native_worker_turns": 24,
              "successes": {arm: sum(pair[arm]["success"] for pair in values) for arm in ["baseline", "challenger"]},
              "paired_outcomes": {"both_pass": sum(p["baseline"]["success"] and p["challenger"]["success"] for p in values),
                                  "baseline_only": sum(p["baseline"]["success"] and not p["challenger"]["success"] for p in values),
                                  "challenger_only": sum(p["challenger"]["success"] and not p["baseline"]["success"] for p in values)},
              "provenance": {"assignments_sha256": file_sha(generation / "assignments.json"), "dispatches_sha256": file_sha(generation / "dispatches.jsonl"),
                             "source_review_sha256": file_sha(generation / "source-review.json"), "m1_freeze_sha256": file_sha(run_dir / "m1-freeze.json"),
                             "routing_manifest_sha256": assignments["routing_manifest_sha256"], "challenger_config_sha256": assignments["challenger_config_sha256"]},
              "limitations": ["Twelve small public tasks with one generation attempt per arm; no no-harness control or repeated sampling.",
                              "Inherited native runtime model, exact identity/usage not exposed; costs are not included in Jev totals.",
                              "Both arms may select identical skills; passing artifacts do not establish a causal benefit from skill loading.",
                              "Parent inspected artifact source before bounded execution. Guards are not an adversarial OS sandbox."]}
    write_new(run_dir / "task-results.json", record)
    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    report = collect(args.run_dir)
    print(json.dumps({"status": report["status"], "pairs": len(report["pairs"]), "successes": report["successes"], "paired_outcomes": report["paired_outcomes"]}))
