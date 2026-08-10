---
name: software-architect
description: Apply software architecture principles to design system boundaries, analyze trade-offs, plan scalability, and evolve architectures. Use when designing component decomposition, evaluating build-vs-buy, reviewing data modeling choices, planning migrations, or advising on reliability patterns. Also use when the user asks about CAP/PACELC, CQRS, event sourcing, bounded contexts, or circuit breakers.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏗️"}'
---

# Software Architecture Rules

## State location

This knowledge-only skill does not create or persist runtime state.

## Decision loop

Use this loop for every architecture recommendation.

### 1. Frame the decision

State the decision, the affected user or business outcome, and the constraints that are already known. Classify it as a boundary, trade-off, scalability, data, reliability, security, or evolution decision.

### 2. Gather the constraints

Obtain or label as assumptions:

- Current and forecast load, data volume, latency and availability objectives
- Team ownership, operational capability, and deployment cadence
- Data invariants, compliance obligations, and recovery objectives
- Dependency behavior, failure modes, and migration constraints
- Reversibility and the cost of changing the decision later

If a missing constraint could change the recommendation, present conditional options rather than inventing a value.

### 3. Compare viable options

For each option, state what it improves, what it costs, the failure or scale boundary that invalidates it, and the migration or exit path. Include the simplest viable option; a modular monolith is the default when ownership and domain boundaries are still unclear.

### 4. Decision checkpoint

Before finalizing, verify that the recommendation includes at least two viable alternatives, the primary risk and mitigation, reversibility, and the current-scale rationale. Record an ADR before an irreversible decision or a migration that changes data ownership.

### 5. Deliver an actionable plan

Return the recommendation, rejected alternatives, assumptions, rollout steps, observability signals, rollback or forward-fix condition, and the ADR location. Store ADRs in `docs/adr/` when the project has that convention.

## Core principles

- Prefer the simplest design that satisfies current constraints; complexity carries an operating cost.
- Place boundaries at change and ownership boundaries, with explicit contracts between them.
- Make dependencies, consistency guarantees, and failure behavior explicit.
- Design for bounded failure and recovery instead of assuming dependency availability.
- Keep decisions reversible until evidence justifies a costly commitment.

## Routing guidance

### System boundaries and data ownership

Define bounded contexts around domain capability and ownership. Give each entity one authoritative writer; publish data to other contexts through a contract appropriate to the consistency and latency needs. A shared writable datastore requires an explicit ownership and migration plan.

Choose a service boundary only when it has clear ownership, a stable interface, and an independently valuable deployment or scaling reason. If those conditions are missing, retain a modular monolith and improve internal module boundaries first.

### Distributed consistency and data patterns

Read `references/architecture-patterns.md` before advising on CAP/PACELC, replicas, data ownership, CQRS, or event sourcing.

Define the invariant and the acceptable stale-read or failed-request behavior before choosing a consistency approach. Use event sourcing when event history is the system of record and the operational costs are justified; use conventional audit logging when it supplies the required evidence more simply. Use CQRS when read and write models have materially different requirements and the team can operate projection lag and reconciliation.

### Reliability and scalability

Read `references/architecture-patterns.md` before setting timeouts, retry policies, circuit breakers, bulkheads, cache policies, queue limits, or autoscaling thresholds.

Set operational controls from measured service objectives, dependency behavior, and load tests. For retryable operations, define idempotency, a bounded retry budget, overload behavior, and the user-visible fallback. At every asynchronous boundary, bound concurrency and queue depth and identify the handling path for poison messages.

### Security and observability

Read `references/architecture-patterns.md` before recommending Zero Trust controls, input validation, secret handling, encryption, identity, alert thresholds, or telemetry retention.

Use an explicit identity-and-policy decision at each trust boundary. Define accepted input, authorization, limits, and failure handling at the boundary. Start observability from service-level objectives and user journeys; record the signals that detect degraded service and prove a migration or recovery is working.

### Evolution and migration

Prefer incremental migration over a big-bang cutover. Define compatibility windows, data-backfill and verification steps, rollout stages, ownership changes, and the conditions for rollback or a forward fix. Feature flags and canaries control release exposure, while data-migration verification remains a separate requirement.

## Recovery playbook

| Failure mode | First response | Escalation condition and path |
|---|---|---|
| Dependency latency or errors cascade | Bound the caller deadline; apply a measured circuit-breaker and bulkhead policy; expose a graceful fallback | If the service still exhausts its error budget, isolate the dependency, shed noncritical work, and revise the dependency contract or architecture |
| Cross-service data diverges | Pause unsafe writes when the invariant requires it; reconcile from the authoritative source and preserve an audit trail | If reconciliation is recurrent, redesign ownership, version contracts, or the transaction workflow with compensations |
| Database or queue saturates | Identify the bounded resource, throttle or shed work according to the overload policy, and protect critical traffic | If demand exceeds the measured capacity plan, change the access pattern, partition workload, or add capacity with a tested migration path |
| Migration degrades user outcomes | Halt rollout at the documented signal, preserve compatible paths, and restore the last verified state or use a forward fix | If rollback would corrupt or lose data, execute the pre-approved forward-fix runbook and communicate the recovery objective |

## Anti-patterns

| Anti-pattern | Signal | Better direction |
|---|---|---|
| Distributed monolith | Independent deployments still require coordinated releases | Strengthen contracts, data ownership, and independently operable boundaries |
| Shared writable database without ownership | Multiple services change the same entity or schema | Assign an authoritative writer and a governed data-sharing path |
| Nano-services | Network hops and operations grow without independent value | Group related behavior by domain capability |
| Premature microservices | Boundaries and ownership remain unclear | Start modular and extract only proven boundaries |
| Unbounded asynchronous work | Queue depth, retries, or memory grow without a limit | Define backpressure, retry budget, and dead-letter handling |
| Pattern-first design | The chosen pattern precedes the stated invariant or constraint | Start from the user outcome, invariant, and operating evidence |