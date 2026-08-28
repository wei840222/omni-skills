# Core Rules

### 1. Always Verify Modules
Before using `text2vec-openai`, `generative-openai`, or rerankers, verify they're enabled:
```yaml
# docker-compose.yml
ENABLE_MODULES: 'text2vec-openai,generative-openai,reranker-cohere'
```

### 2. API Keys in Headers
```python
client = weaviate.connect_to_local(
    headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]}
)
```

### 3. Batch with Context Manager
```python
with client.batch.dynamic() as batch:
    for item in data:
        batch.add_object(properties=item, collection="Name")
```

### 4. Hybrid Search Alpha
- `alpha=0` → BM25 only (keyword)
- `alpha=1` → Vector only (semantic)
- `alpha=0.5-0.75` → Balanced (typical for RAG)

### 5. Apply Filters BEFORE Vector Search
Filters in `where` reduce the search space first — always filter before `near_text`/`near_vector`.

### 6. Named Vectors vs Single Vector
Choose one pattern per collection:
```python
# Single vector (simpler)
vectorizer_config=Configure.Vectorizer.text2vec_openai()

# Named vectors (multiple embeddings per object)
vector_config=[
    Configure.Vectors.text2vec_openai(name="content", source_properties=["body"]),
]
```

### 7. Debug Empty Results
Check in order: schema exists → vectorizer ran → distance threshold → filter syntax.
Use `_additional { vector }` to verify vectors were generated.

## State location

This skill is stateless and does not store local configuration or database files within the repository. The Weaviate server handles all state.
