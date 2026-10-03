# Build Your Own Stack — Help Center

Use when lock-in, compliance, data residency, or custom workflow needs outweigh SaaS time-to-value. Component names below are common examples, not endorsements.

## Core components

| Layer | Example choices | Requirement |
| --- | --- | --- |
| Content store | Git Markdown repo, headless CMS, SQL + admin UI | Versioning, ownership metadata, review states |
| Search | Meilisearch, OpenSearch, Algolia, or equivalent | Typo tolerance, synonyms, query logging |
| Delivery UI | Docs frontend (e.g. Next.js, Astro, static site) | Fast taxonomy navigation and feedback widgets |
| Auth (optional) | SSO/OAuth gateway | Required for private or tiered content |
| Ticket bridge | Webhooks + queue worker | Unresolved intents open pre-tagged tickets |
| Analytics | Product analytics + search/query logs | Deflection, misses, stale content signals |

## Reference architecture

1. **Authoring** — product/support authors update docs in CMS or repository with owners and review dates.
2. **Indexing** — publish events update search index and article metadata.
3. **Delivery** — frontend renders categories, search, and article feedback.
4. **Escalation** — low-confidence or failed self-service opens a pre-tagged support ticket.
5. **Insights** — weekly jobs aggregate deflection, failed queries, and stale articles.

## Guardrails

- Freeze the public URL schema before launch to limit redirect sprawl.
- Keep stable article IDs even when titles change.
- Rehearse rollback for bad index builds or failed deployments.
- Separate public and private content paths from day one.
- Name an on-call owner for search, publish pipeline, and ticket bridge health.
- Score the custom option with the same matrix in `references/provider-matrix.md` so SaaS and build-your-own stay comparable.
