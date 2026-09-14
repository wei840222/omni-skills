# Alert fatigue prevention

Use when storms, duplicate pages, or ignored on-call signals appear.

## Grouping

- Group by root cause labels: `alertname`, `service`, `cluster` (add `env` / `region` when multi-site).
- Do **not** group primarily by instance, pod name, or request ID—those explode cardinality.
- One firing parent should represent the outage; children become context, not separate pages.

```yaml
# Illustrative Alertmanager-style grouping
group_by: ['alertname', 'service', 'cluster']
group_wait: 30s
group_interval: 5m
repeat_interval: 5m   # critical
# repeat_interval: 30m  # cost / noisy performance
```

## Severity ladder

| Level | Meaning | Human response |
|---|---|---|
| P0 | Complete outage, data loss, active security breach | Page immediately, 24/7 |
| P1 | Degraded performance, partial outage, high error rate | Act within ~15 minutes |
| P2 | Non-urgent degradation | Business hours |
| P3 | Trend / hygiene | Weekly review |

Tune numeric SLOs to the user's service; do not invent fake SLOs.

## Cooldowns and repeats

- Identical critical alerts: minimum ~5 minutes between repeats unless still unacked and policy says otherwise.
- Cost and noisy performance alerts: ~30 minutes default.
- After ack, suppress repeats until the incident is resolved or the ack window expires.

## Inhibition

When a root-cause alert fires, silence known symptoms in the same blast radius.

Examples:

- `DatabaseUnreachable` → inhibit `APIHighLatency`, `CheckoutErrorSpike` on the same `cluster`/`service`.
- `ClusterNodeNotReady` (majority) → inhibit single-pod restart flaps on that node pool.

Document each inhibition pair so operators know why a symptom stayed quiet.

## Cardinality hygiene

- Drop or downsample high-churn labels before they become alert labels.
- Prefer recording rules / aggregated metrics for multi-replica symptoms.
- Review top alert volume weekly; demote or fix the noisiest rules.
