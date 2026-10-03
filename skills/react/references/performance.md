# Performance workflow

Measure before changing code (React Profiler / framework analyzer).

| Priority | Technique | When |
|----------|-----------|------|
| P0 | Route-based code splitting (`lazy` + Suspense) | Users pay only for the route they visit |
| P0 | Parallel data loading (`Promise.all`, prefetch) | 2+ independent fetches — waterfalls dominate |
| P1 | Virtualize long lists | Thousands of rows or heavy row trees — DOM nodes cost |
| P1 | `useDeferredValue` / `startTransition` | Typing/dragging jank from heavy subtree updates |
| P2 | `memo` / `useMemo` / `useCallback` | Only without React Compiler, after Profiler proof |

## Compiler

- Compiler **on**: do not hand-memoize by default; fix Rules of React violations the compiler cannot salvage.
- Compiler **off**: memoize only when the same component commits repeatedly with unchanged props.

## Lists

Virtualize when DOM node count hurts; keys stay stable identities (`item.id`), never index on reorderable data.
