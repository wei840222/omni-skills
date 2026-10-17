---
name: notion-api-integration
description: >
  Build and debug Notion API integrations against api.notion.com: data sources,
  pages, blocks, properties, filters, files, webhooks, and bulk import/export.
  Use when calling Notion from code, curl, or an SDK; when requests return 404 on
  a visible object, validation_error, 401, or 429; when queries return wrong/empty
  rows or stop at 100; when relation/rollup values truncate; when bumping
  Notion-Version and database_id becomes data_source_id; or when setting up an
  internal token/OAuth flow. Prefer `notion-calendar` for scheduling views,
  `notes` for writing notes across apps without deep API work, `api` for generic
  third-party REST/OAuth without Notion specifics, and `pkm` for knowledge-base
  organization beyond the Notion API surface.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"N","requires":{"env":["NOTION_API_KEY"]},"primaryEnv":"NOTION_API_KEY"}'
  related-skills: '{"api":"Generic third-party REST/GraphQL client patterns without Notion-specific object models.","http":"Protocol-level HTTP status/headers/caching outside Notion payloads.","notes":"Writing notes into Notion or other apps without operating the Notion API.","notion-calendar":"Date-aware Notion scheduling and planning views rather than raw API integration.","pkm":"Knowledge-base organization across tools once content exists.","webhook":"Generic webhook receiver design and signature verification beyond Notion event payloads."}'
---

# Notion API Integration

Operate Notion's HTTP API with pinned `Notion-Version`, schema-first writes,
full pagination, paced bulk jobs, and pointer-only secrets. This skill is for
integrations — not for generic note-taking UX.

## State location

Preferences, schemas, run records, and id mappings are persistent user state.
Resolve `<state_root>` once per invocation before any read or write:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/notion-api-integration/`,
   `<workspace>/memory/notion-api-integration/`, then
   `~/notion-api-integration/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicates; do not merge them.
4. If none exists and the user confirms saving state, create
   `<workspace>/notion-api-integration/`. If `<workspace>` is unavailable, ask
   for a state root instead of guessing from the current directory.
5. If older data exists only under `~/Clawic/data/notion-api-integration/` or
   `~/clawic/notion-api-integration/`, move it into the resolved `<state_root>/`
   after the user confirms, and say in one line that you moved it and from where.
6. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. Keep
skill resources under `references/` and `assets/`; never write the literal
string `<state_root>` to disk.

Suggested layout (create only paths the user confirms):

```text
<state_root>/
├── config.yaml
├── memory.md
├── schemas/
├── artifacts/
├── runs/
└── mappings/
```

Shared project/contact boxes live under host workspace conventions such as
`<workspace>/projects/` and `<workspace>/contacts/` — not inside this skill
package. Before writing to a database or data source, open its schema box when
`memory.md` `## Boxes` names one.

**Secrets:** never store tokens, OAuth `client_secret`, authorization codes, or
signed Notion file URLs under `<state_root>/`. Store pointers only
(`env:NOTION_API_KEY`, `keychain:…`, `1password:…`).

## When to use

- Calling `api.notion.com` from code, curl, or an official SDK
- Diagnosing 404-as-permission, `validation_error`, mid-run 401, 429, or silent wrong query results
- Standing up internal tokens, OAuth public connections, or capability checks
- Bulk CSV/tool import, export, property backfill, webhook/polling sync
- Migrating across `Notion-Version` — especially the database → data source split

Prefer siblings when the ask is calendar/reschedule UX (`notion-calendar`),
cross-app notes without API depth (`notes`), generic REST client craft (`api`),
HTTP protocol detail (`http`), webhook receiver internals (`webhook`), or PKM
organization (`pkm`).

## Setup

On first use, or when `<state_root>/` is missing or empty, read
`references/setup.md` silently, answer the immediate API need first, then offer
to initialize local boxes from `assets/data-templates.md`.

## Quick reference

