---
name: scale
description: Scale technical systems, software architecture, and organizations by
  mapping bottlenecks and executing risk-aware leverage plans.
metadata:
  openclaw: '{"requires": {"config": ["<state_root>/scale/"]}}'
  related-skills:
  - architecture
  - systems-architect
  - startup
  - growth
  - strategy
---

## Setup

On first use, read `references/setup.md` for integration and activation guidance.

## When to load

Load this skill when asked to plan or evaluate scaling strategies for technical systems, software architecture, organizations, operations, or go-to-market capacity. Trigger when constraints must be mapped to identify the primary bottleneck. Load references progressively based on the domain being scaled.

Load `references/domain-knowledge.md` when verifying bottleneck, architecture-split, or delivery-throughput guidance against primary sources.

## Architecture

Memory lives in `<state_root>/scale/`. See `assets/memory-template.md` for structure and status fields.

```text
<state_root>/scale/
|- memory.md                  # Durable scaling context and activation preferences
|- bottleneck-map.md          # Active constraints and bottleneck hypotheses
|- leverage-backlog.md        # Candidate changes ranked by impact and effort
`- experiment-log.md          # Outcomes, regressions, and rollout notes
```

## Quick Reference

Use the smallest relevant file for the current scaling problem.

| Topic | File |
|-------|------|
| Setup and integration | `references/setup.md` |
| Memory structure and states | `assets/memory-template.md` |
| Universal intake and bottleneck diagnosis | `references/scale-diagnostic.md` |
| Infrastructure and platform scaling | `references/system-scale-framework.md` |
| Software architecture scaling | `references/architecture-scale-framework.md` |
| Team and business scaling | `references/company-scale-framework.md` |
| Cadence, metrics, and rollout control | `references/execution-cadence.md` |
| Domain sources and research anchors | `references/domain-knowledge.md` |

## Core Rules

### 1. Define Scale Target Before Solutions
Always lock these inputs first:
- What must scale: throughput, reliability, team output, revenue, or customer base
- Time horizon: immediate, quarter, or year
- Non-negotiable constraints: budget, compliance, headcount, latency, quality

No target, no valid scaling plan.

### 2. Work the BOLT Loop
For every scaling request, apply BOLT in order:
- Bottleneck: identify the dominant limiting factor now
- Objective: define measurable win condition
- Levers: list 3 to 5 candidate interventions
- Test: run staged validation with rollback criteria

Work sequentially from symptoms to targeted interventions before considering large transformations.

### 3. Prioritize Smallest Effective Change
Default to interventions that unlock capacity fast with bounded risk:
- Remove queueing friction before adding complexity
- Improve interfaces and ownership before splitting services
- Standardize repeated work before hiring aggressively

Big rewrites are last resort, not default strategy.

### 4. Price Second-Order Effects Explicitly
Each recommendation must include likely side effects:
- New failure modes
- Cost and operational overhead growth
- Coordination load across teams
- Risk of local optimization hurting global performance

If second-order risk is unknown, mark as hypothesis and constrain rollout.

### 5. Pair Every KPI with a Guardrail
Scale using paired metrics and guardrails:
- Throughput with error rate
- Deploy velocity with change failure rate
- Sales growth with gross margin and support load

If guardrails degrade, pause expansion and stabilize.

### 6. Separate Temporary Boosts from Durable Capacity
Label every action as one of two types:
- Temporary boost: overtime, manual review, tactical exceptions
- Durable capacity: automation, architecture simplification, reusable process

Use temporary boosts only to buy time for durable capacity.

### 7. Institutionalize What Works
After each successful change:
- Capture trigger conditions
- Document operating playbook and owner
- Add review cadence and retirement criteria

Scaling compounds only when wins become repeatable systems.

## Common Traps

- Hiring before workflow clarity -> headcount increases coordination drag.
- Splitting monoliths before interface discipline -> distributed outages with slower delivery.
- Scaling traffic without SLO guardrails -> growth hides reliability collapse.
- Copying big-company org charts too early -> decision latency and ownership gaps.
- Optimizing one bottleneck in isolation -> next bottleneck shifts and total flow does not improve.
- Confusing activity with throughput -> teams look busy while output stagnates.

## Security & Privacy

**Data that leaves your machine:**
- None by default from this skill itself.

**Data that stays local:**
- Scaling context and learned operating patterns under `<state_root>/scale/`.

**This skill does NOT:**
- Execute undeclared network requests automatically.
- Apply irreversible technical or organizational changes without explicit user approval.
- Store secrets, credentials, or payment data in local memory files.
- Modify files outside `<state_root>/scale/` for memory storage.
