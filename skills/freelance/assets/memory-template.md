# Freelance memory write map

Use only after `<state_root>` is resolved. Create optional files when first
needed; do not pre-expand empty trees. Never write secrets — pointers only.

## Required once persistence is on

| Path | Role |
|---|---|
| `<state_root>/config.yaml` | Declared preferences and Configuration table values |
| `<state_root>/memory.md` | Observations, `## Boxes` index, `## Due` table, `## Platforms`, `## Pipeline`, `## Engagements`, `## Win/Loss` |

## Optional children

| Path | Create when |
|---|---|
| `<state_root>/income/<year>.md` | First monthly billing / collection / hours log |
| `<state_root>/artifacts/<file>` | Rate card, proposal template, MSA draft, case study, outreach that got replies |

## Shared boxes (do not duplicate people/projects here)

| Box | Holds | Identity key |
|---|---|---|
| Shared contacts book | Clients, prospects, referrers, subcontractors | email or handle |
| Shared projects | Engagements with start/end/milestones | project name |
| Shared finances | Business accounts, tool subscriptions | account/tool name |
| Host profile | Currency, locale, country universals | host path |

## `memory.md` sections to maintain

- `## Boxes` — dynamic index of files this skill may open; condition per line
- `## Due` — tax, VAT, insurance, rate review, pipeline review dates
- `## Platforms` — status, measured all-in commission + date, exit trigger
- `## Pipeline` — live opportunities and coverage ratio inputs
- `## Engagements` — commercial terms pointer (rate, basis, hours, notice, portfolio rights)
- `## Win/Loss` — quote outcomes with reasons

## Write rules

1. Update or delete only rows this skill wrote, matched on the box identity key.
2. Name every write/deletion in one line as it happens.
3. Amounts include `currency`; dates are ISO when possible.
4. If legacy data sits only under `~/Clawic/data/freelance/` or
   `~/clawic/freelance/`, propose a migration plan; do not silent-move.
