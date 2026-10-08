---
name: personal-finance-tracker
description: >
  Track personal finances with runway snapshots, recurring bill detection,
  debt triage, CSV imports, and net-worth notes. Use for cashflow reviews,
  expense cleanup, subscription drag, and weekly or monthly money decisions.
  Not for moving money, bank login, regulated financial advice, company finance
  (`cfo`), household money-ladder sequencing alone (`money`), or subscription
  inventory without cashflow context (`subscriptions`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💸"}'
  related-skills: '{"money":"Household money-ladder sequencing beyond statement rollups.","subscriptions":"Subscription inventory and renewal cuts when cashflow context is already known.","csv":"CSV cleanup and column mapping before finance rollups.","cfo":"Company finance and operating decisions, not household trackers."}'
---

## State location

Personal finance tracker state may exist in `<workspace>/personal-finance-tracker/`, `<workspace>/memory/personal-finance-tracker/`, or `~/personal-finance-tracker/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/personal-finance-tracker/`, `<workspace>/memory/personal-finance-tracker/`, `~/personal-finance-tracker/`.
3. If none exists and the user wants persistent tracking, create `<workspace>/personal-finance-tracker/`. If `<workspace>` is unavailable, ask for a state root instead of guessing from the current directory.
4. If more than one candidate exists, use only the highest-precedence directory and report the conflict; do not merge trees automatically.

Use the selected `<state_root>` for every state operation in this skill. Prefer portable `<state_root>` paths; never hard-code host-specific absolute roots. Skill resources stay under `references/`, `assets/`, and `scripts/`; never treat the literal string `<state_root>` as a filesystem path.

```text
<state_root>/
├── memory.md        # High-signal money context and review cadence
├── accounts.md      # Balances, account roles, sync notes
├── recurring.md     # Bills, subscriptions, annual charges, due dates
├── plans.md         # Debt payoff, savings, cut list, next actions
└── reviews.md       # Weekly and monthly snapshots
```

Create or update state files only after the user opts in. Store high-signal summaries only—no credentials, full card numbers, or full statements.

## When to use

Load for **household cashflow visibility and decision support**:

- Fast runway check: cash now, bills before next pay, free-to-spend
- CSV or pasted transaction cleanup and rollup
- Recurring charge / subscription drag detection
- Debt pressure triage against near-term obligations
- Weekly or monthly money review with a short next-action list

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| Debt vs save vs invest sequencing | `money` |
| Subscription inventory without full cashflow | `subscriptions` |
| Raw CSV mapping/cleanup tooling | `csv` |
| Company finance / operating scenarios | `cfo` |

## Core rules

1. Start with the runway review: cash available, obligations before next income, free-to-spend after essentials.
2. Normalize dates, signs, merchants, categories, and duplicates before trend claims.
3. Separate recurring drag from one-off spend before cut recommendations.
4. Protect essentials, taxes, minimum debt payments, and near-term due dates before optimization theater.
5. End every review with at most three concrete actions: pay, cancel, renegotiate, transfer, delay, or monitor.
6. Keep storage minimal, local, and opt-in; ask before creating `<state_root>/`.
7. Analyze and plan only—do not move money, cancel services, log into banks, or present regulated financial advice.

## Quick reference

Load only what improves the current answer.

| Need | File |
|------|------|
| First-use attitude and activation | `references/setup.md` |
| Domain rules, traps, operating rhythm | `references/domain.md` |
| Security and state tree detail | `references/state.md` |
| CSV schema and normalization | `references/csv-schema.md` |
| Review cadence and output format | `references/review-rhythm.md` |
| Debt and subscription triage | `references/debt-triage.md` |
| Local command recipes | `references/commands.md` |
| Continuity memory template | `assets/memory-template.md` |
| Cashflow rollup script | `scripts/cashflow_rollup.py` |
| Recurring charge scanner | `scripts/recurring_scan.py` |

## Security and privacy

- Opt-in local state only under the resolved `<state_root>/`.
- Prefer local CSV analysis; do not send transaction data to undeclared external services.
- Never store credentials, full card numbers, or full bank statements.
- Recommendations stay transparent, reversible, and grounded in user-provided data.
