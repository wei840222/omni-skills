---
name: self-criticism
description: >
  Insert breakpoint self-critique before branching work, after user friction,
  and at risky handoffs so agents catch frame errors early. Use at inflection
  points where one wrong assumption would multiply into downstream rework.
  Prefer `self-improving` for durable execution lessons after outcomes,
  `proactivity` for momentum and next-move anticipation, and `reflection` for
  heavier retrospective loops once the task is complete.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧪","configPaths":["<state_root>/"]}'
  related-skills: '{"self-improving":"Compound durable execution lessons and corrections after outcomes.","proactivity":"Anticipate next moves and recover fragile context without mid-task critique.","agent":"Frame a single agent operating style when the need is identity rather than breakpoints.","agents":"Design multi-agent memory and control loops beyond one critique habit.","reflection":"Run heavier post-task retrospective analysis when a compact breakpoint is not enough."}'
---

# Self-Criticism

Insert a **short critique at breakpoints** so a weak frame is revised before it
spreads into tickets, edits, handoffs, or external actions.

This skill is stateful. Trigger memory lives under a resolved `<state_root>`
outside the package. Never write runtime state into this skill package.

## State location

Self-criticism state may exist in `<workspace>/self-criticism/`,
`<workspace>/memory/self-criticism/`, or `~/self-criticism/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/self-criticism/`, `<workspace>/memory/self-criticism/`, `~/self-criticism/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to
   `<workspace>/self-criticism/` when `<workspace>` is available; otherwise ask
   for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.
Typical layout (create children only when needed):

```text
<state_root>/
├── memory.md       # Durable trigger map, depth preferences, integration status
├── checkpoints.md  # Named breakpoint prompts by workflow phase
├── incidents.md    # Late catches that teach a better insertion point
└── archive/        # Resolved incidents and retired checkpoints
```

Create or update state only after the user opts in. Store trigger timing and
critique-depth preferences only—no credentials, private third-party data, or
unrelated personal details.

## When to use

- Work is about to branch into subtasks, commits, or delegated packets
- Evidence or user friction contradicts the current frame
- The next move is irreversible, external, or expensive to unwind
- A handoff needs a clean frame before another agent or final answer

Prefer adjacent skills when they fit better:

- Durable corrections that should compound across sessions → `self-improving`
- Anticipating next moves / recovering interrupted context → `proactivity`
- Single-agent operating identity → `agent`
- Multi-agent system design → `agents`
- Broad post-task retrospective → `reflection`

## Load order

1. `SKILL.md` state rules and operating path (always)
2. Matching trigger family in `references/triggers.md` when the breakpoint is unclear
3. `references/levels.md` when choosing critique depth
4. `references/domain.md` for the full rule/trap set
5. `references/routing.md` / `references/boundaries.md` before writing state
6. `references/setup.md` and `assets/data-templates.md` only on first setup

## Operating path

1. Detect a breakpoint (branching, commitment, surprising evidence, user friction, or risky handoff). Load `references/triggers.md` when the family is unclear.
2. Read `<state_root>/memory.md` and only the smallest relevant lines from `<state_root>/checkpoints.md` when state exists.
3. Choose light / standard / deep depth from `references/levels.md` by blast radius.
4. Ask the smallest hard questions that can catch the likely frame error; if the frame fails, rewrite the plan before expanding work (`references/domain.md`).
5. After friction or late catches, record a reusable trigger lesson in `<state_root>/` using `references/routing.md` and `references/boundaries.md`.
6. On first setup or missing state, follow `references/setup.md` and seed files from `assets/data-templates.md` with explicit approval before writing SOUL/AGENTS.

## Quick reference

| Topic | File | Load when |
|-------|------|-----------|
| Domain rules and traps | `references/domain.md` | Need full rule set or trap table |
| Trigger families | `references/triggers.md` | Unsure whether this is a breakpoint |
| Critique depth | `references/levels.md` | Choosing light/standard/deep |
| Memory routing | `references/routing.md` | Writing a durable lesson |
| Boundaries | `references/boundaries.md` | Avoiding noisy critique or over-logging |
| Setup / SOUL+AGENTS | `references/setup.md` | First use or missing state |
| File templates | `assets/data-templates.md` | Seeding memory/checkpoints/incidents |
| Sources | `references/sources.md` | Verifying research provenance |
