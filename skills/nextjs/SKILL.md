---
name: nextjs
description: >
  Build and debug Next.js App Router apps across routing, Server Components,
  caching, Server Actions, auth, and deployment. Use when fixing stale cache,
  hydration/boundary errors, protected routes, Docker/Vercel/static-export
  shipping, or App Router data-fetch issues. Prefer `react` for plain React
  questions and keep Pages Router deep-dives out of scope.
metadata:
  version: "1.1.2"
  openclaw: '{"emoji":"⚡"}'
  related-skills: '{"react":"Plain React fundamentals when the ask is not Next.js App Router specific.","typescript":"Type-safety patterns that apply beyond Next.js route/module boundaries.","prisma":"Database ORM setup and query patterns used with Next.js Server Components.","tailwindcss":"Utility-class styling choices and RSC-compatible client boundaries.","nodejs":"Node runtime, packaging, and server process concerns outside Next-specific routing."}'
---

# Next.js App Router

Operate Next.js App Router work with progressive disclosure: keep always-needed
routing and safety rules here, and load `references/` only for the matching
situation.

## When to load

Load when the user is:

- building or debugging an App Router app (routing, rendering, data, deploy)
- hitting boundary or hydration errors
- chasing stale/ISR/cache surprises
- wiring sessions, protected routes, or role checks
- shipping to Vercel, Docker, standalone, or static export

Prefer other skills when the ask is mainly:

- plain React without Next.js routing/data → `react`
- TypeScript-only DX → `typescript`
- Prisma schema/query design → `prisma`

## State location

Optional project memory may live under `<workspace>/nextjs/`,
`<workspace>/memory/nextjs/`, or `~/nextjs/`. `<workspace>` is the host/runtime
workspace root, never the shell cwd.

Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/nextjs/`, `<workspace>/memory/nextjs/`, `~/nextjs/`.
3. If multiple candidates exist, keep the highest-precedence one only, report
   the conflict, and leave other copies unchanged.
4. If none exists and durable notes must be created, describe the write, obtain
   confirmation, then default to `<workspace>/nextjs/`.
5. Keep the resolved `<state_root>` fixed for the invocation. Never write the
   literal string `<state_root>` to disk.

```text
<state_root>/
├── config.yaml   # package_manager, deployment_target, styling, naming prefs
├── memory.md     # stack, conventions, proactivity, safety posture
└── projects/     # per-project learnings
```

If older notes exist at a legacy Clawic nextjs data directory, migrate them into
the resolved `<state_root>/` on first write and say in one line that you moved
them and from where. Seed new memory from `assets/memory-template.md`.

## Configuration

Defaults apply until the user states a preference; store overrides in
`<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| package_manager | npm \| pnpm \| yarn \| bun | npm | Install/run syntax, lockfile references, Docker `corepack`/cache mounts |
| deployment_target | vercel \| docker \| standalone \| static-export | vercel | Build `output` mode and which parts of `references/deployment.md` apply; static-export disables SSR/ISR/Server Actions guidance |
| styling | tailwind \| css-modules \| styled-components \| vanilla-extract | tailwind | Styling examples and RSC caveats (styled-components need a client boundary/registry) |
| component_naming | PascalCase \| kebab-case | PascalCase | Generated component filenames and import examples |
| folder_convention | feature-folders \| type-folders | feature-folders | Where new routes, components, and colocated files land |

Capture preferences as they surface during real work rather than interrogating
up front: conventions, stack (TypeScript/ORM/auth), proactivity, and safety
posture for auth hardening.

## Workflow

1. Confirm the ask is App Router–scoped and identify the primary surface
   (route, cache, auth, deploy).
2. Apply Core Rules below before opening a reference file.
3. Load only the matching reference from Progressive disclosure.
4. Persist durable preferences under `<state_root>/` after consent; keep secrets
   and credentials outside state files.

## Progressive disclosure

| File | Load when |
|---|---|
| `references/setup.md` | First session / no `<state_root>/memory.md` yet |
| `assets/memory-template.md` | Creating `<state_root>/memory.md` or project notes |
| `references/data-fetching.md` | Slow pages, sequential awaits, streaming, Server Actions |
| `references/caching.md` | Stale/over-fresh data, revalidate, ISR, cache debugging |
| `references/auth.md` | Login, sessions, protected routes, roles, DAL checks |
| `references/routing.md` | Modals over pages, parallel routes, layouts, navigation |
| `references/deployment.md` | Docker, self-hosting, env vars, static export |
| `references/sources.md` | Refreshing Gate 6 source ledger or version claims |

## Core Rules

### 1. Server by Default, Client at the Leaves
`'use client'` marks a boundary, not one component: everything imported below it
ships to the browser. Keep interactivity in leaf components; a `'use client'`
layout de-RSCs its whole subtree.

