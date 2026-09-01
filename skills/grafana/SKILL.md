---
name: grafana
description: Troubleshoot and configure Grafana dashboards, PromQL queries, variables, panels, alerting, data sources, provisioning, and transformations. Use when a user needs Grafana-specific guidance.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📊"}'
---

This skill is stateless and does not store local configuration or persistent user state.

## How to use this skill

1. Identify the Grafana surface involved: query, variable, panel, alert, dashboard provisioning, data source, or transformation.
2. Load the matching reference below before recommending configuration changes.
3. For unexpected results, inspect the rendered query or relevant Grafana logs and verify the narrowest applicable configuration first.

## Quick Reference

| Reference | When to load |
|---|---|
| `references/variables-and-templating.md` | Configure or troubleshoot multi-value, chained, or format-specific variables. |
| `references/prometheus-queries.md` | Write or debug PromQL, especially rates, gauges, labels, and regex filters. |
| `references/panel-configuration.md` | Configure visualizations, thresholds, scaling, or no-data handling. |
| `references/alerting.md` | Create, troubleshoot, or migrate Grafana alerts. |
| `references/dashboard-provisioning.md` | Provision dashboards, import dashboard JSON, or configure folders. |
| `references/data-sources.md` | Configure data sources, proxies, authentication exposure, or connectivity. |
| `references/transformations.md` | Aggregate or combine query results with transformations. |
| `references/common-mistakes.md` | Diagnose slow dashboards, unexpected queries, or architectural traps. |
