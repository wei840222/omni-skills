# Paperclip Domain Knowledge

Facts below are grounded in the official Paperclip repository and docs listed in
`references/sources.md`. Re-check those URLs before changing version pins or
command shapes.

## Requirements

- **Node.js 24.11.0+** on `PATH` for supported CLI/server operation
  (`npx` on older Node may warn and continue; managed install refuses older Node)
- **pnpm 9.15+** only when working from a Paperclip git checkout (`pnpm install` / `pnpm dev`)
- `curl` (or equivalent) for direct `/api` checks
- Provider credentials only for the adapters the user chooses
  (for example Anthropic for `claude_local`, OpenAI for `codex_local`)
- Local Claude/Codex subscription-style sign-in also needs Python 3 and the
  corresponding provider CLI on the Paperclip host when that path is used

## Core rules

### 1. Treat Paperclip as the control plane

- Organize companies, agents, goals, issues, approvals, routines, and budgets here.
- Attached runtimes (Claude Code, Codex, OpenClaw, …) perform domain work.
- Paperclip is not “just a chatbot UI,” not an agent framework, and not a prompt vault.

### 2. Start local-first unless infrastructure already exists

- Packaged path: `npx paperclipai@latest onboard --yes` then `paperclipai run`
  (or `npx paperclipai@latest run`).
- Default quickstart bind is trusted local loopback. Use `--bind lan` or
  `--bind tailnet` when the instance must be reachable beyond loopback.
- Repo path: `git clone` → `pnpm install` → `pnpm dev` serves UI/API at
  `http://localhost:3100` with embedded PostgreSQL.
- Isolate experiments with `--data-dir <path>` so config/db/logs/storage stay out
  of the default `~/.paperclip` tree.

### 3. Model the company before spawning workers

- Define company goal, reporting lines, workspaces, and issue flow first.
- Hire a CEO/strategy path and use approval gates before broad autonomy.
- Paperclip value shows up when ownership, budgets, and escalation are explicit.

### 4. Pick adapters by execution boundary

- Same host coding agents → local adapters such as `claude_local` or `codex_local`.
- OpenClaw elsewhere (Docker/remote) → `openclaw_gateway` over `ws://` / `wss://`.
- Fixed scripts → `process`; existing HTTP workers → `http`.
- UI may mark some adapter types “Coming soon” while the runtime still accepts
  them via API or company import—see `references/adapters.md`.

### 5. Lean on heartbeats, approvals, and budgets

- Heartbeats wake agents for assigned work, follow-ups, or schedules.
- Approval gates and spend caps are core controls, not optional polish.
- Budget enforcement uses recorded provider spend; in-flight work can delay a hard stop.

### 6. Use CLI and API for repeatable operations

- Setup layer (`onboard`, `doctor`, `configure`, `run`) talks to local config/process.
- Control-plane layer (company/issue/agent/…) is an HTTP client and needs credentials
  except where `local_trusted` loopback implies board access.
- Keep human chat in OpenClaw/Codex/Claude if desired; Paperclip remains source of truth
  for tickets, approvals, and cost.

## Common traps

| Trap | Failure mode | Fix |
|------|--------------|-----|
| Chatbot mental model | Miss org chart, governance, cost controls | Keep work on issues + approvals |
| Many agents, no structure | Parallel unmanaged tabs | Goal + reports-to + budgets first |
| `localhost` from Docker | Container talks to itself | Host alias + `allowed-hostname` |
| Adapter without local CLI/auth | Heartbeats fail immediately | Install/auth provider CLI before wake |
| Skip issue checkout | Double-work / clobber | Use Paperclip checkout semantics |
| Private npm registry shadows package | `E404` for `paperclipai` | `npx --registry https://registry.npmjs.org paperclipai@latest …` |
| Secrets in skill memory | Credential leak | Store env *names* and redacted facts only |
| Conflating skill `<state_root>` with `~/.paperclip` | Broken instance paths | Instance home vs operator notes stay separate |

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| `http://localhost:3100/api` (or configured API base) | Company, agent, issue, approval, run metadata | Control-plane reads/writes |
| `GET /api/health` | None beyond HTTP | Liveness before ops |
| `ws://` / `wss://` OpenClaw gateway URL | Wake payloads, session routing, agent events | `openclaw_gateway` transport |
| User-selected model providers | Prompt/context tokens via adapters | Actual agent inference |

No other endpoints should be contacted unless the user configures remote deploy,
connectors, or providers.

API base resolution order for CLI clients:

1. `--api-base`
2. `PAPERCLIP_API_URL`
3. selected context profile `apiBase`
4. local Paperclip config server port
5. `http://localhost:3100`

Mutating agent runs may send `X-Paperclip-Run-Id` so comments/checkout attach to the run.

## Security and privacy

**Leaves the machine**

- Traffic to the configured Paperclip API base (local or remote)
- OpenClaw gateway traffic when that adapter is enabled
- Provider traffic created by authorized agent runtimes

**Stays local by default**

- Instance files under `~/.paperclip` or `--data-dir`
- Skill operator notes under `<state_root>/`
- Local project workspaces attached to agents

**This skill does not**

- Require a Paperclip Cloud account for self-hosted use
- Put secrets into commands committed to memory files
- Assume a public deployment by default

**Trust boundary**

Operational data goes to the Paperclip deployment and adapters the user configures.
Only proceed when that deployment, its storage, and backing model providers are trusted.
