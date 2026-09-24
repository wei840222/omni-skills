# Tool selection

Prefer a CLI the agent already knows. Add a tool only when it removes a repeated manual step.

| Task | Prefer | Record it as |
|---|---|---|
| GitHub issues and PRs | `gh` | no extra config |
| Logs | the host's log CLI, such as `vercel` or `axiom` | one line in agent instructions |
| Database | `psql` or the project's existing client | connection via ignored env, not the skill |
| Deploy | the project's existing CLI | no new wrapper |

Claude Code's guidance is the same shape: a focused CLI or script beats an always-on tool that dumps context the task does not need. https://code.claude.com/docs/en/best-practices

## What to skip for this workflow

- A retrieval index, when the agent can already search the checkout.
- An MCP server whose only job is a CLI the agent knows.
- A subagent framework, when a second visible terminal already isolates the task.
- A custom orchestrator, when the user can assign paths directly.

Codex CLI is the local agent when the user wants approval-gated edits in the checkout. Claude Code is the local agent when the user wants its permission modes and parallel sessions. Pick the one the user already runs. https://learn.chatgpt.com/docs/codex/cli

## Background jobs

If a dev server or test suite would block the steering terminal, ask the agent to run it in `tmux` or the terminal's background job. Keep the interactive session free for pause and redirect.

## Browser and voice

Use a browser tool when the task is a runtime bug, a visual check, or an auth flow. For a logic change, ask the agent to read the code first. A voice-to-text tool is optional for long prompts; recommend one only if the user asks.

## Build boundary

This workflow uses existing tools. A new Claude Code wrapper, worktree manager, or orchestration framework is a separate product decision, not a step in coordinating today's agents.
