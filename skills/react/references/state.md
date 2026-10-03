# State: server, client, URL

## Decision tree

```
Is it from an API?
├─ YES → TanStack Query (not Redux, not Zustand, not Context)
└─ NO → Should it survive refresh / be shareable? → URL searchParams
    └─ NO → Shared across components?
        ├─ YES → Zustand (changes often) or Context (rarely changes)
        └─ NO → useState
```

## TanStack Query v5

- Default `staleTime` is 0: fresh mounts and window focus may refetch.
- Set `staleTime` per resource to the staleness users tolerate.
- Keep `gcTime` (default 5 minutes) ≥ `staleTime`.
- One query-key factory as the single source of truth.
- Mutations invalidate or update the keys they affect.
- Prefer Query over hand-rolled `useEffect` + `useState` fetch.

## Zustand v5

- Select slices: bare `useStore()` rerenders on every store write.
- Selectors that return new objects need `useShallow`.
- One store per concern; avoid a god-store.

## Context

- Memoize the value object; split state and dispatch contexts.
- Setter-only consumers should not rerender when state changes.
- Prefer Zustand when updates are frequent.

## URL state

Filters, tabs, and page numbers the user might bookmark or share belong in
searchParams, not only in `useState`.

## Optimistic UI

`useOptimistic` shows a pending value while an async update runs; when the
update fails, recover to the confirmed server/client state and surface the
error. Pair with Query mutation `onError` / rollback when the source of truth
is the cache.
