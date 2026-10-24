---
name: codex
description: "Operate Codex coding agents safely across CLI, review mode, MCP servers, and cloud environments. Use when configuring execution sandboxes, sandboxing tool permissions, or conducting automated code reviews."
metadata:
  openclaw: '{"emoji": "🧭", "requires": {"bins": ["codex"]}}'
  related-skills: '{"agentic-engineering": "Strengthen the human workflow around parallel coding agents and blast-radius thinking.", "api": "Reuse structured API and request-debugging patterns when Codex integrates with services.", "coding": "Improve implementation quality once Codex is operating inside the right repo boundaries.", "git": "Handle branches, diffs, and non-destructive repository recovery safely.", "workflow": "Turn recurring Codex tasks into repeatable, reviewable execution paths."}'
---

## When to load

Load this skill to operate Codex coding agents, manage sandbox boundaries, configure MCP servers, or troubleshoot Codex CLI and execution workflows.

## State location

Codex state may exist in `<workspace>/codex/`, `<workspace>/memory/codex/`, or `~/codex/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/codex/`, `<workspace>/memory/codex/`, `~/codex/`.
3. If none exists and state must be created, default to `<workspace>/codex/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>/codex/`. If `<state_root>/codex/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure.

```text
<state_root>/codex/
|-- memory.md          # Durable activation boundaries and operating defaults
|-- repo-profiles.md   # Per-repo conventions, test surface, and blast-radius notes
|-- safety.md          # Sandbox, approval, and trust defaults
|-- mcp-notes.md       # Approved MCP servers, scopes, and rejection reasons
`-- incidents.md       # Stuck sessions, failed commands, and recovery patterns
```

## Quick Reference

Load only the smallest file needed for the current blocker.

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Install, login, and first-run checks | `references/install-and-auth.md` |
| Repo execution and `codex exec` workflows | `references/repo-execution.md` |
| Approval modes and sandbox choices | `references/approvals-and-sandbox.md` |
| MCP, app-server, cloud, and local-provider guardrails | `references/mcp-and-cloud.md` |
| Review mode and handoff patterns | `references/review-and-handoffs.md` |
| Recovery playbooks for auth, stuck sessions, and wrong-scope work | `references/troubleshooting.md` |

## Requirements

- `codex` binary installed and working on the target machine.
- Active authentication through `codex login` or an explicit `OPENAI_API_KEY` flow when that mode is chosen.
- `git` available when the task involves repository inspection, diff review, or commit-ready workflows.
- Explicit user approval before dangerous sandbox bypass, remote MCP usage, Codex Cloud apply, production commands, or any operation with irreversible side effects.
- Treat model names, features, and app-server behavior as live product surface: verify with `codex --help`, subcommand help, or official docs instead of hardcoding stale assumptions.

## Operating Coverage

This skill treats Codex as an operational coding surface, not as generic AI advice. It covers:
- interactive Codex CLI usage with explicit working-directory and safety choices
- non-interactive `codex exec` and `codex review` workflows
- `resume`, `fork`, and handoff-friendly session recovery
- sandbox and approval policy selection by blast radius
- MCP server trust decisions and local-versus-remote tool boundaries
- Codex app-server and cloud task usage only when their extra trust and review requirements are explicit
- local OSS-provider routing via `--oss` and `--local-provider` when the user intentionally wants local execution

## Data Storage

Keep only durable Codex operating context in `<state_root>/codex/`:
- which repos or workspaces are approved for Codex use
- default sandbox and approval posture per task type
- preferred execution surfaces: interactive CLI, `exec`, `review`, cloud, or local OSS provider
- approved MCP servers and what each one is allowed to touch
- recurring recovery notes for wrong directory, dirty worktree, stalled commands, or broken auth

## Core Rules

Load `references/core-rules.md` for explicit preflight checks, sandbox matching, and review boundaries.

## Codex Traps

Load `references/traps.md` for common operating mistakes and recovery patterns.

## Security, Trust, and Scope

Load `references/security-and-scope.md` for external data flow details, privacy boundaries, and explicit scope rules.
