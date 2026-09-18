---
name: open-source
description: Evaluate, self-host, maintain, and publish open source projects. Use
  this skill when the user wants to compare open source alternatives, set up self-hosting
  operations, manage a project repository, or release new software.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🌍"}'
  related-skills: '{"devops": "Structure delivery, automation, and operational workflows
    end to end.", "docker": "Build and run containerized workloads with practical
    operations guidance.", "git": "Manage repository workflows, branching, and change
    control safely.", "self-host": "Deploy and operate self-hosted services with security
    and reliability basics."}'
---


## State location

Open Source state may exist in `<workspace>/open-source/`, `<workspace>/memory/open-source/`, or `~/open-source/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/open-source/`, `<workspace>/memory/open-source/`, `~/open-source/`.
3. If none exists and state must be created, default to `<workspace>/open-source/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` silently and start helping immediately. This skill is useful from minute zero with no mandatory onboarding.

## When to Use

User needs anything around open source: finding projects, evaluating alternatives, self-hosting, contributing, maintaining, or publishing their own project. Use it when the user asks for practical decisions, not generic theory.

## Architecture

Working context lives in `<state_root>/`. Keep lightweight state and reusable notes there.

```text
<state_root>/
├── memory.md               # Current goals, stack, constraints, decisions
├── discovery-log.md        # Evaluated projects and scoring
├── roadmap.md              # Near-term maintenance and release plan
└── publishing-checklist.md # Release and distribution milestones
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup behavior and integration | `references/setup.md` |
| Memory structure and status model | `assets/memory-template.md` |
| Discovery and ranking framework | `references/discovery-framework.md` |
| Self-host evaluation matrix | `references/self-host-screen.md` |
| Maintainer operations cadence | `references/maintainer-ops.md` |
| Publication and launch workflow | `references/publishing-playbook.md` |

## Core Rules

### 1. Build an Intent Map Before Recommending
- Start from user context: use case, stack, budget, team size, risk tolerance, and time horizon.
- If key constraints are missing, ask the minimum clarifier needed to ensure accurate recommendations.
- Default output shape: shortlist, trade-offs, recommended next action.

### 2. Score Projects with Verifiable Signals
- Use `references/discovery-framework.md` to score each candidate on maintenance health, adoption, security posture, extensibility, and operational burden.
- Prefer projects with active maintainers, documented release cadence, and issue response discipline.
- Flag uncertainty explicitly when data is incomplete.

### 3. Separate Use Paths: Consume, Contribute, or Fork
- For consumption, optimize for reliability and migration safety.
- For contribution, optimize for governance quality and contributor experience.
- For fork decisions, require a clear business or architectural reason plus maintenance capacity.

### 4. Treat Self-Host as an Operations Commitment
- Run `references/self-host-screen.md` before proposing self-host by default.
- Require explicit discussion of backups, upgrades, observability, and incident ownership.
- If operational ownership is weak, recommend managed alternatives or phased rollout.

### 5. Run Maintainer Work in a Predictable Cadence
- Use `references/maintainer-ops.md` to structure triage, review, release, and deprecation work.
- Write changelogs exclusively for users, using clear, external-facing language.
- Prefer small frequent releases over irregular large drops.

### 6. Publish with a Release Contract
- Use `references/publishing-playbook.md` for licensing, docs, versioning, distribution, and announcement readiness.
- Publish only when the release includes a clear install path, compatibility notes, and a defined rollback strategy.
- Announce what changed, who is affected, and how to upgrade safely.

### 7. Preserve Trust and Legal Hygiene
- Adhere strictly to established license terms. If licensing is unclear, state assumptions and advise legal review.
- Always verify license compatibility before recommending code integration, and explicitly warn about any mismatches.
- Distinguish opinion from evidence in all recommendation summaries.

## Open Source Traps

- Popularity-only selection: high stars without maintainer health leads to dead-end dependencies.
- "Self-host is always better": ignores hidden ops cost, on-call load, and security burden.
- Drive-by contributions: submitting PRs without project norms wastes maintainer time.
- Release without migration notes: breaks trust and increases support debt.
- Fork-by-frustration: temporary annoyance creates long-term maintenance tax.

## Security & Privacy

**Data that leaves your machine:**
- None by default from this skill definition.

**Data that stays local:**
- Optional working artifacts and notes in `<state_root>/` when the user asks to persist context.

**This skill does NOT:**
- Execute hidden network requests.
- Access unrelated local paths outside task scope.
- Auto-publish repositories or releases without explicit user intent.
