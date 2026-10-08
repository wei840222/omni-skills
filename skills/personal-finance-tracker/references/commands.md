# Commands — Personal Finance Tracker

Use these local commands when the user provides transaction CSV files and wants a deterministic summary. Run them from a shell with a real CSV path; do not pass the literal string `<state_root>`.

## Cashflow Rollup

```bash
python3 scripts/cashflow_rollup.py /path/to/transactions.csv
```

What it gives:

- total inflow and outflow
- net cashflow
- monthly totals
- top spend categories and merchants

## Recurring Charge Scan

```bash
python3 scripts/recurring_scan.py /path/to/transactions.csv
```

What it gives:

- likely monthly or annual recurring charges after merchant normalization
- average amount per merchant
- repeat count and cadence hint

## Recommended Workflow

1. Normalize the CSV using `csv-schema.md`
2. Run `scripts/cashflow_rollup.py`
3. Run `scripts/recurring_scan.py`
4. Summarize with the `review-rhythm.md` output format
5. If debt pressure exists, apply `debt-triage.md`

## Interpretation Rules

- Large positive months guarantee safety only if early due dates are covered
- Top merchants matter more when they are recurring
- Category spikes need context before recommending cuts
- Script output is a starting point; still apply runway and due-date judgment before declaring the user safe
