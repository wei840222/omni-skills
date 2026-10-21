# Legacy Integration — Enterprise

## Assessment framework

Before changing a legacy system, answer:

| Question | Why it matters |
|----------|----------------|
| Who owns it? | Political cover and change authority |
| When was it last deployed? | Deployment risk and toolchain freshness |
| What depends on it? | Blast radius and rollback sequencing |
| Is there documentation? | Knowledge extraction priority |
| What is the SLA? | Downtime tolerance and parallel-run budget |

Record answers before choosing a pattern. Start with wrap-and-observe; rewrite only after behavior is characterized.

## Integration patterns

### Strangler Fig

Gradually replace legacy by routing traffic through a new façade while the legacy surface shrinks.

```text
[Client] → [Router] → [New Service] (growing)
                   ↘ [Legacy] (shrinking)
```

Use when traffic can be intercepted and value can ship incrementally. Primary write-up: Martin Fowler's Strangler Fig Application; cloud adaptations appear in AWS Prescriptive Guidance and Azure Architecture Center.

### Anti-Corruption Layer (ACL)

Translate between legacy and new domain models so legacy concepts do not leak into the new bounded context.

```text
[New Domain] ← [ACL] ← [Legacy Domain]
```

Use when concepts do not map cleanly and a stable translation boundary is cheaper than a big-bang rewrite. Microsoft Azure Architecture Center documents the ACL pattern.

### Database Sync / CDC

Keep legacy and new datastores aligned during transition with change-data-capture or controlled ETL.

```text
[Legacy DB] ↔ [CDC/ETL] ↔ [New DB]
```

Use when data migration is the hard part and dual-write or batch sync buys a reversible cutover. Require an explicit reconciliation job and a rollback freeze window.

## Decision tree

```text
Can you wrap or intercept traffic?
├─ Yes → Strangler Fig (+ feature flags)
└─ No
   ├─ Is the interface stable enough to translate? → Anti-Corruption Layer
   └─ No → Full migration with parallel run and reconciliation
```

## Positive traps (what to do instead)

| Failure mode | Do this |
|--------------|---------|
| Treating age as simplicity | Inventory hidden jobs, side effects, and tribal knowledge first |
| Rewriting before behavior is known | Capture golden traffic / characterization tests, then change |
| Coupling the new system to the sync bus | Keep CDC as a temporary seam with an exit criterion |
| One-way cutovers | Require a documented rollback and dual-run exit criteria |

## Recovery checks

After a wrap or cutover:

1. Compare golden requests through legacy and new paths.
2. Verify ownership metrics (error rate, latency, data drift) against the pre-change SLA.
3. Confirm the strangler router or ACL can fail closed to the previous path within the agreed window.
