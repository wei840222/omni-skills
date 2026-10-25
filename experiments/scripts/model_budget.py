"""Persist reservations before outbound requests, including retries and failures.

The transport supplies a conservative token upper bound, not an average estimate.
Unknown outcomes retain that reservation. A provider overrun trips the run.
"""

import argparse
from contextlib import contextmanager
from decimal import Decimal
import json
from pathlib import Path
import sqlite3
import time
import uuid


class BudgetExceeded(RuntimeError):
    pass


class BudgetLedger:
    def __init__(self, path, limits, request_cap=None):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.spec = {"providers": limits, "request_cap": request_cap}
        for value in limits.values():
            if value["tokens"] < 1 or value["requests"] < 1:
                raise ValueError("Budget limits must be positive")
        with self.transaction() as db:
            db.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
            db.execute("CREATE TABLE IF NOT EXISTS requests (id TEXT PRIMARY KEY, provider TEXT NOT NULL, fingerprint TEXT NOT NULL, reserved INTEGER NOT NULL, billed INTEGER, status TEXT NOT NULL, created REAL NOT NULL)")
            spec = json.dumps(self.spec, sort_keys=True)
            existing = db.execute("SELECT value FROM settings WHERE key='spec'").fetchone()
            if existing and existing[0] != spec:
                raise ValueError("Budget specification differs from persisted run; refusing a silent reset")
            db.execute("INSERT OR IGNORE INTO settings VALUES ('spec', ?)", (spec,))

    @contextmanager
    def transaction(self):
        db = sqlite3.connect(self.path, timeout=30)
        try:
            db.execute("BEGIN IMMEDIATE")
            yield db
            db.commit()
        except BaseException:
            db.rollback()
            raise
        finally:
            db.close()

    def reserve(self, provider, fingerprint, token_upper_bound):
        if type(token_upper_bound) is not int or token_upper_bound < 1:
            raise ValueError("A positive conservative token bound is required")
        limit = self.spec["providers"][provider]
        with self.transaction() as db:
            if db.execute("SELECT 1 FROM settings WHERE key='tripped'").fetchone():
                raise BudgetExceeded("Budget circuit is open")
            total = db.execute("SELECT COUNT(*) FROM requests").fetchone()[0]
            cap = self.spec["request_cap"]
            if cap is not None and total >= cap:
                raise BudgetExceeded("Run outbound-attempt limit reached")
            count, tokens = db.execute("SELECT COUNT(*), COALESCE(SUM(COALESCE(billed,reserved)),0) FROM requests WHERE provider=?", (provider,)).fetchone()
            if count >= limit["requests"] or tokens + token_upper_bound > limit["tokens"]:
                raise BudgetExceeded("Provider request/token reservation limit reached")
            rid = uuid.uuid4().hex
            db.execute("INSERT INTO requests VALUES (?,?,?,?,NULL,'reserved',?)", (rid, provider, fingerprint, token_upper_bound, time.time()))
            return rid

    def settle(self, rid, billed_tokens, status="completed"):
        if billed_tokens is not None and (type(billed_tokens) is not int or billed_tokens < 0):
            raise ValueError("Invalid reported billed tokens")
        overrun = False
        with self.transaction() as db:
            row = db.execute("SELECT reserved,billed,status FROM requests WHERE id=?", (rid,)).fetchone()
            if not row:
                raise ValueError("Unknown reservation")
            if row[2] != "reserved":
                raise ValueError("Reservation already settled")
            db.execute("UPDATE requests SET billed=?,status=? WHERE id=?", (billed_tokens, status, rid))
            previous = db.execute("SELECT value FROM settings WHERE key='consecutive-errors'").fetchone()
            errors = 0 if status == "completed" else int(previous[0] if previous else 0) + 1
            db.execute("INSERT OR REPLACE INTO settings VALUES ('consecutive-errors',?)", (str(errors),))
            if errors >= 2:
                db.execute("INSERT OR REPLACE INTO settings VALUES ('tripped','consecutive-provider-errors')")
            if billed_tokens is not None and billed_tokens > row[0]:
                db.execute("INSERT OR REPLACE INTO settings VALUES ('tripped','usage-exceeded-reservation')")
                overrun = True
        if overrun:
            raise BudgetExceeded("Reported usage exceeded conservative reservation; stopping run")

    def summary(self):
        with self.transaction() as db:
            rows = db.execute("SELECT provider,COUNT(*),SUM(COALESCE(billed,reserved)),SUM(COALESCE(billed,0)),SUM(billed IS NULL) FROM requests GROUP BY provider").fetchall()
        result = {}
        for provider, count, reserved, billed, unknown in rows:
            rate = self.spec["providers"][provider].get("usd_per_million")
            result[provider] = {
                "attempts": count, "reserved_or_billed_tokens": reserved,
                "observed_billed_tokens": billed, "unknown_usage_attempts": unknown,
                "list_price_usd_observed": str(Decimal(billed) * Decimal(rate) / 1_000_000) if rate is not None else None,
                "list_price_usd_reserved_or_billed": str(Decimal(reserved) * Decimal(rate) / 1_000_000) if rate is not None else None,
            }
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--limits", type=Path, required=True)
    parser.add_argument("action", choices=("reserve", "settle", "summary"))
    parser.add_argument("--provider")
    parser.add_argument("--fingerprint", default="")
    parser.add_argument("--tokens", type=int)
    parser.add_argument("--id")
    parser.add_argument("--status", default="completed")
    args = parser.parse_args()
    spec = json.loads(args.limits.read_text())
    ledger = BudgetLedger(args.ledger, spec["providers"], spec.get("request_cap"))
    if args.action == "reserve":
        output = {"id": ledger.reserve(args.provider, args.fingerprint, args.tokens)}
    elif args.action == "settle":
        ledger.settle(args.id, args.tokens, args.status)
        output = {"settled": args.id}
    else:
        output = ledger.summary()
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
