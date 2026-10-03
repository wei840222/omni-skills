# Migration and legacy patterns

## Before adding features on legacy code

1. Inventory class components, `forwardRef`, PropTypes, string refs, legacy context.
2. Prefer one vertical slice upgrade over a big-bang rewrite.

## React 19 notes

- `ref` as a normal prop reduces `forwardRef` need for app components.
- Context can render as provider directly where supported.
- Replace deprecated patterns using current react.dev upgrade guides; keep
  behavior tests green at each step.

## PropTypes → TypeScript

Delete runtime PropTypes once types cover the same surface; keep runtime
validation at API/form boundaries (Zod), not duplicate prop types.
