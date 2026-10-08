# Quickstart — Paperclip

Official install path uses the `paperclipai` CLI. Prefer packaged npm installs unless
the user is developing Paperclip itself.

## Prerequisites

```bash
node --version   # need v24.11.0+
```

- Node.js **24.11.0 or newer**
- Optional: Anthropic and/or OpenAI API keys for first agents
- Optional: Claude Code / Codex CLIs on the same host for local adapters

## Fastest packaged start

```bash
npx paperclipai@latest onboard --yes
npx paperclipai@latest run
```

If `paperclipai` is already on `PATH` (managed or global install):

```bash
paperclipai onboard --yes
paperclipai run
```

Notes from upstream:

- `onboard` writes instance config; `run` validates (doctor/repair) and starts the server.
- Default quickstart uses **trusted local loopback** for the fastest first run.
- Rerunning `onboard` on an existing config keeps settings; use `paperclipai configure` to edit.
- UI/API default: `http://localhost:3100` (`/api` prefix for JSON).

### Reachability presets

```bash
npx paperclipai@latest onboard --yes --bind lan
npx paperclipai@latest onboard --yes --bind tailnet
```

### Private npm registry workaround

If `npx` returns `E404` for `paperclipai` because a private registry is default:

```bash
npm config get registry
npx --registry https://registry.npmjs.org paperclipai@latest onboard --yes
```

### Managed long-lived CLI

```bash
npx paperclipai install          # installs ~/.local/bin/paperclipai ; store under ~/.paperclip/cli
paperclipai --version
```

`paperclipai uninstall` removes the managed CLI/service wiring and leaves instance data alone.

## Isolated / throwaway instance

```bash
npx paperclipai@latest onboard --yes --data-dir ./tmp/paperclip-dev
npx paperclipai@latest run --data-dir ./tmp/paperclip-dev
npx paperclipai@latest doctor --data-dir ./tmp/paperclip-dev
```

`--data-dir` relocates config, context, db, logs, storage, and secrets away from
`~/.paperclip`.

## Manual monorepo flow

Only when hacking on Paperclip source:

```bash
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
pnpm install
pnpm dev
```

Requirements here: Node.js 24.11+, pnpm 9.15+. Embedded PostgreSQL starts with dev.
In-repo CLI alias: `pnpm paperclipai <command>`.

## Test-drive (foreground demo instance)

```bash
ANTHROPIC_API_KEY=... npx paperclipai test-drive
OPENAI_API_KEY=... npx paperclipai test-drive --harness codex
```

Without `--data-dir`, each run gets a unique retained temporary directory printed
at startup. Does not install a background service or create the first task.

## First operator checks

```bash
curl -sS http://localhost:3100/api/health
npx paperclipai@latest company list
npx paperclipai@latest dashboard get
curl -sS http://localhost:3100/api/companies
```

If control-plane commands fail auth on a non-`local_trusted` instance, run
`paperclipai connect` (or agent `local-cli`) before retrying.

## Five-minute product path (after server is up)

1. Create a company
2. Hire a CEO agent (`claude_local` / `codex_local` common)
3. Enable heartbeat, review strategy approval, watch first issues land

Guided docs: https://docs.paperclip.ing/guides/getting-started/five-minute-path/

## Default disk layout (instance home)

Default home: `~/.paperclip` (override with `PAPERCLIP_HOME` or `--data-dir`).

| Item | Typical path |
|------|----------------|
| Default instance config | `~/.paperclip/instances/default/config.json` |
| Context profiles | `~/.paperclip/context.json` |
| Managed CLI store | `~/.paperclip/cli/` |

Exact child paths can vary by version; treat `doctor` output as authoritative for a live install.
