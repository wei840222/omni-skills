# Memory lifecycle — Accountant

Operating rules for persistent accountant state. Templates live in `assets/accountant-data-templates.md`.

## Required once persistence is enabled

| Path | Role |
|------|------|
| `<state_root>/config.yaml` | User overrides for jurisdiction, basis, entity, software, thresholds |
| `<state_root>/memory.md` | Hot context: status, boxes index, due table, coding rules, open items |

## Optional companions

Create only when the feature is in use:

| Path | Create when |
|------|-------------|
| `<state_root>/chart-of-accounts.md` | User declares or customizes a chart |
| `<state_root>/asset-register.md` | Capital items are tracked |
| `<state_root>/filing-log.md` | Returns or estimates are prepared/submitted |
| `<state_root>/policies.md` | Written accounting policies are adopted |
| `<state_root>/boxes/<name>.md` | A topic needs a dedicated working file named from `## Boxes` |

## `## Boxes` index

`memory.md` holds a `## Boxes` list. Each line is `path — condition`. Open a named box only when its condition applies. Treat the index as the live list of files rather than a static set of box names from the skill package.

## `## Due` table

Every accepted cadence becomes a row: close, recon, AR review, payroll deposit, sales-tax return, estimate, stock count. Columns: item, cadence or next date, owner, status.

## Write discipline

- Write before the session ends whenever something durable was produced.
- In shared external boxes, update or delete only rows this skill authored (match identity key).
- Name every write and deletion in one line as it happens.
- Prefer append + status change over silent rewrite of history.

## Migration

Legacy `~/Clawic/data/accountant/` is a migration source only. After user consent: copy → validate trial balances and open items → cut over `<state_root>` → keep rollback copy until the next successful close.
