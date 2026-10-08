#!/usr/bin/env python3
"""Roll up signed transaction CSV into cashflow totals."""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict


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


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(
            "Usage: python3 scripts/cashflow_rollup.py /path/to/transactions.csv",
            file=sys.stderr,
        )
        return 1

    path = argv[1]
    months: dict[str, dict[str, float]] = defaultdict(lambda: {"in": 0.0, "out": 0.0})
    categories: dict[str, float] = defaultdict(float)
    merchants: dict[str, float] = defaultdict(float)
    days: set[str] = set()
    count = 0

    try:
        with open(path, newline="", encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh):
                amount = parse_amount(row.get("amount", "0"))
                date = (row.get("date") or "")[:10]
                month = date[:7] or "unknown"
                merchant = display_merchant(row.get("merchant") or "unknown")
                category = (row.get("category") or "uncategorized").strip() or "uncategorized"
                count += 1
                if date:
                    days.add(date)
                if amount >= 0:
                    months[month]["in"] += amount
                else:
                    spend = -amount
                    months[month]["out"] += spend
                    categories[category] += spend
                    merchants[merchant] += spend
    except OSError as exc:
        print(f"Error reading CSV: {exc}", file=sys.stderr)
        return 1
    except (KeyError, ValueError) as exc:
        print(f"Error parsing CSV row: {exc}", file=sys.stderr)
        return 1

    total_in = sum(v["in"] for v in months.values())
    total_out = sum(v["out"] for v in months.values())
    daily_burn = total_out / max(len(days), 1)

    print("Cashflow Rollup")
    print(f"Transactions: {count}")
    print(f"Total inflow:  {total_in:,.2f}")
    print(f"Total outflow: {total_out:,.2f}")
    print(f"Net cashflow:  {total_in - total_out:,.2f}")
    print(f"Average daily burn: {daily_burn:,.2f}")

    print("\nMonthly totals")
    for month in sorted(months):
        inflow = months[month]["in"]
        outflow = months[month]["out"]
        print(
            f"- {month}: in {inflow:,.2f} | out {outflow:,.2f} | net {inflow - outflow:,.2f}"
        )

    print("\nTop categories")
    for name, value in sorted(categories.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"- {name}: {value:,.2f}")

    print("\nTop merchants")
    for name, value in sorted(merchants.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"- {name}: {value:,.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
