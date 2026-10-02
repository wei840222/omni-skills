# Gate 6 sources (verified at handoff)

Primary standards and docs used to check telemetry, SLO, and sampling claims:

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| SRE / SLO / burn rate | Google SRE Workbook — Alerting on SLOs | https://sre.google/workbook/alerting-on-slos/ | Multi-window multi-burn-rate pages on fast burn, tickets on slow burn; error budget framing. |
| SRE mental model | Google SRE Book — Monitoring Distributed Systems | https://sre.google/sre-book/monitoring-distributed-systems/ | Four golden signals; symptom-oriented monitoring vs cause-oriented noise. |
| OpenTelemetry overview | OpenTelemetry Docs | https://opentelemetry.io/docs/ | Single SDK + OTLP; collector as transform/sampling/redaction layer. |
| OTel collector | OpenTelemetry Collector | https://opentelemetry.io/docs/collector/ | Agent vs gateway placement; processors before export. |
| Tail sampling | OTel tail sampling processor | https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor | Keep errors/latency outliers; sample successes after the trace completes. |
| Prometheus histograms | Prometheus — Histograms and summaries | https://prometheus.io/docs/practices/histograms/ | Prefer histograms for aggregatable quantiles; `histogram_quantile` over client summaries. |
| Prometheus instrumentation | Prometheus — Instrumentation | https://prometheus.io/docs/practices/instrumentation/ | Counter/gauge/histogram roles; avoid unbounded label sets. |
| PromQL rate | Prometheus — Query functions | https://prometheus.io/docs/prometheus/latest/querying/functions/ | `rate()` for counters; range ≥ 2× scrape interval. |
| W3C trace context | W3C Trace Context | https://www.w3.org/TR/trace-context/ | `traceparent` inject/extract across HTTP and messaging boundaries. |
| Agent Skills format | Agent Skills specification | https://agentskills.io/specification | Frontmatter shape, progressive disclosure, package layout. |
| Reference validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/observability`. |

Operational heuristics retained from the pre-refactor body (cardinality budgets, retention bands, ~1 TB/day vendor crossover, RED/USE pairing) are field practice aligned with the SRE/OTel/Prometheus sources above. Re-check vendor pricing and backend capacity docs before quoting absolute dollar costs.
