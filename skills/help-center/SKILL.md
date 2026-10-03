---
name: help-center
description: >
  Design, migrate, and operate a help center: capture the support model, score
  providers or a custom stack, plan taxonomy and redirects, map docs to ticket
  workflows, and run content ops with deflection metrics. Use when the user is
  choosing a knowledge-base platform, migrating articles, launching a help
  center, or improving search and self-service. Not for live ticket handling
  (`customer-support`), pure product docs without support deflection
  (`documentation`), generic process mapping alone (`workflow`), or CRM
  lifecycle work (`crm`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🛟"}'
  related-skills: '{"crm":"Connect support insights to customer lifecycle systems after help-center priorities are set.","customer-support":"Run live frontline ticket and escalation workflows after the help center is planned.","documentation":"Write product or internal docs when the task is content quality rather than support deflection.","workflow":"Design repeatable operational handoffs that the help center should feed."}'
---

## State location

Help-center planning state may exist in `<workspace>/help-center/`, `<workspace>/memory/help-center/`, or `~/help-center/`. `<workspace>` is the host/runtime workspace root; do not invent it from the shell working directory.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path from the user or host when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/help-center/`, `<workspace>/memory/help-center/`, `~/help-center/`.
3. When no candidate exists and the host supplied `<workspace>`, propose `<workspace>/help-center/` and obtain named consent before creating it.
4. When no candidate exists and no host workspace is available, ask for an explicit state path before creating state.

When multiple candidates exist, use only the highest-precedence one, tell the user about the extra copies, and leave the others unchanged. Keep the selected `<state_root>` fixed for the rest of the run. Create the resolved path itself, never a literal directory named `<state_root>`.

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` is missing or empty, load `references/setup.md` and follow it before durable recommendations.

## When to load

Load this skill to plan or improve a help center as support infrastructure: provider vs custom-stack choice, taxonomy, migration, launch, and deflection-focused content ops. Stay in planning mode until the user explicitly authorizes provider-side edits.

## Workflow

1. Resolve `<state_root>` with the State location procedure. If durable memory is needed and missing, run setup with consent.
2. Capture the support model first: channels, monthly ticket volume, languages, compliance, team size, current stack. Refuse provider picks until these inputs exist or the user accepts explicit assumptions.
3. Choose the objective branch and load only the matching reference:
   - Provider or custom-stack choice → `references/provider-matrix.md` and, when custom wins, `references/build-own-stack.md`
   - Migration → `references/migration-playbook.md`
   - Content operations → `references/content-ops.md`
   - Launch readiness → `references/launch-checklist.md`
4. Produce a single next plan with owners, risks, and rollback. Write approved decisions only to `<state_root>/memory.md` (and optional planning files) after consent.
5. On blocked inputs, missing consent, or conflicting state roots, stop durable writes, state the gap, and offer the safest reversible next step.

## Architecture

Persistent planning state lives under the resolved `<state_root>`. Package templates stay in `assets/`; load them only when creating files.

```text
<state_root>/
├── memory.md            # Required once durable planning is enabled
├── provider-score.md    # Optional scoring snapshots
├── content-inventory.md # Optional article inventory and gaps
└── rollout-log.md       # Optional launch and post-launch notes
```

| Path | Role | Creation condition |
| --- | --- | --- |
| `<state_root>/memory.md` | Status, constraints, decisions, rejected options | First durable planning session after consent |
| `<state_root>/provider-score.md` | Weighted provider scores | When a scored comparison is saved |
| `<state_root>/content-inventory.md` | Keep/merge/rewrite/archive inventory | When migration or content audit starts |
| `<state_root>/rollout-log.md` | Launch notes and incidents | When launch monitoring begins |

## Quick reference

| Topic | File | Load when |
| --- | --- | --- |
| First-run setup | `references/setup.md` | `<state_root>/memory.md` missing/empty or integration preference unset |
| Provider comparison | `references/provider-matrix.md` | Choosing vendors or custom stack |
| Custom stack blueprint | `references/build-own-stack.md` | Custom or sovereignty path is in scope |
| Migration | `references/migration-playbook.md` | Moving articles, URLs, or platforms |
| Content operations | `references/content-ops.md` | Editorial cadence and deflection metrics |
| Launch checklist | `references/launch-checklist.md` | Pre-go-live readiness |
| Memory template | `assets/memory-template.md` | Creating `<state_root>/memory.md` |
| Research notes | `references/sources.md` | Restating vendor scope or policy thresholds |

## Core rules

1. **Support model before tools.** Capture channels, volume, languages, compliance, and staffing before scoring platforms.
2. **Compare at least two vendors plus one custom option** with the same weighted criteria in `references/provider-matrix.md`. Treat fit labels as planning heuristics; verify current packaging and pricing on official pages before any buy decision.
3. **Design taxonomy early.** Categories, ownership, article standards, and review cadence come before bulk migration.
4. **Map docs to ticket workflows.** Every category needs triage tags, escalation routes, and SLA targets.
5. **Treat migration as a controlled release.** Inventory → map → dry run → cutover with redirects and a rehearsed rollback (`references/migration-playbook.md`).
6. **Operate on leading and lagging metrics.** Track deflection, first response time, unresolved search queries, freshness, and escalation noise weekly.
7. **Record decisions with consent.** Update `<state_root>/memory.md` with rationale, rejected options, and risks after the user approves the write.

## Recovery and boundaries

- Missing support-model inputs → ask for the minimum set or label assumptions; do not finalize a provider pick.
- Multiple state roots → use highest precedence only and report the conflict.
- User declines local files → keep the session stateless and answer from package references only.
- Provider production changes → require explicit authorization for the named environment; this skill plans, it does not push live KB edits by default.
- Conflicting official packaging vs local notes → prefer the live vendor page and record the check date in memory.

## Security and privacy

- Default data path is local planning under `<state_root>/` only.
- Keep local planning files on-machine; third-party API uploads require a separate explicit user authorization naming the destination.
- Skill memory reads and writes stay inside the resolved `<state_root>` unless the host supplies another path and the user consents to that path.
- Examples use placeholders only; keep secrets and customer content out of the skill package and git commits.

