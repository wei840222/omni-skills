---
name: dynamodb
description: Design scalable DynamoDB tables, model access patterns, and avoid NoSQL bottlenecks. Use when choosing partition/sort keys, writing Query vs Scan logic, adding GSIs, planning capacity or TTL, implementing pagination, conditional writes, or transactions, or when hot partitions, throttling, or expensive scans appear. Not for general AWS account architecture (`aws`), object-storage workflows (`s3`), Terraform language mechanics (`terraform`), or Kubernetes manifests.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⚡","requires":{"anyBins":["aws"]}}'
  related-skills: '{"aws": "Broad AWS architecture, IAM, networking, and cost work beyond DynamoDB data modeling.", "s3": "Store large objects in S3 and keep only references or metadata keys in DynamoDB.", "terraform": "Author Terraform resources for DynamoDB tables and indexes after the access model is decided."}'
---

Use this skill to design DynamoDB data models, pick efficient access patterns, and prevent cost or latency failures before they reach production.

## State location

This skill is stateless. It does not create or require a local `<state_root>`. Keep skill resources under `references/`. Any AWS credentials, profiles, or temporary CLI output belong to the host environment or caller workspace—never hardcode absolute paths inside the skill package.

## When to Use

- Designing a new table or rewriting keys around real access patterns
- Choosing Query, GSI, sparse index, or single-table patterns instead of Scan
- Handling pagination, eventual consistency, conditional writes, batch ops, or transactions
- Diagnosing hot partitions, throttling, oversized items, or TTL surprises
- Not for whole-account AWS architecture (`aws`), S3 object workflows (`s3`), or Terraform syntax (`terraform`)

## Quick Reference

| Topic | File | Load when |
|-------|------|-----------|
| Key design & single-table patterns | `references/best-practices.md` | Partition/sort keys, hot partitions, entity prefixes |
| Query, GSI, pagination, consistency, writes | `references/operations.md` | Query vs Scan, GSI, batch, transactions, optimistic locking |
| TTL, capacity modes, hard limits | `references/limits-and-capacity.md` | On-demand vs provisioned, item size, throughput ceilings |

## Core Rules

1. Model every required access pattern before creating the table—keys cannot change later.
2. Prefer Query on partition key (+ optional sort key). Treat Scan as a last resort.
3. If callers need “filter by X”, add a GSI or sparse index; do not Scan + FilterExpression as the primary path.
4. Always paginate: loop on `LastEvaluatedKey` until absent. `Limit` caps evaluated items, not total matches.
5. Default reads are eventually consistent. Use `ConsistentRead` only when stale data is unacceptable and budget for 2x RCU.
6. Keep large blobs in S3; store references in DynamoDB. Item size hard limit is 400KB.
7. TTL uses Unix epoch **seconds**. Deletion is eventual background work—items may linger after expiry.
8. Treat `BatchWriteItem` as non-atomic; retry `UnprocessedItems`. Use `TransactWriteItems` only when all-or-nothing is required.

## Anti-Patterns

- Low-cardinality partition keys that create hot partitions
- Scan + FilterExpression as the default read path
- Assuming one Query/Scan call returns the full result set
- Conditional logic missing on overwrite-sensitive writes
- Putting multi-MB payloads in items instead of S3 references
- TTL values in milliseconds (silently ineffective)

## Failure Recovery

| Symptom | Likely cause | Recovery |
|---------|--------------|----------|
| `ProvisionedThroughputExceededException` | Hot key or undersized capacity | Back off/retry; spread keys; raise capacity or switch on-demand |
| Stale read after write | Eventual consistency / GSI lag | Consistent read on base table, short retry, or redesign read-after-write |
| `ConditionCheckFailedException` | Optimistic lock lost | Re-read, recompute, retry with fresh version |
| Partial batch write | Non-atomic batch | Retry only `UnprocessedItems` with exponential backoff |
| Item grows toward 400KB | Oversized attributes | Move bulk content to S3; keep metadata keys only |

## Sources

- [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Best practices for designing and using partition keys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)
- [Best practices for query and scan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html)
- [Global secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html)
- [Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html)
- [Service, account, and table quotas in Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)
