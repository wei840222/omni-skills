# RxJS Traps

- `subscribe()` without cleanup leaks memory — prefer `async` pipe, `takeUntilDestroyed()`, or explicit teardown
- `takeUntilDestroyed()` must run in an injection context — call it during construction/field init, not later in arbitrary callbacks
- `switchMap` cancels in-flight work — use `mergeMap` / `concatMap` / `exhaustMap` when that cancellation is wrong
- `combineLatest` waits for every source to emit once — seed with `startWith(...)` when an initial value is required
- `shareReplay` without `refCount: true` can keep the source alive forever — pass `{ bufferSize: 1, refCount: true }` for view-scoped sharing
- `catchError` must return an Observable — returning a bare value throws
- `forkJoin` fails entirely when any source errors — wrap individual sources if partial results are acceptable
- `distinctUntilChanged` defaults to reference equality — pass a comparator for deep/object comparisons
