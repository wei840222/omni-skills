# Memory lifecycle — Lawyer

Operating rules for persistent lawyer state. Templates live in `assets/lawyer-data-templates.md`.

## Required once persistence is enabled

| Path | Role |
|------|------|
| `<state_root>/config.yaml` | User overrides for jurisdiction, side, entity, caps, counsel |
| `<state_root>/memory.md` | Hot context: status, boxes index, due table, positions, open items |

## Optional companions

Create only when the feature is in use:

| Path | Create when |
|------|-------------|
| `<state_root>/contracts.md` | Multiple agreements need a register |
| `<state_root>/matters/{name}.md` | A matter needs its own working file |
| `<state_root>/artifacts/clause-{topic}.md` | Clause language was accepted and should be reused |
| `<state_root>/artifacts/memo-{topic}.md` | A decision memo should be re-read |
| `<state_root>/boxes/{name}.md` | A topic needs a dedicated file named from `## Boxes` |

## `## Boxes` index

`memory.md` holds a `## Boxes` list. Each line is `path — condition`. Open a named box only when its condition applies. Treat the index as the live list of files rather than a static set of box names from the skill package.

## `## Due` table

Every accepted cadence or hard deadline becomes a row: renewal notice, limitation period, 83(b), patent grace, breach notification follow-up, trademark maintenance, annual entity filing, policy refresh. Columns: item, cadence or next date, counting unit, owner, status.

Write the alarm in the same turn the clause or statute is read. An uncalendared notice window is an automatic renewal.

## Write discipline

- After the user explicitly authorizes the named current-task write, persist the approved durable outcome; otherwise return a proposed diff in chat.
- Durable outcomes include: agreement signed/amended/renewed/terminated; a deadline that now exists; a position taken or conceded; a matter opened/escalated/closed with cost; a filing or registration; a fact about legal setup that changes future answers; accepted clause language, policies, templates, memos.
- In shared external boxes (contacts, projects, finances), update or delete only rows this skill authored (match identity key). Agreements reference counterparties **by name only** — do not duplicate person records into the lawyer box.
- Name every write and deletion in one line as it happens.
- Prefer append + status change over silent rewrite of history.
- Secrets become `<kind>:<locator>` pointers before save.

## People and shared boxes

Counterparties, outside counsel, opposing counsel, and registered agents go to the shared contacts inventory when one exists — one row per person, identified by stable key (lowercase email → handle → kebab-name + disambiguator). Read before naming anyone. Update only this skill's rows in place.

Matter summaries that other skills need may live under an authorized projects path; link by project/matter name only.

Legal-spend rows may live under an authorized finances path; amounts and vendor nicknames only.

## Migration

Legacy `~/Clawic/data/lawyer/` is a migration source only. After user consent: copy → validate registers, dues, and matter files → cut over `<state_root>` → keep rollback copy until the next successful renewal sweep.
