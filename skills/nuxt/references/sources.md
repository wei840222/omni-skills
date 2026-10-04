# Nuxt skill sources

Authoritative references used for this refactor. Prefer these over blog posts when guidance conflicts. Re-open before asserting version-specific defaults.

## Nuxt core

- Data fetching — https://nuxt.com/docs/getting-started/data-fetching
- `useFetch` — https://nuxt.com/docs/api/composables/use-fetch
- `useAsyncData` — https://nuxt.com/docs/api/composables/use-async-data
- `useState` — https://nuxt.com/docs/api/composables/use-state
- Auto-imports — https://nuxt.com/docs/guide/concepts/auto-imports
- Server directory — https://nuxt.com/docs/guide/directory-structure/server
- Middleware directory — https://nuxt.com/docs/guide/directory-structure/middleware
- Plugins directory — https://nuxt.com/docs/guide/directory-structure/plugins
- Components / ClientOnly — https://nuxt.com/docs/api/components/client-only
- Runtime config — https://nuxt.com/docs/guide/going-further/runtime-config
- SEO and meta — https://nuxt.com/docs/getting-started/seo-meta
- Rendering and route rules — https://nuxt.com/docs/guide/concepts/rendering

## Ecosystem

- Pinia on Nuxt (SSR) — https://pinia.vuejs.org/ssr/nuxt.html
- Vue SSR guide (hydration mechanics) — https://vuejs.org/guide/scaling-up/ssr.html

## Agent Skills packaging

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref validator — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Operational note

Nuxt 3 vs 4 docs share many composable names but defaults and file layouts drift. Before promising a concrete default (payload keys, data cache, directory structure), open the live doc page for the project's Nuxt major version.
