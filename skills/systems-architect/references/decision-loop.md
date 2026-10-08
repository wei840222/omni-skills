# Decision Loop and Output Contract

Use this loop for every systems-architecture recommendation.

## 1. Frame the decision

State:

- The decision (topology, reliability target, integration style, capacity, security posture, migration)
- The user or business outcome it protects
- What is already fixed (cloud, compliance, budget ceiling, team skills)

## 2. Gather constraints

Obtain or label as assumptions:

- Load, data volume, latency, and availability objectives
- RTO/RPO and data residency
- Team operational capability and on-call reality
- Dependency failure modes and blast-radius limits
- Reversibility and cost of changing the decision later

When a missing constraint would change the recommendation, present conditional options instead of inventing a value.

## 3. Compare viable options

For each option, state:

- What it improves
- What it costs (money, latency, ops toil, lock-in)
- The failure or scale boundary that invalidates it
- The migration or exit path

Always include the simplest viable option. Multi-region active-active is not the default when a multi-AZ design already meets RTO/RPO.

## 4. Decision checkpoint

Recommend **one default** plus the **escape hatch** (the condition that flips the choice).

Record, when the user wants durability:

- Decision statement
- Alternatives rejected and why
- Assumptions
- Review date or trigger

Store under `<state_root>/decisions/` only after opt-in.

## 5. Handoff boundary

- Platform topology and targets stay in this skill.
- Provider resource wiring → `aws` / `azure` / `gcp`
- IaC modules and state → `terraform`
- Cluster manifests → `k8s`
- Delivery and paging mechanics → `devops` / `monitoring`
- App domain decomposition → `software-architect`
