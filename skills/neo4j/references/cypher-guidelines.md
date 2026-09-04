# Cypher guidelines

## Gather the execution context

Before proposing a query, establish the Neo4j version, labels, relationship types and directions, relevant constraints or indexes, expected result size, and whether the caller intends a read or a mutation. Use parameters supplied by the caller rather than interpolating values into Cypher text.

For a mutation, show the affected labels, properties, and relationship types. Ask for explicit confirmation before running a destructive or high-volume operation; first use a bounded read query or `EXPLAIN` to verify the match set.

## Use `MERGE` with an intentional identity

`MERGE` matches the complete pattern that it is given. Define node identity first, then merge a relationship separately when the relationship is optional or has its own properties:

```cypher
MERGE (a:User {id: $source_id})
MERGE (b:User {id: $target_id})
MERGE (a)-[r:KNOWS]->(b)
ON CREATE SET r.created_at = datetime()
ON MATCH SET r.last_seen_at = datetime()
RETURN a, r, b
```

Back the identity properties used by `MERGE` with the appropriate uniqueness constraint where the data model requires uniqueness. Keep mutable properties out of the identity map so an update does not accidentally create a second node.

## Bound traversal and preserve path semantics

Use an explicit hop range for variable-length traversal. Begin at one hop unless including the start node is intentional:

```cypher
MATCH p = (a:User {name: $source})-[:KNOWS*1..5]-(b:User {name: $target})
WHERE none(rel IN relationships(p) WHERE rel.active = true)
RETURN p
```

Choose direction from the schema. An undirected match is useful only when either direction is semantically acceptable. Use `shortestPath()` when one path is sufficient; use `allShortestPaths()` only when all equally short paths are required and the expected search space is bounded.

## Inspect plans before scaling up

Run `EXPLAIN` to inspect the planned operators before executing an unfamiliar query. Use `PROFILE` only after the caller accepts executing the query, because it runs the query while collecting runtime statistics. Look for unintended `CartesianProduct` operators and label scans that indicate a missing selective predicate or index.

Keep patterns connected. If an intentional cross product is necessary, bound each input set with `WITH`, `ORDER BY`, `LIMIT`, or a selective predicate before combining it.

## Keep scope and null handling explicit

Only variables named by `WITH` continue into the next clause. Place pagination deliberately, for example:

```cypher
MATCH (n:Event)
WITH n
ORDER BY n.created_at DESC
SKIP $offset
LIMIT $limit
RETURN n
```

`OPTIONAL MATCH` can produce `null`. Place follow-up predicates so they preserve the intended rows, and use `COALESCE()` when a default value is part of the query contract. `count(nullable_value)` counts only non-null values.

## Batch mutations with observable limits

For large writes, start with a small bounded batch and monitor transaction duration, heap pressure, page-cache behavior, locks, and error rates. Use `UNWIND $rows AS row` with parameters for batch input. Where the deployed Neo4j version supports it, `CALL { ... } IN TRANSACTIONS OF <batch-size> ROWS` can partition a bulk operation; test it against the target version and data volume before production use.

If a batch fails, retain the input identifiers and rerun only the failed, idempotent subset after correcting the cause. For operations that cannot be safely retried, create a backup or an explicit rollback plan before execution.

## Sources

### Cypher language and query planning

- Neo4j Cypher Manual — https://neo4j.com/docs/cypher-manual/current/
- Neo4j Cypher Manual: `MERGE` — https://neo4j.com/docs/cypher-manual/current/clauses/merge/
- Neo4j Cypher Manual: execution plans — https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/execution-plans/

### Operations and performance

- Neo4j Operations Manual: performance recommendations — https://neo4j.com/docs/operations-manual/current/performance/
- Neo4j Operations Manual: batch import and `CALL { ... } IN TRANSACTIONS` — https://neo4j.com/docs/cypher-manual/current/subqueries/subqueries-in-transactions/
