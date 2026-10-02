---
name: observability
description: >
  Design and debug observability pipelines across metrics, logs, and traces:
  OpenTelemetry collectors, Prometheus histograms and cardinality, structured
  logging with trace correlation, tail-based sampling, SLOs/error budgets, and
  symptom-based burn-rate alerts. Use when configuring OTel, writing PromQL,
  cutting ingest cost, defining SLIs/SLOs, or investigating p99/latency and
  broken traces. Prefer `alerts` for paging/routing/fatigue playbooks alone,
  `metrics` for product KPI contracts (not telemetry series), `monitoring` for
  uptime-tool ladders still unrefactored, and `grafana` for dashboard UX depth.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📡"}'
  related-skills: '{"alerts":"Incident paging, severity ladders, webhook reliability, and fatigue controls once a signal exists.","grafana":"Dashboard layout and panel craft on top of already-chosen metrics/logs/traces.","metrics":"Product/KPI metric contracts and formulas, not Prometheus/OTel telemetry series.","monitoring":"Uptime and tool-ladder setup when the ask is coverage tiers rather than signal design.","devops":"Delivery and platform operations surrounding the observability stack.","sysadmin":"Host logs, services, and capacity signals that often feed collectors."}'
---

# Observability

Domain guidance for **telemetry architecture**: complementary metrics/logs/traces,
cardinality and cost control, OpenTelemetry collectors, SLOs, and burn-rate
alerting. This skill is **stateless** — it does not store credentials, scrape
configs, or tenant inventories in the package.

## When to load

Load for signal-design and pipeline work:

- choosing metrics vs logs vs traces for a failure mode
- Prometheus histogram buckets, PromQL `histogram_quantile` / `rate`, recording rules
- high-cardinality label review and collector attribute drops
- OpenTelemetry SDK/collector placement, OTLP, tail sampling, redaction
- SLI/SLO/error-budget and multi-window multi-burn-rate alerts
- broken W3C `traceparent` propagation or expensive trace/log volume

Prefer other skills when the ask is mainly:

- PagerDuty/Slack routing, silences, status-page ops → `alerts`
- product KPI definitions and formula registries → `metrics`
- Grafana panel/dashboard polish → `grafana`
- “which uptime tool tier” ladders → `monitoring`
- host service/log plumbing without signal design → `sysadmin`

## Progressive disclosure

| File | Load when |
|------|-----------|
| `references/observability-guide.md` | Full mental model, PromQL/SLO/sampling depth, situation table |
| `references/sources.md` | Verifying claims against SRE books, OTel, Prometheus, W3C |

Keep `SKILL.md` as the router; open one reference when the question needs that depth.

## Core rules

1. **Three signals, one budget** — metrics for “is it broken / where”, logs for “why”, traces for “which hop and how long”. Exemplars bridge metrics → traces; reach for an exemplar before adding a metric label.
2. **Cardinality multiplies** — treat new labels like schema changes. Keep `user_id`, raw URL, `request_id`, email, IP off metric labels; put them on spans/logs or exemplars. Strip high-card attributes at the collector.
3. **Percentiles and histograms** — alert and report on p99 (or SLO boundary), not the mean. Use histograms (aggregatable buckets), not summaries; set buckets to the SLO threshold.
4. **Route through a collector** — OTel collector does tail sampling, redaction, path drops (`/healthz`, `/metrics`), and fan-out before SaaS ingest. Prefer tail sampling: keep errors and slow traces at 100%, sample the rest.
5. **SLO burn, not CPU pages** — SLI is user-perceived; alert on multi-window multi-burn-rate. Page on symptoms; every page carries a runbook link.
6. **Structured logs + `trace_id`** — JSON/logfmt with templated messages; put `trace_id`/`span_id` on every line so metric → trace → log stays one path.
7. **Propagation is the usual break** — inject/extract W3C `traceparent` on every HTTP/queue/RPC boundary; a missing hop splits the tree.
8. **Secrets stay out of git** — redaction at the collector; examples use placeholders only.

## Quick reference

| Situation | Play |
|-----------|------|
| p99 up, cause unclear | Exemplar `trace_id` from latency histogram → critical path on the trace |
| Storage bill spiked | `/api/v1/status/tsdb` top labels; move high-card label to span/log |
| Trace splits at one service | Fix `traceparent` inject/extract on that boundary |
| Nightly pages, no action | Delete/tune noisy alerts; re-baseline on SLO burn + runbooks |
| One user failure | Search logs by `trace_id` → open trace → read spans |
| Log volume ~TB/day | Counters for counts; log errors/warnings; tail-sample successes |
| Dashboard query >1s | Recording rule for the heavy expression |
| Keep all errors, cut cost | Tail sample at gateway collector; drop health/metrics spans |
| New label in a PR | Ask “how many distinct values?” before merge |
| SLI green, users unhappy | Wrong SLI (mean/uptime vs user journey); re-derive from perception |

## Default answer shape

1. Name the primary signal (metric / log / trace) and the failure mode.
2. Give the minimal query, collector policy, or SLO/burn rule.
3. Call the matching cost or false-positive failure mode (cardinality, head sampling, mean latency, missing propagation).
4. Point to one reference file for depth—do not dump both references on a simple ask.

## Safety

- Do not commit real scrape tokens, SaaS API keys, or customer PII into the skill tree.
- Prefer collector-side redaction for tokens, passwords, and raw PII.
- Treat vendor pricing figures as time-sensitive; re-check vendor docs before quoting bills.
