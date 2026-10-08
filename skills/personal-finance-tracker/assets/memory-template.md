# Memory Template — Personal Finance Tracker

Create `<state_root>/memory.md` only if the user wants continuity across sessions and `<state_root>` is already resolved.

```markdown
# Personal Finance Tracker Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending

## Context
- Income pattern:
- Accounts in scope:
- Monthly fixed obligations:
- Debt pressure:
- Savings or buffer target:
- Review cadence:

## Notes
- Current runway summary:
- Recurring charges to watch:
- Active cut list:
- Next due dates:
- Next actions:

---
*Updated: YYYY-MM-DD*
```

## Optional Support Files

If the user wants deeper continuity, create under the same resolved root:

- `<state_root>/accounts.md` — balances, account roles, sync notes
- `<state_root>/recurring.md` — subscriptions, bills, annual expenses
- `<state_root>/plans.md` — debt payoff, savings, and cut decisions
- `<state_root>/reviews.md` — weekly and monthly snapshots

## Key Principles

- Keep memory short enough to scan before answering
- Save decisions and pressure points, not full ledgers
- Update `last` whenever the local workspace changes
- Ask before widening the scope of stored data
- Never write credentials, full card numbers, or full statements
