# OpenClaw Integration — Paperclip

Upstream adapter type: `openclaw_gateway`.
Docs: https://docs.paperclip.ing/reference/adapters/openclaw-gateway.md

## What fits best

If the user keeps talking through OpenClaw, Paperclip should stay the company
control plane. OpenClaw is one employee (or operator surface), not a replacement
for org chart, issues, approvals, or budgets.

## Recommended modes

| Mode | Use when | Result |
|------|----------|--------|
| OpenClaw as employee | OpenClaw should execute assigned company work | Paperclip owns tickets; OpenClaw receives wakes over gateway |
| OpenClaw as human-facing shell | Chat-first UX while Paperclip tracks work | Source of truth stays in Paperclip issues/approvals |
| Mixed company | OpenClaw + Codex/Claude/etc. share one goal | One org chart, many adapters |

## Core workflow

1. Start Paperclip and confirm a URL **OpenClaw can actually reach** (not blind `localhost` from inside Docker).
2. Allow the hostname Paperclip/OpenClaw will use (`paperclipai allowed-hostname …` when required).
3. Hire/invite OpenClaw through Paperclip's OpenClaw invite flow or API config for `openclaw_gateway`.
4. Keep work on issues + heartbeats; do not strand state only in chat transcripts.

## Transport and auth

- URL must be `ws://` or `wss://`.
- Provide one of: gateway token (`authToken`/`token`), headers (`x-openclaw-token` or legacy `x-openclaw-auth`), or password.
- Device auth is on by default; pin `devicePrivateKeyPem` for stable identity across runs.
- `autoPairOnFirstConnect` (default true) can approve the first pairing over shared auth; otherwise approve the device inside OpenClaw and retry.

Invite helper endpoint (board/CEO copy-ready prompt):

```text
POST /api/companies/{companyId}/openclaw/invite-prompt
```

## Session strategy

| Strategy | Behavior |
|----------|----------|
| `issue` (good default) | One OpenClaw session per issue |
| `fixed` | Single `sessionKey` every run |
| `run` | Fresh session per run (no cross-heartbeat memory) |

## Critical Docker caveat

From an OpenClaw container, `127.0.0.1` is the container itself.
Use a host gateway alias (often `host.docker.internal`) and verify with smoke tooling.

Example patterns from upstream docs (adapt container/name/token paths to the live deploy):

```bash
pnpm smoke:openclaw-join
pnpm smoke:openclaw-docker-ui
paperclipai allowed-hostname host.docker.internal
```

## UI note

The agent-config dropdown may label `openclaw_gateway` as **Coming soon** while
the runtime still supports it via invite flow, API, or company import. Do not
treat the label as “adapter missing.”
