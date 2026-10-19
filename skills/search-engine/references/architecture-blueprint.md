# Architecture Blueprint — Search Engine

Use this file when choosing or reviewing system architecture.

## Core Components

1. Source connectors
- pull content from trusted systems
- assign source identifiers and timestamps

2. Processing pipeline
- normalize fields and clean noisy content
- split long documents with stable chunk ids

3. Index layer
- maintain primary retrieval index and optional fallback index
- keep schema version and transform version explicit

4. Query service
- parse intent and map to retrieval strategy
- apply filters, faceting, and ranking policy

5. Result composer
- merge retrieval output into user-facing response objects
- include trace metadata for debugging

## Architecture Choices by Scale

| Scale Pattern | Recommended Approach | Main Risk |
|---------------|----------------------|-----------|
| Small corpus, low QPS | Single index service, simple lexical retrieval | Premature complexity |
| Mid corpus, mixed query types | Hybrid retrieval with light reranking | Unclear policy boundaries |
| Large corpus, strict latency | Tiered indexes and async refresh paths | Operational overhead |

## Schema Rules

- define required fields and type contracts before indexing
- separate fields for retrieval, filtering, and display
- prevent silent schema drift with validation gates
- version schema updates and include migration path

## Operational Baseline

- every index job emits run id, duration, and error counts
- every query path reports latency by stage
- every release includes rollback instructions

## Vector Search and Hybrid Retrieval

When implementing semantic search or RAG-capable retrieval:

- Prefer dense-vector fields inside the primary search store when operations want one cluster; use a dedicated vector store when isolation, specialized ANN, or multi-tenancy demands it. Verify field types against current vendor docs (for example Elasticsearch `dense_vector`).
- Choose embeddings models for the domain vocabulary and language mix; do not treat a model name as portable without a live docs check.
- For hybrid lexical + vector retrieval, combine BM25-style candidates with kNN via Reciprocal Rank Fusion (RRF) or an explicitly versioned learned weight, then measure with the offline suite in `evaluation-metrics.md` before production writes.
- Keep embedding model id, dimension, similarity metric, and index schema version in the retrieval-contract notes under `<state_root>/`.
