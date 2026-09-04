---
name: neo4j
description: Write, review, and optimize Neo4j Cypher queries. Use when modeling graph data, using MERGE or variable-length paths, diagnosing query plans, or preparing safe batch graph updates.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🕸️","requires":{"anyBins":["cypher-shell","neo4j"]}}'
---

## Quick reference

Load [Cypher guidelines](references/cypher-guidelines.md) before writing Cypher, reviewing a graph query, or advising on Neo4j performance. It covers parameterized query patterns, `MERGE`, path traversal, plan inspection, batching, and recovery checks.

## State location

This skill is stateless. It does not store local configuration or persistent user state.
