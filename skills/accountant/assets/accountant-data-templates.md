# Accountant data templates

Copyable templates for accountant state files. Operating rules stay in `references/`; this file is the template source of truth.

## `<state_root>/config.yaml`

```yaml
jurisdiction: ""          # country + state/province
accounting_basis: accrual # cash | accrual | modified-cash
reporting_framework: us-gaap
entity_type: sole-trader
fiscal_year_end: "12-31"
base_currency: USD
ledger_software: spreadsheet
materiality_pct: 0.5
capitalization_threshold: 2500
close_target_days: 10
chart_of_accounts: ""     # e.g. chart-of-accounts.md under state_root
```

## `<state_root>/memory.md`

```markdown
# Accountant Memory

## Status
status: ongoing
version: 1.0.2
last: YYYY-MM-DD
integration: pending

## Context
- Entity:
- Basis / framework:
- Jurisdiction assumption:
- Ledger software:
- Live constraint this week:

## Configuration notes
- Overrides beyond config.yaml:
- Coding conventions:

## Boxes
- chart-of-accounts.md — when chart is customized
- asset-register.md — when capital items are tracked
- filing-log.md — when returns or estimates are prepared
- policies.md — when written policies are adopted

## Due
| Item | Next date / cadence | Owner | Status |
|------|---------------------|-------|--------|
| Bank recon | | | |
| Month-end close | | | |
| Payroll deposits | | | |
| Sales tax / VAT return | | | |

## Coding Rules
| Pattern | Account(s) | Discipline (accrual vs invoice) |
|---------|------------|----------------------------------|

## Open Items
| Date | Item | Owner | Due |
|------|------|-------|-----|

## Period log
| Period | Closed? | Lock date | TB totals note |
|--------|---------|-----------|----------------|

## Notes
- Decisions and policies worth keeping
- Follow-ups

---
Updated: YYYY-MM-DD
```

## `<state_root>/chart-of-accounts.md`

```markdown
# Chart of accounts

| Code | Name | Type | Normal bal | Notes |
|------|------|------|------------|-------|
```

## `<state_root>/asset-register.md`

```markdown
# Asset register

| ID | Description | Acquired | Cost | Life | Method | Accum dep | NBV | Status |
|----|-------------|----------|------|------|--------|-----------|-----|--------|
```

## `<state_root>/filing-log.md`

```markdown
# Filing log

| Period | Return / estimate | Jurisdiction | Amounts | Filed date | Source year for rates | Notes |
|--------|-------------------|--------------|---------|------------|----------------------|-------|
```

## `<state_root>/policies.md`

```markdown
# Accounting policies

## Basis and framework
## Revenue
## Capitalization threshold
## Inventory costing
## Bad debt
## Close cadence
## Record retention
```
