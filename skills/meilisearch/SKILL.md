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

## Quick Reference

| Topic | When to load | File |
|---|---|---|
| Indexing | When configuring an index or troubleshooting indexing failures | `references/indexing.md` |
| Search & Filtering | When writing search queries, tuning typo tolerance, or using filters/facets | `references/search-filtering.md` |
| Production & Security | When deploying, securing, or scaling a production instance | `references/production.md` |
| Gotchas | Before making architectural decisions or upgrading | `references/gotchas.md` |
