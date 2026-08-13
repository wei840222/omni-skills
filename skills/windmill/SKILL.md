---
name: windmill
description: Create and manage scripts, flows, schedules, and variables in a Windmill workspace. Trigger this skill when the user asks to build internal tools or automate workflows using Windmill.
metadata:
  openclaw: '{"emoji":"🌀"}'
---

## Script Traps
- Main function signature determines input schema — Windmill infers from type hints, wrong types break the UI form
- Always return a value to ensure downstream steps receive the script output
- For Python scripts, use top-level imports so Windmill can resolve dependencies; read `references/advanced.md` before adding nonstandard dependencies
- TypeScript scripts can use Bun or Deno; choose the configured runtime and confirm API compatibility before relying on runtime-specific behavior

## Secrets and Variables
- Store original secrets securely elsewhere, as they cannot be read back from the UI after creation
- Store sensitive values in secret variables; ordinary variables remain readable to principals with the required workspace permissions
- Path format matters — `u/username/secret` for user, `f/folder/secret` for shared

## State Location

Optional local planning state may exist in `<workspace>/windmill/`, `<workspace>/memory/windmill/`, or `~/windmill/`.

Before reading or writing local planning state, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/windmill/`, `<workspace>/memory/windmill/`, `~/windmill/`.
3. If none exists and the user requests persistent local planning state, create `<workspace>/windmill/`.

Use the selected `<state_root>` consistently during the invocation. Store only requested planning notes there; never store credentials, copied secrets, or workspace exports.

Windmill resources, variables, secrets, and script state belong to the selected Windmill workspace, not this skill package. Before creating or changing those persistent workspace objects, confirm the workspace and target path with the user.

## Advanced Information
- For information on flow execution, scheduling, self-hosting, webhooks, and common mistakes, read `references/advanced.md`.
