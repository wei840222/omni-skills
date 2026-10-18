---
name: cursor
description: >
  Operate Cursor safely across editor Agent/Ask/Plan modes, the `agent` CLI
  (interactive and headless), Cloud Agents, Bugbot, rules, ignore files, and
  MCP with explicit privacy and surface boundaries. Use when the hard part is
  choosing the right Cursor surface, shaping repo context, setting `.cursor/rules`,
  running non-interactive CLI, enabling Cloud Agents/Bugbot, or deciding whether
  indexing/MCP/remote execution is acceptable. Prefer `coding` once Cursor is
  already correctly scoped for implementation; prefer `git` for branch/diff/
  recovery mechanics; prefer `workflow` for generic SOP design outside Cursor
  product surfaces; prefer `api` when the blocker is an external HTTP integration
  rather than Cursor itself.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⌨️","requires":{"config":["<state_root>/"]},"configPaths":["<state_root>/"],"displayName":"Cursor"}'
  related-skills: '{"agentic-engineering":"Strengthen multi-agent workflow design, review discipline, and blast-radius thinking around Cursor usage.","api":"Reuse request-debugging and integration patterns when Cursor work touches external services.","coding":"Improve implementation quality once Cursor is operating inside the right repo boundaries.","git":"Handle branches, diffs, stashes, and non-destructive repo recovery around Cursor-driven changes.","workflow":"Turn recurring Cursor tasks into cleaner, repeatable operating procedures."}'
---

## When to Use

User wants to operate Cursor as a real coding environment instead of a vague AI editor: choose the right surface, shape repo context, set rules correctly, use the `agent` CLI, run Cloud Agents, review with Bugbot, or decide whether MCP and remote execution are acceptable.

Use this skill when the hard part is not "write code" but "make Cursor behave predictably" across editor chat, Agent / Ask / Plan flows, CLI runs, project rules, repo indexing, remote agents, GitHub integration, and privacy-sensitive work.

## State location

Cursor operating state may exist in `<workspace>/cursor/`, `<workspace>/memory/cursor/`, or `~/cursor/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/cursor/`, `<workspace>/memory/cursor/`, `~/cursor/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and state must be created, default to `<workspace>/cursor/` when `<workspace>` is available; otherwise ask for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation. Never write the literal string `<state_root>` to disk.

Use the selected `<state_root>` for every state operation in this skill. Prefer:

- `<state_root>/memory.md` — durable activation boundaries and workflow defaults
- `<state_root>/repo-profiles.md` — per-repo conventions, trust posture, verification expectations
- `<state_root>/rules-notes.md` — project-rule strategy and instruction hierarchy notes
- `<state_root>/privacy.md` — indexing, ignore, remote execution, and data-handling defaults
- `<state_root>/remote-workflows.md` — Cloud Agent, Bugbot, and GitHub integration decisions
- `<state_root>/incidents.md` — repeated failures, wrong-surface runs, and recovery patterns

If `<state_root>/` is missing or empty, load `references/setup.md`. Initialize missing files from `assets/memory-template.md`. Keep live state under `<state_root>/`; treat `assets/` as templates only.

## Architecture

```text
<state_root>/
|-- memory.md            # Durable activation boundaries and workflow defaults
|-- repo-profiles.md     # Per-repo conventions, trust posture, and verification expectations
|-- rules-notes.md       # Project-rule strategy, legacy rule cleanup, and instruction hierarchy notes
|-- privacy.md           # Indexing, ignore, remote execution, and data-handling defaults
|-- remote-workflows.md  # Cloud Agent, Bugbot, and GitHub integration decisions
`-- incidents.md         # Repeated failures, wrong-surface runs, and recovery patterns
```

## Quick Reference

Load only the smallest file needed for the current blocker.

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Install and choose the right Cursor surface | `references/install-and-surfaces.md` |
| Rules, context hierarchy, and mode choice | `references/rules-and-context.md` |
| `agent` CLI, non-interactive runs, and MCP boundaries | `references/cli-and-mcp.md` |
| Cloud Agents, Bugbot, and GitHub-connected workflows | `references/background-agents-and-bugbot.md` |
| Privacy mode, indexing, and ignore files | `references/privacy-and-indexing.md` |
| Recovery playbooks for auth, bad context, and remote-run mistakes | `references/troubleshooting.md` |
| Verified research URLs | `references/sources.md` |

## Requirements

- Cursor installed and usable on the target machine, or permission to guide installation.
- Cursor CLI (`agent`) available when the task depends on terminal or automation workflows.
- `git` available for repo-aware work, diff review, branch handling, Cloud Agents, or Bugbot.
- Explicit user approval before enabling Cloud Agents, granting GitHub app write access, using remote MCP servers, or running high-trust non-interactive commands (`agent -p --force` / `--yolo`).
- Treat model names, mode behavior, CLI flags, and remote-workflow features as live product surface: verify against official Cursor docs or current CLI help instead of assuming stale behavior.

## Operating Coverage

This skill treats Cursor as an operational coding system, not as generic editor advice. It covers:
- editor-side usage across Agent, Ask, Plan, and custom mode patterns
- project rules through `.cursor/rules` (`.mdc`), user rules, team rules, and `AGENTS.md`, with `.cursorrules` treated as legacy
- context shaping through repo boundaries, indexing, and ignore files
- local and non-interactive `agent` CLI workflows, including resume and MCP-aware execution
- Cloud Agents and Bugbot when work shifts from local interaction to remote GitHub-connected execution
- privacy, data exposure, and review discipline when Cursor features move code or prompts off the local machine

## Data Storage

