# Mixpanel Query & Export API

Default US Query host pattern: `https://mixpanel.com/api/query/...`.
Raw Export host pattern: `https://data.mixpanel.com/api/2.0/export`.
Replace hosts for EU/IN residency when the project requires it
(`{regionAndDomain}` / `{server}.mixpanel.com` in official docs).

Auth helper used below:

```bash
export MP_SERVICE_ACCOUNT="..."
export MP_SERVICE_SECRET="..."
export MP_PROJECT_ID="123456"
# Prefer curl --user so shells do not echo secrets into history scrapers.
USERPASS="$MP_SERVICE_ACCOUNT:$MP_SERVICE_SECRET"
```

## Retention (GET `/retention`)

Required with Service Account: `project_id`, `from_date`, `to_date` (`YYYY-MM-DD`).
`retention_type` defaults to `birth` (first-time). Use `compounded` for recurring.
`born_event` is required when `retention_type=birth`.

```bash
curl -sG "https://mixpanel.com/api/query/retention" \
  --user "$USERPASS" \
  --data-urlencode "project_id=$MP_PROJECT_ID" \
  --data-urlencode "from_date=2024-01-01" \
  --data-urlencode "to_date=2024-01-31" \
  --data-urlencode "retention_type=birth" \
  --data-urlencode "born_event=Sign Up" \
  --data-urlencode "event=App Open" \
  --data-urlencode "unit=week" | jq
```

## Engage profiles (POST `/engage`)

Required with Service Account: `project_id` query param. Body is
`application/x-www-form-urlencoded`. Cohort filter example:
`filter_by_cohort='{"id":12345}'`. Page with `session_id` + `page`.

```bash
curl -s "https://mixpanel.com/api/query/engage?project_id=$MP_PROJECT_ID" \
  --user "$USERPASS" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode 'filter_by_cohort={"id":12345}' \
  --data-urlencode 'output_properties=["$email","$name","plan"]' | jq
```

## Insights (preferred report path)

Use Insights Query for in-app report data, including modern funnel reporting.
Load https://docs.mixpanel.com/reference/insights-query for current params and
bookmark ids before inventing request bodies.

## Funnels Query (maintenance mode)

GET `/funnels` still exists but is in maintenance mode. Required params include
`project_id` (Service Account), `funnel_id`, `from_date`, `to_date`. Prefer
building a Funnels report in-app and querying via Insights instead of new
direct Funnels Query integrations.

```bash
curl -sG "https://mixpanel.com/api/query/funnels" \
  --user "$USERPASS" \
  --data-urlencode "project_id=$MP_PROJECT_ID" \
  --data-urlencode "funnel_id=12345" \
  --data-urlencode "from_date=2024-01-01" \
  --data-urlencode "to_date=2024-01-31" \
  --data-urlencode "unit=day" | jq
```

## Raw Event Export (GET `/export`)

Host: `https://data.mixpanel.com/api/2.0/export`. Required: `from_date`,
`to_date`. Include `project_id` when using Service Account auth. `event` is a
JSON array string. Response is JSONL (one event per line).

```bash
curl -sG "https://data.mixpanel.com/api/2.0/export" \
  --user "$USERPASS" \
  --data-urlencode "project_id=$MP_PROJECT_ID" \
  --data-urlencode "from_date=2024-01-01" \
  --data-urlencode "to_date=2024-01-07" \
  --data-urlencode 'event=["Purchase"]'
```

## JQL (maintenance mode)

POST `/jql` remains documented but is in maintenance mode. Prefer Export,
Engage, Insights, or Data Pipelines for new work. If you must run a legacy
script, send `application/x-www-form-urlencoded` with `script` (+ optional
`params`) and `project_id` for Service Account auth. Queries time out around
two minutes; keep result sets bounded.

## Rate limits & traps

| Surface | Limit (per project) |
|---------|---------------------|
| Query API (includes JQL) | 60 queries/hour, 5 concurrent |
| Raw Export API | 60 queries/hour, 3/sec, 100 concurrent |

- Missing `project_id` with Service Account auth → unauthorized / invalid request
- Wrong date format → use inclusive `YYYY-MM-DD`
- HTTP 429 → slow down, consolidate filters, cache under `<state_root>/`
- Funnels Query without `funnel_id` → not a free-form event-array POST body
- Assuming US hosts for EU/IN projects → use residency-specific hosts from docs
