# Sources — Search Engine

Live-checked on 2026-10-19. Prefer these URLs over memorized product facts. Re-check before quoting version-specific field names, ranking defaults, or pricing.

## Agent Skills / packaging

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Agent Skills specification | https://agentskills.io/specification | HTTP 200 |
| Agent Skills llms.txt | https://agentskills.io/llms.txt | HTTP 200 |

## Lexical ranking foundations

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Okapi BM25 overview | https://en.wikipedia.org/wiki/Okapi_BM25 | HTTP 200 |
| Lucene BM25Similarity | https://lucene.apache.org/core/9_0_0/core/org/apache/lucene/search/similarities/BM25Similarity.html | HTTP 200 |

## Elasticsearch / OpenSearch

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Elasticsearch `dense_vector` field | https://www.elastic.co/guide/en/elasticsearch/reference/current/dense-vector.html | HTTP 200 |
| Elasticsearch Reciprocal Rank Fusion (RRF) | https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html | HTTP 200 |
| Elasticsearch Rank Eval API | https://www.elastic.co/guide/en/elasticsearch/reference/current/search-rank-eval.html | HTTP 200 |
| OpenSearch neural search | https://opensearch.org/docs/latest/search-plugins/neural-search/ | HTTP 200 |
| OpenSearch hybrid search | https://opensearch.org/docs/latest/search-plugins/searching-data/hybrid-search/ | HTTP 200 |

## Meilisearch

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Meilisearch vs Elasticsearch comparison | https://www.meilisearch.com/docs/resources/comparisons/elasticsearch | HTTP 200 |
| Meilisearch ranking rules | https://www.meilisearch.com/docs/capabilities/full_text_search/relevancy/ranking_rules | HTTP 200 |
| Meilisearch docs (legacy host still serves content) | https://docs.meilisearch.com/learn/core_concepts/relevancy.html | HTTP 200 |

## Vector / hybrid vendors and embeddings

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Pinecone hybrid search intro | https://www.pinecone.io/learn/hybrid-search-intro/ | HTTP 200 |
| Weaviate hybrid search | https://weaviate.io/developers/weaviate/search/hybrid | HTTP 200 |
| SentenceTransformers | https://www.sbert.net/ | HTTP 200 |
| OpenAI embeddings guide | https://platform.openai.com/docs/guides/embeddings | HTTP 200 |
| Cohere embeddings | https://docs.cohere.com/docs/embeddings | HTTP 200 |

## Unreachable from this runner

| Attempted source | Result | Handling |
|------------------|--------|----------|
| https://milvus.io/docs/hybrid_search_with_milvus.md | redirect loop / unreachable | Do not invent Milvus API details; re-check from another egress or omit vendor-specific claims. |

## Claim checklist

Before stating a product-specific fact in answers or PRs:

1. Open the matching URL above (or a newer official replacement).
2. Quote only what the live page supports (field names, fusion method, eval API).
3. If the page is unreachable, say so and keep guidance engine-agnostic.
