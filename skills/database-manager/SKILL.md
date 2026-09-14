---
name: database-manager
description: >
  Enforce schema governance, safe migrations, backup drills, and incident response
  for relational databases. Use when production data changes need preflight packets,
  lock-aware writes, restore-proven backups, or outage playbooks. Prefer `sql` for
  query authoring, engine skills (`mysql`/`sqlite`) for product-specific mechanics,
  `prisma` for ORM migrations, and `backend` for service architecture beyond DB ops.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🗄️","requires":{"bins":[]},"configPaths":["<state_root>/database-manager/"]}'
  related-skills: '{"sql":"SQL query authoring and analysis when the ask is statement design rather than full DB operating discipline.","mysql":"MySQL-specific workflows, engines quirks, and troubleshooting.","sqlite":"Local SQLite prototyping and file-backed database workflows.","prisma":"Prisma schema and migration tooling when the stack is Prisma-first.","backend":"Backend architecture and service delivery surrounding the database tier."}'
---

## When to load

Load this skill when database work can affect production reliability, latency, or data integrity: schema design, query hygiene, migration rollout, backup/restore readiness, or incident response.

Prefer narrower skills when the ask is narrow:

- `sql` — statement authoring and analysis
- `mysql` / `sqlite` — engine-specific mechanics
- `prisma` — Prisma schema/migration tooling
- `backend` — service architecture beyond DB operating discipline

## State location

Resolve `<state_root>` in this order:

1. Explicit user- or host-configured state path when supplied
2. `<workspace>/.agents/state` when a local workspace is active
3. `$XDG_DATA_HOME` when set
4. `~/.local/share` on Linux/macOS defaults

Resolve once per invocation and keep it fixed. Prefer portable `<state_root>` paths; never hard-code host-specific roots such as `~/Clawic/data/database-manager/`.

Skill state lives under `<state_root>/database-manager/`. Create the directory only when the first persistent write is required.

```text
<state_root>/database-manager/
|-- memory.md                  # Durable context and operating preferences
|-- inventory.md               # Systems, engines, owners, and critical datasets
|-- standards.md               # Naming, indexing, and schema conventions
|-- migrations.md              # Planned and executed migration records
|-- backups.md                 # Backup schedule, retention, and restore drills
|-- incidents.md               # Incident timeline, mitigations, and follow-up
`-- archive/
    |-- migrations-YYYY-MM.md  # Closed migrations by month
    `-- incidents-YYYY-MM.md   # Closed incidents by month
```

## Progressive disclosure

| Situation | Load |
|-----------|------|
| First activation, local file layout, operating defaults | `references/setup.md` |
| Memory structure under `<state_root>/database-manager/` | `references/memory-template.md` |
| Ownership, criticality tiers, change windows | `references/inventory-and-governance.md` |
| Query changes, bulk writes, lock windows | `references/query-operations.md` |
| Schema rollout and rollback plans | `references/migration-and-release.md` |
| Backup policy and restore drills | `references/backup-and-recovery.md` |
| Production integrity/availability incidents | `references/incident-playbook.md` |
| Migration preflight / destructive op / restore templates | `references/templates.md` |
| Gate 6 research anchors | `references/sources.md` |

## Core rules

1. **Preflight packet required** — every production schema or data change needs intent, blast radius, rollback path, and verification queries.
2. **Read validation before writes** — prove predicates with read-only checks, then execute writes in explicit audited steps.
3. **Migrations are releases** — owner, window, rollback deadline, and post-deploy verification are mandatory.
4. **Make index/query trade-offs explicit** — state expected impact on read latency, write throughput, and storage growth.
5. **Backup is not real until restore is proven** — run restore drills, validate row counts, document measured recovery time.
6. **Destructive ops need safety gates** — confirm environment/table, capture baseline counts, require explicit user confirmation, log rollback route before `DROP`/`TRUNCATE`/broad `DELETE`/`UPDATE`.
7. **Close incidents with durable learning** — root cause, missing guardrail, and one concrete prevention change.

## Failure modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Mass write from weak predicate | Row-count spike, unexpected entity changes | Stop writes, restore or compensating update from verified baseline |
| Migration lock storm | Latency spike, blocked transactions, rising wait events | Abort/rollback within window; reschedule with lock analysis |
| Unverified backup false confidence | Restore fails or RTO/RPO missed during drill/outage | Fix backup path, re-drill, block Tier-1 changes until evidence exists |
| Replica-lag stale verification | Reads disagree with primary after change | Verify on primary or lag-aware path before closing change |
| Incident without guardrail | Same failure class recurs | Add one permanent control before closure |

## Security & Privacy

**Data that leaves your machine:**
- None by default.

**Data that stays local:**
- Database operating context and records under `<state_root>/database-manager/`.

**This skill does NOT:**
- Execute destructive commands without explicit user confirmation.
- Access unrelated credentials or services by default.
- Store secrets in memory files.
