---
name: matomo
description: Use to query, analyze, and manage Matomo Analytics via its Reporting API. Use when the user asks for traffic insights, goal conversions, analytics reports, or Reporting API help for a self-hosted Matomo instance.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji": "📊"}'
---

## State location

Matomo state may exist in `<workspace>/matomo/`, `<workspace>/memory/matomo/`, or `~/matomo/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/matomo/`, `<workspace>/memory/matomo/`, `~/matomo/`.
3. If none exists and state must be created, default to `<workspace>/matomo/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` for integration guidelines. The skill stores configuration in `<state_root>/`.

## When to Use

User needs to query Matomo analytics, generate reports, track goals, or manage their self-hosted analytics. Agent handles API queries, data analysis, visitor insights, and conversion tracking.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure.

```
<state_root>/
├── memory.md         # Sites, credentials ref, preferences
├── reports/          # Saved report templates
└── queries/          # Reusable API query templates
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | When configuring connection to a Matomo instance for the first time. |
| Memory template | `references/memory-template.md` | When initializing or updating state format in memory.md. |
| API reference | `references/api.md` | When writing or executing curl requests to Matomo reporting API. |
| Report templates | `assets/reports.md` | When user asks to generate a report (e.g. daily dashboard, weekly summary). |

## Core Rules

### 1. Secure Credentials Handling
- Store the token exclusively in system keychain or env var, keeping memory files free of raw credentials
- Refer to credentials by reference name only
- If user pastes token in chat, warn and suggest secure storage

### 2. Use Reporting API for Reads
```bash
# Base pattern
curl -sS --get "https://{matomo_url}/index.php" \
  --data-urlencode "module=API" \
  --data-urlencode "method={method}" \
  --data-urlencode "idSite={site_id}" \
  --data-urlencode "period={period}" \
  --data-urlencode "date={date}" \
  --data-urlencode "format=json" \
  --data-urlencode "token_auth=${MATOMO_TOKEN}"
```
Common methods:
- `VisitsSummary.get` — visitors, visits, pageviews
- `Actions.getPageUrls` — top pages
- `Referrers.getWebsites` — traffic sources
- `Goals.get` — conversion data
- `Events.getCategory` — event categories

### 3. Understand Date Ranges
| Period | Date Format | Example |
|--------|-------------|---------|
| `day` | `YYYY-MM-DD` | `2025-01-15` |
| `week` | `YYYY-MM-DD` | Week containing that date |
| `month` | `YYYY-MM` | `2025-01` |
| `year` | `YYYY` | `2025` |
| `range` | `YYYY-MM-DD,YYYY-MM-DD` | `2025-01-01,2025-01-31` |

Special dates: `today`, `yesterday`, `last7`, `last30`, `lastMonth`, `lastYear`

### 4. Handle Multi-Site Setups
- Always confirm which site before querying
- Store site list in memory.md with idSite mappings
- Default to most-used site if configured

### 5. Format Data for Humans
- Round percentages to 1 decimal
- Use K/M suffixes for large numbers
- Compare periods when context helps (vs last week/month)
- Highlight significant changes (>10% delta)

### 6. Respect Rate Limits
- Batch related queries into single date range when possible
- Cache recent results in memory for follow-up questions
- Reuse cached recent results in memory to answer follow-up questions instead of repeating identical queries

### 7. Use Segments for Deeper Insights
Segments filter data by visitor attributes. Add `&segment=` to any query:

```bash
# Mobile visitors only
&segment=deviceType==smartphone

# From specific country
&segment=countryCode==US

# Returning visitors who converted
&segment=visitorType==returning;goalConversionsSome>0

# Combine with AND (;) or OR (,)
&segment=browserCode==CH;operatingSystemCode==WIN
```

Common segment dimensions:
- `deviceType` — smartphone, tablet, desktop
- `browserCode` — CH (Chrome), FF (Firefox), SF (Safari)
- `countryCode` — ISO 2-letter code
- `visitorType` — new, returning
- `referrerType` — direct, search, website, campaign

## Matomo Traps

Use these checks to keep reporting requests accurate:

- **Wrong idSite** → querying wrong property, misleading data. Always confirm site first.
- **Missing token_auth** → 403 or empty response. Token required for all non-public methods.
- **date vs period mismatch** → confusing results. `period=range` requires `date=start,end` format.
- **Expecting GA terminology** → Matomo uses "visits" not "sessions", "actions" not "events". Translate mentally.
- **Missing segments** → missing the real insight. Segments filter data by visitor attributes.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| `{user_matomo_url}/index.php` | API method, site ID, date range, auth token | Query analytics data |

No other data is sent externally. All requests go to user's own Matomo instance.

## Security & Privacy

**Data that leaves your machine:**
- API queries sent to user's Matomo instance only
- Auth token included in requests (user-controlled)

**Data that stays local:**
- Site configurations in `<state_root>/`
- Report templates
- No data sent to third parties

**Required Protections:**
- Ensure auth tokens are stored securely outside of plain text files
- Route all data transmissions exclusively to the user's configured Matomo instance
- Confine file access strictly to `<state_root>/`
