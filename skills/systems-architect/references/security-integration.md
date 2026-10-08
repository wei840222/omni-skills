# Security Posture and Integration Patterns

## Security defaults

- Defense in depth — network, identity, workload, data, and detection layers; assume one layer fails.
- Least privilege for humans **and** services; prefer short-lived workload identity over static keys.
- Centralize secrets in a purpose-built store; keep them out of images, IaC plain text, and chat logs.
- Encrypt in transit on external and internal paths that carry sensitive or multi-tenant data.
- Audit privileged control-plane actions for forensics and compliance evidence.
- Patch or replace vulnerable runtime components on a written cadence; known CVEs are actively exploited.

High-impact production changes (open firewall to the world, disable auth, destroy data stores) stay recommendation-only until the user explicitly accepts the risk.

## Integration patterns

| Need | Default pattern | Watch-outs |
|------|-----------------|------------|
| Request/response user path | Synchronous API | Timeouts, retries, idempotency keys |
| Decensible work, fan-out | Queue / event bus | Poison messages, DLQ, ordering myths |
| Loose coupling across teams | Events + versioned contracts | Consumer lag, schema evolution |
| Complex east-west mesh | Service mesh when ops skill exists | Mesh tax; start simpler if fleet is small |
| Protect producers | Rate limit + backpressure | Slow consumers must not crash fast paths |
| Failed async work | Dead-letter queue + replay runbook | DLQ without owners is silent data loss |

Match the pattern to coupling and failure tolerance. Do not default to a mesh or multi-bus topology for a modular monolith that still fits one team.

## API and messaging hygiene

- Timeouts on every outbound call; bounded retries with jitter; circuit breakers for persistent faults.
- Explicit idempotency for any write that may be retried.
- Schema compatibility rules before sharing events across teams.
- Separate control-plane traffic from data-plane traffic when blast radius differs.

## Handoff

- Cloud IAM primitives → `aws` / `azure` / `gcp`
- Secret engine operations stay provider-specific after the centralization rule is set here
- Delivery-time credential design in pipelines → `devops`
