# Gate 6 sources (verified at handoff)

Primary docs and product pages used to check coverage-ladder, RED/USE, uptime,
Prometheus, Loki, Sentry, and Agent Skills claims. Checked HTTP 200 on
2026-10-17 unless noted.

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Agent Skills format | Agent Skills specification | https://agentskills.io/specification | Frontmatter shape, progressive disclosure, package layout. |
| Agent Skills index | agentskills.io llms.txt | https://agentskills.io/llms.txt | Spec entry points. |
| Reference validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/monitoring`. |
| SRE mental model | Google SRE Book — Monitoring Distributed Systems | https://sre.google/sre-book/monitoring-distributed-systems/ | Golden signals; symptom-oriented monitoring. |
| SLO / burn-rate alerting | Google SRE Workbook — Alerting on SLOs | https://sre.google/workbook/alerting-on-slos/ | Pages on fast burn; tickets on slow burn; hand off deep SLO design to `observability`. |
| Prometheus instrumentation | Prometheus — Instrumentation | https://prometheus.io/docs/practices/instrumentation/ | Counter/gauge/histogram roles; avoid unbounded labels. |
| Prometheus histograms | Prometheus — Histograms and summaries | https://prometheus.io/docs/practices/histograms/ | Prefer histograms for aggregatable quantiles. |
| PromQL rate | Prometheus — Query functions | https://prometheus.io/docs/prometheus/latest/querying/functions/ | `rate()` on counters; range ≥ 2× scrape interval. |
| Alertmanager | Prometheus — Alertmanager | https://prometheus.io/docs/alerting/latest/alertmanager/ | Grouping, inhibition, routing primitives. |
| Grafana | Grafana documentation | https://grafana.com/docs/grafana/latest/ | Dashboards / data sources; panel depth → `grafana`. |
| Loki | Grafana Loki docs | https://grafana.com/docs/loki/latest/ | Label-based log aggregation with Grafana. |
| OpenTelemetry | OpenTelemetry Docs | https://opentelemetry.io/docs/ | Vendor-neutral SDK + OTLP; collector depth → `observability`. |
| Sentry | Sentry Docs | https://docs.sentry.io/ | Error + performance quick start; DSN pointer-only. |
| Uptime Kuma | louislam/uptime-kuma | https://github.com/louislam/uptime-kuma | Self-hosted uptime + status pages. |
| UptimeRobot | UptimeRobot | https://uptimerobot.com/ | SaaS uptime monitors; verify free-tier limits live. |
| Healthchecks | Healthchecks.io docs | https://healthchecks.io/docs/ | Cron / heartbeat monitoring. |

Operational heuristics retained from the pre-refactor body (tier ladder, RED/USE,
compose shape, fatigue rules, rough cost bands) are field practice aligned with
the SRE/Prometheus sources above. Re-check vendor pricing and free-tier limits
before quoting absolute dollar costs or monitor quotas.
