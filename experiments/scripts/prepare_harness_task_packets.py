"""Prepare opaque solver packets from completed frozen task routing. No models."""
import argparse
import json
from pathlib import Path

from harness_task_checks import public_task_input
from summarize_harness_variants import checked_content, file_sha

ROOT = Path(__file__).resolve().parents[2]


def read(path):
    return json.loads(path.read_text())


def write_new(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def prepare_packets(run_dir):
    run_dir = Path(run_dir).resolve()
    if not run_dir.is_relative_to(ROOT / "experiments/datasets"):
        raise ValueError("Run directory outside experiments")
    select_dir = run_dir / "task-routing/select"
    manifest_path = select_dir / "manifest.json"
    manifest = read(manifest_path)
    checked_content(manifest, "contentSha256")
    common = manifest["binding"]["common"]
    freeze_path = run_dir / "m1-freeze.json"
    freeze = read(freeze_path)
    fixture = ROOT / "experiments/fixtures/harness_task_checks.json"
    if (manifest["status"] != "complete" or common["m1FreezeSha256"] != file_sha(freeze_path)
            or common["challengerConfigSha256"] != file_sha(run_dir / "challenger-config.json")
            or common["taskChecksSha256"] != file_sha(fixture)
            or file_sha(fixture) != freeze["artifacts"][fixture.relative_to(ROOT).as_posix()]):
        raise ValueError("Frozen routing provenance mismatch")
    ids = [f"t{i:02d}" for i in range(1, 13)]
    if [row["id"] for row in manifest["cases"]] != ids:
        raise ValueError("Exactly12 ordered completed task routes required")
    sources = {row["path"]: row["recorded_sha256"] for row in read(run_dir / "dataset-audit.json")["source_file_audits"]}
    output = run_dir / "task-generation"
    if output.exists():
        raise ValueError("Existing task-generation preserved; no automatic restart")
    output.mkdir()
    assignments = []
    for index, entry in enumerate(manifest["cases"]):
        route_path = select_dir / (entry["id"] + ".json")
        if file_sha(route_path) != entry["sha256"]:
            raise ValueError("Route checkpoint bytes changed")
        route = read(route_path)
        checked_content(route, "contentSha256")
        value = route["value"]
        task = public_task_input(entry["id"])
        if value["status"] != "complete" or value["input"] != {"id": entry["id"], "publicTask": task}:
            raise ValueError("Public task projection mismatch")
        # Alternate first arm to avoid assigning a constant order to variants.
        for arm in (["baseline", "challenger"] if index % 2 == 0 else ["challenger", "baseline"]):
            result = value["arms"][arm]
            if result["status"] not in {"completed", "skipped-empty-pool"}:
                raise ValueError("Unavailable route cannot supply a solver packet")
            selected = result["selection"]["skills"]
            if len(selected) > 6 or len(set(selected)) != len(selected):
                raise ValueError("Invalid selected skill set")
            instructions, references = [], []
            for name in selected:
                if not isinstance(name, str) or Path(name).name != name or name in {".", ".."}:
                    raise ValueError("Unsafe selected skill name")
                source = f"skills/{name}/SKILL.md"
                path = ROOT / source
                if path.is_symlink() or file_sha(path) != sources.get(source):
                    raise ValueError("Selected full SKILL differs from frozen public source")
                instructions.append({"name": name, "content": path.read_text(), "sha256": file_sha(path)})
                for relative, expected in sorted(sources.items()):
                    if relative.startswith(f"skills/{name}/references/") and relative.endswith(".md"):
                        ref = ROOT / relative
                        if ref.is_symlink() or not ref.resolve().is_relative_to(ROOT / "skills" / name) or file_sha(ref) != expected:
                            raise ValueError("Public reference differs from frozen source")
                        references.append({"path": str(ref), "sha256": expected})
            opaque = f"u{len(assignments) + 1:03d}"
            folder = output / opaque
            folder.mkdir()
            packet_path = folder / "packet.json"
            packet = {"public_task": task, "selected_skill_instructions": instructions,
                      "public_reference_allowlist": references}
            write_new(packet_path, packet)
            assignments.append({"opaque_id": opaque, "task_id": entry["id"], "arm": arm,
                                "packet": str(packet_path.relative_to(run_dir)), "packet_sha256": file_sha(packet_path),
                                "artifact": str((folder / task["artifact_contract"]["filename"]).relative_to(run_dir)),
                                "selected_skills": selected, "route_sha256": entry["sha256"],
                                "status": "prepared", "attempts_allowed": 1})
    record = {"schema_version": 1, "status": "prepared", "routing_manifest_sha256": file_sha(manifest_path),
              "challenger_config_sha256": common["challengerConfigSha256"],
              "m1_freeze_sha256": common["m1FreezeSha256"], "native_worker_turns_max": 24,
              "grader_feedback_to_workers": False, "model_override": None, "assignments": assignments}
    write_new(output / "assignments.json", record)
    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    record = prepare_packets(args.run_dir)
    print(json.dumps({"status": record["status"], "packets": len(record["assignments"]), "model_calls": 0}))
