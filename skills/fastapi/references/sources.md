# FastAPI Domain Knowledge and Sources

## Claim inventory and freshness

| Topic | Freshness | Source of truth | Refactor outcome |
| --- | --- | --- | --- |
| Concurrency model / `def` vs `async def` | Stable domain | FastAPI concurrency docs | Retained core rule 1–2; blocking work stays off the event loop. |
| Dependencies, caching, lifespan | Version-sensitive | FastAPI dependencies + events docs | Lifespan owns process singletons; per-request `Depends` cache retained. |
| Pydantic v2 migration names | Version-sensitive | Pydantic migration guide | Kept v1→v2 rename traps (`model_dump`, `from_attributes`, settings package). |
| Async SQLAlchemy session pitfalls | Version-sensitive | SQLAlchemy asyncio extension | Kept `MissingGreenlet`, one-session-per-task, and pool sizing guidance. |
| Async tests with httpx | Version-sensitive | FastAPI async tests docs | Prefer `httpx.AsyncClient` + ASGI transport over sync-only assumptions. |
| Workers / multi-process deployment | Stable domain | FastAPI server workers + Uvicorn | Reload vs workers split; pool math uses workers × pool. |
| Middleware / CORS order | Stable domain | FastAPI middleware + CORS tutorial | Last registered middleware is outermost; CORS last so errors keep headers. |

## Verified sources

### FastAPI (official)

- **Concurrency and async / await** — documents why blocking calls inside `async def` stall the worker and when to use plain `def`. <https://fastapi.tiangolo.com/async/>
- **Dependencies** — documents `Depends`, sub-dependencies, and per-request caching behavior. <https://fastapi.tiangolo.com/tutorial/dependencies/>
- **Lifespan events** — documents the lifespan context manager replacing startup/shutdown event decorators. <https://fastapi.tiangolo.com/advanced/events/>
- **Bigger applications** — routers, structure, and dependency placement for multi-file apps. <https://fastapi.tiangolo.com/tutorial/bigger-applications/>
- **Middleware** — registration order and pure ASGI considerations. <https://fastapi.tiangolo.com/advanced/middleware/>
- **CORS** — `CORSMiddleware` usage and browser-visible failure modes. <https://fastapi.tiangolo.com/tutorial/cors/>
- **Testing** — TestClient basics. <https://fastapi.tiangolo.com/tutorial/testing/>
- **Async tests** — httpx async client patterns for ASGI apps. <https://fastapi.tiangolo.com/advanced/async-tests/>
- **Testing dependencies** — dependency overrides for isolation. <https://fastapi.tiangolo.com/advanced/testing-dependencies/>
- **Server workers** — multi-worker process model implications. <https://fastapi.tiangolo.com/deployment/server-workers/>
- **FastAPI reference** — framework surface used by routing and response-model guidance. <https://fastapi.tiangolo.com/reference/fastapi/>

### Pydantic

- **Migration guide** — v1→v2 renames and behavior changes (`model_dump`, validators, `orm_mode` → `from_attributes`). <https://docs.pydantic.dev/latest/migration/>
- **Models** — model configuration and validation edge cases. <https://docs.pydantic.dev/latest/concepts/models/>

### SQLAlchemy / runtime

- **Asyncio extension** — async session/engine patterns and greenlet constraints behind `MissingGreenlet`. <https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html>
- **AnyIO** — shared thread limiter context for `def` endpoints under async servers. <https://anyio.readthedocs.io/en/stable/>
- **Uvicorn** — ASGI server process model and worker notes. <https://uvicorn.dev/>
- **Uvicorn source** — canonical project repository when docs.site DNS is unavailable. <https://github.com/encode/uvicorn>

### Agent Skills format

- **Agent Skills specification** — frontmatter, progressive disclosure, and resource layout used by this package. <https://agentskills.io/specification>

## Update notes

- Operational rules in `SKILL.md` and topic files preserve the pre-refactor FastAPI diagnostic intent; paths now use `references/`.
- Version floors remain gates, not substitutes for reading the installed package versions.
- Do not invent live pricing, vendor SLAs, or uncited benchmark percentages in this skill.
