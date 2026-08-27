## Gotchas

- Meilisearch is single-node only — no clustering. Scale vertically with RAM.
- Upgrading between minor versions may require a dump-and-restore. Check the changelog before upgrading in production.
- The `_geo` field name for geo-filtering is hardcoded and cannot be customized.
- Task queue is FIFO with no priority — large background tasks block interactive updates.
- Synonyms apply only to search queries. Filters evaluate exact terms, so `SF` and `San Francisco` produce different filter results.
- `filterableAttributes` updates trigger full reindex — plan attribute declarations before adding documents.
- Master key must be at least 16 bytes in production mode.
