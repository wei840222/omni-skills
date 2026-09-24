## Core Rules

### 1. Treat the calendar as date-driven Notion data

- The operational unit is a Notion database or data source with at least one date property.
- Keep this skill on Notion database pages. Google Calendar sync and native Notion Calendar app settings are separate products and stay out of this workflow.

### 2. Discover schema before writing

- `GET /v1/databases/{database_id}` for the container, then read the child `data_source_id`.
- `GET /v1/data_sources/{data_source_id}` for live property names before create or update.
- After the user approves a mapping, cache title, date, status, assignee, and timezone fields in `<state_root>/calendars.md`.

### 3. Use explicit time windows

- Convert "next week" or "this quarter" into bounded ISO dates with a declared timezone.
- Query the requested window first. Widen only when the result set is empty or clearly incomplete.

### 4. Match the client to the API version

- Send `Notion-Version` on every `api.notion.com` request. For new work, use `2025-09-03` or the newer version named in `references/sources.md`.
- Use the optional `notion` CLI only for basic search, read, or simple page CRUD on a stable older database.
- When the task needs `data_source_id`, schema migration, or any command the CLI does not support, call `api.notion.com` directly.

### 5. Read before write, then read back

- Before create, reschedule, archive, or status changes, fetch matching rows in the exact target window.
- After a write, read the changed page and report the final title, date, status, and URL.

### 6. Keep calendar semantics explicit

- Confirm whether a row is all-day, a single timestamp, or a start/end range before writing date values.
- Repeating items are templates or a batch of future pages. State that model before creating them.

### 7. Resolve ambiguity before a destructive change

- When several pages share a title, ask for the page URL, page ID, or the exact date window.
- Archive or move a row only after a unique ID match, or after the user confirms the exact page.

## Common Traps

- Treating a database ID as enough on `2025-09-03` -> query and create need `data_source_id`.
- Writing the first property named "Date" -> confirm the view's date column first.
- Assuming Notion rows recur -> model repeats as templates or explicit future pages.
- Rescheduling by title only -> duplicate launch or editorial rows get changed.
- Querying an open-ended range first -> noisy results and a weak read-back.

## External Endpoints

Send `Authorization: Bearer $NOTION_API_KEY` and `Notion-Version` on each call. No other host receives calendar data.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| `POST https://api.notion.com/v1/search` | Search text, filters, pagination cursor | Find candidate databases, data sources, or pages shared with the connection |
| `GET https://api.notion.com/v1/databases/{database_id}` | Database ID | Retrieve container metadata and child data sources |
| `GET https://api.notion.com/v1/data_sources/{data_source_id}` | Data source ID | Read live property schema |
| `POST https://api.notion.com/v1/data_sources/{data_source_id}/query` | Filters, sorts | List pages in a time window |
| `POST https://api.notion.com/v1/pages` | Parent `data_source_id`, properties | Create a calendar page |
| `PATCH https://api.notion.com/v1/pages/{page_id}` | Property updates | Reschedule or change status, then read back |

The older `POST /v1/databases/{database_id}/query` path is only for a caller pinned to `2022-06-28`. See `references/sources.md`.

## Security and privacy

**Data that leaves the machine:**
- Search text, page properties, dates, and page content sent to Notion at `api.notion.com`.

**Data that stays local:**
- Workspace context, property mappings, and safe defaults under the resolved `<state_root>`.

**This skill keeps:**
- API keys in the host environment, outside skill memory files.
- Third-party calendar traffic limited to Notion endpoints declared above.
- A write report that includes a read-back of title, date, status, and URL.
- Skill writes inside `<state_root>/` unless the user names a separate host path.

## Scope

This skill:
- Works with Notion databases, data sources, and pages used as calendar items.
- Uses the optional `notion` CLI when it is installed and the operation matches its older API shape.
- Falls back to direct Notion API calls when the CLI lags the current API shape.

Separate products, not this skill:
- Notion Calendar app preferences and account settings.
- Google Calendar account sync.
- Destructive changes chosen from a low-confidence title match.

## Trust

Calendar-related workspace data is sent to Notion. Install only if that trust covers page titles, dates, status fields, and related planning metadata.
