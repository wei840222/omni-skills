# Reliability, DR, and Observability

## SLO and error budgets

- Define SLIs that mirror user experience (successful requests, good-latency fraction), not raw host uptime alone.
- Set an SLO as both a **minimum** and a **maximum** reliability target: excess nines burn feature velocity and cost without user-visible gain (Google SRE *Embracing Risk*).
- Convert SLO to an error budget; spend budget deliberately on change, reclaim it when burn is high.
- Example math (time-based, illustrative): 99.9% ≈ 8.76 hours/year unavailability budget; 99.99% ≈ 52.56 minutes/year. Prefer request-success SLIs for multi-region serving systems where partial uptime is the norm.

## Disaster recovery

- RTO (time to restore service) and RPO (acceptable data loss) are business inputs the architecture must meet, not outputs guessed after the diagram.
- Backups count only after a timed restore drill succeeds.
- Map standby class to targets:

| Class | Typical use | Notes |
|-------|-------------|-------|
| Cold | Rarely needed systems | Cheap; slow restore |
| Warm | Moderate RTO | Data replicated; compute partially ready |
| Hot | Strict RTO | Near-full capacity standing by |
| Multi-live | Strict RTO + regional independence | Highest cost and data complexity |

- Cross-region replication for data that cannot tolerate regional loss; single-region remains a single failure domain.
- Run DR drills on a calendar; drills expose the gap between the runbook and reality.

## Chaos and operational readiness

- Practice failure in staging (and carefully in production only with explicit guardrails).
- Every user-visible alert needs a runbook: symptom → checks → mitigate → escalate.
- Page on symptom burn (users hurt), not on every cause metric.

## Observability design

- Golden signals per critical service: latency, traffic, errors, saturation (Google SRE monitoring guidance).
- Combine metrics, logs, and traces; each answers a different question.
- Bound cardinality and retention to cost; keep forensic windows for incidents without infinite raw storage.
- Distributed tracing across dependency hops for multi-service paths.

Hand stack-specific wiring (Prometheus, vendor APM, log ships) to `monitoring` once signals and budgets are chosen here.
