---
name: monitoring
description: >
  Choose and stand up coverage ladders for uptime, cron heartbeats, error
  capture, and progressive OSS/SaaS stacks (UptimeRobot/Uptime Kuma → Sentry →
  Prometheus/Grafana/Loki/Alertmanager → managed platforms). Use when the ask
  is "is it down?", which tool tier to start with, RED/USE checklists, or a
  first monitoring compose. Prefer `observability` for OTel/SLO/cardinality
  signal design, `alerts` for paging/routing/fatigue playbooks, `grafana` for
  dashboard UX depth, `metrics` for product KPI contracts, `dashboard` for
  local static HTML boards, `devops` for delivery/on-call system design, and
  `sysadmin` for host journal and capacity surgery.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📡"}'
  related-skills: '{"observability":"OTel collectors, PromQL histograms, SLOs, and cardinality once the coverage ladder is chosen.","alerts":"Severity ladders, PagerDuty/Slack routing, silences, and fatigue controls for actionable pages.","grafana":"Dashboard panels, variables, provisioning, and Grafana-native alerting craft.","metrics":"Product/KPI metric contracts and formulas, not Prometheus scrape series.","dashboard":"Local static HTML KPI boards instead of managed Grafana or infra monitors.","devops":"CI/CD, release strategy, and on-call system design surrounding the monitoring stack.","sysadmin":"Linux host journals, services, and capacity signals that feed exporters."}'
---

# Monitoring

Own the **coverage ladder**: pick the smallest stack that answers "is it
broken?", then grow into APM and full metrics/logs/traces only when the failure
modes demand it. This skill is **stateless by default**. Optional inventory of
monitors, DSNs, and compose paths may live under a resolved `<state_root>` when
the user wants continuity.

## State location

Before reading or writing optional state, resolve `<state_root>` once per
invocation:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/monitoring/`, `<workspace>/memory/monitoring/`, then
   `~/monitoring/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicates; do not merge them.
4. If none exists and the user confirms saving monitor inventory, create
   `<workspace>/monitoring/`. If `<workspace>` is unavailable, ask for a state
   root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state path under
`<state_root>/monitoring/`. Keep skill resources under `references/`; never
write the literal string `<state_root>` to disk. Credentials and DSNs are
**pointer-only** — store names or secret-manager references, never raw keys.

Suggested layout (all optional):

```text
<state_root>/monitoring/
├── inventory.md      # URLs, check kinds, owners
├── compose/          # paths to Prometheus/Grafana/Loki stacks
└── pointers.md       # secret names / DSN labels only
```

If legacy Clawic paths such as `~/Clawic/data/monitoring/` appear, treat them as
migration sources only; move with explicit confirmation and never auto-merge.

## When to load

- Choosing Minimal → Standard → Professional → Enterprise coverage tiers
- Standing up UptimeRobot, Uptime Kuma, Healthchecks.io, or Sentry quickly
- Scaffolding a first Prometheus + Grafana + Loki + Alertmanager compose
- Applying RED (apps) / USE (infra) checklists and symptom-first alert rules
- Comparing rough cost bands before quoting live vendor list prices

Prefer siblings when they own the job:

| Job | Skill |
|-----|-------|
| OTel pipelines, SLOs, cardinality, PromQL depth | `observability` |
| Paging, escalation, webhook reliability, fatigue | `alerts` |
| Grafana panels / variables / provisioning | `grafana` |
| Product KPI formulas and reporting cadence | `metrics` |
| Local static HTML dashboards | `dashboard` |
| Delivery pipelines and on-call system design | `devops` |
| Host journals, systemd, disk/capacity surgery | `sysadmin` |

## Workflow

1. Classify the ask: uptime only, error capture, full observability, or cost
   comparison. Load `references/domain.md` before recommending a stack.
2. Resolve optional `<state_root>` only if the user wants inventory continuity.
3. Recommend the **smallest** tier that covers the failure mode; do not start
   with Prometheus when Uptime Kuma suffices.
4. For alerts: symptoms over causes, every page needs a runbook action, keep
   severity ladders coherent with `alerts` when routing gets deep.
5. For prices and free-tier limits: treat tables as heuristics and re-check the
   live vendor page before quoting absolute dollars (see `references/sources.md`).
6. Output: chosen tier, tools, assumed outside-in checks, alert posture, cost
   ballpark with "verify-live" tag, and any confirmation gate before creating
   state directories or migrating Clawic paths.

## Quick reference

| Reference | When to load |
|-----------|--------------|
| `references/domain.md` | Tiers, RED/USE, tool ladders, compose traps, costs, mistakes |
| `references/state.md` | Inventory layout, pointer-only secrets, Clawic migration |
| `references/sources.md` | Live-checked primary docs and product pages |

## Safety

- Never commit DSNs, Grafana admin passwords, or cloud keys into the skill tree
  or into state files — pointers only.
- Outside-in checks matter; internal-only probes miss DNS/TLS/edge failures.
- Do not invent absolute list prices; mark heuristics and verify live sources.
- Destructive retention or silence changes need explicit confirmation.
