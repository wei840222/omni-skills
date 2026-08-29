# Routing Traps

- `snapshot.params` stays frozen on same-component navigation — subscribe to `paramMap` / `queryParamMap`
- A guard that returns `false` leaves a blank navigation — return a `UrlTree` to redirect intentionally
- `canDeactivate` alone may miss browser back/refresh — add `beforeunload` when unsaved-work warnings are required
- `loadChildren` paths should stay relative to the route config — absolute paths can fail with an empty module
- Resolver errors block navigation — wrap recoverable failures in `catchError` and return a fallback
- Relative `navigate()` calls need `relativeTo` — omitting it navigates from the root
- Query params disappear on bare `navigate()` — pass `queryParamsHandling: 'preserve'` or re-supply them
