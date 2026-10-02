# Darwin evaluation (Gate 8)

**Evaluation date:** 2026-10-03  
**Package:** `skills/cassandra`  
**Final score:** **84 / 100** (threshold ≥ 80)  
**Method:** Structural dry-run over final `SKILL.md`, `references/*`, `references/sources.md`, and three recorded full_test `actual` strings in `test-prompts.json`. No live cluster mutation, JMX auth, or destructive nodetool during scoring.

## Dimension scores

| Dimension | Score | Notes |
|---|---:|---|
| Frontmatter quality | 6.5/7 | Imperative + trigger-rich description; negative scope; `metadata.version` string; related-skills to existing slugs; openclaw JSON with anyBins |
| Workflow clarity | 10/12 | When-to-load → state root → routing → core rules → triage table → depth refs |
| Failure mode encoding | 10/12 | ALLOW FILTERING, tombstones, batches, multi-DC CL, repair after outage covered |
| Checkpoint design | 5.5/6 | Operator gates for assassinate/RF/mass delete; schema agreement wait; restore-tested backups |
| Executable specificity | 15/18 | Concrete CQL PK example, nodetool/cqlsh commands, strategy table |
| Resource integration | 4/4 | best-practices + ops + sources + darwin artifacts; progressive load instructions |
| Overall architecture | 10/12 | Portable `<state_root>`, clawic/`_meta` removed, query-first framing |
| Measured performance | 19/23 | Three full_test actuals align with expected log-PK, tombstone, and routing guidance |
| Counter-examples and blacklists | 4/6 | Near-miss routing to db/sql/dynamodb/mongodb/backups/observability |
| **Total** | **84/100** | pass |

## Full-test provenance

Executed as skill-conditioned answers against the repaired package text:

1. User logs PK design — require clustering timestamp + `CLUSTERING ORDER BY (... DESC)`.
2. Read timeouts with high tombstones — explain DELETE/TTL tombstones, compaction/repair, stop mass deletes.
3. Generic Postgres SQL ask — decline primary use; route to `sql` / `db`.

All three `pass: true` with expected/actual alignment in `test-prompts.json`.

## Iteration notes

- Jules patch migrated openclaw metadata, moved body bullets into `references/cassandra-best-practices.md`, and added two test prompts, but left `related-skills: null`, retained `_meta.json`, omitted `metadata.version`/sources/ops/Darwin artifacts, and kept a thin single-section entry point.
- This pass completed Gates 1–9: deleted `_meta.json` and clawic residue, added portable state root, real related-skills, official source URLs, ops playbook, three evidenced tests, Freud-positive wording, and recorded **84/100**.
