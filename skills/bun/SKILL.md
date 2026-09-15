---
name: bun
description: Assist with migrating to the Bun runtime, bundling JavaScript/TypeScript,
  and managing packages by guiding users through runtime traps, bundler pitfalls,
  and resolution gotchas.
metadata:
  openclaw: '{"emoji": "🥟", "requires": {"bins": ["bun"]}}'
---

## When to load

Load this skill when the user explicitly requests assistance with the Bun runtime (`bun run`, `bun install`, `bun build`), is migrating a Node.js project to Bun, or encounters compatibility traps, bundler pitfalls, or package manager resolution issues using Bun.

## Quick Reference

| Topic | File |
|-------|------|
| Node.js API differences | `references/node-compat.md` |
| Bundler configuration | `references/bundler.md` |
| Package management | `references/packages.md` |

## Runtime Compatibility Traps

- `process.nextTick` timing differs from Node — race conditions appear that didn't exist before, use `queueMicrotask` for cross-runtime code
- `__dirname` and `__filename` are omitted in ESM — instead, use `import.meta.dir` and `import.meta.file` to prevent ReferenceErrors
- `fs.watch` misses events that Node catches — file watcher scripts silently miss changes, add polling fallback
- `child_process.spawn` options subset — some stdio configurations silently ignored, test subprocess code explicitly
- `cluster` module not supported — app crashes immediately if code uses cluster, must refactor to workers
- `vm` module partial — sandboxed code may escape or behave differently, security implications

## Bundler Traps

- `--target=browser` strips Node APIs silently — build succeeds, then runtime crashes on `fs`, `path`, etc.
- `--splitting` requires `--format=esm` — error message doesn't mention this, just fails cryptically
- Everything bundled by default — server code bundles node_modules, use `--external:package` for server deps
- Tree-shaking assumes no side effects — code with side effects may be removed, add `"sideEffects": false` to package.json or lose code
- CSS imports work differently than webpack — `url()` paths resolve wrong, test in actual browser
- `--minify` mangles names aggressively — debugging production crashes is harder, use `--minify-syntax` for safer minification

## Package Manager Traps

- `bun.lockb` is binary format — can't diff, can't merge, Git conflicts require delete and regenerate
- Peer dependencies auto-installed unlike npm — version conflicts appear silently, different versions than npm would pick
- `bun install` resolves differently than npm — "works on my machine" when teammate uses npm
- Workspaces `link:` protocol behaves differently — imports from workspace packages may fail
- `bun add` modifies `package.json` formatting — unwanted diff noise in commits
- No `npm audit` equivalent — security vulnerabilities not surfaced automatically

## TypeScript Traps

- Bun runs TypeScript directly without `tsc` — type errors bypass execution blocks, check types explicitly to prevent shipping bugs to production
- Type-only imports may be kept — bundle size larger than expected
- `tsconfig.json` paths work differently — imports that worked in Node+tsc may fail
- Decorators experimental — behavior may differ from tsc, especially with legacy decorators

## Testing Traps

- `bun test` has different assertion API — tests written for Jest need adaptation
- Mock timing differs — tests that pass in Jest may fail or flake
- No native coverage like c8/nyc — need different tooling
- Snapshot format incompatible with Jest — can't share snapshots between runners

## Hot Reload Traps

- `bun --hot` doesn't reload native modules — changes require restart
- State preserved across reloads — bugs from stale state hard to debug
- WebSocket connections not re-established — clients appear connected but dead
