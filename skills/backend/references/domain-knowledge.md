# Backend Domain Knowledge

Verified primary sources that back the practices encoded in this skill.

## API and HTTP Semantics

- **RFC 9110 — HTTP Semantics** — status codes, method safety/idempotency, and response expectations via https://www.rfc-editor.org/rfc/rfc9110
- **RFC 7807 — Problem Details for HTTP APIs** — structured error payloads (`type`, `title`, `status`, `detail`, `instance`) via https://www.rfc-editor.org/rfc/rfc7807
- **RFC 6585 — Additional HTTP Status Codes** — `429 Too Many Requests` and related client/server signaling via https://www.rfc-editor.org/rfc/rfc6585

## Resilience Patterns

- **Azure Architecture Center — Circuit Breaker** — Closed / Open / Half-Open states and failure isolation via https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
- **Azure Architecture Center — Retry** — exponential backoff, jitter, and idempotency considerations via https://learn.microsoft.com/en-us/azure/architecture/patterns/retry

## Lifecycle and Observability

- **Kubernetes Pod Lifecycle / Container Probes** — liveness, readiness, and startup probe semantics via https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
- **Prometheus Metric Types** — counters, gauges, histograms/summaries for RED-style instrumentation via https://prometheus.io/docs/concepts/metric_types/

## Security Baseline

- **OWASP API Security Project** — API-focused threats and defensive priorities via https://owasp.org/www-project-api-security/
