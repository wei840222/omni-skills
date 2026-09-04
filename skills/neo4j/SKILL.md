---
name: neo4j
description: Write, review, and optimize Neo4j Cypher queries. Use when modeling graph data, using MERGE or variable-length paths, diagnosing query plans, or preparing safe batch graph updates; not for operating a non-Neo4j database.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🕸️","requires":{"anyBins":["cypher-shell","neo4j"]}}'
---

## Workflow

1. Identify the Neo4j version, graph schema, query intent, expected result size, and whether the work reads or mutates data.
2. Load [Cypher guidelines](references/cypher-guidelines.md) before drafting or reviewing Cypher.
3. Use parameters and a bounded read or `EXPLAIN` to validate the query shape. For a high-volume or destructive mutation, obtain explicit confirmation before execution.
4. Return the query with its assumptions, expected effect, and any plan or recovery checks the caller should perform.

## State location

This skill is stateless. It does not store local configuration or persistent user state.
