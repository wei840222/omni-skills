# Convex Phase 0 semantic-preservation inventory

Baseline: `origin/main:skills/convex/` before this refactor. These rows cover the pre-change operational, safety, state, and example contracts. Source sections are in the original package; destinations are in this package.

| Original item | Source | Disposition | Destination / reason |
|---|---|---|---|
| Discover Convex backend work, no generic tutorial | `SKILL.md#When-to-Use` | retain | `SKILL.md` description and Execution |
| Setup without delaying active work | `setup.md#Golden-Rule` | move | `references/setup.md#Golden-Rule`, `SKILL.md#Execution` |
| Integration preference and team/project context | `setup.md#Priority-Order` | retain | `references/setup.md#Priority-Order`; persistent state requires consent |
| Four separate state children with roles | `SKILL.md#Architecture`, `#Data-Storage` | retain | `SKILL.md#State-location`: summary, schema, rollout, auth notes; optional creation after consent |
| Legacy data path and status/integration values | `SKILL.md#Architecture`, `memory-template.md#Status-Values` | replace | New state resolver discloses legacy copy, leaves it untouched; `assets/memory-template.md` retains values |
| Secrets excluded from memory, no external credentials required by skill | `SKILL.md#Requirements`, `#Security-and-Privacy` | retain | `SKILL.md#Privacy-and-boundaries`, `references/setup.md` |
| Access-path-first schema, selective indexes, uniqueness | `SKILL.md#Core-Rules-1`, `#Core-Rules-4` | move/correct | `references/schema-and-indexes.md#Modeling-Checklist`, `#Index-Design-Heuristics`; uniqueness now transactional indexed invariant, not assumed schema constraint |
| Deterministic read/write vs external effects | `SKILL.md#Core-Rules-2` | retain | `SKILL.md#Decision-boundaries`, `references/operations-playbook.md#Function-and-authorization-boundaries` |
| Auth per entrypoint and client identifier verification | `SKILL.md#Core-Rules-3` | retain | `SKILL.md#Decision-boundaries`, `references/operations-playbook.md#Auth-and-Authorization` |
| Webhook key, replay-safe upsert, processing status | `SKILL.md#Core-Rules-5` | retain/strengthen | `SKILL.md#Decision-boundaries`, `references/operations-playbook.md#Webhook-and-Action-Safety`: atomic status and data write, reconcile external effects |
| Compatible clients, staged migration and rollback | `SKILL.md#Core-Rules-6` | retain | `SKILL.md#Decision-boundaries`, `references/operations-playbook.md#Safe-Rollout-Discipline` |
| Reproduction, structured diagnostics, root-cause memory | `SKILL.md#Core-Rules-7` | retain | `references/operations-playbook.md#Debuggability` and `#Post-Incident-Learning` |
| Original six common traps and operational anti-patterns | `SKILL.md#Common-Traps`, `operations-playbook.md#Operational-Anti-Patterns` | replace | `references/operations-playbook.md#Risk-action--safe-recovery`, `references/schema-and-indexes.md#Common-Traps`; map to positive fixes |
| Schema/index checklist and review questions | `schema-and-indexes.md#Modeling-Checklist`, `#Review-Before-Merge` | move/correct | `references/schema-and-indexes.md` including bounded scan exception |
| Predeploy checks, incident triage, webhook signature/freshness | `operations-playbook.md#Pre-Deploy-Gate`, `#Incident-Triage`, `#Webhook-and-Action-Safety` | retain/strengthen | `references/operations-playbook.md` with publication consent and atomic dedupe |
| Promotional homepage, catalog, related list and feedback | `SKILL.md` frontmatter, `#Related-Skills`, `#Feedback` | remove | Project Gate 1/4/5 forbids promotional copy; JSON related map retains valid relationships |
| `_meta.json` vendor registry metadata | `_meta.json` | remove | External historical registry data, not a runtime skill contract; repository Git history preserves it |
