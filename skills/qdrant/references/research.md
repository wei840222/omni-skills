# Qdrant Architecture & Best Practices

## Vector Database Core

Qdrant is an open-source, high-performance vector search engine/database written in Rust. It utilizes the Hierarchical Navigable Small World (HNSW) algorithm for Approximate Nearest Neighbor (ANN) search, making it highly suitable for AI applications requiring semantic similarity or recommendation systems based on dense vectors.

Primary docs:
- https://qdrant.tech/documentation/
- https://github.com/qdrant/qdrant

## Collections & Vectors

Collections store points with a fixed vector size and distance metric. Dimension mismatches produce empty search results rather than hard failures, so agents must verify embedding model output size before creating or querying a collection.

- Collections concepts: https://qdrant.tech/documentation/manage-data/collections/

## HNSW & Quantization

Qdrant's HNSW implementation supports precision/recall tradeoffs through parameters such as `m` and `ef_construct`. Product and scalar quantization reduce memory footprint for large high-dimensional datasets.

- Indexing: https://qdrant.tech/documentation/manage-data/indexing/
- Optimize / quantization: https://qdrant.tech/documentation/operations/optimize/

## Payload and Filtering

Unlike older nearest-neighbor libraries (for example raw FAISS), Qdrant treats metadata (payload) as a first-class citizen. It provides robust pre-filtering of vectors prior to distance computation. Pre-filtering explores the HNSW graph only across nodes matching the filters, avoiding post-filter exhaustion.

- Filtering: https://qdrant.tech/documentation/search/filtering/

## Distributed & Cloud

Qdrant supports clustering for high availability and distributed search, with built-in consensus and sharding logic. Local Docker or remote clusters are both valid targets; this skill remains stateless in the repository and does not store cluster credentials.

## Sources

- Qdrant documentation home — https://qdrant.tech/documentation/
- Collections — https://qdrant.tech/documentation/manage-data/collections/
- Indexing — https://qdrant.tech/documentation/manage-data/indexing/
- Filtering — https://qdrant.tech/documentation/search/filtering/
- Optimize — https://qdrant.tech/documentation/operations/optimize/
- Upstream repository — https://github.com/qdrant/qdrant
