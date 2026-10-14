---
name: fastapi
description: >
  Build, debug, and harden FastAPI services: async endpoints, Pydantic models,
  dependency injection, auth, SQLAlchemy sessions, tests, and deployment. Use when
  writing or reviewing a FastAPI app, router, or schema; when routes hang because a
  sync call blocks the event loop; when a request returns 422, a POST becomes 307,
  or a 500 arrives without CORS headers; when migrating Pydantic v1→v2; when
  Depends/yield/lifespan misbehave; when SQLAlchemy raises QueuePool limit or
  MissingGreenlet; when TestClient/httpx AsyncClient tests close the loop; or when
  uvicorn/gunicorn workers, root_path, WebSockets, SSE, or OpenAPI docs misbehave.
  Not for Django, Flask, or plain Python — prefer django, flask, or py.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⚡","requires":{"bins":["python3"]}}'
  related-skills: '{"django":"Full Django stack, ORM, admin, and templates when the service is not async-first FastAPI.","flask":"WSGI Flask apps, blueprints, and application context instead of FastAPI.","py":"Plain Python packaging, typing, asyncio primitives, and pytest outside FastAPI-specific behavior.","pg":"PostgreSQL plans, indexes, vacuum, locks, and server connection limits below the FastAPI/SQLAlchemy layer.","auth":"Protocol-level OAuth, OIDC, MFA, and passwordless design beyond FastAPI dependency wiring.","rest-api":"Framework-independent API contracts, versioning, and error shapes.","docker":"Container images, process model, and runtime packaging for the FastAPI service.","http":"Protocol-level HTTP status, headers, and caching independent of FastAPI."}'
---

# FastAPI

Ship **async-safe FastAPI services**: honest `def` vs `async def`, request/response
models at the edge, dependencies and lifespan that own resources, pools sized to
the database, and tests that exercise the real ASGI path.

This skill is **stateless by default** for one-shot design and debug coaching.
Optional preference notes may live under a resolved `<state_root>` only when the
user wants continuity. Never store secrets, tokens, connection strings, or live
customer payloads in the skill package.

## State location

