---
name: paperclip
description: >
  Run Paperclip as a local AI-company control plane: onboard/run instances,
  design org charts, pick adapters (Claude/Codex/OpenClaw and others), operate
  issues/approvals/heartbeats/budgets, and call the JSON API. Use when the user
  wants Paperclip install, multi-agent company orchestration, OpenClaw-as-employee
  setup, CLI/API automation, or spend governance. Not a general coding agent,
  chat UI replacement, or one-off single-agent harness without company state.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📎","requires":{"bins":["curl"],"env":{"optional":["PAPERCLIP_API_URL","PAPERCLIP_API_KEY","PAPERCLIP_COMPANY_ID","PAPERCLIP_AGENT_ID","PAPERCLIP_RUN_ID","PAPERCLIP_HOME","OPENAI_API_KEY","ANTHROPIC_API_KEY","OPENCLAW_GATEWAY_TOKEN"]}}}'
  related-skills: '{"agent":"General single-agent execution patterns when Paperclip is not the control plane.","agents":"Multi-agent role design that maps into Paperclip org charts.","api":"Generic HTTP/API payload design when debugging Paperclip endpoints.","company":"Company strategy framing before encoding goals and reporting lines in Paperclip.","workflow":"Repeatable handoffs that become issues, routines, or approval gates."}'
---

## When to use

Load for **Paperclip control-plane work**:

- Install / onboard / doctor a local Paperclip instance
- Create companies, hire agents, set goals and reporting lines
- Choose adapters (`claude_local`, `codex_local`, `openclaw_gateway`, …)
- Operate issues, approvals, heartbeats, routines, and budgets
- Integrate OpenClaw as an employee over the gateway
- Automate the same flows with `paperclipai` CLI or `/api`

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| One agent run without company state | `agent` |
| Role design before Paperclip encoding | `agents` / `company` |
| Generic HTTP debugging outside Paperclip schemas | `api` |
| Process design not yet bound to issues/routines | `workflow` |

## State location

This skill keeps **operator memory** (instances touched, adapter prefs, blockers)
separate from **Paperclip application data**.

Skill operator state may exist in `<workspace>/paperclip/`,
`<workspace>/memory/paperclip/`, or `~/paperclip/`.
`<workspace>` means the workspace root provided by the host/runtime, not the shell CWD.

Before any skill-state read or write, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/paperclip/`, `<workspace>/memory/paperclip/`, `~/paperclip/`.
3. If none exists and the user asks to save durable operator notes, create
   `<workspace>/paperclip/` only after consent.
4. If multiple candidates exist, use only the highest-precedence path, report the
   duplicates, and leave the others untouched.

Use the selected `<state_root>` for every **skill memory** operation in this skill.
Create only the resolved filesystem path; the placeholder name `<state_root>` is
documentation-only.

**Paperclip instance home** (config, embedded DB, logs, storage, secrets) defaults
to `~/.paperclip` (`PAPERCLIP_HOME`), with the default instance under
`~/.paperclip/instances/default/`. Isolate with `--data-dir <path>` or
`paperclipai run --data-dir …`. Do **not** write instance DB/secrets into
`<state_root>` unless the user explicitly set `--data-dir` there.

Legacy path `~/Clawic/data/paperclip/` is a migration source only. Propose copy,
validation, cutover, and rollback; do not move or delete automatically.

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` is missing, read
`references/setup.md`. Confirm before the first write to `<state_root>`.

For product install itself, load `references/quickstart.md`.

## Primary workflow

Execute in order. Stop early only when a step already blocks progress.

1. **Intent** — Classify: install, diagnose, company design, adapter choice,
   day-to-day ops, OpenClaw hire, or API automation.
2. **Resolve paths** — Select `<state_root>` for skill notes; detect Paperclip
   home (`PAPERCLIP_HOME` / `--data-dir` / `~/.paperclip`) and API base
   (`--api-base` → `PAPERCLIP_API_URL` → profile → local config port →
   `http://localhost:3100`).
3. **Route detail** — Load only the reference that owns the current pain:

| Bottleneck | Load |
|------------|------|
| First-run activation / consent | `references/setup.md` |
| Install, onboard, run, doctor | `references/quickstart.md` |
| Adapter matrix and selection | `references/adapters.md` |
| CLI/API day-to-day commands | `references/operations.md` |
| OpenClaw gateway hire path | `references/openclaw.md` |
| Rules, traps, security, endpoints | `references/domain.md` |
| Operator memory schema | `references/memory-template.md` |
| Verified product sources | `references/sources.md` |

4. **Prefer control-plane verbs** — Companies, issues, approvals, heartbeats,
   and budgets stay in Paperclip; runtimes only execute assigned work.
5. **Confirm before external impact** — Creating companies, waking agents,
   approving strategy, changing budgets, or calling paid providers needs current
   explicit authorization. Never embed real API keys in memory files.
6. **Write durable notes** — After consent, update `<state_root>/memory.md` and
   related notes with non-secret environment facts only.

## Operating rules

- Treat Paperclip as the company OS, not the domain worker.
- Model goal, org chart, workspaces, and budgets before waking many agents.
- Prefer `npx paperclipai@latest …` or an installed `paperclipai` binary for
  packaged installs; use `pnpm paperclipai` only inside a Paperclip monorepo checkout.
- Heartbeats are the default execution loop; agents need not run continuously.
- From Docker/OpenClaw containers, never assume `localhost` reaches the host
  Paperclip process—use a reachable host alias and `allowed-hostname` when needed.
- Atomic issue checkout matters: do not bypass it with ad-hoc parallel edits.

## Quick reference

| Topic | File |
|-------|------|
| Setup / consent | `references/setup.md` |
| Local bootstrap | `references/quickstart.md` |
| Adapters | `references/adapters.md` |
| CLI + API ops | `references/operations.md` |
| OpenClaw | `references/openclaw.md` |
| Domain rules | `references/domain.md` |
| Memory template | `references/memory-template.md` |
| Sources | `references/sources.md` |
