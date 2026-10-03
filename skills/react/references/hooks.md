# Hooks discipline

## Replacement table (you might not need an effect)

| Goal | Prefer |
|------|--------|
| Derive value from props/state | Compute in render |
| Reset state when identity changes | Change `key` on the component |
| Notify parent of state | Call in the event handler that updates state |
| Subscribe to external store | `useSyncExternalStore` |
| Fetch remote data | TanStack Query or server fetch + `use()` |
| One-time app bootstrap | Framework entry or Query client setup, not ad-hoc effects |

## Effect rules

1. Name the **external system** (DOM, network, third-party widget). No system → no effect.
2. Return cleanup for subscriptions, timers, and in-flight work.
3. Never `useEffect(async () => …)` — define async inside and call it; return cleanup separately.
4. Dependency arrays: primitives or stable references; object literals in deps retrigger every render.

## Refs

- `ref` is a normal prop in React 19 for function components; drop `forwardRef`
  unless a library boundary still requires it.
- Refs hold imperative handles; do not use them as reactive state substitutes.
