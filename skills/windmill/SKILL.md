---
name: windmill
description: Create and manage scripts, flows, schedules, and variables in a Windmill workspace. Trigger this skill when the user asks to build internal tools or automate workflows using Windmill.
metadata:
  openclaw: '{"emoji":"🌀"}'
---

## Script Traps
- Main function signature determines input schema — Windmill infers from type hints, wrong types break the UI form
- Always return a value to ensure downstream steps receive the script output
- Python dependencies go in inline `requirements.txt` comment — not a global file, each script is isolated
- TypeScript runs on Bun — Node.js-specific APIs may not work

## Secrets and Variables
- Store original secrets securely elsewhere, as they cannot be read back from the UI after creation
- Store sensitive data exclusively in secrets, as variables are plaintext and visible
- Path format matters — `u/username/secret` for user, `f/folder/secret` for shared

## State location

- `$HOME/.config/windmill`: Configuration and local state.
- Workspace directories for scripts and flows should be explicitly defined by the user.

## Advanced Information
- For information on flow execution, scheduling, self-hosting, webhooks, and common mistakes, read `references/advanced.md`.
