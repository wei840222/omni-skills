# Framework patterns (React, Next.js, SPA)

Load for React hooks traps, Next.js App Router defaults, and SPA hydration issues. Deep UI systems → `frontend` / `react` / `nextjs`.

## React

- State updates are asynchronous — derive next state with the functional updater when depending on previous state.
- List **keys must be stable identities**; index keys break state when lists reorder, insert, or filter.
- Honor `exhaustive-deps`: missing effect deps cause stale closures; do not disable the lint without a documented reason.
- Effects that subscribe or start timers must return cleanup.
- Hooks cannot sit behind conditions or loops — order must be stable across renders.
- Context value identity changes rerender all consumers — memoize value objects or split contexts.

## Next.js App Router

- Components are **Server Components by default**; add `"use client"` only for hooks, browser APIs, and event handlers.
- `fetch` in Server Components is cached/deduped by default in many setups — use explicit cache/revalidate options when freshness matters (`no-store`, tags, time-based revalidate).
- Middleware/edge runtimes lack full Node APIs — stick to Web APIs and edge-compatible packages.
- Route handlers export HTTP methods from `route.ts`, not from `page.tsx`.
- After mutations, invalidate with `revalidatePath` / `revalidateTag` (or the project's cache strategy).
- **`NEXT_PUBLIC_`** env vars are inlined for the client; everything else stays server-only. Never put secrets behind a public prefix.
- Parallel routes use the `@folder` convention inside a shared layout.

## General SPA / SSR

- **Hydration mismatch** — first client render must match server HTML; gate browser-only values behind `useEffect` or client components.
- Tree-shaking needs ES modules; default imports from large barrels often pull excess code (prefer named imports / `lodash-es` style packages).
- Code-split below-fold routes with `React.lazy` / `next/dynamic` to protect LCP.
- Fetch initial data on the server when SEO or first paint matters; avoid pure client waterfalls for primary content.

## Critical rules

- **Environment variables leak** — public prefixes expose values to any visitor; keep secrets server-side only.
- Prefer server fetch for first paint; use client fetch for post-interaction data.

## Framework decision tree

- **Static content, fast builds** → Astro or plain HTML
- **Blog/docs with MDX** → Astro or Next.js App Router
- **Interactive app with auth** → Next.js or Remix
- **Full SSR/ISR control** → Next.js
- **Simple SPA, weak SEO need** → Vite + React/Vue
