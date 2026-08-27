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
