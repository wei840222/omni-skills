---
name: loop
description: >
  Run controlled iterative agent loops until explicit success criteria pass,
  with a hard max of 10 iterations, portable state under `<state_root>/loop/`,
  and learnings carried across attempts. Use when a task has clear verify
  criteria but an uncertain path, a previous attempt failed with a fixable
  error, or the user says keep trying until a check passes. Prefer `cycle`
  for multi-phase Plan→Do→Check→Act designs, and `workflow` when building
  reusable automated pipelines rather than a single iterative attempt loop.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔄"}'
  related-skills: '{"cycle":"Design multi-phase Plan→Do→Check→Act processes; a cycle phase may embed loop until that phase passes.","workflow":"Build executable automated pipelines with components, triggers, and flock once iteration belongs inside a reusable flow."}'
---

## State location

Loop runtime state may exist in `<workspace>/loop/`, `<workspace>/memory/loop/`, or `~/loop/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/loop/`, `<workspace>/memory/loop/`, `~/loop/`.
3. If none exists and state must be created, default to `<workspace>/loop/` after the user consents.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/loop/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Never write the literal string `<state_root>` to disk. Treat legacy `~/Clawic/data/loop/` paths as migration sources only—ask before migrating.

On first durable use, create only the paths needed under `<state_root>/loop/`.

## Architecture

```
<state_root>/loop/
├── active.json              # Currently running loops
├── history/                 # Completed loop logs
│   └── {loop-id}.json
└── learnings.md             # Optional cross-loop patterns
```

## Role

**Loop** means one bounded attempt cycle: task + success criteria → execute → verify → record learnings → retry or stop. It is not open-ended exploration, not multi-phase process design (`cycle`), and not a reusable automation package (`workflow`).

## Workflow

1. Capture task, success criteria, max iterations (default 5, hard max 10), and optional verify command.
2. Resolve `<state_root>` before any state read/write.
3. For each iteration: carry only task, criteria, count, and learnings; execute; verify; append history; decide pass / retry / stop.
4. Stop on success, max iterations, or unrecoverable error (missing dependency, permission denied).
5. On max-without-success: summarize attempts, name the common failure pattern, and recommend a different approach or manual intervention.

## Load the relevant reference

| Reference | Load when |
| --- | --- |
| `references/examples.md` | Need concrete loop shapes (tests, performance, creative iteration). |
| `references/memory.md` | Deciding what to persist between iterations or estimating cost. |
| `references/sources.md` | Re-checking iteration / retry / stop-rule guidance against primary docs. |

## Critical rules

1. **Criteria first** — do not start a loop without explicit success criteria.
2. **Hard cap** — never exceed 10 iterations; default to 5 unless the user sets another value ≤10.
3. **Fresh context** — carry only task, criteria, iteration count, and learnings; drop full conversation and failed-code noise.
4. **Verify before retry** — each attempt must check the stated criteria (command exit, metric, or user approval).
5. **No silent scope expansion** — Git commits, production deploys, and system-configuration changes stay out of scope unless the user authorizes that specific action.
6. **Portable state only** — all durable loop files live under `<state_root>/loop/`; never treat `~/Clawic/data/loop/` as the active root.
7. **Route adjacent asks** — multi-phase process design → `cycle`; reusable pipelines / cron / flock → `workflow`.
