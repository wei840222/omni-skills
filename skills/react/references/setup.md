# React Setup

First-time preference setup for the React skill. Resolve `<state_root>` per
`SKILL.md` before any create or copy. Do not auto-create legacy paths.

## Step 1: Confirm state root

1. Use an explicit path if the user or host configured one.
2. Otherwise use the first existing directory among
   `<workspace>/react/`, `<workspace>/memory/react/`, `~/react/`.
3. If none exists and preferences must be saved, create `<workspace>/react/`
   only with user consent.
4. Legacy `~/Clawic/data/react/` and `~/clawic/react/` are migration sources
   only — copy with consent after verify; never auto-delete.

## Step 2: Initialize memory

Copy `assets/memory-template.md` to `<state_root>/memory.md` when the user
wants persistent notes. Fill the Stack Decisions table on first use — later
sessions read it instead of re-asking.

Optional defaults live in `<state_root>/config.yaml` (framework, styling,
state_library, package_manager). See Configuration in `SKILL.md`.

## Step 3: Verify setup

Ready when the chosen `<state_root>` is known and, if used,
`<state_root>/memory.md` exists.

## Project structure

Feature folders, not type folders (→ SKILL.md, Where Experts Disagree):

```
src/
├── app/                 # Routes (Next.js App Router) or framework entry
├── features/            # One folder per feature
│   └── [feature]/
│       ├── components/
│       ├── hooks/
│       ├── api/         # Fetchers + query key factory + types
│       └── index.ts     # Public exports — other features import ONLY from here
├── shared/              # Used by 2+ features (move here at second consumer)
│   ├── components/ui/
│   └── hooks/
└── providers/           # Context providers, QueryClient
```

The `index.ts` barrel is the enforcement point: cross-feature imports that
bypass it already tangle the dependency graph.

## Recommended stack

Pin exact versions from the project lockfile. Verified latest lines at repair
time (2026-10-03): React 19.3.x, Next.js 16.x when using App Router, TanStack
Query 5.x, Zustand 5.x. Prefer `create-next-app@latest` / current install docs
over hard-coded minor pins in commands.

| Layer | Tool | Why this over alternatives |
|-------|------|----------------------------|
| Framework | Next.js (App Router) or Vite | RSC + Actions when SEO/content matters; Vite for login-gated SPA dashboards |
| Styling | Tailwind CSS | Styles colocated with markup; no naming layer to maintain |
| Components | shadcn/ui | Copied into your repo — you own the code |
| Server state | TanStack Query v5 | Cache lifecycle, dedupe, devtools; SWR only if you need nothing but GET |
| Client state | Zustand v5 | Selectors without providers; no boilerplate ceremony |
| Forms | React Hook Form + Zod | Uncontrolled inputs; one schema for client and server |
| Testing | Vitest + Testing Library | Queries by role/label — tests survive refactors |

## TypeScript config

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

`noUncheckedIndexedAccess` makes `array[0]` typed `T | undefined`, surfacing
empty-state crashes at compile time (→ SKILL.md, Core Rule 7).

## Common commands

```bash
# Next.js (current major via create-next-app)
npx create-next-app@latest my-app --typescript --tailwind --app

# Vite (SPA)
npm create vite@latest my-app -- --template react-ts

# Add shadcn/ui
npx shadcn@latest init

# Data + state + forms
npm install @tanstack/react-query zustand react-hook-form zod @hookform/resolvers
```

Use the package manager from `<state_root>/config.yaml` when set.
