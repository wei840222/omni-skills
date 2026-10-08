# Sources — Paperclip

Verified while refactoring this skill. Re-open before changing pins or commands.

## Product and install

- Paperclip README (quickstart, Node 24.11+, `npx paperclipai@latest onboard --yes`, `pnpm dev` on `:3100`)
  — https://github.com/paperclipai/paperclip/blob/master/README.md
- Five-minute path after install
  — https://docs.paperclip.ing/guides/getting-started/five-minute-path.md
- CLI installation (managed install paths, onboard/run, `--data-dir`, Node gate)
  — https://docs.paperclip.ing/reference/cli/installation.md
- CLI overview (setup vs control-plane layers, API base resolution, personas)
  — https://docs.paperclip.ing/reference/cli/overview.md

## Adapters, API, cost

- Adapters overview (type keys, OpenClaw/process/http UI notes)
  — https://docs.paperclip.ing/reference/adapters/overview.md
- OpenClaw gateway adapter (transport, auth, session strategies, Docker caveats)
  — https://docs.paperclip.ing/reference/adapters/openclaw-gateway.md
- API overview (`/api` prefix, auth callers, `X-Paperclip-Run-Id`)
  — https://docs.paperclip.ing/reference/api/overview.md
- Costs and budgets (provider spend, hard stops)
  — https://docs.paperclip.ing/guides/day-to-day/costs.md

## Format authority

- Agent Skills specification
  — https://agentskills.io/specification.md
- Agent Skills doc index
  — https://agentskills.io/llms.txt

## npm package signal

- Published CLI package name `paperclipai` (repo `cli/package.json` on master)
  — https://github.com/paperclipai/paperclip/tree/master/cli