Keep only durable Cursor operating context in `<state_root>/`:
- which repos, teams, or task types are approved for Cursor use
- preferred surface by task type: editor, CLI, Cloud Agent, or Bugbot
- rule hierarchy decisions and recurring `.cursor/rules` patterns that worked
- privacy and trust defaults around indexing, ignore files, GitHub integration, and remote MCP
- repeated failures such as wrong repo scope, ignored rules, unsafe non-interactive runs, or remote review noise

## Core Rules

### 1. Lock the Cursor Surface First
- Name the active surface before doing anything else: editor Agent, Ask, Plan, custom mode, `agent` CLI, Cloud Agent, or Bugbot.
- Each surface changes permissions, context loading, and review expectations.
- Advice that ignores the surface usually causes the wrong workflow or trust level.

### 2. Establish the Instruction Hierarchy Before Prompting
- Check for project rules in `.cursor/rules`, `AGENTS.md`, repo agent guidance, and any team-level user rules before asking Cursor to act.
- Treat `.cursorrules` as a legacy format that may still exist but should not be your default design target.
- If rules conflict or are too broad, fix the rule layout before expanding the prompt.

### 3. Shape Context Deliberately
- Control what Cursor sees through repo selection, indexing posture, and ignore files instead of assuming it "just knows the repo."
- Use `.cursorignore` to reduce Agent/Tab/@-mention access, but treat it as a filter rather than a perfect secret barrier; terminal and MCP tools can still reach ignored paths.
- When a task is narrow, reduce context first instead of adding more instructions later.

### 4. Separate Local Work From Remote Work
- Editor Agent and local CLI use are different from Cloud Agents and Bugbot.
- Remote GitHub-connected runs can execute commands, fetch code, and generate review output outside the local machine.
- Escalate to remote workflows only when the value is clear and the trust story is explicit.

### 5. Treat Non-Interactive CLI and MCP as High-Trust Modes
- Headless `agent -p` (especially with `--force` / `--yolo`) is powerful and deserves an explicit repo, objective, allowlist, and verification path before launch.
- Review MCP server scope, host, transport, and side effects before turning it on; MCP connections and tool calls require approval in Cursor's defaults.
- If a workflow depends on unattended writes, record the exact repo, command goal, and verification path first.

### 6. Make Privacy and Data Flow Explicit
- Cursor requests, indexing, and remote workflows may send code or prompts to Cursor services, model providers, GitHub, or user-approved MCP hosts.
- Privacy Mode changes training expectations; it does not make Cloud Agents or remote features equivalent to local-only execution.
- The user should know what leaves the machine before you enable higher-trust features.

### 7. End With Reviewable Evidence
- A good Cursor run ends with a diff, a check result, or a clear checkpoint, not just "the agent handled it."
- For Cloud Agents and Bugbot, inspect the output before merging or applying anything locally.
- Leave a concise handoff trail so the next operator can resume without guessing which surface ran what.

## Cursor Operating Targets

Keep these failure modes visible as positive operating targets:
- Prefer naming local vs remote surfaces before approving Cloud Agents or Bugbot.
- Prefer checking `.cursor/rules` / `AGENTS.md` before dumping more chat instructions.
- Prefer filesystem, secret-store, or integration controls for sensitive files; treat `.cursorignore` as access reduction, not a guarantee.
- Prefer an explicit trust discussion before remote command execution.
- Prefer pinned repo + objective + verification for headless CLI runs.
- Prefer one named owner when Bugbot, editor Agent, and local git state are all in play.
- Prefer verifying current product behavior against docs/CLI help rather than assuming a provider API key equals direct provider execution.

## External Endpoints

Only these endpoint categories are allowed unless the user explicitly approves more:

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://cursor.com/* | prompts, selected repo context, diffs, integration metadata, and remote-workflow payloads needed by Cursor features | Cursor editor, agent, indexing, Cloud Agent, and review workflows |
| https://docs.cursor.com/* / https://cursor.com/docs/* | doc queries only | Verify current Cursor behavior, feature scope, and integration details |
| https://github.com/* | repository metadata, code, pull-request context, and review actions approved by the user | Cloud Agents, Bugbot, and GitHub-connected Cursor workflows |
| https://api.github.com/* | repository, branch, PR, and review metadata approved by the user | GitHub API access used by Cursor-connected review and remote execution flows |
| https://{user-approved-mcp-host} | request payloads required by the approved MCP server | Optional MCP tool access beyond the local machine |

Ask for explicit user approval before sending data to any host outside this list.

## Security and privacy

Keep durable operating notes under the resolved `<state_root>/`. Open paths outside that root only after the user names them.

Expect these data paths during normal Cursor use:
- prompts and selected code context sent to Cursor services / model providers
- indexing-related code chunks or metadata needed for codebase features
- optional repo, branch, and PR context when Cloud Agents or Bugbot use GitHub-connected flows
- optional MCP payloads only for user-approved MCP servers

Keep these local unless the user enables a remote feature:
- durable notes under `<state_root>/`
- local repo state, local rules, and diffs
- files excluded from the Cursor request or approved tool call

Require explicit approval before enabling Cloud Agents, Bugbot, or remote MCP. Leave package files under `skills/cursor/` unchanged during normal operating sessions.

## Trust

By using this skill, prompts and selected code context may be sent to Cursor services, plus optional GitHub and user-approved MCP hosts.
Only install if you trust those services with that data.

## Scope

This skill helps operate Cursor safely across editor, CLI, rules, indexing, remote agents, and review workflows; structures repo work into the right local or remote execution surface; and keeps durable notes for approved repos, rule strategy, privacy posture, and recurring failure fixes.

Stay inside those operating goals. Keep local editor help distinct from Cloud Agent execution, treat ignore files as one control among several, require explicit approval for high-trust unattended runs, and treat Cursor as a product surface with its own trust boundaries rather than a generic chat wrapper.
