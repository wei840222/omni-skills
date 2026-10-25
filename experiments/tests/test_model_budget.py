"""Guard against spending past a persisted, shared experiment budget."""

import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from model_budget import BudgetExceeded, BudgetLedger


class ModelBudgetTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.path = Path(self.folder.name) / "budget.sqlite"
        self.limits = {"jev": {"requests": 30, "tokens": 1000, "usd_per_million": "0.042"}}
        self.ledger = BudgetLedger(self.path, self.limits)

    def tearDown(self):
        self.folder.cleanup()

    def test_reservation_counts_inflight_and_does_not_reopen_on_restart(self):
        self.ledger.reserve("jev", "a", 700)
        reopened = BudgetLedger(self.path, self.limits)
        with self.assertRaises(BudgetExceeded):
            reopened.reserve("jev", "b", 301)

    def test_reconcile_uses_real_billed_input_tokens(self):
        rid = self.ledger.reserve("jev", "a", 700)
        self.ledger.settle(rid, 100)
        self.ledger.reserve("jev", "b", 900)
        summary = self.ledger.summary()["jev"]
        self.assertEqual(summary["reserved_or_billed_tokens"], 1000)
        self.assertEqual(summary["observed_billed_tokens"], 100)

    def test_failure_keeps_conservative_reservation(self):
        rid = self.ledger.reserve("jev", "a", 1000)
        self.ledger.settle(rid, None, status="transport-error")
        with self.assertRaises(BudgetExceeded):
            self.ledger.reserve("jev", "retry", 1)

    def test_concurrent_reservations_cannot_overspend(self):
        def attempt(i):
            try:
                self.ledger.reserve("jev", str(i), 100)
                return True
            except BudgetExceeded:
                return False
        with ThreadPoolExecutor(max_workers=8) as pool:
            self.assertEqual(sum(pool.map(attempt, range(40))), 10)

    def test_request_and_global_probe_limits_include_retries(self):
        small = BudgetLedger(Path(self.folder.name) / "small.sqlite", self.limits, request_cap=2)
        for i in range(2):
            rid = small.reserve("jev", str(i), 1)
            small.settle(rid, 1)
        with self.assertRaises(BudgetExceeded):
            small.reserve("jev", "retry", 1)

    def test_reopening_cannot_silently_increase_limits(self):
        with self.assertRaises(ValueError):
            BudgetLedger(self.path, {"jev": {**self.limits["jev"], "tokens": 2000}})

    def test_unexpected_usage_trips_circuit_and_keeps_actual_charge(self):
        rid = self.ledger.reserve("jev", "a", 10)
        with self.assertRaises(BudgetExceeded):
            self.ledger.settle(rid, 11)
        with self.assertRaises(BudgetExceeded):
            self.ledger.reserve("jev", "b", 1)
        self.assertEqual(self.ledger.summary()["jev"]["observed_billed_tokens"], 11)

    def test_two_consecutive_failures_stop_new_outbound_requests(self):
        for i in range(2):
            rid = self.ledger.reserve("jev", str(i), 1)
            self.ledger.settle(rid, None, status="transport-error")
        with self.assertRaises(BudgetExceeded):
            self.ledger.reserve("jev", "third", 1)


if __name__ == "__main__":
    unittest.main()
