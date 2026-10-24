# Official Sources & Vector Benchmarks

This document records the official documentation and benchmark sources for modern vector embedding models and similarity search architectures.

## Provider Specifications & Documentation

- **OpenAI Embeddings API**:
  - Documentation: [https://platform.openai.com/docs/guides/embeddings](https://platform.openai.com/docs/guides/embeddings)
  - Models: `text-embedding-3-small` (1536 dims), `text-embedding-3-large` (3072 dims).
  - Native dimension reduction: `dimensions` parameter supported via Matryoshka representation learning without losing semantic integrity. Note: legacy `text-embedding-ada-002` is superseded.
- **Cohere Embed v3**:
  - Documentation: [https://docs.cohere.com/docs/cohere-embed](https://docs.cohere.com/docs/cohere-embed)
  - Models: `embed-english-v3.0`, `embed-multilingual-v3.0` (1024 dims).
  - Compression support: Native int8 and binary embeddings for cost-effective vector index storage.
- **Voyage AI Embeddings**:
  - Documentation: [https://docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)
  - Specialized domain models for code (`voyage-code-3`), law, and finance.

## Empirical Evaluation Benchmarks

- **Massive Text Embedding Benchmark (MTEB) Leaderboard**:
  - Benchmark Portal: [https://huggingface.co/spaces/mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard)
  - Standardized evaluation across classification, clustering, pair classification, reranking, retrieval, semantic textual similarity (STS), and summarization.
