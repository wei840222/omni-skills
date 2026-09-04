---
name: qdrant
description: Construct vector similarity searches, pre-filtered queries, and optimize HNSW indices using Qdrant for semantic recommendation systems.
metadata:
  openclaw: '{"emoji": "\ud83d\udd0d", "requires": null}'
---

## When to Use

User needs vector similarity search, semantic search, or recommendation systems. Agent handles collection design, point insertion, filtered queries, and index optimization.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Query patterns | `references/queries.md` | When designing filtering logic, scroll, or search queries. |
| Performance tuning | `references/performance.md` | When optimizing HNSW indices, quantization, or handling large datasets. |
| Architecture | `references/research.md` | When needing context on Qdrant core behavior and HNSW principles. |

## Core Rules

### 1. Collection Setup
- Set vector dimension to match embedding model (e.g., OpenAI ada-002 = 1536)
- Choose distance metric deliberately: `Cosine` for normalized embeddings, `Dot` for raw scores, `Euclid` for absolute distance
- Verify dimension matches exactly; mismatches cause silent failures with zero results

### 2. Payload Strategy
- Store filterable metadata as payload fields
- Index payload fields used in filters: `create_payload_index`
- Store large blobs in external storage and include only their reference IDs in payloads

### 3. Batch Operations
- Insert points in batches of 100-1000, instead of one by one
- Use `upsert` to handle duplicates by ID
- Parallel uploads with `wait=false` then verify with collection info

### 4. Filtering vs Post-Filtering
| When | Use |
|------|-----|
| Known constraints | Filter in query (pre-filter) |
| Score threshold | `score_threshold` parameter |
| Complex logic | Combine `must`, `should`, `must_not` |

- Pre-filtering reduces search space = faster
- Post-filtering on results = slower, may miss relevant items

### 5. Search vs Scroll
| Need | Use |
|------|-----|
| Top-K similar | `search` |
| All matching | `scroll` with filter |
| Paginated results | `scroll` with `offset` |
| Export/backup | `scroll` all with pagination |

### 6. Index Optimization
- HNSW parameters: increase `m` for recall, increase `ef_construct` for index quality
- Default `m=16, ef_construct=100` works for most cases
- For millions of vectors: enable `on_disk` storage
- Use quantization (`scalar` or `product`) to reduce memory 4-8x

### 7. Multi-Tenancy
- Payload field for tenant ID + filter on every query
- Or separate collections per tenant (simpler isolation, harder to manage)
- Isolate tenant data securely to ensure one tenant's data is never exposed to another

## Common Traps

- Ensure collection vector size matches the model, as mismatches cause all searches to return empty
- Include `wait=true` on insert if querying immediately to ensure data is indexed
- Set explicit limits when using scroll to prevent memory exhaustion on large collections
- Index payload fields used in filters to avoid full collection scans
- Place embeddings in the designated vector field rather than the payload

## State location

This skill is stateless locally. It connects to an external Qdrant instance (remote cluster or local Docker container) and does not store local configuration or state files within the repository.
