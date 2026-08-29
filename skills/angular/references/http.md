# HTTP Traps

- `HttpClient` Observables are cold — each `subscribe()` fires a new request; share with `shareReplay({ bufferSize: 1, refCount: true })` when reuse is intended
- An interceptor must call `next.handle(req)` — omitting it silently drops the request
- Interceptor order matters — the last registered interceptor is innermost; keep auth early in the chain
- Non-JSON bodies need an explicit `responseType` — default JSON parsing throws on HTML error pages
- `catchError` in an interceptor should rethrow or return a deliberate fallback Observable — swallowing errors hides failures downstream
- Cross-origin cookies need `withCredentials: true` plus matching CORS server config
- Immediate retry loops hammer the server — use bounded retry with delay/backoff