### 2. Parallel Fetches or You Pay the Sum
Sequential awaits cost sum(t1..tn); `Promise.all` costs max(). Chain awaits only
when one call genuinely needs the other's result.

### 3. One Dynamic Read Poisons the Whole Route
`cookies()`, `headers()`, or an uncached fetch anywhere in the tree — layouts
included — forces the entire route to render per-request. Read them in the leaf
that needs them, behind `<Suspense>`.

### 4. Dev Lies About Caching
`next dev` renders everything dynamically. Verify cache behavior only with
`next build && next start`; debug headers and build-output symbols live in
`references/caching.md`.

### 5. Middleware Redirects, the Data Layer Enforces
Middleware does optimistic cookie checks for UX; every Server Action, route
handler, and query re-verifies the session. CVE-2025-29927 let a spoofed
`x-middleware-subrequest` header skip middleware entirely — use patched versions
and the data-access-layer pattern in `references/auth.md`.

### 6. Server Actions Are Public Endpoints
Anyone can POST to an action with its id; a hidden button protects nothing.
First lines of every action: session check, then input validation.

### 7. Write, Revalidate, Then Redirect
Every mutating action ends with `revalidatePath`/`revalidateTag`, or the UI keeps
serving stale cache. `redirect()` throws — call it after the try/catch, never
inside one.

### 8. `NEXT_PUBLIC_` Is Baked at Build Time
Inlined into the bundle during `next build`; changing it at runtime does
nothing. Unprefixed vars stay server-only — and any differing public var means
one Docker image per environment (`references/deployment.md`).

### 9. Suspense Converts Blocking Into Streaming
TTFB = the slowest await chain outside any Suspense boundary. Wrap each
independent slow fetch in its own `<Suspense>` so the shell paints immediately.

## Server vs Client

| Server Component | Client Component |
|------------------|------------------|
| Default in App Router | Requires `'use client'` |
| Can be async | Cannot be async |
| Access backend, env vars | Access hooks, browser APIs |
| Zero JS shipped | JS shipped to browser |

**Decision:** Start Server. Add `'use client'` only for useState, useEffect,
event handlers, or browser APIs.

**The boundary is a serialization boundary.** Props crossing server→client must
serialize: plain objects, arrays, Date, Map, Set — yes; functions and class
instances — no (exceptions: Server Actions passed as props, and Promises the
client unwraps with `use()`). A Server Component cannot be imported into a
Client Component — pass it as `children`.

## Version Gates

- `next >=13.4` — App Router stable; everything here assumes it
- `next 14` — `fetch` cached by default (the version where the default flips)
- `next >=15` — `fetch` and GET route handlers uncached by default;
  `params`/`searchParams` are Promises — `await` them; React 19 (`useActionState`)
- `next >=16` — Turbopack is the default bundler; synchronous `params` access
  removed; `middleware.ts` renamed `proxy.ts` (old name deprecated)

## Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| `try/catch` around `redirect()` | it throws `NEXT_REDIRECT`; the catch swallows it | redirect after the try, or rethrow |
| Fetching your own API route from a Server Component | extra HTTP round-trip, lost types | call the DB/function directly |
| `useEffect` for initial data | double round-trip (HTML, then JSON), no streaming | fetch in a Server Component |
| `cookies()` in root layout | whole app goes dynamic (Rule 3) | read in the consuming leaf |
| `new PrismaClient()` at module top level | dev hot-reload piles up connections | `globalThis` singleton |
| `Date.now()`/`Math.random()` in render | server/client HTML differ → hydration error | compute in `useEffect`, or pass from server as prop |
| Secrets imported into client code | bundled into public JS | `import 'server-only'` in server modules |
| `next/image` with `fill` but no `sizes` | srcset assumes 100vw | set `sizes` to the actual rendered width |
| Heavy work or DB calls in middleware | runs on every matched request | optimistic checks only; real work in the route |
| `router.push` in a Server Component | no client router on the server | `redirect()` |

## Where Experts Disagree

| Question | Camps | The boundary |
|----------|-------|--------------|
| Server Actions vs route handlers for mutations | actions-everywhere vs REST | Actions for your own app's forms; handlers for webhooks, external clients, explicit status codes |
| Edge vs Node runtime | edge-first vs Node-default | Node unless the route is latency-critical AND every dependency runs on edge |
| Still need SWR/React Query? | server-only vs client cache | Server fetch for read-mostly pages; client libraries for polling, optimistic UI, or infinite scroll |
| Vercel vs self-host | DX vs cost/control | Vercel to validate; revisit when ISR/image bills grow or compliance demands your infra — see `references/deployment.md` |
