import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from collect_harness_tasks import collect
from harness_task_checks import public_task_input
from prepare_harness_task_packets import ROOT, write_new
from summarize_harness_variants import file_sha


class TaskCollectionTests(unittest.TestCase):
    def make_run(self, folder, wrong_filename=False):
        run = Path(folder)
        generation = run / "task-generation"
        generation.mkdir()
        rows, reviews, dispatches = [], [], []
        for index in range(24):
            opaque = f"u{index + 1:03d}"
            task_id = f"t{index // 2 + 1:02d}"
            arm = ["baseline", "challenger"][index % 2]
            task_dir = generation / opaque
            task_dir.mkdir()
            filename = public_task_input(task_id)["artifact_contract"]["filename"]
            artifact = task_dir / filename
            artifact.write_text("unreviewed contract file" if wrong_filename and index == 0 else "reviewed artifact")
            if wrong_filename and index == 0:
                artifact = task_dir / "reviewed.py"
                artifact.write_text("reviewed artifact")
            packet = task_dir / "packet.json"
            packet.write_text("{}")
            relative = artifact.relative_to(run).as_posix()
            rows.append({"opaque_id": opaque, "task_id": task_id, "arm": arm, "artifact": relative,
                         "packet": packet.relative_to(run).as_posix(), "packet_sha256": file_sha(packet), "selected_skills": []})
            reviews.append({"artifact": relative, "sha256": file_sha(artifact)})
            dispatches.append({"opaque_id": opaque, "agent": opaque, "attempt": 1, "fresh_context": True, "model_override": None})
        write_new(generation / "assignments.json", {"assignments": rows, "routing_manifest_sha256": "a" * 64, "challenger_config_sha256": "b" * 64})
        write_new(generation / "source-review.json", {"reviewer": "primary-agent", "allow_execution": True, "artifacts": reviews})
        (generation / "dispatches.jsonl").write_text("\n".join(json.dumps(row) for row in dispatches) + "\n")
        files = ["experiments/fixtures/harness_task_checks.json", "experiments/scripts/harness_task_checks.py"]
        write_new(run / "m1-freeze.json", {"artifacts": {name: file_sha(ROOT / name) for name in files}})
        return run

    def test_wrong_reviewed_filename_stops_before_grader(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "experiments/datasets") as folder:
            run = self.make_run(folder, wrong_filename=True)
            with patch("collect_harness_tasks.run_task_check", return_value={"passed": True, "checks": [], "failures": []}) as grader:
                with self.assertRaisesRegex(ValueError, "contract filename"):
                    collect(run)
                grader.assert_not_called()

    def test_correct_reviewed_contract_files_are_the_files_graded(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "experiments/datasets") as folder:
            run = self.make_run(folder)
            with patch("collect_harness_tasks.run_task_check", return_value={"passed": True, "checks": [], "failures": []}) as grader:
                result = collect(run)
            self.assertEqual(grader.call_count, 24)
            self.assertEqual(result["successes"], {"baseline": 12, "challenger": 12})
            for call in grader.call_args_list:
                task_id, directory = call.args
                expected = directory / public_task_input(task_id)["artifact_contract"]["filename"]
                self.assertEqual(expected.read_text(), "reviewed artifact")


if __name__ == "__main__":
    unittest.main()
