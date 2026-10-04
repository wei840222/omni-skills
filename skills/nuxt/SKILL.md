---
name: nuxt
description: >
  Build and debug Nuxt 3/4 Vue apps around SSR data fetching, hydration,
  auto-imports, server routes, useState, middleware, runtimeConfig, and SEO.
  Use when useFetch vs $fetch, hydration mismatches, Nitro API handlers,
  route middleware, or Nuxt routeRules come up. Not for plain Vue SPA-only
  work (vue), React/Next (react/nextjs), or generic Vite bundler setup (vite).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💚","requires":{"bins":["node"]}}'
  related-skills: '{"vue":"Vue reactivity, SFC, and SPA patterns when the problem is not Nuxt-specific.","vite":"Bundler and Vite plugin issues outside Nuxt conventions.","typescript":"Language-level typing outside Nuxt auto-import and Nitro types.","frontend":"Cross-framework UI polish and accessibility.","seo":"General SEO strategy beyond Nuxt useSeoMeta helpers.","nodejs":"Node runtime and process concerns outside Nitro handlers."}'
---

# Nuxt

Nuxt-specific SSR/SSG guidance for Vue apps: pick the right data-fetching API, keep server and client HTML aligned, use Nitro server routes correctly, and keep secrets out of the client bundle.

This skill is stateless. Keep project notes, env inventories, and deploy runbooks in ordinary user files outside the skill package.

## When to use

- Choosing `useFetch` / `useAsyncData` vs `$fetch` in components or event handlers
- Fixing hydration mismatches from `Date.now()`, `Math.random()`, `localStorage`, or client-only branches
- Writing `server/api` handlers, middleware, or `runtimeConfig` secrets
- Debugging auto-import naming, `useState` collisions, or Pinia SSR setup
- SEO with `useSeoMeta` / `useHead`, or deploy choices (`nuxt build` vs `nuxt generate`, `routeRules`)

Prefer `vue` for SPA-only reactivity, `vite` for bare Vite config, `react`/`nextjs` for React stacks, and `seo` for non-Nuxt SEO strategy.

## Quick workflow

1. **Name the layer** — data fetching, hydration, server route, state, middleware, config, or SEO.
2. **Check the boundary** — does the code run on server, client, or both? Secrets and browser APIs cannot cross blindly.
3. **Load one reference** — open only the matching file from the table below.
4. **Verify against sources** — version-sensitive API claims against URLs in `references/sources.md`.
5. **Keep answers operational** — state the failing layer, the concrete API, and the reference that justifies it.

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/nuxt-patterns.md` | Data fetching, hydration, auto-imports, server routes, state, middleware, config, SEO, plugins, build |
| `references/sources.md` | Official Nuxt / Nitro / Pinia docs used for Gate 6 freshness |
| `test-prompts.json` | Evaluation harness only — do not load during normal user assistance |

## Operating rules

### Data fetching

- In components and pages during SSR, prefer `useFetch` / `useAsyncData` so Nuxt deduplicates and transfers payload; bare `$fetch` in `<script setup>` often runs on server and again on client.
- Use `$fetch` in event handlers, `server/` code, and other non-setup call sites where a one-shot request is intentional.
- Pass a stable `key` when the URL path is fixed but params/filters change; otherwise cached payload can look stale.
- Use `useLazyFetch` / `useLazyAsyncData` when navigation must not block; always handle pending and error states.

### Hydration

- Do not render `Date.now()`, `Math.random()`, or locale/timezone-dependent strings during SSR without a shared server-provided value.
- Browser-only APIs (`window`, `document`, `localStorage`) belong in `onMounted`, `import.meta.client` guards, or `<ClientOnly>`.
- Client-only UI that would change the first paint should use `<ClientOnly>` with a fallback rather than a server/client-divergent `v-if`.

### Auto-imports and server routes

- `components/` auto-import with directory prefixes (`components/UI/Button.vue` → `<UIButton>`).
- Composables auto-import when named `use*`; plain `utils` exports need explicit import.
- `server/utils/` is server-only — never assume it exists in client bundles.
- `server/api/users.get.ts` maps to `GET /api/users`; method suffixes select HTTP verbs.
- Read input with `getQuery` / `readBody` / H3 helpers; throw `createError({ statusCode })` for failures.

### State, middleware, config

- `useState` is SSR-friendly shared state keyed app-wide — colliding keys silently share data; defaults must be server-safe.
- Prefer `storeToRefs` when destructuring Pinia state; create Pinia per request on SSR.
- Global route middleware uses `middleware/*.global.ts`; page middleware via `definePageMeta`. Always `return navigateTo(...)` when redirecting.
- Put secrets in private `runtimeConfig`; expose only `runtimeConfig.public`. Override with `NUXT_` env vars. Never send private keys to the client payload.

### SEO, plugins, deploy

- Prefer `useSeoMeta` for typed meta; `useHead` for arbitrary tags/scripts.
- Plugins: `.client.ts` / `.server.ts` suffixes; ordered prefixes when dependencies matter.
- `nuxt generate` is static — API routes need a server. Deploy `nuxt build` output from `.output`. Use `routeRules` for ISR/prerender intentionally.

## Safety boundaries

- Treat `runtimeConfig` private keys, `.env`, and deployment tokens as secrets — never commit or echo them into client guidance.
- Do not invent Nuxt version behavior from memory; re-open `references/sources.md` links for disputed APIs.
- Route non-Nuxt Vue questions to `vue` instead of overloading this skill.
