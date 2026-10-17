# Sources — Notion API Integration

Live-checked during local takeover of Jules session `5310316903503542588`
(2026-10-17, Asia/Taipei). Prefer these URLs over model memory for normative
claims. Re-check before quoting version-sensitive details.

## Claim inventory

| Topic | Freshness | Source of truth | Refactor outcome |
| --- | --- | --- | --- |
| Agent Skills package shape | Spec-sensitive | agentskills.io + skills-ref | Frontmatter `metadata.version` + JSON-string `openclaw` / `related-skills` |
| Notion-Version / data sources | Version-sensitive | Upgrade guide 2025-09-03 | Discover `data_source_id`; query `/v1/data_sources/{id}/query` |
| Rate limits | Version-sensitive | Request limits reference | ~3 rps default / 180/min; Business 600/min; honour `Retry-After` |
| Auth / sharing | Stable domain | Authorization guide | 404 often means not shared; pointer-only secrets |
| Files | Version-sensitive | Working with files and media | Signed URLs expire; store ids; plan-based size caps |
| Webhooks | Version-sensitive | Webhooks API reference | Prefer events + idempotent receiver; poll with `last_edited_time` otherwise |
| Pagination | Stable domain | API list responses | `page_size` max 100; loop `has_more` |

## Verified sources

### Agent Skills

- **Specification** — <https://agentskills.io/specification>
- **Docs index** — <https://agentskills.io/llms.txt>
- **skills-ref validator** — <https://github.com/agentskills/agentskills/tree/main/skills-ref>

### Notion official

- **API introduction** — <https://developers.notion.com/reference/intro>
- **Authorization** — <https://developers.notion.com/docs/authorization>
- **Create a connection** — <https://developers.notion.com/docs/create-a-notion-integration>
- **Upgrade guide 2025-09-03** — <https://developers.notion.com/docs/upgrade-guide-2025-09-03>
- **Request limits** — <https://developers.notion.com/reference/request-limits>
- **Query a data source** — <https://developers.notion.com/reference/query-a-data-source>
- **Retrieve a database** — <https://developers.notion.com/reference/retrieve-a-database>
- **Create a page** — <https://developers.notion.com/reference/post-page>
- **Working with files and media** — <https://developers.notion.com/docs/working-with-files-and-media>
- **Webhooks reference** — <https://developers.notion.com/reference/webhooks>

### Corrections applied this refactor

- Replaced folklore "always ~3 rps hard cap" with plan-based per-connection budgets and shared workspace limits from Request limits.
- Made `2025-09-03` data-source migration an explicit reference (`references/data-sources.md`) instead of a single sentence.
- Removed Clawic promotional paths/URLs; state uses portable `<state_root>` resolver.
