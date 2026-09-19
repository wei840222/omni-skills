# Async/Await Traps

- `.Result` or `.Wait()` blocks and can deadlock — especially on UI/ASP.NET sync context
- `async void` — only for event handlers, exceptions can't be caught
- `ConfigureAwait(false)` in library code — prevents deadlocks, loses sync context
- `Task.Run` vs `await` — `Task.Run` adds thread pool overhead, use specifically for CPU-bound work
- Fire-and-forget loses exceptions — at minimum log: `_ = DoAsync().ContinueWith(t => Log(t.Exception))`
- `await foreach` for async streams — iterate directly instead of calling `.ToListAsync()`
- `ValueTask` — can only await once, ensure it is awaited exactly once
- Cancellation token ignored — always pass and check `token.ThrowIfCancellationRequested()`
- `Task.WhenAll` vs `await` in loop — WhenAll runs parallel, loop is sequential
