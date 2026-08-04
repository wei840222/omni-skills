---
name: software-architect
description: Apply software architecture principles to design system boundaries, analyze trade-offs, plan scalability, and evolve architectures. Use when designing component decomposition, evaluating build-vs-buy, reviewing data modeling choices, planning migrations, or advising on reliability patterns. Also use when the user asks about CAP/PACELC, CQRS, event sourcing, bounded contexts, or circuit breakers.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏗️"}'
---

# Software Architecture Rules

## How to Use This Skill

When the user asks an architecture question, follow this procedure:

### Step 1: Classify the Decision

Identify which category the question falls into:

| Category | Key Question | Section to Apply |
|---|---|---|
| Boundary | "How do we split this?" | System Boundaries |
| Trade-off | "Which option is better?" | Trade-off Analysis |
| Scalability | "Will this handle growth?" | Scalability |
| Data | "How do we model/store this?" | Data Architecture |
| Reliability | "What if something breaks?" | Reliability |
| Security | "How do we protect this?" | Security |
| Evolution | "How do we change this later?" | Evolution |

### Step 2: Gather Constraints

Before recommending, identify:
- Current scale (requests/day, data volume, team size)
- Growth trajectory (10× in how long?)
- Team structure (how many teams? do they align with proposed boundaries?)
- Reversibility (can we change this decision later without rewriting everything?)

### Step 3: Present Options with Trade-offs

For each viable option, state:
1. What you gain
2. What you give up
3. When this option breaks down (the scaling limit, the complexity threshold)

### Step 4: 🔴 CHECKPOINT — Validate Before Finalizing

Before presenting the recommendation, verify:
- [ ] At least 2 alternatives were considered with explicit trade-offs
- [ ] The #1 risk was identified with a concrete mitigation
- [ ] The decision's reversibility was assessed — if irreversible, an ADR is required
- [ ] The recommendation matches the team's current scale, not their hypothetical future scale

### Step 5: Document

Write an ADR with: title, date, status, context, decision, consequences, alternatives considered. Store in `docs/adr/`.

## Design Principles

- Simple until proven insufficient — complexity is a cost, not a feature
- Separate what changes from what stays stable — boundaries at change boundaries
- Design for the next 10x, not 100x — over-engineering wastes resources
- Make decisions reversible when possible — defer irreversible ones until necessary
- Constraints clarify design — embrace limitations and let them guide early decisions
- Prefer explicit dependencies over hidden magic — implicit coupling causes surprise failures

## System Boundaries

- Define clear interfaces between components — contracts enable independent evolution
- Use bounded contexts from Domain-Driven Design to scope ownership — each context has its own model, terms, and boundaries; map relationships explicitly (context map)
- Boundaries where teams split — Conway's Law is real, design with it
- Data ownership at boundaries — one source of truth per entity, enforced by data contracts between services
- Async communication for loose coupling — sync calls create distributed monoliths
- Fail independently — one component's failure shouldn't cascade

### Gotchas

- **Split by domain capability** (not technical layer) — technical layers create one-directional dependencies and force coordinated deploys. Domain capabilities enable independent evolution.
- **Give each service its own datastore** — shared databases create implicit coupling. Share data via APIs or events to maintain independence.
- **Group by domain capability** (not by function) — single-endpoint services add network overhead without reducing complexity. Meaningful domain scope justifies service boundaries.

## Trade-off Analysis

- Every decision has costs — articulate what you're giving up
- **Distributed data consistency**: during a network partition, choose consistency (CP — refuse stale reads) or availability (AP — serve potentially stale data). Partition tolerance is not optional. PACELC extends this: even without partitions, you trade off latency vs consistency for every read. Map your datastores explicitly:
  - PA/EL (availability + low latency): DynamoDB, Cassandra, CouchDB
  - PC/EC (consistency always): PostgreSQL single-node, Redis (single-master)
  - PA/EC (availability during partition, consistency otherwise): MongoDB default, most SQL with replicas
- Performance vs maintainability — optimize hot paths, keep the rest readable
- Build vs buy — build differentiators, buy commodities; the "build" option must justify ongoing maintenance cost
- Document the "why not" for rejected alternatives — future you needs context

### Failure Recovery

When an architecture decision leads to problems, apply this recovery sequence:

1. **Identify the failure mode** — Is it a cascade failure, data inconsistency, performance degradation, or operational complexity?
2. **Apply the immediate fix** from the table below
3. **If the fix doesn't resolve within 1 sprint**, escalate to the fallback strategy
4. **Document the lesson** as an ADR to prevent recurrence

