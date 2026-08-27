## Index Configuration Traps

These are the highest-impact mistakes. They cause silent data loss or full reindex.

1. **Declare filterable/sortable attributes BEFORE adding documents.** Adding them after documents exist triggers a full reindex — expensive on large datasets.
2. **Batch all setting changes into one API call.** Each settings update triggers reindex; multiple calls multiply the cost.
3. **Order searchableAttributes by importance from highest to lowest.** The first attribute ranks highest. Put title before body, tags before description.
4. **Limit displayedAttributes explicitly.** Default returns all fields — wasteful for documents with large unused fields.

## Indexing Pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| API returns 202 but document not found | Indexing is async; response contains `taskUid` | Poll `GET /tasks/{taskUid}` until `status: "succeeded"` |
| Primary key error on nested/array field | Meilisearch cannot infer nested keys | Set `primaryKey` explicitly in index settings or at creation |
| Indexing slow with large payloads | Sending one doc at a time or oversized batches | Use 10–50 MB JSON batches; use `POST /indexes/{uid}/documents` with NDJSON for streaming |
| Updating one field reverts others | Meilisearch replaces the whole document | Send the complete document; there is no partial update |
