# Nuxt patterns

Operational rules for Nuxt 3/4 apps. Load this file when the active layer is data fetching, hydration, auto-imports, server routes, state, middleware, configuration, SEO, plugins, or build/deploy.

## Data fetching

| API | Use when | Avoid when |
|---|---|---|
| `useFetch` / `useAsyncData` | Component/page setup needs SSR-aware deduped data and payload transfer | Fire-and-forget clicks inside event handlers |
| `useLazyFetch` / `useLazyAsyncData` | Non-blocking navigation; show pending UI | The route is unusable without the data |
| `$fetch` | Event handlers, Nitro/`server` code, one-shot imperative calls | Top-level `<script setup>` during SSR (double fetch + possible mismatch) |

- `useFetch` is a convenience wrapper around `useAsyncData` + `$fetch`.
- Provide an explicit `key` when the request identity is not fully encoded in the URL string (filters, ids, locale).
- On client navigation, cached Nuxt data may return until `refresh`/`clearNuxtData` — treat that as design, not random staleness.
- Prefer calling server functions/repositories directly from server components/routes instead of HTTP-looping your own public API without reason.

## Hydration traps

| Symptom | Likely cause | Fix |
|---|---|---|
| Text mismatch warning | `Date.now()`, `Math.random()`, unstable ids in render | Compute once on server and pass as prop, or render inside `<ClientOnly>` |
| SSR crash | `window` / `document` / `localStorage` at setup | `onMounted`, `import.meta.client`, or client-only plugin |
| Flash of wrong tree | Client-only `v-if` true on first client paint | Start false, flip after mount, or use `<ClientOnly fallback=...>` |
| Invalid HTML nesting | Browser “fixes” DOM before hydrate | Correct markup (`p` > `div`, table structure, button contents) |

`<ClientOnly>` still ships the slot logic to the client; it does not make secrets safe. Use it for browser-only UI, not access control.

## Auto-imports

- Components under `components/` are auto-imported; nested folders become name prefixes.
- Composables under `composables/` auto-import when named `use*`.
- `server/utils` auto-imports only inside server routes/plugins — client code must not rely on them.
- Name collisions: import explicitly or adjust filenames; do not silence with blanket `@ts-nocheck` unless diagnosing types.

## Server routes (Nitro)

- File `server/api/users.get.ts` → `GET /api/users`; `server/api/users.post.ts` → `POST /api/users`.
- Without a method suffix the handler accepts all methods — usually unintentional.
- Use H3 helpers: `getQuery(event)`, `readBody(event)`, `getHeader(event, ...)`, `setResponseStatus`.
- Return serializable data; throw `createError({ statusCode: 404, statusMessage: '...' })` for errors.
- Middleware in `server/middleware/` runs for server requests (including API), not as Vue route middleware.

## State management

- `useState('key', init)` — SSR-safe, shared across component instances with the same key. Keys must be unique for distinct data.
- `init` runs on server too: no `localStorage` or `window` inside the factory.
- Pinia: call `useStore()` inside setup/plugins after Pinia is installed; on SSR create a fresh Pinia per request. Destructure state with `storeToRefs`.
- Module-scope reactive singletons leak across requests under SSR — treat them as bugs.

## Middleware and navigation

- Vue route middleware: `middleware/auth.ts` + `definePageMeta({ middleware: 'auth' })`, or `*.global.ts` for every route.
- Always `return navigateTo('/login')` (or equivalent); a bare `navigateTo` without `return` continues the original navigation.
- Server middleware ≠ route middleware. Pick the layer that matches auth enforcement vs UX redirect.
- Route middleware is not a security boundary by itself — API handlers must re-check auth.

## Configuration

```ts
export default defineNuxtConfig({
  runtimeConfig: {
    apiSecret: '',
    public: { apiBase: '/api' },
  },
})
```

- Private keys: server-only. Public keys: embedded for client + server.
- Env override pattern: `NUXT_API_SECRET`, `NUXT_PUBLIC_API_BASE`.
- `app.config` / `app.config.ts` is public build-time app config (hot-reload friendly).
- `nuxt.config` changes typically need a restart; do not put secrets in `app.config`.

## SEO and head

- `useSeoMeta({ title, ogTitle, description, ... })` for typed common tags.
- `useHead` for arbitrary link/script/meta shapes.
- Static values may live in `definePageMeta` only when they never depend on async data; dynamic titles belong in setup composables.
- `app.head` / `titleTemplate` in config for site-wide defaults (`%s · Site`).

## Plugins

- `plugins/foo.ts` runs for both sides unless suffixed `.client.ts` / `.server.ts`.
- Use `defineNuxtPlugin` and prefer `provide` / composables over deep global mutation.
- Numeric prefixes (`01.auth.ts`) control order when one plugin depends on another.
- Do not touch `window` in a universal plugin without a client guard.

## Build and deploy

| Command | Result | Notes |
|---|---|---|
| `nuxt dev` | Dev server | Not proof of production cache/hydration behavior |
| `nuxt build` | Server bundle in `.output` | Needed for API routes / SSR |
| `nuxt generate` | Static output | API routes will not run without a separate server |
| `routeRules` | Hybrid rendering | e.g. ISR `{ isr: 3600 }`, `prerender: true` |

Deploy the `.output` directory for Node-like hosts. Confirm hybrid rules per path instead of assuming global SSR or global static.

## Safety

- Never guide users to put private `runtimeConfig` values under `public` or `NUXT_PUBLIC_*`.
- Auth checks in middleware are UX; enforce again in `server/api` handlers.
- Clear guidance beats dumping this entire file — answer from the active section only.
