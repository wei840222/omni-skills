---
name: mixpanel
description: >
  Query Mixpanel product analytics with Service Account auth: Retention, Engage
  profiles, Insights-first reporting, Raw Event Export, and legacy Funnels/JQL
  caveats. Use when the user needs Mixpanel Query API or Export API curls,
  funnel/retention cohort pulls, profile lookups, or rate-limit handling. Prefer
  `analytics` for cross-vendor routing, `plausible`/`umami` for privacy-first web
  analytics, `data-analysis` after numbers are in hand, and `api` for generic REST
  shaping outside Mixpanel endpoints.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📊","requires":{"bins":["curl","jq"],"env":["MP_SERVICE_ACCOUNT","MP_SERVICE_SECRET","MP_PROJECT_ID"]},"primaryEnv":"MP_SERVICE_SECRET","os":["linux","darwin"],"displayName":"Mixpanel","configPaths":["<state_root>/"]}'
  related-skills: '{"analytics":"Cross-vendor analytics routing when the ask is not Mixpanel-specific.","api":"Generic REST request shaping outside Mixpanel Query/Export endpoints.","data-analysis":"General analysis patterns after Mixpanel returns raw numbers.","plausible":"Privacy-first web analytics alternative to Mixpanel product analytics.","umami":"Self-hosted web analytics alternative when Mixpanel is not the product."}'
---

# Mixpanel

Query **Mixpanel** report and profile data with Service Account Basic auth.
Keep credentials in env vars only. Persist project context and saved query notes
under `<state_root>/` (see `references/setup.md` and `assets/data-templates.md`).

## State location

Mixpanel notes may live under `<workspace>/mixpanel/`,
`<workspace>/memory/mixpanel/`, or `~/mixpanel/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/mixpanel/`, `<workspace>/memory/mixpanel/`, `~/mixpanel/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to
   `<workspace>/mixpanel/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/mixpanel/`, move them into the resolved
`<state_root>/` after the user confirms. Scripts must receive the resolved
filesystem path — never write the literal string `<state_root>` to disk.

## When to use

- Retention cohorts, Engage profile pulls, Raw Event Export, Insights reports
- Service Account setup and `project_id` query-parameter requirements
- Rate-limit planning for Query API (60/hour, 5 concurrent) and Export API
- Migrating away from maintenance-mode Funnels Query / JQL toward Insights or Export

Prefer other skills when the ask is mainly:

- Cross-vendor analytics choice → `analytics`
- Plausible / Umami product deep dives → `plausible` / `umami`
- Generic REST debugging → `api`
- Post-query statistical framing → `data-analysis`

## Progressive disclosure

| Need | Load |
|------|------|
| First-use integration and credentials | `references/setup.md` |
| Endpoint curls, params, residency hosts | `references/query-api.md` |
| Official doc anchors for fact checks | `references/sources.md` |
| Memory / saved-query templates | `assets/data-templates.md` |

## Architecture

```
<state_root>/
├── memory.md        # Project context, key events, insights
└── queries/         # Saved query notes (optional)
```

## Core rules

1. **Service Account Basic auth** — Use `MP_SERVICE_ACCOUNT` + `MP_SERVICE_SECRET`
   via HTTP Basic Auth. Include `project_id=$MP_PROJECT_ID` on Query API calls
   when authenticating with a Service Account.
2. **Dates are `YYYY-MM-DD`** — Query and Export date params are inclusive calendar
   dates, not unix timestamps.
3. **Prefer Insights over legacy Funnels Query** — The Funnels Query API is in
   maintenance mode; build a Funnels report in-app and query it with Insights, or
   use Export for raw events.
4. **Treat JQL as legacy** — JQL is in maintenance mode; prefer Insights, Engage,
   Export, or Data Pipelines for new work.
5. **Respect rate limits** — Query API: 60 queries/hour and 5 concurrent. Raw
   Export API: 60/hour, 3/sec, 100 concurrent. On HTTP 429, back off and batch.
6. **Secrets stay in env** — Never store Service Account secrets in
   `<state_root>/memory.md` or chat paste prompts.

## Workflow

1. Resolve `<state_root>`; if `memory.md` is missing, load `references/setup.md`.
2. Confirm env has `MP_SERVICE_ACCOUNT`, `MP_SERVICE_SECRET`, and `MP_PROJECT_ID`.
3. Choose the endpoint family from `references/query-api.md` (Retention / Engage /
   Insights / Export first; Funnels Query / JQL only with maintenance caveats).
4. Run curl with Basic auth + required params; pipe through `jq` when JSON.
5. Cache useful selectors and insights under `<state_root>/` without credentials.
6. Re-open URLs in `references/sources.md` before asserting version-sensitive facts.

## Security & privacy

**Data sent to Mixpanel over HTTPS:** Service Account credentials, `project_id`,
query/export parameters (event names, dates, filters, cohort ids).

**Data that stays local:** Credentials in environment variables only; query notes
and cached results under `<state_root>/`.

**Boundaries:** Transmit analytics traffic only to the configured Mixpanel hosts;
treat tracking SDKs and project write paths as outside this skill's mutation scope.
