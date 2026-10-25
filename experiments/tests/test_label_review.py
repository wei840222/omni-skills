"""Blind-review packet and execution controls, using fake CLI responses only."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import review_harness_labels as review


class LabelReviewTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[1] / "datasets"
        scratch.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="label-review-test-", dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skills = self.root / "skills"
        for name in ("alpha", "beta"):
            directory = self.skills / name
            (directory / "references").mkdir(parents=True)
            (directory / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Public {name} scope\n---\nPublic scope\n")
            (directory / "references/public.md").write_text("A public reference\n")
            (directory / "test-prompts.json").write_text("FORBIDDEN_OWNING_TEST_PROMPTS")
            (directory / "references/test-prompts.md").write_text("FORBIDDEN_REFERENCE_TEST_PROMPTS")
        self.cases_path = self.root / "cases-input.json"
        self.cases = [{"id": f"p{i:03}", "latest": f"Task {i}",
                       "conversation": [{"role": "user", "text": "Earlier request"}]} for i in range(180)]
        self.cases_path.write_text(json.dumps({"schema_version": 1, "cases": self.cases}))
        self.run_dir = self.root / "run"

    def prepare(self):
        return review.prepare(self.cases_path, self.skills, self.run_dir, expected_skills=2)

    def response(self, ids, usage=None):
        body = {"annotations": [{"case_id": case_id, "acceptable_sets": [["alpha"]], "status": "resolved",
                                 "rationale": "Public alpha scope fits", "evidence": [{"skill": "alpha", "path": "alpha/SKILL.md"}]}
                                for case_id in ids], "file_read_count": 0, "policy_violations": []}
        result = {"response": json.dumps(body)}
        if usage is not None:
            result["usage"] = usage
        return result

    def validate(self, envelope, ids=("p000",)):
        catalog, sources = review.public_sources(self.skills, expected_count=2)
        return review.validate_review_output(json.dumps(envelope), list(ids), catalog, sources)

    def fake_runner(self, calls, usage=None, malformed=False):
        def runner(command, **kwargs):
            calls.append((command, kwargs))
            self.assertTrue((self.run_dir / "execution.reservation.json").is_file())
            self.assertTrue(kwargs["input"].endswith(b"\n"))
            self.assertEqual(len(kwargs["input"].splitlines()), 1)
            message = json.loads(kwargs["input"])
            manifest = json.loads((self.run_dir / "prepare.json").read_text())
            batch = next(batch for batch in manifest["batches"] if batch["transport_input_sha256"] == review.digest(kwargs["input"]))
            self.assertTrue((self.run_dir / f"batches/{batch['index']:02d}/call.reservation.json").is_file())
            self.assertEqual(set(message), {"event", "message"})
            self.assertEqual(message["event"], "user")
            self.assertEqual(set(message["message"]), {"content"})
            packet = json.loads(message["message"]["content"].split("INPUT_JSON\n", 1)[1])
            envelope = self.response([case["id"] for case in packet["cases"]], usage)
            envelope["status"] = "SUCCESS"
            envelope["num_turns"] = (usage or {}).get("num_turns", 1)
            stdout = b"not json" if malformed else self.stream(envelope)
            return subprocess.CompletedProcess(command, 0, stdout, b"fake stderr")
        return runner

    def stream(self, envelope):
        events = [{"event": "init", "init": {"permission_mode": "request-review"}},
                  {"event": "step_update", "step_update": {"step_type": "agent_response", "state": "DONE"}},
                  {"event": "result", "result": envelope}]
        return b"".join(json.dumps(event).encode() + b"\n" for event in events)

    def test_schema_output_is_authoritative_over_concatenated_response_text(self):
        envelope = self.response(["p000"])
        final = json.loads(envelope["response"])
        draft = json.loads(envelope["response"])
        draft["annotations"][0]["rationale"] = "Earlier free-text draft"
        envelope.update({"status": "SUCCESS", "num_turns": 1,
                         "json_schema": review.SCHEMA, "structured_output": final,
                         "response": json.dumps(draft) + "\n" + json.dumps(final)})
        original = json.dumps(envelope)
        result, retained = self.validate(envelope)
        self.assertEqual(result, final)
        self.assertEqual(json.dumps(envelope), original)
        self.assertEqual(retained["response"], envelope["response"])
        envelope["structured_output"] = {"invalid": "Do not fall back to response"}
        with self.assertRaisesRegex(ValueError, "fields"):
            self.validate(envelope)
        envelope["structured_output"] = final
        envelope["json_schema"] = {"type": "string"}
        with self.assertRaisesRegex(ValueError, "schema"):
            self.validate(envelope)

    def test_stream_command_and_single_ndjson_transport(self):
        command = review.cli_command(Path("response-schema.json"))
        self.assertNotIn("--print", command)
        self.assertEqual(command[command.index("--input-format") + 1], "stream-json")
        self.assertEqual(command[command.index("--output-format") + 1], "stream-json")
        self.prepare()
        batch = json.loads((self.run_dir / "prepare.json").read_text())["batches"][0]
        transport = (self.run_dir / batch["transport_input_path"]).read_bytes()
        self.assertTrue(transport.endswith(b"\n"))
        self.assertEqual(len(transport.splitlines()), 1)
        message = json.loads(transport)
        self.assertEqual(message, {"event": "user", "message": {
            "content": (self.run_dir / batch["prompt_path"]).read_text()}})
        self.assertEqual(review.digest(transport), batch["transport_input_sha256"])
        self.assertNotEqual(batch["transport_input_sha256"], batch["prompt_sha256"])

    def test_stream_parser_requires_one_terminal_result(self):
        catalog, sources = review.public_sources(self.skills, expected_count=2)
        envelope = self.response(["p000"], {"input_tokens": 123, "output_tokens": 45})
        envelope.update({"status": "SUCCESS", "num_turns": 1})
        raw = self.stream(envelope)
        result, parsed = review.validate_review_output(raw, ["p000"], catalog, sources)
        self.assertEqual(result["annotations"][0]["case_id"], "p000")
        self.assertEqual(parsed["usage"]["input_tokens"], 123)
        for invalid in (raw.splitlines()[0] + b"\n", raw + raw.splitlines()[-1] + b"\n",
                        raw + json.dumps({"event": "step_update", "step_update": {}}).encode() + b"\n"):
            with self.subTest(raw=invalid):
                with self.assertRaises(ValueError):
                    review.validate_review_output(invalid, ["p000"], catalog, sources)
        for updates in ({"status": "ERROR"}, {"status": "WAITING_FOR_PERMISSION"}, {"num_turns": 2}):
            with self.subTest(updates=updates):
                invalid = self.stream({**envelope, **updates})
                with self.assertRaises(ValueError):
                    review.validate_review_output(invalid, ["p000"], catalog, sources)

    def test_positive_projection_excludes_nested_sentinels(self):
        rows = copy.deepcopy(self.cases)
        rows[0].update({"expected": "SENTINEL_EXPECTED", "family": "SENTINEL_FAMILY",
                        "split": "SENTINEL_SPLIT", "source": {"skill": "SENTINEL_SOURCE"}})
        rows[0]["conversation"][0].update({"labels": {"skill": "SENTINEL_NESTED"}})
        direct = review.make_packet(rows[:20], [{"name": "alpha", "description": "scope", "path": "alpha/SKILL.md", "private": "SENTINEL_CATALOG"}])
        self.assertNotIn("SENTINEL", json.dumps(direct))
        self.cases_path.write_text(json.dumps({"annotations": "SENTINEL_TOP", "cases": rows}))
        self.prepare()
        prompt = (self.run_dir / "batches/01/prompt.txt").read_text()
        self.assertNotIn("SENTINEL", prompt)
        packet = json.loads((self.run_dir / "batches/01/packet.json").read_text())
        self.assertEqual(set(packet), {"cases", "global_catalog", "source_docroot"})
        self.assertEqual(set(packet["cases"][0]), {"id", "latest", "conversation"})
        self.assertEqual(packet["cases"][0]["conversation"], [{"role": "user", "text": "Earlier request"}])
        rows[0]["conversation"][0] = {"role": "assistant", "content": "Legacy content", "expected": "SENTINEL"}
        self.cases_path.write_text(json.dumps(rows))
        self.assertEqual(review.load_cases(self.cases_path)[0]["conversation"][0], {"role": "assistant", "text": "Legacy content"})

    def test_preparation_nine_batches_full_catalog_and_public_snapshot(self):
        manifest = self.prepare()
        self.assertEqual(len(manifest["batches"]), 9)
        self.assertLessEqual(manifest["total_prompt_utf8_bytes"], review.MAX_PROMPT_BYTES)
        for batch in manifest["batches"]:
            packet = json.loads((self.run_dir / batch["packet_path"]).read_text())
            self.assertEqual(len(packet["cases"]), 20)
            self.assertEqual(len(packet["global_catalog"]), 2)
        for path in (self.run_dir / "public-skills").rglob("*"):
            if path.is_file():
                self.assertNotIn("FORBIDDEN", path.read_text())
                self.assertTrue(path.name == "SKILL.md" or path.name == "public.md")
        self.assertEqual(manifest, self.prepare())
        (self.run_dir / "public-skills/alpha/SKILL.md").write_text("changed")
        with self.assertRaisesRegex(ValueError, "mismatch"):
            self.prepare()

    def test_case_shape_and_snapshot_boundary_rejections(self):
        self.cases[0]["conversation"][0]["text"] = {"nested": "data"}
        self.cases_path.write_text(json.dumps(self.cases))
        with self.assertRaisesRegex(ValueError, "string"):
            review.load_cases(self.cases_path)
        (self.skills / "alpha/references/escape.md").symlink_to(self.cases_path)
        with self.assertRaisesRegex(ValueError, "escapes"):
            review.public_sources(self.skills, expected_count=2)

    def test_unexpected_snapshot_files_are_rejected(self):
        self.prepare()
        (self.run_dir / "public-skills/alpha/references/extra.md").write_text("unexpected data")
        with self.assertRaisesRegex(ValueError, "Unexpected file"):
            self.prepare()

    def test_actual_public_cases_shape_when_available(self):
        path = Path(__file__).resolve().parents[1] / "fixtures/harness_pilot_cases.json"
        if not path.exists():
            self.skipTest("Public pilot cases not written yet")
        cases = review.load_cases(path)
        self.assertEqual(len(cases), 180)
        self.assertEqual(len({case["id"] for case in cases}), 180)

    def test_parser_accepts_fences_alternatives_multi_and_no_skill(self):
        envelope = self.response(["p000", "p001", "p002"])
        body = json.loads(envelope["response"])
        body["annotations"][0]["acceptable_sets"] = [["alpha"], ["beta"]]
        body["annotations"][1]["acceptable_sets"] = [["beta", "alpha"]]
        body["annotations"][1]["status"] = "uncertain"
        body["annotations"][2]["acceptable_sets"] = [[]]
        body["annotations"][2]["evidence"] = []
        envelope["response"] = "```json\n" + json.dumps(body) + "\n```"
        output, _ = self.validate(envelope, ("p000", "p001", "p002"))
        self.assertEqual(output["annotations"][0]["acceptable_sets"], [["alpha"], ["beta"]])
        self.assertEqual(output["annotations"][1]["acceptable_sets"], [["alpha", "beta"]])
        self.assertEqual(output["annotations"][2]["acceptable_sets"], [[]])

    def test_parser_rejects_bad_ids_skills_evidence_and_duplicate_sets(self):
        changes = [
            ("case_id", "unknown"), ("acceptable_sets", [["unknown"]]),
            ("acceptable_sets", [["alpha", "alpha"]]), ("acceptable_sets", [["alpha"], ["alpha"]]),
            ("acceptable_sets", [[], ["alpha"]]), ("status", "pending"), ("status", []), ("rationale", ""),
            ("evidence", [{"skill": "alpha", "path": "../private.md"}]),
            ("evidence", [{"skill": "alpha", "path": "beta/SKILL.md"}]), ("evidence", []),
        ]
        for key, value in changes:
            with self.subTest(key=key, value=value):
                envelope = self.response(["p000"])
                body = json.loads(envelope["response"])
                body["annotations"][0][key] = value
                envelope["response"] = json.dumps(body)
                with self.assertRaises(ValueError):
                    self.validate(envelope)
        envelope = self.response(["p000", "p000"])
        with self.assertRaises(ValueError):
            self.validate(envelope, ("p000", "p001"))

    def test_parser_rejects_pending_permission_and_reported_policy_violation(self):
        envelope = self.response(["p000"])
        envelope["permission_requests"] = [{"tool": "read"}]
        with self.assertRaisesRegex(ValueError, "permission"):
            self.validate(envelope)
        for key, value in (("file_read_count", 25), ("file_read_count", True),
                           ("policy_violations", ["shell used"])):
            envelope = self.response(["p000"])
            body = json.loads(envelope["response"])
            body[key] = value
            envelope["response"] = json.dumps(body)
            with self.assertRaises(ValueError):
                self.validate(envelope)

    def test_execution_reserved_before_calls_and_success_reused(self):
        self.prepare()
        calls = []
        success = review.execute(self.run_dir, "a" * 64, self.fake_runner(calls, {
            "input_tokens": 100, "output_tokens": 50, "num_turns": 1, "model": "fake-reported"}))
        self.assertEqual(len(calls), 9)
        self.assertEqual(success["cli_calls"], 9)
        self.assertEqual(success["observed_input_tokens"], 900)
        self.assertTrue(success["usage_complete"])
        self.assertEqual(success["batches"][0]["reported_model"], "fake-reported")
        self.assertFalse(success["cost"]["available"])
        self.assertEqual(len(json.loads((self.run_dir / "silver-labels.json").read_text())["annotations"]), 180)
        for command, kwargs in calls:
            self.assertIn("--sandbox", command)
            self.assertIn("--disable-slash-commands", command)
            self.assertNotIn("--print", command)
            self.assertEqual(command[-2:], ["--print-timeout", "5m"])
            self.assertFalse({"--mode", "--model", "--continue", "--dangerously-skip-permissions"} & set(command))
            self.assertEqual(kwargs["timeout"], 300)
        reservation = json.loads((self.run_dir / "batches/01/call.reservation.json").read_text())
        self.assertEqual(reservation["transport_input_sha256"], review.digest(calls[0][1]["input"]))
        raw_events = [json.loads(line) for line in (self.run_dir / "batches/01/stdout.json").read_bytes().splitlines()]
        self.assertEqual([event["event"] for event in raw_events], ["init", "step_update", "result"])
        self.assertEqual(review.execute(self.run_dir, "a" * 64, self.fake_runner(calls)), success)
        self.assertEqual(len(calls), 9)
        (self.run_dir / "silver-labels.json").write_text("corrupted")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls))

    def test_malformed_failure_has_raw_reply_no_aggregate_and_no_retry(self):
        self.prepare()
        calls = []
        with self.assertRaises(ValueError):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls, malformed=True))
        self.assertEqual(len(calls), 1)
        self.assertEqual((self.run_dir / "batches/01/stdout.json").read_bytes(), b"not json")
        self.assertEqual((self.run_dir / "batches/01/stderr.txt").read_bytes(), b"fake stderr")
        self.assertTrue((self.run_dir / "execution.failed.json").exists())
        self.assertFalse((self.run_dir / "silver-labels.json").exists())
        with self.assertRaisesRegex(ValueError, "reruns"):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls))
        self.assertEqual(len(calls), 1)

    def test_observable_caps_stop_next_batch(self):
        for usage in ({"input_tokens": 4_000_001}, {"output_tokens": 100_001}, {"num_turns": 31}):
            with self.subTest(usage=usage):
                self.run_dir = self.root / ("run-" + next(iter(usage)))
                self.prepare()
                calls = []
                with self.assertRaisesRegex(ValueError, "ceiling"):
                    review.execute(self.run_dir, "a" * 64, self.fake_runner(calls, usage))
                self.assertEqual(len(calls), 1)
                self.assertFalse((self.run_dir / "silver-labels.json").exists())

    def test_unknown_usage_stays_unknown_and_missing_freeze_refuses(self):
        self.assertEqual(review.reported_usage({}), {"input_tokens": None, "output_tokens": None,
                                                   "num_turns": None, "reported_model": None})
        self.prepare()
        calls = []
        with self.assertRaisesRegex(ValueError, "freeze"):
            review.execute(self.run_dir, "", self.fake_runner(calls))
        self.assertEqual(calls, [])
        (self.run_dir / "execution.reservation.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "reruns"):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls))

    def test_success_without_usage_does_not_invent_zero_counters(self):
        self.prepare()
        success = review.execute(self.run_dir, "a" * 64, self.fake_runner([]))
        self.assertIsNone(success["observed_input_tokens"])
        self.assertIsNone(success["observed_output_tokens"])
        self.assertFalse(success["usage_complete"])

    def test_malformed_labels_preserve_reported_usage(self):
        self.prepare()
        def malformed(command, **kwargs):
            data = self.stream({"status": "SUCCESS", "num_turns": 1, "response": "not labels", "usage": {"input_tokens": 123}})
            return subprocess.CompletedProcess(command, 0, data, b"")
        with self.assertRaises(ValueError):
            review.execute(self.run_dir, "a" * 64, malformed)
        failure = json.loads((self.run_dir / "execution.failed.json").read_text())
        self.assertEqual(failure["usage"][0]["input_tokens"], 123)

    def test_timeout_captures_partial_reply_and_never_retries(self):
        self.prepare()
        def timed_out(command, **kwargs):
            raise subprocess.TimeoutExpired(command, 300, output=b"partial", stderr=b"timeout stderr")
        with self.assertRaisesRegex(ValueError, "timeout"):
            review.execute(self.run_dir, "a" * 64, timed_out)
        self.assertEqual((self.run_dir / "batches/01/stdout.json").read_bytes(), b"partial")
        self.assertEqual(json.loads((self.run_dir / "execution.failed.json").read_text())["cli_calls"], 1)

    def child_command(self, events, sleep=0):
        source = ("import json,sys,time; sys.stdin.buffer.read(); "
                  "sys.stderr.write('child stderr\\n'); sys.stderr.flush(); "
                  f"events=json.loads({json.dumps(json.dumps(events))}); "
                  "[print(json.dumps(event),flush=True) for event in events]; "
                  f"time.sleep({sleep})")
        return [sys.executable, "-c", source]

    def test_streaming_child_terminal_success_cleans_up_lingering_process(self):
        events = [{"event": "init", "init": {}}, {"event": "result", "result": {
            "status": "SUCCESS", "num_turns": 1, "response": "done", "usage": {"input_tokens": 123}}}]
        started = time.monotonic()
        completed = review.run_streaming(self.child_command(events, sleep=10), input=b'{"event":"user","message":{"content":"test"}}\n',
                                         cwd=self.root, timeout=2, capture_output=True, check=False,
                                         exit_grace=0.05, kill_grace=0.1)
        self.assertLess(time.monotonic() - started, 2)
        self.assertEqual(completed.returncode, 0)
        self.assertIn(b"child stderr", completed.stderr)
        self.assertEqual(review.cli_result(completed.stdout)["usage"]["input_tokens"], 123)
        self.assertEqual(completed.process_cleanup["exit_mode"], "terminated_after_terminal_result")
        self.assertLess(completed.process_cleanup["actual_returncode"], 0)
        self.assertFalse(completed.process_cleanup["natural_exit"])

    def test_streaming_child_natural_exit_and_strict_error_results(self):
        success = {"event": "result", "result": {"status": "SUCCESS", "num_turns": 1, "response": "done"}}
        normal = review.run_streaming(self.child_command([success]), input=b"one input\n", cwd=self.root,
                                      timeout=2, capture_output=True, check=False, exit_grace=0.05)
        self.assertEqual(normal.returncode, 0)
        self.assertTrue(normal.process_cleanup["natural_exit"])
        for events in ([success, success], [{"event": "result", "result": {"status": "ERROR", "response": "failed"}}]):
            with self.subTest(events=events):
                completed = review.run_streaming(self.child_command(events, sleep=10), input=b"one input\n", cwd=self.root,
                                                 timeout=2, capture_output=True, check=False, exit_grace=0.05, kill_grace=0.1)
                self.assertNotEqual(completed.returncode, 0)
                self.assertIn(b'"event": "result"', completed.stdout)

    def test_streaming_child_timeout_before_result_preserves_partial_output(self):
        with self.assertRaises(subprocess.TimeoutExpired) as caught:
            review.run_streaming(self.child_command([{"event": "init", "init": {}}], sleep=10), input=b"one input\n",
                                 cwd=self.root, timeout=0.15, capture_output=True, check=False, exit_grace=0.05, kill_grace=0.1)
        self.assertIn(b'"event": "init"', caught.exception.stdout)
        self.assertIn(b"child stderr", caught.exception.stderr)
        self.assertFalse(caught.exception.process_cleanup["terminal_result_observed"])

    def seed_terminal_timeout(self, usage=None, bad_response=False):
        self.prepare()
        ids = [row["id"] for row in self.cases[:20]]
        envelope = self.response(ids, usage)
        envelope.update({"status": "SUCCESS", "num_turns": 1})
        if bad_response:
            envelope["response"] = "malformed"
        raw = self.stream(envelope)
        def timed_out(command, **kwargs):
            raise subprocess.TimeoutExpired(command, 300, output=raw, stderr=b"retained stderr")
        with self.assertRaises(ValueError):
            review.execute(self.run_dir, "a" * 64, timed_out)
        return {path.relative_to(self.run_dir).as_posix(): path.read_bytes()
                for path in self.run_dir.rglob("*") if path.is_file()}

    def test_explicit_recovery_reuses_success_without_rewriting_inputs_or_old_failure(self):
        before = self.seed_terminal_timeout({"input_tokens": 12345, "output_tokens": 123})
        calls = []
        with self.assertRaisesRegex(ValueError, "reruns"):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls))
        success = review.execute(self.run_dir, "a" * 64, self.fake_runner(calls, {"input_tokens": 100, "output_tokens": 20}),
                                 recover_terminal_results=True)
        self.assertEqual(len(calls), 8)
        self.assertEqual(success["cli_calls"], 9)
        self.assertEqual(success["imported_review_calls"], 1)
        self.assertEqual(success["new_cli_calls"], 8)
        self.assertEqual(success["observed_input_tokens"], 12345 + 800)
        self.assertEqual(success["observed_output_tokens"], 123 + 160)
        self.assertIn("execution.failed.json", success["result_hashes"])
        self.assertIn("execution.recovery.json", success["result_hashes"])
        for relative, data in before.items():
            self.assertEqual((self.run_dir / relative).read_bytes(), data, relative)
        marker = json.loads((self.run_dir / "execution.recovery.json").read_text())
        self.assertEqual(marker["imported_review_calls"], 1)
        self.assertEqual(marker["evidence_hashes"]["batches/01/stdout.json"], review.digest(before["batches/01/stdout.json"]))
        self.assertEqual(review.execute(self.run_dir, "a" * 64, self.fake_runner(calls)), success)
        self.assertEqual(len(calls), 8)

    def test_recovery_rejects_malformed_terminal_and_changed_reservation(self):
        for invalid in ("labels", "freeze", "transport", "missing_stdout"):
            with self.subTest(invalid=invalid):
                self.run_dir = self.root / ("run-" + invalid)
                self.seed_terminal_timeout(bad_response=invalid == "labels")
                path = self.run_dir / "batches/01/call.reservation.json"
                if invalid in {"freeze", "transport"}:
                    reservation = json.loads(path.read_text())
                    reservation["m1_freeze_sha256" if invalid == "freeze" else "transport_input_sha256"] = "b" * 64
                    path.write_text(json.dumps(reservation))
                if invalid == "missing_stdout":
                    (self.run_dir / "batches/01/stdout.json").unlink()
                calls = []
                with self.assertRaises(ValueError):
                    review.execute(self.run_dir, "a" * 64, self.fake_runner(calls), recover_terminal_results=True)
                self.assertEqual(len(calls), 0)
                self.assertFalse((self.run_dir / "execution.recovery.json").exists())

    def test_recovered_usage_stops_next_call_when_aggregate_ceiling_crossed(self):
        before = self.seed_terminal_timeout({"input_tokens": 3_999_950, "output_tokens": 99_995})
        calls = []
        with self.assertRaisesRegex(ValueError, "ceiling"):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls, {"input_tokens": 100, "output_tokens": 20}),
                           recover_terminal_results=True)
        self.assertEqual(len(calls), 1)
        self.assertFalse((self.run_dir / "silver-labels.json").exists())
        self.assertEqual((self.run_dir / "execution.failed.json").read_bytes(), before["execution.failed.json"])
        self.assertTrue((self.run_dir / "execution.recovery.failed.json").exists())

    def test_recovery_rejects_imported_usage_already_over_limit(self):
        self.seed_terminal_timeout({"input_tokens": 4_000_001})
        calls = []
        with self.assertRaisesRegex(ValueError, "ceiling"):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls), recover_terminal_results=True)
        self.assertEqual(len(calls), 0)

    def test_explicit_budget_amendment_preserves_preparation_and_old_failure(self):
        before = self.seed_terminal_timeout({"input_tokens": 100, "output_tokens": 100_001})
        amendment = self.run_dir / "execution.budget-amendment.json"
        amendment.write_text(json.dumps({"schema_version": 1, "authorization_source": "user-message",
            "authorization_quote": "Approve the remaining batches with a 250000 output limit.",
            "m1_freeze_sha256": "a" * 64,
            "preparation_sha256": review.digest((self.run_dir / "prepare.json").read_bytes()),
            "previous_output_tokens": 100_000, "output_tokens": 250_000}))
        calls = []
        with self.assertRaisesRegex(ValueError, "explicit"):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls), recover_terminal_results=True)
        self.assertEqual(calls, [])
        result = review.execute(self.run_dir, "a" * 64,
            self.fake_runner(calls, {"input_tokens": 10, "output_tokens": 10}),
            recover_terminal_results=True, budget_amendment_path=amendment)
        self.assertEqual(len(calls), 8)
        self.assertEqual(result["cli_calls"], 9)
        self.assertEqual(result["execution_limits"]["output_tokens"], 250_000)
        self.assertEqual(result["observed_output_tokens"], 100_081)
        self.assertIn(amendment.name, result["result_hashes"])
        for relative, content in before.items():
            self.assertEqual((self.run_dir / relative).read_bytes(), content)

    def test_budget_amendment_is_bound_to_original_freeze_and_ceiling(self):
        self.prepare()
        path = self.run_dir / "execution.budget-amendment.json"
        for field, value in [("authorization_source", "agent"), ("authorization_quote", ""),
                             ("m1_freeze_sha256", "b" * 64), ("preparation_sha256", "b" * 64),
                             ("previous_output_tokens", 99_999), ("output_tokens", 100_000)]:
            amendment = {"schema_version": 1, "authorization_source": "user-message", "authorization_quote": "Approved",
                "m1_freeze_sha256": "a" * 64, "preparation_sha256": review.digest((self.run_dir / "prepare.json").read_bytes()),
                "previous_output_tokens": 100_000, "output_tokens": 250_000}
            amendment[field] = value
            path.write_text(json.dumps(amendment))
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "amendment"):
                review.execute(self.run_dir, "a" * 64, self.fake_runner([]), budget_amendment_path=path)
        self.assertFalse((self.run_dir / "execution.reservation.json").exists())

    def test_recovery_refuses_any_later_reserved_batch_without_success(self):
        before = self.seed_terminal_timeout({"input_tokens": 123})
        def incomplete(command, **kwargs):
            raise subprocess.TimeoutExpired(command, 300, output=b'{"event":"init","init":{}}\n', stderr=b"incomplete")
        with self.assertRaisesRegex(ValueError, "timeout"):
            review.execute(self.run_dir, "a" * 64, incomplete, recover_terminal_results=True)
        calls = []
        with self.assertRaisesRegex(ValueError, "terminal"):
            review.execute(self.run_dir, "a" * 64, self.fake_runner(calls), recover_terminal_results=True)
        self.assertEqual(len(calls), 0)
        self.assertFalse((self.run_dir / "execution.recovery.02.json").exists())
        self.assertEqual((self.run_dir / "execution.failed.json").read_bytes(), before["execution.failed.json"])

    def test_later_explicit_recovery_requires_and_imports_new_successful_terminal(self):
        self.seed_terminal_timeout({"input_tokens": 123, "output_tokens": 10})
        def terminal_but_lingering(command, **kwargs):
            packet = json.loads(json.loads(kwargs["input"])["message"]["content"].split("INPUT_JSON\n", 1)[1])
            envelope = self.response([case["id"] for case in packet["cases"]], {"input_tokens": 456, "output_tokens": 20})
            envelope.update({"status": "SUCCESS", "num_turns": 1})
            raise subprocess.TimeoutExpired(command, 300, output=self.stream(envelope), stderr=b"second retained stderr")
        with self.assertRaisesRegex(ValueError, "timeout"):
            review.execute(self.run_dir, "a" * 64, terminal_but_lingering, recover_terminal_results=True)
        before = {path.relative_to(self.run_dir).as_posix(): path.read_bytes()
                  for path in self.run_dir.rglob("*") if path.is_file()}
        calls = []
        success = review.execute(self.run_dir, "a" * 64, self.fake_runner(calls, {"input_tokens": 100, "output_tokens": 5}),
                                 recover_terminal_results=True)
        self.assertEqual(len(calls), 7)
        self.assertEqual(success["cli_calls"], 9)
        self.assertEqual(success["imported_review_calls"], 2)
        self.assertEqual(success["new_cli_calls"], 7)
        self.assertEqual(success["observed_input_tokens"], 123 + 456 + 700)
        self.assertIn("execution.recovery.02.json", success["result_hashes"])
        self.assertIn("execution.recovery.failed.json", success["result_hashes"])
        for relative, data in before.items():
            self.assertEqual((self.run_dir / relative).read_bytes(), data, relative)


if __name__ == "__main__":
    unittest.main()
