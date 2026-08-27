## Logging

- Structured logs (JSON)—parseable by log aggregators
- Request ID in every log—trace request across services
- Log level appropriate: debug for dev, info/error for prod
- Sensitive data must not be logged—passwords, tokens, PII

## Observability

- Metrics: request count, latency percentiles, error rate—the RED method
- Distributed tracing for microservices—follow request across services
- Alerting on symptoms, not causes—high error rate, not CPU usage
- Dashboards for operational visibility—know normal to spot abnormal
