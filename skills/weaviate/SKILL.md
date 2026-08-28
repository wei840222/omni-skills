---
name: weaviate
description: Build vector search with Weaviate using v4 syntax, proper module configuration, and production-ready patterns.
metadata:
  openclaw: '{"emoji":"🔷","os":["linux","darwin","win32"],"displayName":"Weaviate","requires":null}'
---

## Standard: v4 Syntax (Dec 2024+)

Always use v4 syntax. Before generating Weaviate code, ensure you apply the v4 patterns:

1. **Verify client version** — must be `weaviate-client>=4.0`
2. **Use context managers** — `with weaviate.connect_to_*() as client:` or explicit `client.close()`
3. **New imports** — `from weaviate.classes.config import Configure, Property`

When migrating legacy patterns (like `weaviate.Client()`, `client.schema.create_class()`, `path=[...]` filters), rewrite them using the modern v4 API equivalents.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| v3→v4 migration table | `references/v4-syntax.md` | Load when migrating legacy Weaviate code or encountering v3 syntax. |
| Module configuration | `references/modules.md` | Load when configuring vectorizers, generative models, or rerankers. |
| Batch, hybrid, HNSW | `references/operations.md` | Load for batch imports, hybrid search tuning, or index optimization. |
| Weaviate v4 Concepts | `references/weaviate-v4-concepts.md` | Load for general architecture and concepts of Weaviate. |
| Core Rules | `references/core-rules.md` | Load before generating any Weaviate API calls to ensure proper patterns. |
| Domain knowledge + sources | `references/domain-knowledge.md` | Load for Gate 6 research notes and verified docs URLs. |

## v4 Syntax Essentials

```python
# Connection (ALWAYS close)
with weaviate.connect_to_local() as client:
    # Collections (not classes)
    collection = client.collections.get("Article")
    
    # Queries
    response = collection.query.hybrid("search term", alpha=0.7)
    
    # Vector access
    vector = obj.vector["default"]  # Dict, not List
    
    # Filters
    Filter.by_property("category").equal("tech")
```

## Scope

This skill covers:
- Schema design for RAG and semantic search
- Vectorizer and reranker module configuration
- Batch imports with error handling
- Hybrid search tuning (alpha parameter)
- HNSW index configuration for scale
