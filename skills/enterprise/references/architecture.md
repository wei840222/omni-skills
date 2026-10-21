# Architecture Decisions — Enterprise

## ADR template

Record every major architecture decision as an ADR:

```markdown
# ADR-{number}: {Title}

## Status
Proposed | Accepted | Deprecated | Superseded by ADR-X

## Context
What issue motivates this decision?

## Decision
What change are we making?

## Consequences
What becomes easier or harder because of this change?
```

Site and tooling overview: https://adr.github.io/

## Trade-off matrix

| Factor | Monolith | Microservices | Serverless |
|--------|----------|---------------|------------|
| Initial velocity | Fast | Slow | Fast |
| Team independence | Low | High | High |
| Operational cost | Low | High | Variable |
| Debugging | Easier | Harder | Harder |
| Scaling | All-or-nothing | Granular | Auto |

Prefer the smallest topology that meets team boundaries and SLA; do not adopt microservices for fashion.

## Decision frameworks

### Buy vs build

- **Build** when the capability is a core differentiator, exact fit is required, and long-term ownership is funded.
- **Buy** when the capability is commodity, time-to-market dominates, or the expertise gap is real.

### Synchronous vs async

- **Sync** when a user is waiting, transaction semantics are required, or the path is a simple request/response.
- **Async** when work is long-running, decoupling or spike absorption matters, and at-least-once processing is acceptable with idempotency.

## Common patterns

### API Gateway

Single external entry for authn/authz, rate limits, request shaping, and analytics. Keep business rules out of the gateway when possible.

### Event Sourcing

Persist state as an append-only event stream for audit and temporal queries. Budget for projection rebuild complexity.

### CQRS

Split read and write models when scale or query shapes diverge. Expect eventual consistency and document the lag budget.

## Anti-patterns → preferred moves

| Anti-pattern | Preferred move |
|--------------|----------------|
| Distributed monolith | Clear service boundaries with independent deployability, or stay modular monolith |
| Database-per-service without ownership | Explicit data ownership + published contracts |
| Long synchronous service chains | Break with async boundaries and timeouts/circuit breakers |
| Shared libraries that force lock-step deploys | Versioned contracts / copy-small shared kits with ownership |

## Stakeholder translation

| Role | Cares about | Speak in |
|------|-------------|----------|
| Engineering | Debt, velocity | Patterns, trade-offs, blast radius |
| Product | Features, timeline | User impact, scope, sequencing |
| Security | Risk, compliance | Threats, controls, evidence |
| Finance | Cost, ROI | TCO, licensing, run cost |
| Legal | Liability, data | Contracts, retention, consent |

Restate the same ADR consequences in each language before seeking approval.

## Change management

- Prefer feature flags and progressive delivery over hard cutovers.
- Document blast radius and rollback for every production change.
- Pair architecture decisions with the delivery mechanics owned by `devops`.
