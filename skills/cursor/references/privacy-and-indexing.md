# Privacy And Indexing - Cursor

Use this file when the user cares about where code goes, what indexing really means, or whether ignore files provide enough protection.

## Core Reality

Cursor features can send prompts and code context to Cursor services and model providers.
That remains true even when the user supplies their own model provider key for some flows.
Describe a workflow as local-only only when that specific path truly stays local.

Privacy Mode changes training expectations for LLM requests. It does not turn Cloud Agents, Bugbot, or remote MCP into local-only execution.

## Two Data Flows To Keep Separate

1. **LLM requests** — prompts and selected code context sent for AI features.
2. **Cloud Agents** — optional remote VMs that clone authorized repos and store code while the run needs it.

If policy prohibits code storage in Cursor's cloud, keep Cloud Agents disabled and stay on local editor/CLI surfaces.

## Indexing

Codebase indexing improves retrieval, but it is also a data-flow decision.
Treat indexing as a separate approval question for privacy-sensitive repos.

## Ignore Files

### `.cursorignore`
Use it to reduce what Agent, Tab, Inline Edit, and @-mention references can access.
It helps security and performance, but complete protection is not guaranteed.
Terminal and MCP tools used by Agent are not blocked by `.cursorignore`.

### Narrower indexing controls
Prefer current Cursor settings / docs for indexing-only ignore options when the goal is narrower than full Agent access control.
"Not indexed" is not the same as "impossible to reach."

## Important Boundary

Ignore controls do not guarantee protection against everything an agent can reach through terminal commands or MCP tool calls.
If a file requires strict exclusion from exposure, solve that at the repo, filesystem, secret store, or integration boundary, not only with Cursor ignore settings.

## Practical Policy

- for sensitive repos, ask whether indexing is acceptable before enabling rich context features
- keep secrets and production credentials out of repo paths the agent can touch
- treat Cloud Agents, Bugbot, GitHub integration, and MCP as additional privacy layers to review separately
- verify Privacy Mode / team enforcement expectations against current Cursor privacy docs when the user asks for compliance language
