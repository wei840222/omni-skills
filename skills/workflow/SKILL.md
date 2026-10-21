---
name: workflow
description: >
  Build automated pipelines with reusable components, node data flow, triggers,
  locks, and portable state under `<state_root>/workflows/`. Use when creating or
  repairing cron/webhook pipelines, composing connections/nodes/triggers, adding
  cursor/seen/checkpoint recovery, or preventing concurrent runs with flock.
  Prefer `cycle` for LLM-driven multi-phase process design before automation, and
  `loop` when a single phase must iterate until success criteria.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"⚡","requires":{"bins":["jq","yq","curl","uuidgen","flock"]},"os":["linux","darwin"],"displayName":"Workflow"}'
  related-skills: '{"cycle":"Design LLM-driven multi-phase processes before turning them into executable pipelines.","loop":"Iterate one action or phase until success criteria once the pipeline step is chosen."}'
---

## State location

Workflow runtime state may exist in `<workspace>/workflows/`, `<workspace>/memory/workflows/`, or `~/workflows/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/workflows/`, `<workspace>/memory/workflows/`, `~/workflows/`.
3. If none exists and state must be created, default to `<workspace>/workflows/` after the user consents.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/workflows/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Never write the literal string `<state_root>` to disk. Treat legacy `~/Clawic/data/workflow/` paths as migration sources only—ask before migrating.

On first durable use, create only the paths needed under `<state_root>/workflows/`. Host secrets stay in the platform secret store (Keychain, env, or equivalent); store pointers, never raw tokens, in skill files.

## Architecture

Workflow packages live under `<state_root>/workflows/` with shared components and per-flow runtime trees:

```
<state_root>/workflows/
├── index.md                 # Inventory with tags
├── components/
│   ├── connections/         # Auth configs
│   ├── nodes/               # Reusable operations
│   └── triggers/            # Event sources
├── tmp/                     # Lock files for concurrent-run prevention
└── flows/{name}/
    ├── flow.md              # Definition
    ├── config.yaml          # Parameters
    ├── run.sh               # Executable
    ├── state/               # Persistent between runs
    ├── data/                # Intermediate node outputs
    └── logs/                # JSONL per run
```

## Quick Reference

| Topic | File |
|-------|------|
| Directory layout, naming, formats | `references/structure.md` |
| Data passing between nodes | `references/data-flow.md` |
| Cursor, seen set, checkpoint | `references/state.md` |
| Retry, rollback, idempotency | `references/errors.md` |
| Connections, nodes, triggers | `references/components.md` |
| Create, test, update, archive | `references/lifecycle.md` |
| Verified sources | `references/sources.md` |

## Requirements

- **jq** — JSON processing
- **yq** — YAML config parsing
- **curl** — HTTP requests
- **uuidgen** — run / artifact identifiers when needed
- **flock** — lock files to prevent concurrent runs
- Secrets via host secret store (`security find-generic-password` on macOS, env vars, or equivalent). Prefer pointers such as `env:…` / `keychain:…` in docs; never commit live tokens.

## Data Storage

- **Location:** `<state_root>/workflows/`
- **State:** `<state_root>/workflows/flows/{name}/state/` — cursor.json, seen.json, checkpoint.json
- **Logs:** `<state_root>/workflows/flows/{name}/logs/` — JSONL per run
- **Data:** `<state_root>/workflows/flows/{name}/data/` — intermediate files between nodes
- **Locks:** `<state_root>/workflows/tmp/workflow-{name}.lock`

## Core Rules

### 1. Data Flow Pattern
Each node writes output to `data/{NN}-{name}.json`. Next node reads it.
```bash
curl ... > data/01-fetch.json
jq '...' data/01-fetch.json > data/02-filter.json
```
Keep the numbered data/{NN}-name.json contract so each node can read the previous output.

### 2. Error Declaration
Every node in flow.md MUST declare:
- **On error:** retry(N) | fail | continue | alert
- **On empty:** skip | continue | fail

Declare on-error and on-empty for every node so recovery stays explicit.

### 3. Lock Files
Prevent concurrent runs under the resolved state root:
```bash
LOCKFILE="$RESOLVED_STATE_ROOT/workflows/tmp/workflow-${NAME}.lock"
mkdir -p "$(dirname "$LOCKFILE")"
exec 200>"$LOCKFILE"
flock -n 200 || exit 0
```

### 4. State Files
| File | Purpose |
|------|---------|
| cursor.json | "Where did I leave off?" |
| seen.json | "What have I processed?" |
| checkpoint.json | "Multi-step recovery" |

### 5. Component Reuse
Before creating new connections/nodes/triggers:
```bash
ls "$RESOLVED_STATE_ROOT/workflows/components/connections/"
ls "$RESOLVED_STATE_ROOT/workflows/components/nodes/"
```
Use existing. Update "Workflows Using This" when adding.

## When to load references

- New flow layout or naming → `references/structure.md`
- Node I/O contracts → `references/data-flow.md`
- Resume / dedupe → `references/state.md`
- Retry, rollback, locks → `references/errors.md`
- Connections / triggers / webhook router → `references/components.md`
- Create, cron, archive, debug → `references/lifecycle.md`
- Source ledger → `references/sources.md`