| Failure Mode | Immediate Fix | If Still Failing (Fallback) |
|---|---|---|
| Cascade failure (one service down takes others) | Add circuit breakers with 5s timeout, 30s half-open probe | Isolate with bulkhead pattern (separate thread pools per dependency) |
| Data inconsistency across services | Implement saga pattern with compensating transactions | Switch to event sourcing with eventual consistency + read model reconciliation |
| Performance bottleneck at database | Add read replicas + cache-aside with 5min TTL | Denormalize hot read paths; if write-bound, shard by tenant or entity ID |
| Deployment coupling (services must deploy together) | Introduce async messaging (Kafka/RabbitMQ) between services | Extract bounded contexts; give each service its own database |
| Unbounded queue growth | Add backpressure (rate limiter at producer, max queue depth) | Switch to pull-based consumption; add dead-letter queue for poison messages |

## Scalability

- Stateless services scale horizontally — state makes scaling hard
- Cache aggressively, invalidate carefully — use cache-aside, write-through, or write-behind with explicit TTL and invalidation strategy; stale cache bugs are the #1 source of "it works on my machine"
  - **Concrete defaults**: cache-aside TTL = 5min for read-heavy data, 30s for near-real-time; max cache size = 2× working set; eviction = LRU
- Database is usually the bottleneck — read replicas, sharding, or denormalization; choose sharding key carefully (hot shards are the #1 scaling failure)
  - **Sharding key selection**: pick a key with uniform distribution (tenant_id, user_id hash); verify with `SELECT shard_key, COUNT(*) GROUP BY 1 ORDER BY 2 DESC LIMIT 10` — if top shard > 3× median, re-key
- Queue work that can be async — deliver results immediately by deferring non-critical processing
- Scale for expected load, prepare for 3x spikes — headroom prevents outages
  - **Capacity rule**: provision for 2× peak; auto-scale trigger at 70% CPU or 80% connection pool; cooldown = 5min to prevent flapping
- Backpressure is architecture — every async boundary needs flow control; unbounded queues are unbounded memory
  - **Queue depth limit**: set max depth = 10× expected steady-state; reject with 503 above threshold; dead-letter after 3 poison-message retries

## Data Architecture

- Schema design constrains everything — get it right early, migrations are expensive
- Normalize for writes, denormalize for reads — optimize for access patterns
- Event sourcing when audit trail matters — reconstruct state from events; pair with snapshots for read performance
- CQRS when read/write patterns differ significantly — separate models for each; the write model enforces invariants, the read model optimizes queries
- Data gravity is real — processing moves to data, not vice versa
- Data contracts between services define schema ownership — producer-owned schemas with consumer notification on breaking changes; use schema registries for enforcement

### When to Use Event Sourcing

Use event sourcing when:
- You need a complete audit trail (financial, compliance, medical)
- State reconstruction from events is cheaper than maintaining complex update logic
- You want to replay events to debug or rebuild read models

Event sourcing fits poorly when:
- Simple CRUD with current-state-only access patterns
- Team lacks experience with event-driven thinking (eventual consistency surprises)
- You need random-access updates (e.g., "update field X in record Y" requires loading and replaying all events)

## Reliability

- Design for failure — everything fails eventually, handle it gracefully
- Timeouts on all external calls — hung connections cascade into outages; set timeouts based on SLOs, not defaults
- Circuit breakers prevent cascade failures — fail fast, recover gradually; use half-open state for gradual recovery (let one request through every N seconds to test if the dependency recovered)
- Idempotency for retries — duplicate messages shouldn't corrupt state; use idempotency keys or deduplication tokens
- Graceful degradation over total failure — partial functionality beats error pages
- Bulkhead pattern — isolate resource pools (thread pools, connections) so one slow dependency can't exhaust shared resources
- Chaos engineering validates reliability assumptions — inject failures in staging (or production with blast radius controls) to verify fallbacks actually work

### Failure Recovery Decision Table

| Symptom | First-line fix | If still failing |
|---|---|---|
| Cascade failure (one slow service brings down others) | Add circuit breaker: 5 failures → open for 30s → half-open (1 req/5s) | Add bulkhead: separate thread pools per dependency; set pool size = 2× expected concurrent calls |
| Intermittent timeouts on external API | Set timeout = p99 latency × 1.5 (measure first); add retry with exponential backoff (1s, 2s, 4s, max 3 retries) | Add idempotency key header; if API doesn't support idempotency, queue-and-replay with dedup |
| Database connection pool exhaustion | Check for connection leaks (unclosed connections); set max pool = expected QPS × avg query time × 2 | Add read replicas for read-heavy workloads; implement connection timeout = 5s |
| Memory growth / OOM under load | Profile heap; check for unbounded caches or event queues | Add backpressure: reject requests with 503 when queue depth > threshold; implement circuit breaker on queue size |
| Data inconsistency after partial failure | Add idempotency keys to all write operations; implement saga pattern for multi-service transactions | Add compensating transactions; implement event sourcing for full audit trail and replay capability |

## Security

- Zero Trust: verify every request explicitly, apply least privilege per call, assume breach at every layer — no implicit trust from network location alone (NIST SP 800-207)
- Defense in depth — multiple layers, no single point of failure
- Encrypt in transit and at rest — assume networks and disks are hostile; TLS 1.3 minimum; AES-256-GCM for data at rest
- Validate at boundaries — verify schema, type, range, and encoding for all external input; treat outside data as untrusted
  - **Concrete validation**: reject inputs > 1MB at API gateway; use allowlist schemas (JSON Schema / Protobuf); sanitize SQL with parameterized queries only — no string concatenation
- Secrets management from day one — use a secrets manager (Vault, AWS Secrets Manager); rotate automatically; store secrets only in the secrets manager, not in code or logs
  - **Rotation cadence**: API keys every 90 days; database credentials every 30 days; TLS certificates every 365 days (automated via cert-manager)
- mTLS between services — service identity via short-lived certificates (1h TTL), not shared secrets or API keys

## Observability

- Observability is an architectural concern, not an afterthought — design for it before you need it
- Three pillars: structured logs (with correlation IDs), metrics (RED for services: Rate, Errors, Duration; USE for infrastructure: Utilization, Saturation, Errors), distributed traces (end-to-end request flow)
  - **Concrete setup**: log format = JSON with fields `{timestamp, level, service, trace_id, span_id, message}`; metrics export every 10s; trace sampling = 1% for high-traffic, 100% for errors
- SLOs drive observability priorities — define service-level objectives first, then instrument what matters; without SLOs you're collecting data without knowing what's broken
  - **SLO template**: "99.9% of requests succeed (2xx/3xx) within 500ms over 30-day window" — error budget = 0.1% = 43 minutes downtime/month
- Alert on symptoms, not causes — alert on error budget burn rate and user-facing impact, not on CPU thresholds; cause-based alerts create noise
  - **Alert thresholds**: page on 50% error budget consumed in 1 hour; ticket on 25% consumed in 24 hours; no alert on CPU < 90%

## Evolution

- Design for replacement, not immortality — components will be rewritten
- Incremental migration over big bang — strangler fig pattern works; route traffic gradually from old to new
- Backwards compatibility for APIs — breaking changes break trust; use versioning (URL, header, or consumer-driven) and deprecation windows
- Feature flags decouple deploy from release — ship dark, enable gradually; separate deploy frequency from release cadence
- Monitor before, during, and after changes — data beats intuition; use canary deployments with automated rollback on SLO violation

## Documentation

- Document decisions with Architecture Decision Records (ADRs) — capture: title, date, status, context, decision, consequences, alternatives considered; store in `docs/adr/` alongside code
- Diagrams at multiple zoom levels — context (system + external actors), containers (deployable units), components (internal structure)
- Keep docs near code — separate wikis go stale; docs in the same repo get updated with the code
- Update docs when architecture changes — wrong docs are worse than none; make doc updates part of the PR checklist
- Document operational aspects — runbooks, SLOs, failure modes, on-call handbooks

## Communication

- Translate technical decisions to business impact — stakeholders need context
- Present options with trade-offs — explain the reasoning behind each recommendation, not just the recommendation itself
- Listen to operators — they know what breaks
- Involve security early — bolt-on security is weak security
- Decisions need buy-in — imposed architecture breeds resentment

## Common Anti-patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| Distributed monolith | Microservices that must all deploy together | Introduce async boundaries and data ownership |
| Shared database | Multiple services writing same tables | Give each service its own datastore; use APIs/events |
| Nano-services | Services so small they add overhead without reducing complexity | Group by domain capability, not technical layer |
| Premature microservices | Splitting before understanding domain boundaries | Start modular monolith; extract as boundaries clarify |
| Missing observability | Scaling service count without distributed tracing | Add tracing before adding services |
| Golden hammer | Applying one pattern to every problem | Match pattern to specific problem constraints |
