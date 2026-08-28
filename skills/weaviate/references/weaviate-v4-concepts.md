# Weaviate v4 Concepts

Weaviate is an open-source vector database designed for scalable vector search, AI, and machine learning applications.

- **Architecture**: Weaviate stores both objects and vectors, allowing for combining vector search with structured filtering.
- **Client v4**: The v4 Python client leverages gRPC for faster data ingestion and querying, and introduces a more Pythonic, object-oriented API compared to v3.
- **Collections**: Data in Weaviate v4 is organized into Collections, which define the schema, vectorizer, and indexing configuration for the objects they contain.
- **Hybrid Search**: Weaviate supports hybrid search, allowing you to combine keyword-based search (BM25) with vector search to improve recall and precision.
