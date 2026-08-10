# Architecture Pattern Reference

Load this reference when the decision involves distributed consistency, a reliability-control configuration, security controls, observability thresholds, or a datastore boundary. Keep the final recommendation tied to measured service objectives and the operating environment.

## Distributed consistency

CAP is a property of a distributed operation during a network partition: define the required consistency guarantee and whether the operation may fail or return an unavailable response. Partition tolerance is an assumed failure condition for distributed systems, rather than a product label to select.

PACELC can frame the complementary normal-operation question: specify the latency target and consistency guarantee for each read and write path. Evaluate CAP or PACELC behavior from the replication mode, topology, read/write settings, and operation under review instead of assigning a universal datastore category.

Before recommending a consistency model, record:

1. The invariant that must hold.
2. The bounded staleness or failed-request behavior users can accept.
3. The partition and replica failure scenarios that matter.
4. The read/write paths that enforce or observe the invariant.

## Reliability controls

Treat timeouts, retry budgets, circuit-breaker thresholds, bulkhead limits, cache TTLs, queue limits, and autoscaling thresholds as service-specific controls. Derive values from service objectives, dependency behavior, and load tests; document the measurement and owner in the ADR or runbook.

Use this calibration sequence:

1. Measure dependency latency and error behavior by operation; reserve enough of the caller deadline for fallback and response handling.
2. Set a timeout within that budget, and test that it expires before upstream resources saturate.
3. Retry only transient, bounded failures when the operation is idempotent or protected by an idempotency key. Apply exponential backoff with jitter and a retry budget.
4. Set circuit-breaker failure, recovery, and half-open probe policies from observed error rates and dependency recovery behavior.
5. Bound concurrency, queue depth, cache size, and retention. Define overload behavior, including what is rejected, deferred, or sent to a dead-letter path.
6. Exercise the controls in staging with a defined blast radius and verify the user-facing degradation path.

## Data and event patterns

Use a modular monolith when team and domain boundaries remain unclear. Extract a service when a bounded context has clear ownership, a stable contract, and an independently valuable deployment or scaling need.

For cross-service data, name one owner for each entity. Consumers receive data through a versioned API, event, or explicitly governed replication path. A shared writable database is a coupling decision that requires an explicit migration and ownership plan.

Use event sourcing when event history is the system of record and replay, auditability, or temporal reconstruction outweigh operational costs. It needs event-versioning, idempotent consumers, replay controls, projection reconciliation, retention policy, and an access strategy for current state. Conventional audit logging is usually the simpler fit when those properties are not required.

Use CQRS when read and write models have materially different invariants or access patterns. Its cost includes asynchronous projection lag, operational monitoring, and reconciliation.

## Security baseline

Zero Trust is an architectural approach: make access decisions per request from authenticated identity, device or workload context, and policy; apply least privilege; monitor and reassess access. Select ciphers, certificate lifetimes, token rotation, and products through the organization’s cryptographic and risk policy.

At every external boundary, define the accepted schema, size limit, types, ranges, encodings, authentication and authorization requirements, and failure response. Use allowlist validation where the input domain is known; parameterize data-layer operations. Set size limits from documented service capacity and abuse resistance rather than a universal number.

Store secrets in the approved secret-management system, restrict access by workload identity, audit access, and rotate or revoke them according to the organization’s risk policy and incident process. Choose transport and at-rest protection that meets the organization’s current cryptographic policy and the relevant protocol or storage requirements.

## Observability and evolution

Start with a service-level objective and the user journey it represents. Instrument request rate, failures, latency, saturation, dependency behavior, and trace context needed to diagnose that objective. Choose sampling, retention, and alert thresholds from traffic volume, cost, and error-budget policy.

For migrations, define compatibility windows, data-backfill and verification steps, rollout stages, rollback or forward-fix conditions, and the monitoring signals that advance or halt the rollout. Feature flags and canaries are release controls, not substitutes for a migration plan.

## Sources consulted

- NIST SP 800-207, *Zero Trust Architecture*: https://csrc.nist.gov/pubs/sp/800/207/final
- Google, *Addressing Cascading Failures* (Site Reliability Engineering): https://sre.google/sre-book/addressing-cascading-failures/
- Microsoft Azure Architecture Center, *Circuit Breaker pattern*: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
- OWASP Cheat Sheet Series, *Input Validation Cheat Sheet*: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- Gilbert and Lynch, *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*: https://doi.org/10.1145/564585.564601
