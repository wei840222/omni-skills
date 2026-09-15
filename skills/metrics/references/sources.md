# Sources - Metrics

Authoritative references used for Gate 6 domain accuracy. Prefer primary standards and official docs over secondary blog summaries.

## Metric definition and measurement systems

- Google Analytics Help, [About metrics](https://support.google.com/analytics/answer/1033861) — metric vs dimension distinction and reporting semantics.
- MDN Web Docs, [Performance API](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API) — observed runtime signals versus derived product KPIs.

## Product / growth formulas

- a16z, [16 Startup Metrics](https://a16z.com/16-startup-metrics/) — CAC, LTV, retention, and cohort framing for decision-oriented reporting.
- Reforge, [Retention is the core of product-led growth](https://www.reforge.com/blog/retention-is-the-core) — retention as a primary decision metric and cohort comparison caveats.

## Data quality and observability

- Google SRE Book, [Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) — SLI/SLO framing, alert fatigue, and actionable thresholds.
- OpenTelemetry, [Metrics data model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/) — instruments, aggregation temporality, and why raw signals must stay distinct from derived metrics.
- dbt Labs docs, [About metrics](https://docs.getdbt.com/docs/build/metrics) — governed metric layer and versioned semantic definitions.

## Reporting governance

- Nielsen Norman Group, [Dashboards: Making charts and graphs easier to understand](https://www.nngroup.com/articles/dashboards-preattentive/) — decision-oriented report layout over vanity charts.
- DAMA International / DMBOK data-quality dimensions (completeness, consistency, accuracy, timeliness) as applied in operational metric contracts; pair with the quality checklist in `data-quality.md`.

## Obsolete knowledge corrected

- Replaced hardcoded `~/Clawic/data/metrics/` paths with portable `<state_root>/metrics/` resolution.
- Removed Clawic homepage / `_meta.json` packaging noise from the skill package root.
- Moved progressive-disclosure docs under `references/` and required metric contracts before calculation.
