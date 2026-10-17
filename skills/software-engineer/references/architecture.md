# Architecture Decisions — Software Engineer

## Layer Boundaries

```
┌─────────────────────────────────────┐
│  Handlers / Controllers / Routes    │  ← HTTP parsing, validation
├─────────────────────────────────────┤
│  Services / Use Cases / Domain      │  ← Business logic, orchestration
├─────────────────────────────────────┤
│  Repositories / Adapters / Gateways │  ← Data access, external APIs
├─────────────────────────────────────┤
│  Infrastructure / Config            │  ← DB connections, env vars
└─────────────────────────────────────┘
```

### What Lives Where

| Layer | Allowed | Out of Scope |
|-------|---------|-----------|
| Handler | Parse request, validate schema, call service | SQL, business rules |
| Service | Business logic, coordinate repos | HTTP details, raw SQL |
| Repository | Data access, query building | Business decisions |
| Infrastructure | Connections, configs | Business logic |

## When to Abstract

**Create abstraction when:**
- You have 3+ concrete implementations
- You need to swap implementations (testing, different environments)
- The boundary naturally exists (external API, database)

**Defer abstraction when:**
- You have 1 concrete case
- "Maybe we'll need this later"
- To follow a pattern for pattern's sake

## Dependency Direction

```
Domain ← Application ← Infrastructure
         ↑
      Ensure one-way flow
```

Domain/core should have no dependencies on infrastructure. Use interfaces/ports.

## Configuration Strategy

**Environment-based:**
```
.env.development    # Local defaults
.env.production     # Production values (exclude from commits)
.env.example        # Template with dummy values (committed)
```

**Access pattern:**
```typescript
const config = {
  db: {
    host: env.DB_HOST || 'localhost',
    port: parseInt(env.DB_PORT || '5432'),
  }
};
```

Abstract `process.env` access throughout codebase — centralize in config.

## Database Decisions

| Scale | Recommendation |
|-------|----------------|
| <10K rows, single writer | SQLite |
| <1M rows, moderate concurrency | PostgreSQL |
| High read, eventual consistency OK | Add Redis cache |
| >1M rows, complex queries | PostgreSQL + read replicas |

**Migration rules:**
- Always reversible (up + down)
- Verify backups before destructive actions
- Small, incremental changes
- Test on production copy first

## API Design

**RESTful conventions:**
```
GET    /users          # List
GET    /users/:id      # Get one
POST   /users          # Create
PUT    /users/:id      # Replace
PATCH  /users/:id      # Update
DELETE /users/:id      # Remove
```

**Response structure:**
```json
{
  "data": { ... },
  "meta": { "page": 1, "total": 100 },
  "error": null
}
```

Or on error:
```json
{
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "field": "email"
  }
}
```

## Scaling Checkpoints

| Symptom | First Action |
|---------|--------------|
| Slow reads | Add index, check query plans |
| High latency | Add caching layer |
| CPU bound | Profile, optimize hot paths |
| Memory pressure | Check for leaks, reduce in-memory data |
| Single point of failure | Add health checks, basic redundancy |

**Defer until necessary:**
- Add microservices (monolith is fine for a long time)
- Add Kubernetes (Docker Compose works to 100K users)
- Add message queues (sync is fine until proven otherwise)


## Industry Standard References

- **The Twelve-Factor App**: Methodology for building software-as-a-service apps. Source: [https://12factor.net/](https://12factor.net/)
- **OWASP Top 10**: Standard awareness document for developers and web application security. Source: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
