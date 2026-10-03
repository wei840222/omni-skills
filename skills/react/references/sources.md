# Gate 6 sources (verified 2026-10-03)

Full URLs used for domain claims. Prefer these over model memory.

## Agent Skills format

- https://agentskills.io/llms.txt
- https://agentskills.io/specification.md
- https://github.com/agentskills/agentskills/tree/main/skills-ref

## React

- https://react.dev/blog/2024/12/05/react-19 — React 19 features (Actions, `use`, compiler direction, ref/context changes)
- https://react.dev/reference/react/use — `use(promise)` rules
- https://react.dev/reference/react/useActionState
- https://react.dev/reference/react/useOptimistic
- https://react.dev/reference/react/useFormStatus
- https://react.dev/learn/you-might-not-need-an-effect
- https://react.dev/reference/rsc/server-components
- https://registry.npmjs.org/react/latest — version line **19.3.0** at check time

## TanStack Query

- https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults — `staleTime` default 0; `gcTime` default 5 minutes
- https://registry.npmjs.org/@tanstack/react-query/latest — **5.104.1** at check time

## Zustand

- https://zustand.docs.pmnd.rs/ — v5 docs hub; selector/`useShallow` guidance
- https://registry.npmjs.org/zustand/latest — **5.0.15** at check time

## Next.js (framework default in setup)

- https://nextjs.org/docs/app/getting-started/installation — current install / `create-next-app`
- https://registry.npmjs.org/next/latest — **16.3.8** at check time (do not hard-code as the only supported app version; SPA/Vite remains valid)

## Corrections vs older skill text

- Replaced hard pin “Next.js 15” with current install docs + npm latest line, while keeping Vite SPA guidance.
- Kept TanStack Query staleTime/gcTime semantics aligned with Important Defaults docs.
- Optimistic UI: describe failure recovery explicitly rather than implying a single hidden mechanism.
