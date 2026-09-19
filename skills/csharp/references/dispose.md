# Dispose Traps

- Missing `using` — resource leak for files, connections, streams
- `using` with null — throws, use `using var x = maybeNull;` (C# 8+ handles null)
- `Dispose()` not called on exception — `using` or try/finally required
- Finalizer runs on GC thread — restrict access to unmanaged resources only
- `IAsyncDisposable` — use `await using` for async cleanup
- Double dispose — should be safe (no-op), but some implementations throw
- Dispose in constructor failure — if constructor throws, Dispose not called
- `HttpClient` — reuse a single instance per application or use `IHttpClientFactory`
