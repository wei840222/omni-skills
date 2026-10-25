"""Launch one frozen task-routing stage; never print settings or credentials."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

from harness_task_checks import public_task_input
from run_harness_stage import WORKSPACE, MODELS, frozen_inputs, load_endpoints, read_json


def task_settings(stage, run_dir):
    run_dir = Path(run_dir).resolve()
    if stage not in {"raw", "prepare", "select"} or not run_dir.is_relative_to(WORKSPACE / "experiments/datasets"):
        raise ValueError("Invalid task stage/directory")
    frozen_inputs(WORKSPACE, run_dir)
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    freeze = read_json(run_dir / "m1-freeze.json")
    settings = {
        "stage": stage, "runDir": str(run_dir),
        "tasks": [{"id": f"t{i:02d}", "publicTask": public_task_input(f"t{i:02d}")} for i in range(1, 13)],
        "expectedTaskChecksSha256": freeze["artifacts"]["experiments/fixtures/harness_task_checks.json"],
        "m1FreezeSha256": digest(run_dir / "m1-freeze.json"),
        "challengerConfigSha256": digest(run_dir / "challenger-config.json"),
        "policy": read_json(run_dir / "m0-query-probes.json")["raw_hitlists"]["policies"],
        "timeoutMs": 8000, "models": dict(MODELS),
    }
    # The producer requires explicit endpoint identity even during its offline
    # preparation stage. Only the existing allowlisted fields enter stdin.
    settings["endpoints"] = load_endpoints(Path.home() / ".config/qmd/index.yml", "capture")
    return settings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=["raw", "prepare", "select"], required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        settings = task_settings(args.stage, args.run_dir)
        child = subprocess.run(
            ["node", str(WORKSPACE / "experiments/scripts/capture_harness_tasks.mjs")],
            input=json.dumps(settings, ensure_ascii=False, allow_nan=False),
            capture_output=True, text=True, check=False,
        )
        if child.returncode:
            raise ValueError("Task stage failed")
        result = json.loads(child.stdout.strip().splitlines()[-1])
        if result["status"] not in {"complete", "cached-complete"} or result.get("tasks") != 12 or result.get("stage") != args.stage:
            raise ValueError("Incomplete task stage")
        print(json.dumps({"stage": args.stage, "status": result["status"], "tasks": 12,
                          "physicalAttempts": result["physicalAttempts"], "cacheHits": result["cacheHits"]}))
    except Exception:
        print("Task stage stopped; inspect preserved artifacts. Settings and child diagnostics omitted.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
