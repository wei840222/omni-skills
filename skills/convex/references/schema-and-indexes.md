# Convex Schema and Indexes

Use this file when defining or refactoring table and index design.

## Modeling Checklist

1. List core entities and invariants before coding.
2. Define tenant boundaries in each table early.
3. List uniqueness requirements and enforce them in a mutation using an appropriate indexed lookup plus a write within the same transaction; a schema index is not a SQL UNIQUE constraint.
4. Decide soft-delete behavior up front.
5. Map each user-visible feature (including admin and background queues) to an expected query path; inspect scanned-document limits and pagination.

## Index Design Heuristics

- List observed user-facing query paths and order indexes by their leading equality filters, next range field, and required sort; prioritize paths with measured document scans or latency risk.
- Prefer explicit index names that reveal intent and document which product paths rely on them.
- For a high-churn table, compare query benefit with write amplification before adding an index. Include an infrequent admin query only when its measured scan cost or operational criticality justifies the maintenance cost.

## Query Alignment Rules

- For selective production reads, use an index with equality filters in field order, then a range on the next field. Example: a `by_recipient_created` index on `[recipientId, createdAt]` supports `withIndex("by_recipient_created", q => q.eq("recipientId", actorId)).order("desc").paginate(opts)` for a recipient's recent notifications; confirm the installed SDK's pagination API. For a bounded scan, record the maximum expected table size, observed documents examined, and acceptable query latency; add an index if measured cost exceeds the application's limits.
- When production traces show repeated post-filtering discards or scanned-document growth, compare an aligned index against the documented size and latency limits; change the schema or index when those limits fail.
- Re-check index coverage after each product surface expansion.

## Migration-Safe Changes

- Additive changes first, removals later.
- Keep compatibility shims during rollout windows.
- Document old and new read/write paths before cleanup.

## Review Before Merge

- Which query becomes slower with this change?
- Which tenant boundary could be bypassed?
- Which retry path can now duplicate writes?
- Which dashboards or alerts must change?

### Common Traps
- Building schema from entities only, not query paths -> slow reads and rework.
- Adding indexes reactively during outages -> unstable rollout under pressure.