| Topic | File | Load when |
|-------|------|-----------|
| Setup / boxes | `references/setup.md` | First use / empty state |
| Data templates | `assets/data-templates.md` | Creating state files |
| Auth & sharing | `references/auth.md` | 401/403/404 access, OAuth, tokens |
| Data sources migration | `references/data-sources.md` | Version bump / multi-source DB |
| Databases & schema | `references/databases.md` | Create/alter schema |
| Pages | `references/pages.md` | Page CRUD / trash |
| Properties | `references/properties.md` | Property write shapes |
| Blocks | `references/blocks.md` | Content tree / rich text |
| Filters | `references/filters.md` | Query returns wrong/empty rows |
| Pagination | `references/pagination.md` | Results stop at 100 |
| Bulk jobs | `references/bulk.md` | Import/export/backfill |
| Sync | `references/sync.md` | Webhooks or polling |
| Files | `references/files.md` | Upload/attach/expiring URLs |
| Search | `references/search.md` | Unknown-id discovery |
| Users | `references/users.md` | People/bots/capabilities |
| Comments | `references/comments.md` | Discussions / replies |
| Errors & retries | `references/errors.md` | Status/code diagnosis |
| Verified sources | `references/sources.md` | Version-sensitive claims |

## Core rules

1. **Read the schema before writing.** Property names are case- and space-sensitive. Retrieve the database/data source, save `<state_root>/schemas/…`, and build payloads from that box (`references/databases.md`).
2. **Pin `Notion-Version` on every request.** Omitting it is a 400. Under `2025-09-03+`, queries use `/v1/data_sources/{id}/query` after discovering `data_source_id` (`references/data-sources.md`). If unset, state the assumed version before acting.
3. **Treat 404 as "not shared" until proven otherwise.** Check connection → object-type mismatch (view id vs object id) → true absence (`references/auth.md`).
4. **Paginate every list.** `page_size` maxes at 100. Loop while `has_more` with `next_cursor` (`references/pagination.md`).
5. **Pace by plan; retry with `Retry-After`.** Default assume ~3 rps unless the workspace plan is known higher. 429/529 honour `Retry-After` with jitter; workspace-wide budgets can throttle a quiet client (`references/bulk.md`, `references/errors.md`).
6. **Writes are per-object and non-transactional.** Checkpoint cursors and id mappings; filter on external ids before create; inspect 503 `retry_guidance` before repeating a write (`references/bulk.md`).
7. **State blast radius before destructive calls.** `archived`/`in_trash`, block deletes, and select-option removals need affected counts and confirmation unless `write_mode: direct`.
8. **Page retrieve is a summary.** Content is in blocks (`has_children`). Relation/rollup/people inside the page object may cap around 25 entries — use the property-item endpoint and paginate (`references/properties.md`, `references/blocks.md`).

## Failure cheat sheet

| Symptom | Likely cause | Move |
|---|---|---|
| 404 on a browser-visible page | Not shared with the integration | Share ancestor; see `references/auth.md` |
| `validation_error` on property name | Case/space/rename drift | Re-retrieve schema box |
| Empty query, rows visible in UI | Filter type ≠ property type | Type-match filters (`references/filters.md`) |
| Exactly 100 results | Ignored `has_more` | Cursor loop |
| Short relation/rollup/people | Page-object cap | Property-item pagination |
| 429 | Connection or workspace budget | Honour `Retry-After`; central pacing |
| File URL 403 after an hour | Signed URL expiry | Refetch block; store id only |
| Breakage after version bump | `database_id` vs `data_source_id` | `references/data-sources.md` |

## Configuration defaults

Store overrides in `<state_root>/config.yaml` (see `assets/data-templates.md`).

| Variable | Default | Effect |
|---|---|---|
| `api_version` | `2022-06-28` until user/version needs force a pin; state assumption aloud | Selects endpoint shapes |
| `rate_limit_rps` | `3` | Pacing for generated loops |
| `write_mode` | confirm-destructive | Whether archive/schema/multi-page overwrites auto-run |
| `readonly_targets` | `[]` | Object ids never written |

## Security & privacy

- Auth via `NOTION_API_KEY` / OAuth tokens held by the user's app — never committed.
- Sent to Notion: only the queries and content the user asked for, to `api.notion.com`.
- Local: ids, property names, counts, run checkpoints under `<state_root>/`.
- Reads by default; destructive or multi-page writes need explicit confirmation unless configured otherwise.

## Output checklist

Before delivering a payload, script, or migration plan:

- Schema box consulted for every write target?
- `Notion-Version` pinned and named?
- List calls loop `has_more`; writes paced?
- Destructive impact counted and confirmed?
- Tokens and signed URLs stripped from notes?
- Durable findings written to the correct box?
