# Research Sources — symphony

Verified anchors used while refactoring this skill. Prefer primary specs and
current vendor docs over blog summaries.

## Upstream Symphony contract

- **OpenAI Symphony SPEC.md** — authoritative domain model, workflow contract, orchestration state machine, workspace safety, agent-runner protocol, and operational safety via https://github.com/openai/symphony/blob/main/SPEC.md
- **OpenAI Symphony repository** — reference implementation layout and WORKFLOW conventions via https://github.com/openai/symphony

## Tracker and agent runner

- **Linear GraphQL API** — issue metadata, workflow states, and mutation surface used for dispatch/reconciliation via https://developers.linear.app/docs/graphql/working-with-the-graphql-api
- **Linear API authentication** — personal API keys and header expectations via https://developers.linear.app/docs/graphql/authentication
- **OpenAI Codex** — coding agent / app-server oriented automation surface used by unattended runners via https://developers.openai.com/codex/

## Skill packaging and progressive disclosure

- **Agent Skills specification** — frontmatter shape, description triggers, and resource layout via https://agentskills.io/specification
- **Anthropic skill authoring best practices** — keep SKILL.md concise, push detail into references, encode evaluation prompts via https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices

## Safety and secrets hygiene

- **OWASP Secrets Management Cheat Sheet** — keep credentials out of durable local state files via https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
