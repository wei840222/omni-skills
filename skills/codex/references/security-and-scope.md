# Security, Trust, and Scope

## External Endpoints

Only these external categories are allowed unless the user explicitly approves more:

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://api.openai.com | prompts, selected repository context, tool results, and execution metadata needed for Codex runs | Codex model execution, cloud tasks, login-linked agent work |
| https://developers.openai.com/* | doc queries only | Verify current Codex product behavior and configuration details |
| https://{user-approved-mcp-host} | request payloads required by the specific MCP server | Optional user-approved tool access beyond the local machine |

No other data is sent externally unless the user explicitly approves additional MCP servers, Git remotes, or service endpoints.

## Security & Privacy

Data that leaves your machine:
- prompts and the repo context selected for Codex runs against OpenAI services
- optional MCP payloads only for user-approved MCP servers
- optional cloud task payloads and diffs when Codex Cloud is intentionally used

Data that stays local:
- `~/.codex/config.toml` and the user's local Codex session/config state
- durable operating notes under `<state_root>/codex/`
- local diffs, verification output, and repo metadata unless the user explicitly pushes or uploads them

This skill does NOT:
- assume dangerous bypass is acceptable by default
- enable remote MCP or cloud apply silently
- scrape tokens from arbitrary files to "help" auth succeed
- hide sandbox or approval choices from the user
- claim that CLI, app-server, cloud, and local `--oss` flows have identical risk

## Trust

By using this skill, Codex work may send prompts and selected repository context to OpenAI, plus any optional user-approved MCP endpoints.
Only install if you trust those services with that data.

## Scope

This skill ONLY:
- helps operate Codex safely and effectively in real coding environments
- structures repo work into explicit execution, review, and handoff modes
- keeps durable memory for approved repos, safety posture, and recurring recovery patterns

This skill STRICTLY EXCLUDES:
- treat every available Codex feature as automatically approved
- recommend destructive git cleanup as a default fix
- blur the line between local-only, cloud, and MCP-assisted execution
- modify its own skill files
