# Sources - Cursor

Live-checked on 2026-10-18. Prefer these URLs (or current `agent --help`) over remembered product claims.

## Agent Skills format

- https://agentskills.io/llms.txt
- https://agentskills.io/specification.md
- https://agentskills.io/skill-creation/best-practices.md
- https://agentskills.io/skill-creation/optimizing-descriptions.md

## Cursor product docs

- https://cursor.com/docs/llms.txt
- https://cursor.com/docs/agent/overview.md
- https://cursor.com/docs/agent/security.md
- https://cursor.com/docs/rules.md
- https://cursor.com/docs/mcp.md
- https://cursor.com/docs/cli/overview.md
- https://cursor.com/docs/cli/headless.md
- https://cursor.com/docs/cli/mcp.md
- https://cursor.com/docs/cloud-agent.md
- https://cursor.com/docs/cloud-agent/security.md
- https://cursor.com/docs/bugbot.md
- https://cursor.com/docs/reference/ignore-file.md
- https://cursor.com/docs/enterprise/privacy-and-data-governance.md
- https://cursor.com/help/security-and-privacy/privacy.md

## Domain notes verified against those sources

- Project rules live in `.cursor/rules` as `.mdc` files; plain `.md` under that folder is ignored by the rules system. `AGENTS.md` is a supported simple alternative.
- `.cursorignore` reduces Agent/Tab/@-mention access, but terminal and MCP tools used by Agent are not blocked by it.
- Cursor CLI entrypoint in current docs is `agent`; headless automation uses `-p` / `--print`, and file writes in scripts need `--force` or `--yolo`.
- Cloud Agents run in isolated cloud VMs, clone authorized repos, and hand off via branch/PR; they are optional and distinct from local editor Agent.
- Bugbot reviews PR diffs (auto or via `cursor review` / `bugbot run`) and is configured through Cursor Automations after source-control connection.
- Privacy Mode changes training expectations for LLM requests; Cloud Agents are a separate data-flow that stores code while the remote run needs it.
