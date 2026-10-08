# Systems Architecture Domain Rules

Stable platform principles. Prefer these over vendor slogans. For decision sequencing see `decision-loop.md`; for network layout see `topology.md`; for SLO/DR see `reliability.md`; for auth and messaging see `security-integration.md`.

## Infrastructure design

- Design for failure at every layer — hardware fails, networks partition, regions degrade.
- Price redundancy against downtime cost; pick an explicit risk tolerance instead of maximizing nines.
- Prefer managed services for undifferentiated work; keep custom control planes only where they are a differentiator.
- Infrastructure as code from day one; manual console changes are drift until reconciled.
- Prefer immutable replace over long-lived in-place patching for compute and images.

## Cloud architecture

- Multi-AZ is the default minimum for stateful and user-facing systems.
- Add multi-region only when RTO/RPO, data residency, or correlated-AZ risk justifies the cost and complexity.
- Right-size the steady baseline first; autoscaling amplifies a wrong baseline.
- Match purchase model to load shape: committed capacity for steady load, spot/preemptible for interruptible burst.
- Treat egress and cross-region chatter as first-class cost and latency; keep chatty paths local when possible.
- Abstract providers where exit cost is high; accept native services where the escape hatch is cheap and documented.

## Capacity planning

- Measure current baseline (QPS, concurrency, payload size, storage growth, p95/p99) before projecting.
- Load-test to find the real breaking point; theory understates queueing and dependency saturation.
- Lead demand with capacity that accounts for provisioning lag and warm-up time.
- Model cost at 2× and 10×; user growth is rarely linear in infrastructure cost.
- Revisit capacity assumptions on a fixed cadence (at least quarterly) or after material product changes.

## Migration and evolution

- Strangler fig for legacy replacement — shift traffic by capability or cohort, not a single big cut.
- Blue-green or canary for infrastructure changes that need fast rollback of the serving path.
- Treat database and stateful moves as their own program: expand → dual-write/backfill → contract.
- Write the rollback plan, owner, and time box before rollout; assume the first attempt can fail.
- Communicate maintenance windows and blast radius to operators and users before the change window.

## Cost and sustainability posture

- Attach a cost owner to every always-on component.
- Prefer architecture choices that cut idle waste (scale-to-zero where latency allows, right-sized storage classes).
- Track unit cost (per request, per active user, per GB) so growth debates use the same denominator.
