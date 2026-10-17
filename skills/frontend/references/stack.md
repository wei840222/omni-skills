# Stack & Tooling — Frontend

## Recommended Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Framework | Next.js (current App Router) | RSC, file routing, first-party deploy path |
| Language | TypeScript | Catch errors early, better DX |
| Styling | Tailwind CSS | Utility-first, design tokens built-in |
| Components | shadcn/ui | Accessible primitives you own in-repo |
| Animation | Framer Motion | Declarative motion with reduced-motion hooks |
| Forms | React Hook Form + Zod | Type-safe validation |
| State | Zustand or Jotai | Simple client state without boilerplate |

Pin exact major versions from the project's lockfile; do not invent a version that is not installed.

Verify current docs when scaffolding:

- React: https://react.dev/learn
- Next.js App Router: https://nextjs.org/docs/app/getting-started
- Tailwind utilities: https://tailwindcss.com/docs/styling-with-utility-classes
- shadcn/ui: https://ui.shadcn.com/docs
- Framer Motion: https://www.framer.com/motion/

## Project Structure

```
src/
├── app/                 # Next.js App Router
│   ├── layout.tsx
│   ├── page.tsx
│   └── [feature]/
├── components/
│   ├── ui/              # shadcn/ui components
│   └── [feature]/
├── lib/
│   ├── utils.ts         # cn(), formatters
│   └── api.ts
├── hooks/
├── styles/
│   └── globals.css
└── config/
    └── site.ts
```

## Essential Utils

```typescript
// lib/utils.ts
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

## shadcn/ui Setup

```bash
npx shadcn@latest init
npx shadcn@latest add button card dialog
```

Most used: Button, Card, Dialog, Accordion, Tabs, Sheet, NavigationMenu.

For framework-specific bugs, load `react`, `nextjs`, `tailwindcss`, or `css` instead of stretching this skill.
