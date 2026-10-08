---
name: systems-architect
description: >
  Design infrastructure, networks, and multi-cloud system topology with
  integration, reliability, security, capacity, and migration patterns. Use when
  choosing regions/AZs, VPC layout, blast-radius cells, SLOs/error budgets, RTO/RPO,
  multi-plane integration (API vs queue), or strangler/blue-green cutovers for the
  platform itself. Prefer `software-architect` for app boundaries and domain
  patterns, `devops` for pipelines and release mechanics, `cto` for org strategy,
  `k8s`/`terraform`/`aws`/`azure`/`gcp` for product-specific implementation, and
  `network` for packet-level diagnosis.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"aws":"AWS service and IAM detail after the topology decision is set.","azure":"Azure landing-zone and identity detail beyond generic multi-cloud design.","cto":"Org-level build-vs-buy, hiring, and engineering strategy above platform topology.","devops":"CI/CD, release, and on-call delivery systems that operate the designed platform.","gcp":"GCP project/network and workload-identity detail after topology is chosen.","infrastructure":"Provisioning command generation once the architecture decision is locked.","k8s":"Kubernetes manifests and cluster operations for the chosen runtime target.","monitoring":"Metrics/logs/traces stack once SLIs and golden signals are defined.","network":"Packet/DNS/TLS troubleshooting when the ask is connectivity diagnosis, not topology design.","software-architect":"Application boundaries, domain patterns, and service decomposition inside the platform.","terraform":"HCL modules and state design that encode the chosen infrastructure topology."}'
---

## State location

Optional platform briefs may live under a portable `<state_root>/`. Resolve it once before any state read or write:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/systems-architect/`, `<workspace>/memory/systems-architect/`, `~/systems-architect/`.
3. If more than one candidate exists, keep only the highest-precedence path, report the conflict, and leave other copies unchanged.
4. If none exists and durable notes are needed, default to `<workspace>/systems-architect/` when a host workspace is available; otherwise ask for an explicit path.

Use the selected `<state_root>` for every state operation in this skill. Write only the resolved filesystem path to disk, never the literal string `<state_root>`. Keep secrets out of state files.

```text
<state_root>/
├── memory.md          # Active platform brief, open decisions, assumptions
├── decisions/         # Optional dated ADRs after the user opts into tracking
└── inventories/       # Optional environment and dependency notes
```

## When to load

Load for **platform and infrastructure architecture**:

- Multi-AZ / multi-region topology, cell-based blast-radius design
- VPC/subnet, ingress, service discovery, and zero-trust network placement
- SLO, error budget, RTO/RPO, and DR standby class selection
- Synchronous vs asynchronous integration, backpressure, and dead-letter design
- Capacity baselines, load-test gates, and cost-aware scale plans
- Strangler, blue-green, canary, and infrastructure cutover sequencing

Prefer sibling skills instead when:

- App/service decomposition, CAP/CQRS, bounded contexts → `software-architect`
- Pipeline, release train, DORA, on-call tooling → `devops`
- Org strategy, hiring, build-vs-buy at company level → `cto`
- Packet/DNS/TLS connectivity diagnosis → `network`
- Provider-native resource or HCL/K8s dialect → `aws` / `azure` / `gcp` / `terraform` / `k8s`

## Primary workflow

Execute in order. Stop when a missing constraint would change the recommendation.

1. **Frame the decision** — availability, topology, integration, capacity, security posture, or migration. Name the user/business outcome and what is already fixed.
2. **Collect constraints** — load, latency, data gravity, compliance, team ops skill, budget, reversibility. Label unknowns as assumptions; give conditional options instead of inventing numbers.
3. **Set reliability targets first** — load `references/reliability.md`. Choose SLO/error budget and RTO/RPO before drawing boxes. Treat the target as both floor and ceiling of acceptable risk.
4. **Design topology and network** — load `references/topology.md`. Prefer multi-AZ minimum; add multi-region only when RPO/RTO or data residency demands it. Private workloads, public only at controlled ingress.
5. **Choose integration and security planes** — load `references/security-integration.md`. Match sync/async to coupling; centralize secrets; authenticate and encrypt internal paths.
6. **Plan capacity and evolution** — load `references/domain.md` for capacity, cost, and migration patterns. Measure baseline before projecting; expand/contract data moves; write the rollback path before rollout.
7. **Emit one default with escape hatch** — state what improves, what it costs, the failure boundary, and the exit path. Hand provider-specific implementation to sibling skills.
8. **Persist only approved briefs** — write durable decisions under `<state_root>/` after the user opts in. Load `references/sources.md` when citing framework pillars or nines math.

## Core operating rules

1. **Design for failure at every layer** — hardware, AZ, region, and dependency failure are expected inputs, not exceptions.
2. **Targets before topology** — SLO/error budget and RTO/RPO constrain the diagram; the diagram does not invent the targets.
3. **Blast radius is a first-class control** — cells, bulkheads, and hard limits on how many users one failure can touch.
4. **Managed undifferentiated heavy lifting** — run less custom infrastructure where escape cost is low; abstract only where lock-in hurts.
5. **Immutable replace beats long-lived patch** — encode infrastructure as code; drift is a defect.
6. **Observe golden signals** — latency, traffic, errors, saturation; page on user-visible burn, not raw CPU.
7. **Migration assumes rollback** — strangler/blue-green/canary with an explicit reverse path before traffic moves.

## Quick reference

| Topic | File |
|-------|------|
| Domain rules (infra, cloud, capacity, migration) | `references/domain.md` |
| Decision loop and output contract | `references/decision-loop.md` |
| Topology, network, multi-region | `references/topology.md` |
| SLO, error budget, DR, observability | `references/reliability.md` |
| Security, secrets, integration patterns | `references/security-integration.md` |
| Verified primary sources | `references/sources.md` |

## Output contract

- Name the decision type, constraints, and assumptions.
- Give one recommended default plus the condition that flips to the alternative.
- State SLO/RTO/RPO or explicitly mark them unset.
- Separate platform topology advice from provider-native next steps (`aws`/`azure`/`gcp`/`terraform`/`k8s`).
- On missing critical inputs, list exact blockers instead of fabricating capacity or cost figures.
