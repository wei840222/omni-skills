# CLI And MCP - Cursor

Use this file when the user wants repeatable terminal execution, unattended runs, or tool access through MCP.

## `agent` CLI Posture

Treat the Cursor CLI (`agent`) as a real execution surface, not a thin wrapper around editor chat.
Good fits:
- bounded repo tasks
- reproducible automation
- explicit terminal-first workflows
- session resume and checkpointed work

Current docs distinguish interactive `agent` sessions from print/non-interactive mode (`-p` / `--print`). Modes such as Agent, Ask, and Plan are available in the CLI as well as the editor.

## Non-Interactive Risk

- Headless usage is high trust, especially with `--force` or `--yolo` for file writes.
- Without `--force`, print-mode changes may be proposed only; with it, scripts can modify files without confirmation.
- Before launching, lock the repo, objective, allowed files, and verification path.
- Prefer current `agent --help` / docs over remembered flag names.

## MCP Boundaries

Cursor supports MCP in the editor and CLI, but the question is not "can it connect?"
The question is:
- which host is involved
- which transport is used (`stdio`, SSE, Streamable HTTP)
- what data it can read
- what side effects it can trigger
- whether local-only assumptions still hold once MCP is enabled

Cursor's default security posture requires approval for MCP connections and for individual MCP tool calls after connection.

## Default Policy

- prefer no MCP unless the workflow materially benefits
- prefer local or tightly scoped servers over broad remote ones
- require explicit approval before remote MCP
- document what each approved server is allowed to touch
- for CLI workflows, inspect `agent mcp list` / `agent mcp list-tools` before relying on a server

## Failure Signs

- the run uses the wrong repo because CLI context was left unpinned
- the task widens after launch because the prompt stayed vague
- MCP was enabled to "help" before its scope was reviewed
- the user expected local-only work but the workflow now depends on remote tools
