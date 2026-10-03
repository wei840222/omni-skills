# Debug symptom chains

Work top-down: reproduce in dev (full messages), then apply the matching chain.

## Too many re-renders

1. Find `setState` during render or `onClick={fn()}` instead of `onClick={fn}`.
2. Move updates into handlers or effects; derive values inline in render.

## Hooks order / invalid hook call

1. No conditional hooks; every early return below the last hook.
2. `npm ls react` — monorepos often ship two React copies.

## Hydration mismatch

1. Suspect `Date.now()`, `Math.random()`, locale formatting, `typeof window`.
2. Move non-deterministic UI into an effect, or `suppressHydrationWarning` on one node.
3. Fix invalid HTML nesting (e.g. `<p>` inside `<p>`) before blaming data.

## Stale state / effect races

1. Functional updates when next value depends on previous.
2. Abort in-flight fetches on dependency change (`AbortController` cleanup).
3. Do not delete StrictMode to “fix” double mount — fix cleanup instead.

## Minified production #NNN

Decode at https://react.dev/errors/NNN, then reproduce with a development build.
