# Verified sources

Checked 2026-09-25 against the public Notion developer docs. Prefer these pages over memory of older `/v1/databases/{id}/query` examples.

## API shape (2025-09-03 and later)

- **Upgrade guide** — databases and data sources split; most operations that used `database_id` now need `data_source_id`; create-page parents use `{"type":"data_source_id","data_source_id":"..."}`. https://developers.notion.com/guides/get-started/upgrade-guide-2025-09-03
- **Versioning** — every REST call must send `Notion-Version`. The versioning page listed `2026-03-11` as the then-current example. https://developers.notion.com/reference/versioning
- **Retrieve a database** — `GET /v1/databases/{database_id}` still returns the container, including child data sources, so discovery can start from a database ID. https://developers.notion.com/reference/retrieve-database
- **Retrieve a data source** — `GET /v1/data_sources/{data_source_id}` returns column schema. Use this before writing property names. https://developers.notion.com/reference/retrieve-a-data-source
- **Query a data source** — `POST /v1/data_sources/{data_source_id}/query` lists child pages with filter and sort. An unshared parent database returns 404. https://developers.notion.com/reference/query-a-data-source
- **Create a page** — `POST /v1/pages` with a `data_source_id` parent. https://developers.notion.com/reference/post-page
- **Update a page** — `PATCH /v1/pages/{page_id}` changes properties, then read the page back. https://developers.notion.com/reference/patch-page
- **Search by title** — `POST /v1/search` returns pages or data sources shared with the connection. https://developers.notion.com/reference/post-search
- **Date filters** — `on_or_after` and `on_or_before` compare ISO 8601 values; a date-time is compared at millisecond precision. https://developers.notion.com/reference/post-database-query-filter

## Deprecated path

- **Post database query** — `POST /v1/databases/{database_id}/query` is documented for API versions up to `2022-06-28` and marked deprecated as of `2025-09-03`. Use it only when the caller is pinned to that older version. https://developers.notion.com/reference/post-database-query

## What this skill does not claim

Notion's public API does not expose Google Calendar sync or Notion Calendar app preferences. Those stay out of scope. Recurrence is not a page-create field in the endpoints above; repeating items are modeled as templates or explicit future pages.
