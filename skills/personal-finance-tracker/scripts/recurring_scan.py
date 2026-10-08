#!/usr/bin/env python3
"""Scan signed transaction CSV for likely recurring charges."""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from datetime import datetime


def parse_amount(raw: str) -> float:
    text = (raw or "").strip().replace(",", "")
    text = re.sub(r"[^0-9().-]", "", text)
    if text.startswith("(") and text.endswith(")"):
        text = "-" + text[1:-1]
    return float(text or 0)


def normalize_merchant(name: str) -> str:
    text = (name or "unknown").strip().lower()
    text = re.sub(r"[*#]+", " ", text)
    text = re.sub(r"\.(com|net|org|io|co)\b", "", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text or "unknown"


def display_merchant(name: str) -> str:
    norm = normalize_merchant(name)
    return norm.title() if norm != "unknown" else "unknown"


def similar_amounts(values: list[float]) -> bool:
    avg = sum(values) / len(values)
    return all(abs(v - avg) <= max(2.0, avg * 0.15) for v in values)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 scripts/recurring_scan.py /path/to/transactions.csv", file=sys.stderr)
        return 1

    groups: dict[str, list[tuple[datetime, float]]] = defaultdict(list)
    try:
        with open(argv[1], newline="", encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh):
                amount = parse_amount(row.get("amount", "0"))
                if amount >= 0:
                    continue
                key = normalize_merchant(row.get("merchant") or "unknown")
                raw_date = (row.get("date") or "").strip()[:10]
                if not raw_date:
                    continue
                try:
                    date = datetime.fromisoformat(raw_date)
                except ValueError:
                    continue
                groups[key].append((date, -amount))
    except OSError as exc:
        print(f"Error reading CSV: {exc}", file=sys.stderr)
        return 1
    except (KeyError, ValueError) as exc:
        print(f"Error parsing CSV row: {exc}", file=sys.stderr)
        return 1

    print("Recurring charge candidates")
    found = 0

    for merchant, items in sorted(groups.items()):
        if len(items) < 2:
            continue
        items.sort()
        gaps = [(items[i][0] - items[i - 1][0]).days for i in range(1, len(items))]
        amounts = [value for _, value in items]
        avg_gap = sum(gaps) / len(gaps)
        cadence = None
        if 25 <= avg_gap <= 35:
            cadence = "monthly"
        elif 330 <= avg_gap <= 380:
            cadence = "annual"
        if cadence and similar_amounts(amounts):
            found += 1
            avg = sum(amounts) / len(amounts)
            print(
                f"- {display_merchant(merchant)}: {cadence}, {len(items)} charges, "
                f"avg {avg:,.2f}"
            )

    if found == 0:
        print("- No strong recurring patterns found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
