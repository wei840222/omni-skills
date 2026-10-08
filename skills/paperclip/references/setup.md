# Setup — Paperclip skill memory

Read this silently when `<state_root>/` does not exist or `memory.md` is missing.
Start by helping with the user's immediate Paperclip task instead of pausing for
onboarding theater.

## Start with the current goal

Answer the install, debugging, architecture, or integration question first.
Capture only context that prevents repeated setup mistakes.

## Early integration

Within the first exchanges, learn whether Paperclip should activate proactively for:

- AI company setup
- multi-agent orchestration
- heartbeats, approvals, or budgets
- OpenClaw, Codex, or Claude operating under one control plane

Save that integration preference to the user's main host memory when appropriate,
not only this skill folder.

## Capture only reusable context

Store non-secret facts such as:

- API base URL and whether mode is `local_trusted` or `authenticated`
- instance home (`~/.paperclip`, `PAPERCLIP_HOME`, or `--data-dir`)
- adapters in use and host vs Docker placement
- whether OpenClaw is native or containerized (and reachable hostname)
- active companies, primary workspaces, budget posture, current blockers

## Learn organically

Infer patterns from repeated behavior. Ask only when missing context blocks the
next correct action.

## Respect boundaries

- Provider and gateway secrets stay private.
- Note the missing credential name, explain the blocker, continue with dry-run or
  read-only guidance when possible.
- First durable write to `<state_root>` requires consent.
- Never treat skill `<state_root>` as a substitute for Paperclip instance home.

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning the environment | Keep gathering context while working |
| `complete` | Enough context is stored | Operate normally |
| `paused` | User does not want more setup now | Stop probing; use existing context |
| `never_ask` | User wants no setup follow-up | Skip setup prompts unless reopened |
