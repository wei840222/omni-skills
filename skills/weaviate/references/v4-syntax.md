# v3 → v4 Migration Reference

## Connection

```python
# Legacy v3
client = weaviate.Client("http://localhost:8080")

# Modern v4
client = weaviate.connect_to_local()  # localhost
client = weaviate.connect_to_weaviate_cloud(cluster_url, auth_credentials)
client = weaviate.connect_to_custom(http_host, http_port, grpc_host, grpc_port)

# Always close when done
client.close()

# Or use context manager (preferred)
with weaviate.connect_to_local() as client:
    ...
```

## Schema / Collections

```python
# Legacy v3
client.schema.create_class({"class": "Article", ...})
client.schema.get()

# Modern v4
client.collections.create("Article", properties=[...])
client.collections.list_all()
collection = client.collections.get("Article")
```

## Properties

```python
# Legacy v3
{"dataType": ["text"], "name": "title"}

# Modern v4
from weaviate.classes.config import Property, DataType
Property(name="title", data_type=DataType.TEXT)
```

## Queries

```python
# Legacy v3
client.query.get("Article").with_near_text({"concepts": ["AI"]}).with_limit(10).do()

# Modern v4
collection = client.collections.get("Article")
collection.query.near_text(query="AI", limit=10)
collection.query.hybrid(query="AI", alpha=0.7, limit=10)
collection.query.fetch_objects(limit=10)
```

## Filters

```python
# Legacy v3
Filter(path=["category"]).equal("tech")
Filter(path=["ref", "Author", "name"])

# Modern v4
from weaviate.classes.query import Filter
Filter.by_property("category").equal("tech")
Filter.by_ref("ref").by_property("name")
Filter.by_id().equal(uuid)
```

## Vector Access

```python
# Legacy v3
vector = obj.vector  # List[float]

# Modern v4
vector = obj.vector["default"]  # Dict[str, List[float]]
vector = obj.vector["my_named_vector"]  # For named vectors
```

## Batch Import

```python
# Legacy v3
client.batch.configure()
client.batch.add_data_object({...}, "ClassName")
client.batch.create_objects()

# Modern v4
with client.batch.dynamic() as batch:  # or .fixed_size() or .rate_limit()
    batch.add_object(properties={...}, collection="ClassName")
```

## Timestamps

```python
# Legacy v3
obj.metadata.creation_time_unix  # int (milliseconds)

# Modern v4
obj.metadata.creation_time  # datetime object
```

## Full Comparison Table

| Concept | Legacy v3 | Modern v4 |
|---------|-----------------|--------------|
| Connect | `weaviate.Client(url)` | `weaviate.connect_to_*()` |
| Close | Not required | `client.close()` required |
| Create collection | `client.schema.create_class()` | `client.collections.create()` |
| Get collection | `client.query.get("Class")` | `client.collections.get("Class")` |
| Query | `.with_near_text().do()` | `.query.near_text()` |
| Filter path | `path=["prop"]` | `Filter.by_property("prop")` |
| Vector | `obj.vector` | `obj.vector["default"]` |
| UUID | `obj.metadata.uuid` | `obj.uuid` |
| Vectorizer config | String in schema | `Configure.Vectorizer.*()` |
