---
name: dashboard
description: >
  Build local static HTML dashboards from user-chosen data sources with fetch
  scripts, layout widgets, and a visual QA loop. Use when the user wants a
  self-hosted KPI/chart page fed by APIs, docker stats, CSV, or sheets, needs
  credential-safe fetch scripts plus cron wiring, or asks to validate layout
  contrast and widget structure before delivery. Not for managed Grafana ops
  (`grafana`), metric-contract design (`metrics`), or Stripe payment-code
  debugging (`stripe-api-integration`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📊","displayName":"Dashboard"}'
  related-skills: '{"grafana":"Managed Grafana panels, PromQL, alerting, and provisioning instead of static local HTML.","metrics":"Metric contracts, formulas, and reporting cadence before building a presentation surface.","stripe-api-integration":"Stripe API, webhook, and billing integration failures beyond revenue-dashboard fetch scripts.","html":"General HTML/CSS structure when the task is markup craft rather than a data dashboard.","monitoring":"Infrastructure monitoring strategy and checks beyond a local static dashboard page."}'
---

# Dashboard

Generate **local static dashboards**: fetch scripts the user runs, `data.json` snapshots, HTML/widget layouts, and a visual QA pass before delivery.

## State location

Dashboard registry files, per-dashboard `config.json` / `data.json` / `index.html`, and generated fetch scripts are persistent user state.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/dashboard/`, `<workspace>/memory/dashboard/`, then `~/dashboard/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicate locations; do not merge or synchronize them.
4. If none exists and the user confirms saving dashboard files, create
   `<workspace>/dashboard/`. If `<workspace>` is unavailable, ask for a state
   root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every dashboard read or write under
`<state_root>/dashboard/`. Keep skill resources under `references/`; never treat
them as mutable user state. Scripts must receive the resolved filesystem path —
never write the literal string `<state_root>` to disk.

See `references/state.md` for the on-disk layout.

## Scope

This skill:

- Generates static HTML dashboards and widget layouts
- Creates fetch scripts the user can run manually or via cron
- Stores dashboards under `<state_root>/dashboard/`

**User-driven model:**

- User chooses data sources
- User supplies API credentials via environment variables
- User runs fetch scripts (cron or manual)
- Skill generates HTML, config, and fetch scripts

**Operational boundaries:**

- Use only credentials the user places in environment variables or an approved secret store pointer
- Leave scheduling to the user's cron or scheduler
- Integrate only services the user explicitly requests
- Default bind/serve guidance to `127.0.0.1`; do not expose publicly without user-owned auth

## Quick Reference

| Topic | File |
|-------|------|
| Data source patterns | `references/sources.md` |
| Visual design rules | `references/design.md` |
| Widget templates | `references/widgets.md` |
| Domain rules and architecture | `references/domain.md` |
| State layout | `references/state.md` |

## Core Rules

### 1. User provides data and credentials

When creating a dashboard:

```text
User: "Dashboard for my Stripe revenue"
Agent: "I'll create a fetch script. Set STRIPE_API_KEY (or STRIPE_SECRET_KEY)
        in your environment, then run the script against the resolved state path."
→ Generates: <state_root>/dashboard/stripe/fetch.sh
→ User cron example: */15 * * * * /absolute/path/to/<state_root>/dashboard/stripe/fetch.sh
```

Resolve `<state_root>` first, then substitute the real path into generated scripts.

### 2. Visual QA before delivery

- Open the page in a browser and capture a screenshot when a browser tool is available
- Check: no overlap, readable fonts (≥14px body), sufficient contrast, labeled axes
- If issues remain → fix → re-check
- Deliver only after visual validation or an explicit note that browser QA was unavailable

### 3. Fail closed on secrets and PII

- Never write API secrets into `config.json`, `data.json`, HTML, or git
- Prefer env var names in scripts (`STRIPE_API_KEY`, service tokens)
- Strip or aggregate PII before rendering tables
- If the user later exposes the dashboard beyond localhost, require their auth plan first
