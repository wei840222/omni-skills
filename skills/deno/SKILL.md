---
name: deno
description: Configure Deno environments. Use when writing or running Deno code to manage permissions, import dependencies securely, and migrate Node.js patterns.
metadata:
  openclaw: '{"emoji":"🦕","requires":{"bins":["deno"]}}'
  related-skills: '{"nodejs":"Node.js runtime patterns when comparing APIs or migrating away from Node.","typescript":"TypeScript language guidance that pairs with Deno-first TS workflows.","javascript":"Core JavaScript patterns shared across Deno and other JS runtimes.","bun":"Alternative JS runtime often compared during migration decisions."}'
---

## When to load

Load this skill when you are writing, executing, or migrating code that uses the Deno runtime. Load this skill for Node.js environments only when actively porting code to Deno.

## Critical rules

- Prefer least-privilege flags over `--allow-all`; scope `--allow-read`, `--allow-net`, `--allow-env`, and `--allow-run` to exact paths/hosts/vars/binaries.
- In CI, pass explicit permissions plus `--no-prompt` so missing grants fail fast instead of hanging on interactive prompts.
- Commit a lockfile and prefer `--cached-only` (or vendored deps) in production so remote URL imports cannot drift or fail offline.
- Use `npm:` / `node:` specifiers deliberately; plain Node-style bare imports and extensionless `.ts` imports fail under Deno.
- Keep import maps inside `deno.json` / `deno.jsonc` (Deno 2.x); do not rely on a separate import-map file.

## State location

Deno project configuration stays in the workspace:
- `deno.json` or `deno.jsonc`
- `deno.lock` (commit with the project)

This skill does not own a mutable `<state_root>` package path.

## Progressive disclosure

For implementation detail, load the matching file under `references/`:

- Read `references/permissions.md` to configure runtime boundaries and prevent missing-permission hangs in CI.
- Read `references/imports.md` to resolve dependencies securely and manage import maps / lockfiles.
- Read `references/node-compat.md` to migrate Node.js patterns (`fs`, `process.env`, npm packages) safely.