User preferences may exist in `<workspace>/fastapi/`,
`<workspace>/memory/fastapi/`, or `~/fastapi/`. Before reading or writing state,
resolve `<state_root>`:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/fastapi/`, `<workspace>/memory/fastapi/`, `~/fastapi/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/fastapi/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/fastapi/` only;
   otherwise ask for a state root before creating data.
6. If older data exists only under `~/clawic/fastapi/` or
   `~/Clawic/data/fastapi/`, move it into the resolved `<state_root>/` after the
   user confirms, and say in one line that you moved it and from where.

Use the selected `<state_root>` for every state operation in this skill.
Typical layout (create children only when needed):

- `<state_root>/config.yaml` — stated preferences (stack choices, not secrets)
- `<state_root>/notes.md` — optional project-specific traps (no live credentials)

## When to use

- Writing or reviewing FastAPI routers, dependencies, request/response models, middleware
- Diagnosing latency and stalls: one blocking call, exhausted pool, saturated threadpool
- Modelling data at the edge: 422 bodies, serialization, ORM objects, Pydantic v1→v2
- Wiring auth, settings, database sessions, and background work into the dependency graph
- Production: workers, proxies, shutdown, health checks, logging, body/upload limits
- Tests that hang, pass wrongly, or die with a closed event loop

Prefer `django` for Django ORM/admin/templates. Prefer `flask` for WSGI Flask.
Prefer `py` for plain Python. Prefer `pg` once the question is PostgreSQL engine
tuning. Prefer `auth` for protocol-level identity design beyond FastAPI wiring.
Prefer `rest-api` for framework-independent API contracts.

Load deeper notes only on demand from the Quick reference table; do not preload every `references/` file.

## Quick reference

| Situation | Play |
| --- | --- |
| Every route slow at once, health check included | Blocking call inside `async def`, or threadpool full → `references/async.md` |
| Choosing `def` vs `async def` | Any blocking body → `def`; all-await → `async def` → `references/async.md` |
| CPU / image / big parse in a request | Off the loop and off the threadpool: process pool or queue → `references/async.md` |
| 422 on a request that looks correct | Read `loc`: alias, nesting, nullable without default → `references/pydantic.md` |
| `.dict()` / `parse_obj` / `@validator` / `orm_mode` broken | Pydantic v2 renames → `references/pydantic.md` |
| ORM instance will not serialize | `from_attributes` + response model → `references/pydantic.md` |
| `Depends` runs more/fewer times than expected | Per-request cache, `use_cache=False`, lifespan singletons → `references/dependencies.md` |
| Current user, scopes, tokens, password hashing | `references/auth.md` |
| `/users/me` hits `{user_id}`; 307 on POST | Declaration order and trailing slashes → `references/routing.md` |
| Layout, circular imports, app factory | `references/structure.md` |
| Env ignored, secrets misplaced | `references/settings.md` |
| Sessions, pools, N+1, MissingGreenlet | `references/database.md` |
| Error body shape, custom handlers | `references/errors.md` |
| CORS missing, middleware order, body read twice | `references/middleware.md` |
| Dependency overrides, lifespan, async client | `references/testing.md` |
| Workers, gunicorn vs uvicorn, `root_path`, shutdown | `references/deployment.md` |
| Slow under load with healthy loop | Serialization, caching, pagination → `references/performance.md` |
| Large upload/download, SSE, streaming JSON | `references/streaming.md` |
| WebSocket drops / multi-worker broadcast | `references/websockets.md` |
| Work after the response | `BackgroundTasks` vs real queue → `references/background.md` |
| OpenAPI / clients / operation ids | `references/openapi.md` |
| Logs, health vs readiness, metrics | `references/observability.md` |
| Ownership, mass assignment, SSRF, path traversal | `references/security.md` |
| Jinja2 / forms / HTMX / static | `references/templates.md` |
| Version-sensitive claim needs a source | `references/sources.md` |
| Anything else | One-file minimal repro: one route, no middleware, no DB — then add layers |

Read this file first; open **exactly one** reference when the situation matches.

## Core rules

1. **`async def` obliges the whole chain to await.** One blocking call inside an async endpoint (`psycopg2`, `requests`, `time.sleep`, large sync I/O) freezes every concurrent request on that worker. If any step blocks and cannot be replaced, declare the endpoint `def` and let Starlette move it to the threadpool.
2. **The threadpool has a finite default.** Every `def` endpoint and `def` dependency shares AnyIO's default limiter (commonly 40 threads per process). Concurrency budget ≈ `limit × workers`; raise limits only after measuring.
3. **Dependencies cache per request; singletons live in lifespan.** `Depends(get_x)` used three times runs once per request. DB engines, HTTP clients, and cache clients are created in the lifespan handler and stored on `app.state`.
4. **Validate at the edge, twice.** Request model in, response model out, plain objects in between. `response_model` re-validates returns; skip only on a profiled hot path with an explicit `Response`.
5. **Size the pool against the database, not the app.** SQLAlchemy defaults (`pool_size=5`, `max_overflow=10`) are per process. Total ≈ `workers × (pool_size + max_overflow)` must fit the DB `max_connections` with headroom for admin/migrations.
6. **One event loop and one memory space per worker.** Lifespan runs once per worker. Shared state across requests goes to Redis or the database — a module-level dict is a per-process cache.
7. **Every outbound call carries a timeout.** `httpx.AsyncClient(timeout=...)`, DB statement timeouts, lock bounds. Without one, a hung upstream becomes an unbounded pending queue.
8. **Raise errors; do not return them from helpers.** `raise HTTPException(...)` goes through handlers; a bare `JSONResponse` from a service skips handlers and response-model checks.
9. **Middleware order is the reverse of registration.** Last `add_middleware` is outermost. Register CORS last so 500s still carry CORS headers; prefer handlers that return errors rather than uncaught escapes.

## Version floors

| Feature | Needs |
| --- | --- |
| Return-type annotation as response model | fastapi >= 0.89 |
| `lifespan` context manager (replaces `@app.on_event`) | fastapi >= 0.93 |
| `Annotated[X, Depends(...)]` | fastapi >= 0.95 |
| Pydantic v2 models / `model_config` | fastapi >= 0.100 |
| `yield` dependency resources unusable inside `BackgroundTasks` | fastapi >= 0.106 |
| `fastapi dev` / `fastapi run` (`fastapi[standard]`) | fastapi >= 0.111 |
| `BaseSettings` in `pydantic-settings` | pydantic >= 2.0 |
| `asyncio.TaskGroup` / `asyncio.timeout` | python >= 3.11 |

Confirm the installed FastAPI/Pydantic versions before applying a version-gated fix. Sources: `references/sources.md`.

## Error signatures

| Signature | Cause | Go to |
| --- | --- | --- |
| 422 with `"loc": ["body", ...]` | Body/model mismatch; nullable field required in v2 | `references/pydantic.md` |
| 307 on POST | Trailing-slash mismatch; bad proxy scheme headers | `references/routing.md` |
| 500 in browser with no CORS headers | Exception escaped above `CORSMiddleware` | `references/middleware.md` |
| `QueuePool limit of size 5 overflow 10 reached` | Sessions not closed, or pool × workers too large | `references/database.md` |
| `MissingGreenlet` / `greenlet_spawn has not been called` | Lazy relationship access outside await (async SQLAlchemy) | `references/database.md` |
| `asyncpg ... another operation is in progress` | One connection/session shared across concurrent tasks | `references/database.md` |
| `RuntimeError: Event loop is closed` in tests | Session-scoped async fixture on function-scoped loop | `references/testing.md` |
| `FastAPIError: Invalid args for response field` | Non-Pydantic type used as `response_model` | `references/pydantic.md` |
| Endpoint hangs waiting for body | Middleware consumed the request stream | `references/middleware.md` |
| SSE arrives only at the end | Proxy buffering | `references/streaming.md` |
| WebSocket 1006, never 1000 | Proxy idle timeout or worker restart | `references/websockets.md` |
| Everything 200 but clients time out | Blocked loop or full threadpool | `references/async.md` |

## Output gates

Before delivering FastAPI code, verify:

- No blocking call on an `async def` path; blocking work uses `def`, `run_in_threadpool`, or a queue
- Every outbound HTTP, DB, and lock call has an explicit timeout
- Request and response models declared; ORM objects cross the boundary only via `from_attributes` models
- `workers × (pool_size + max_overflow)` fits the database connection limit
- Configuration and secrets come from the settings object, not scattered `os.getenv`
- Auth on business routers; health/readiness/metrics stay unauthenticated
- Reads/writes filter by owner or tenant inside the query
- Errors raised as `HTTPException` with a consistent body; no stack/SQL/upstream payload in `detail`
- Request and upload sizes bounded (proxy or middleware)
- Tests override dependencies instead of patching, and run inside lifespan

## Configuration preferences

Defaults apply until the user states a preference. Store preferences in
`<state_root>/config.yaml` only when continuity is requested. Record a preference
the moment it is stated — do not interview first.

| Variable | Type | Default | Effect |
| --- | --- | --- | --- |
| pydantic_version | 1 \| 2 | 2 | API names: `model_dump` vs `.dict()`, validators, settings package → `references/pydantic.md` |
| db_stack | sqlalchemy-async \| sqlalchemy-sync \| sqlmodel \| tortoise \| none | sqlalchemy-async | Session/engine pattern → `references/database.md` |
| server_stack | uvicorn \| gunicorn-uvicorn \| hypercorn | uvicorn | Process model → `references/deployment.md` |
| auth_scheme | jwt \| session-cookie \| oauth2-provider \| api-key \| none | jwt | Current-user dependency → `references/auth.md` |
| min_fastapi | version text | 0.111 | Gates Version floors features |
| deploy_target | container \| vm \| serverless \| unknown | container | Workers, health, shutdown → `references/deployment.md`, `references/observability.md` |
| error_envelope | bare \| enveloped | bare | Error body shape → `references/errors.md` |
| task_backend | background-tasks \| celery \| arq \| rq \| dramatiq | background-tasks | After-response work → `references/background.md` |
| test_client | async-httpx \| testclient | async-httpx | Test transport → `references/testing.md` |
| json_renderer | default \| orjson | default | Response class → `references/performance.md` |
| render_mode | json \| html-htmx \| both | json | JSON vs templates → `references/templates.md` |

Also record, when stated: package manager, naming conventions, reverse proxy,
Python version, banned libraries (e.g. `requests` vs `httpx`), and whether the
user wants whole-file vs minimal-diff output.

## Traps

| Trap | Why it fails | Do instead |
| --- | --- | --- |
| `requests.get()` inside `async def` | Blocks the loop for the full RTT | `httpx.AsyncClient` from lifespan, or endpoint `def` → `references/async.md` |
| `@app.on_event("startup")` | Deprecated; weak resource lifecycle | `lifespan` async context manager → `references/structure.md` |
| Module-level `cache = {}` as app cache | One copy per worker | Redis, or accept per-process caching → `references/performance.md` |
| Auth dependency on every router including probes | Orchestrator restarts healthy pods | Auth only on business routers → `references/observability.md` |
| `Optional[str]` without default | Pydantic v2: required-and-nullable | `= None` → `references/pydantic.md` |
| `await request.body()` in middleware then endpoint | Receive channel exhausted | Replay middleware or read only in endpoint → `references/middleware.md` |
| `BackgroundTasks` for durable work | Lost on crash/deploy after 200 | Queue with retries → `references/background.md` |
| `uvicorn --reload --workers 4` | Reload forces single process | Reload in dev, workers in prod → `references/deployment.md` |
| `TestClient` for async concurrency bugs | Sync portal hides loop/cancellation issues | `httpx.AsyncClient` + `ASGITransport` → `references/testing.md` |
| Returning raw ORM objects | Lazy load after session close | Eager load + response model → `references/database.md` |
| Secrets in `HTTPException(detail=...)` | Detail is client JSON | Generic message out; full context in logs → `references/errors.md` |

## Where experts disagree

- **Async everywhere vs honest `def`.** All-await stack → `async def`; any blocking library in the chain → `def` is safer (damage bounded by the threadpool).
- **ORM vs raw SQL vs SQLModel.** One shape serving one API → SQLModel can work; separate read/write shapes or older schema → SQLAlchemy + explicit response models.
- **Service layer.** Pays off at the second caller (HTTP + worker + CLI); below that it is often indirection.
- **Bare errors vs envelope.** Public/generated clients → bare status + problem details; single legacy front end → one declared envelope applied everywhere.

## Fast path

1. Match the symptom to Quick reference / Error signatures and open one file.
2. Check installed FastAPI, Pydantic, and driver versions against Version floors and `references/sources.md`.
3. Prefer a one-file repro before changing production layout.
4. Apply Output gates before shipping the change.
