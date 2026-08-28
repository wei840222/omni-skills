# Weaviate Domain Knowledge

## Product position

Weaviate is an open-source vector database that stores objects together with embeddings so agents can combine vector search with structured filters. Client v4 is the supported Python surface for new work: gRPC-backed ingestion/query paths and collection-oriented APIs replace the v3 `Client` / schema class model.

## Operational defaults

- Prefer `weaviate-client>=4.0` and `weaviate.connect_to_*()` with explicit close or a context manager.
- Enable only the modules you will call (`text2vec-*`, `generative-*`, rerankers) and pass provider API keys through request headers.
- Use dynamic batching for bulk imports; inspect failed objects instead of assuming silent success.
- Hybrid search `alpha` blends BM25 (`0`) and vector (`1`); `0.5–0.75` is a common RAG starting range.
- Apply property filters before `near_text` / `near_vector` so the candidate set shrinks first.
- Choose either a single default vectorizer or named vectors per collection; do not mix both patterns casually.

## Sources

- Weaviate docs — introduction: https://docs.weaviate.io/weaviate
- Weaviate docs — Python client: https://docs.weaviate.io/weaviate/client-libraries/python
- Weaviate docs — batch / import: https://docs.weaviate.io/weaviate/manage-objects/import
- Weaviate docs — hybrid search: https://docs.weaviate.io/weaviate/search/hybrid
- Weaviate docs — vector index concepts: https://docs.weaviate.io/weaviate/concepts/vector-index
- Weaviate docs — OpenAI embeddings module: https://docs.weaviate.io/weaviate/model-providers/openai/embeddings
- Weaviate docs — modules configuration: https://docs.weaviate.io/weaviate/configuration/modules
- weaviate-python-client repository: https://github.com/weaviate/weaviate-python-client
