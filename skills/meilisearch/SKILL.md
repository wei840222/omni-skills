---
name: meilisearch
description: "Deploy, configure, and tune Meilisearch for production search: index settings, filterable/sortable attributes, typo tolerance, API key scoping, and performance tuning. Use when setting up a Meilisearch instance, designing index settings before adding documents, debugging empty or wrong search results, tuning typo tolerance or ranking, scoping API keys for multi-tenant or frontend use, scheduling snapshots, or diagnosing indexing bottlenecks. Covers Meilisearch v1.x. Not for Elasticsearch/OpenSearch cluster operations (elasticsearch) or vector-only stores (vector-databases)."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔎"}'
  related-skills: '{"api":"REST API integration patterns including auth, rate limits, and retries.","database-manager":"Relational database schema governance and recovery playbooks.","docker":"Containerizing Meilisearch with proper volume and secret handling.","elasticsearch":"Elasticsearch/OpenSearch cluster operations and advanced query DSL."}'
---

## State location

Meilisearch is a stateless reference skill — it does not create persistent files. The Meilisearch server itself manages its own data directory (default `./data.ms` or `MEILI_DB_PATH`). If this skill later needs local state (e.g., saved tuning profiles), resolve `<state_root>` as:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/meilisearch/`, `<workspace>/memory/meilisearch/`, `~/meilisearch/`.
3. If none exists and state must be created, default to `<workspace>/meilisearch/`.

## Index Configuration Traps

These are the highest-impact mistakes. They cause silent data loss or full reindex.

1. **Declare filterable/sortable attributes BEFORE adding documents.** Adding them after documents exist triggers a full reindex — expensive on large datasets.
2. **Batch all setting changes into one API call.** Each settings update triggers reindex; multiple calls multiply the cost.
3. **Order searchableAttributes by importance, not alphabetically.** The first attribute ranks highest. Put title before body, tags before description.
4. **Limit displayedAttributes explicitly.** Default returns all fields — wasteful for documents with large unused fields.

## Indexing Pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| API returns 202 but document not found | Indexing is async; response contains `taskUid` | Poll `GET /tasks/{taskUid}` until `status: "succeeded"` |
| Primary key error on nested/array field | Meilisearch cannot infer nested keys | Set `primaryKey` explicitly in index settings or at creation |
| Indexing slow with large payloads | Sending one doc at a time or oversized batches | Use 10–50 MB JSON batches; use `POST /indexes/{uid}/documents` with NDJSON for streaming |
| Updating one field reverts others | Meilisearch replaces the whole document | Send the complete document; there is no partial update |

## Typo Tolerance

- Default behavior by word length: 1–4 chars = no typo allowed (prefix/same-length only); 5–8 chars = 1 typo; 9+ chars = 2 typos.
- A typo on the first character counts as 2 typos — so "tset" won't match "test" (4 chars, 0 typos allowed), but "caturday" could match "saturday" (8 chars, 1 typo allowed) only if the first letter is correct.
- Typo tolerance on IDs, SKUs, or codes causes false matches. Disable with `typoTolerance.disableOnAttributes: ["sku", "code"]` or `disableOnWords: ["exact-term"]`.
- Adjust thresholds via `typoTolerance.minWordSizeForTypos: {oneTypo: N, twoTypos: M}` where `0 ≤ oneTypo ≤ twoTypos ≤ 255`. Recommended: `oneTypo` 2–8, `twoTypos` 4–14.

## Filtering

- Filters on undeclared `filterableAttributes` return an `invalid_search_filter` error listing available filterable attributes. Always declare attributes before filtering.
- Geo-filtering requires a field named exactly `_geo` with `{lat, lng}`. The field name is hardcoded and cannot be renamed.
- Filter syntax is not SQL. Use `TO` for ranges: `year 2020 TO 2024`, not `BETWEEN`.
- Empty array in `IN` clause causes an error. Validate array length before building the filter string.

## Search Behavior

- Default `limit` is 20, max is 1000. Meilisearch supports two pagination styles:
  - **offset/limit**: `offset` + `limit` (no hard cap on total results, but `limit` ≤ 1000).
  - **page/hitsPerPage**: finite pagination with `page` + `hitsPerPage` (returns `totalPages`, `totalHits`; `hitsPerPage` ≤ 1000).
- Multi-word queries match ANY word by default. Use `"exact phrase"` in the query for phrase matching.
- Highlighting only works on fields listed in `searchableAttributes` — not on stored-only fields.
- `facetsDistribution` counts include all matching documents, not just the returned page.

## 🔴 Production Security Checkpoint

Before deploying Meilisearch to any non-local environment, verify all of the following:

1. **Master key is set** — without it, all endpoints are public and unauthenticated.
2. **Search-only API keys are created for frontend use** — use scoped keys with `actions: ["search"]` for client-side access.
3. **API key scoping is configured** — restrict keys to specific indexes and actions (`search`, `documents.get`) for multi-tenant isolation.
4. **Backups are configured** — schedule snapshots for regular recovery, create dumps before version upgrades, store backup artifacts off-server, and test restores periodically.
5. **`MEILI_ENV` is set to `production`** — enables authentication and disables the search preview UI.

If any check fails, resolve it before serving traffic.

## Performance Realities

- Indexes live in memory-mapped files — RAM determines the maximum index size.
- Payload limit is 100 MB per request — split large imports into batches.
- Indexing blocks during settings updates — queries still work but new documents queue.
- The task queue has no priority — a large reindex blocks small document additions. Plan reindex operations during low-traffic windows.

## API Key Restrictions

- Keys can restrict to specific indexes — use this for multi-tenant isolation.
- Keys support `expiresAt` — but there is no auto-rotation; manage expiration manually.
- Actions are granular: `search`, `documents.add`, `documents.get`, `indexes.create`, `settings.update`, etc.
- Invalid key and missing key on a protected instance both return 401 — check both causes when debugging auth failures.

## Gotchas

- Meilisearch is single-node only — no clustering. Scale vertically with RAM.
- Upgrading between minor versions may require a dump-and-restore. Check the changelog before upgrading in production.
- The `_geo` field name for geo-filtering is hardcoded and cannot be customized.
- Task queue is FIFO with no priority — large background tasks block interactive updates.
- Synonyms do not apply to filters — `SF` and `San Francisco` as synonyms still produce different filter results.
- `filterableAttributes` updates trigger full reindex — plan attribute declarations before adding documents.
- Master key must be at least 16 bytes in production mode.
