---
name: wiki-js
description: >
  Deploy and operate Wiki.js documentation sites while avoiding Site URL,
  database, editor, permission, and sync traps. Use when choosing PostgreSQL
  over SQLite, fixing HTTPS/login redirect loops, picking Markdown vs Visual
  Editor, writing page-rule patterns, configuring Git/S3 storage, or recovering
  after a domain move. Prefer `wiki` for information-architecture craft,
  `documentation` for Diátaxis product docs, `nginx`/`caddy` for reverse-proxy
  TLS termination details, `pg`/`sqlite` for database engine internals, and
  `markdown` for parser/syntax issues.
metadata:
  openclaw: '{"emoji":"📖"}'
  related-skills: '{"wiki":"Wiki page craft, templates, redirects, and freshness audits once the Wiki.js site itself is healthy.","documentation":"Product/README/API documentation systems and Diátaxis structure rather than Wiki.js deploy traps.","nginx":"Reverse-proxy TLS termination, redirects, and 502/loop debugging in front of Wiki.js HTTP.","caddy":"Simpler automatic HTTPS reverse proxy when nginx control is unnecessary.","pg":"PostgreSQL internals, backups, and extensions once Wiki.js is already on Postgres.","sqlite":"Embedded SQLite concurrency limits when evaluating why multi-user Wiki.js should leave SQLite.","markdown":"Markdown syntax and CommonMark parser issues inside Wiki.js pages.","backups":"Backup retention and restore drills for the Wiki.js database dump beyond day-to-day site ops.","docker":"Container/compose packaging around a Wiki.js deployment."}'
---

# Wiki.js

Operate **Wiki.js** (Requarks) deployments: first-run Site URL, database choice,
editor conversion traps, page rules, storage modules, and post-import recovery.
This skill is **stateless by default**. Optional inventory of Site URL,
compose paths, and backup pointers may live under a resolved `<state_root>` when
the user wants continuity across sessions.

## State location

Before reading or writing optional state, resolve `<state_root>` once per
invocation:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/wiki-js/`, `<workspace>/memory/wiki-js/`, then `~/wiki-js/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicates; do not merge them.
4. If none exists and the user confirms saving deployment inventory, create
   `<workspace>/wiki-js/`. If `<workspace>` is unavailable, ask for a state
   root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state path under this skill. Keep
skill resources under `references/`; never write the literal string
`<state_root>` to disk. Credentials are **pointer-only** — store secret names,
never raw DB passwords or SSH keys.

Suggested layout (all optional):

```text
<state_root>/
├── inventory.md   # Site URL, host, DB engine, proxy front-end
├── compose/       # paths to docker-compose / systemd units
└── pointers.md    # secret names / backup labels only
```

If legacy Clawic paths such as `~/Clawic/data/wiki-js/` appear, treat them as
migration sources only; move with explicit confirmation and never auto-merge.

## When to use

- First install or domain migration: Site URL must match the public HTTPS URL
- Choosing PostgreSQL vs SQLite/MySQL for multi-user production
- Login redirect loops / broken assets after putting a reverse proxy in front
- Deciding Markdown vs Visual Editor, or converting between them
- Writing page-rule Allow/Deny patterns and default group setup
- Enabling Git or S3/Spaces storage modules and understanding sync direction
- Prefer `wiki` for page IA/templates; `nginx`/`caddy` for TLS proxy details;
  `pg`/`sqlite` for engine internals; `documentation` for Diátaxis product docs

## Quick reference

| Situation | Play |
|---|---|
| Login redirect loop after HTTPS / domain change | Site URL protocol+host mismatch — `references/troubleshooting.md` |
| Assets 404 / mixed content after proxy | Site URL must equal the browser access URL |
| Multi-user / concurrent writes on SQLite | Move to PostgreSQL 9.5+ (latest recommended) — requirements docs |
| Choosing editor for durable docs | Prefer Markdown; Visual Editor is HTML underneath |
| Convert Markdown page → Visual Editor | Page Actions → Convert to HTML (one-way content shape change) |
| Page 404 right after create | Prefer lowercase alphanumeric path segments; avoid special characters |
| Group can read some paths but not others | Page rules: exact / start-with / regex; Deny vs Allow |
| Need Git backup of pages | Storage → Git module; content still lives in the DB |
| Large images bloating DB backups | Offload assets to S3 / Spaces / similar storage module |
| Slow after bulk import | Search reindex in progress — Admin → Utilities |

## Critical initial config

- **Site URL first**: set the public URL (scheme + host + path prefix) correctly
  on first setup. Changing it later rewrites every internal link; mismatches
  cause login loops and broken assets (`references/troubleshooting.md`).
- **PostgreSQL for production**: docs recommend PostgreSQL 9.5+ (latest when
  possible). SQLite is supported today for low-end/dev only and is **not**
  recommended for production; MySQL/MariaDB/MSSQL/SQLite are slated to drop in
  the next major version. For multi-user concurrent writes, prefer PostgreSQL
  and hand engine internals to `pg`.
- **TLS at the edge**: Wiki.js can terminate HTTPS itself (custom certs or
  Let's Encrypt) **or** sit behind a reverse proxy. When a proxy owns TLS,
  keep Wiki.js on HTTP internally and make Site URL use `https://…`. Proxy
  craft belongs in `nginx` / `caddy`.

## Editor traps

- Editors include Markdown, Visual Editor (rich-text WYSIWYG), AsciiDoc, code,
  and raw HTML (`https://docs.requarks.io/editors`).
- Visual Editor stores HTML. Converting a Markdown page to Visual Editor goes
  through **Convert to HTML**; treat that as a content-shape change, not a
  lossless toggle.
- Prefer Markdown as the durable default for docs that must stay diffable and
  portable; use Visual Editor only when authors explicitly need WYSIWYG.

## Permission pitfalls

- Global permissions are the master Allow/Deny switch; page rules refine path
  access with exact / start-with / regex patterns
  (`https://docs.requarks.io/groups`).
- Overlapping Deny rules beat casual Allow expectations — test with a non-admin
  account before inviting a whole team.
- New self-registered users start with no access until placed in a group; configure
  the default group **before** opening registration.

## Storage and sync

- All content lives in the database; a DB backup is the complete content backup.
- Storage modules (Git, AWS S3, Azure Blob, DigitalOcean Spaces, local FS, SFTP,
  …) add backup/sync. Some modules (notably Git) can sync **both directions**;
  do not assume every module is Wiki.js→remote only
  (`https://docs.requarks.io/storage`, `…/storage/git`).
- Large asset blobs in the DB bloat dumps — prefer object storage for images on
  bigger wikis; retention/restore policy beyond the dump itself is `backups`.

## Search behavior

- Built-in DB search respects permissions (users only see hits they can read).
- PostgreSQL search needs the `pg_trgm` extension on the host.
- Elasticsearch is optional; after large imports, wait for automatic reindex
  (Admin → Utilities) before declaring search broken.

## Diagnostics

For login loops, asset failures, create-time 404s, or post-import slowness, load:

- `references/troubleshooting.md`

## Sources

Official docs verified during this refactor (HTTP 200):

- https://docs.requarks.io/install/requirements
- https://docs.requarks.io/install/config
- https://docs.requarks.io/editors
- https://docs.requarks.io/editors/markdown
- https://docs.requarks.io/groups
- https://docs.requarks.io/storage
- https://docs.requarks.io/storage/git
- https://docs.requarks.io/auth
- https://js.wiki/
- https://github.com/requarks/wiki
- https://agentskills.io/specification
