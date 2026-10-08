# Adapter Matrix — Paperclip

Adapters connect Paperclip's control plane to the runtime that does the work.
Type keys below match upstream docs (`docs.paperclip.ing` adapter reference).

## Built-in adapters (common)

| Type key | Best for | Needs | Notes |
|----------|----------|-------|-------|
| `claude_local` | Claude Code on the Paperclip host | `claude` CLI + Anthropic auth | Session persistence, skills sync; common CEO path |
| `codex_local` | OpenAI Codex CLI on host | `codex` CLI + OpenAI auth | Managed `CODEX_HOME`, resume support |
| `gemini_local` | Gemini CLI on host | Gemini CLI + auth | Local skills sync |
| `cursor` | Cursor Agent CLI | Cursor CLI | `--resume` continuity |
| `opencode_local` | OpenCode CLI | OpenCode + provider routing | `--session` resume |
| `pi_local` | Pi CLI | Pi CLI | Built-in tool set |
| `hermes_local` | Hermes Agent | Hermes install | Persistent memory + large tool/skill set |
| `grok_local` | Grok Build CLI | Grok CLI | Resume + staged skills |
| `kimi_local` | Kimi Code CLI | Kimi CLI | ACP engine + headless fallback |
| `openclaw_gateway` | OpenClaw elsewhere | `ws://`/`wss://` URL + auth | Invite-prompt flow; UI may say “Coming soon” |
| `process` | Local scripts/wrappers | Executable + args | API/import if UI hidden |
| `http` | Remote webhook workers | Reachable HTTP service | API/import if UI hidden |

External adapter plugins install via Board UI or `POST /api/adapters/install` and
version independently.

## Selection rules

1. Same machine, coding-heavy → `claude_local` or `codex_local` first.
2. OpenClaw in Docker or another host → `openclaw_gateway` (not localhost-from-container).
3. Already an HTTP worker → `http`.
4. Deterministic shell without an LLM runtime → `process`.
5. Need independent packaging → external adapter plugin.

## Environment readiness

Before enabling heartbeats:

- Run the adapter's environment test from UI/API when available.
- Confirm provider CLI login on the **Paperclip host**, not only on the operator laptop.
- Set company/agent budgets; providers bill token usage outside Paperclip's license.

## Useful local-CLI handoff

Hand a terminal identity to an agent (exports `PAPERCLIP_API_URL`, company/agent ids, key):

```bash
paperclipai agent local-cli <agent-id> -C <company-id>
```

Use when a human or local model should act *as* that agent and report through the API.
Inside a Paperclip monorepo checkout only, the equivalent is `pnpm paperclipai …`.
