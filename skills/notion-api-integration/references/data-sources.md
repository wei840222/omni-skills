# Data Sources — API Version `2025-09-03`

Under `Notion-Version: 2025-09-03`, a database can contain multiple data sources. Most operations that previously took `database_id` for query/schema now take `data_source_id`.

**Contents:** [Why it breaks](#why-it-breaks) · [Discovery](#discovery) · [Endpoint map](#endpoint-map) · [Parents and relations](#parents-and-relations) · [Migration checklist](#migration-checklist)

## Why it breaks

If a workspace adds a second data source to a database while your client still uses a pre-`2025-09-03` version, create-page / query / relation writes against that database can fail. Treat version bumps as migrations, not header cosmetics.

## Discovery

1. `GET /v1/databases/{database_id}` with `Notion-Version: 2025-09-03` returns `data_sources: [{id, name}, …]`.
2. Store the chosen `data_source_id` in the schema box under `<state_root>/schemas/`.
3. Schema detail moves to `GET /v1/data_sources/{data_source_id}`.

Database id and data source id are **not** interchangeable.

## Endpoint map

| Pre-`2025-09-03` | `2025-09-03`+ |
|---|---|
| `GET /v1/databases/{id}` (schema) | `GET /v1/databases/{id}` lists sources; schema via `GET /v1/data_sources/{id}` |
| `POST /v1/databases/{id}/query` | `POST /v1/data_sources/{id}/query` |
| Page parent `{database_id}` | Prefer `{type: data_source_id, data_source_id}` |
| Relation target `database_id` only | Write path should send `data_source_id` |

## Parents and relations

When creating pages into a multi-source database, send the specific data source parent. Relation property reads may include both ids; writes should prefer `data_source_id`.

## Migration checklist

1. Pin `Notion-Version` explicitly in every client.
2. Add discovery; persist `data_source_id`.
3. Switch query / retrieve-schema / page-parent / relation writes.
4. Update webhook payload handling if subscribed (parent shape changes).
5. Upgrade SDK major only after request paths are ready.

Official source: Upgrade guide for `2025-09-03`.
