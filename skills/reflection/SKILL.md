---
name: reflection
description: >
  Run continuous self-reflection and lesson retention: evaluate deliverables
  against 7 dimensions before sending, log post-mistake corrections, detect
  recurring blind spots, and inject past lessons before repeating them. Use
  for pre-delivery QA, after user corrections, weekly pattern review, or when
  a heavier retrospective is needed once work is complete. Prefer
  `self-criticism` for short mid-task breakpoints, `self-improving` for durable
  execution lessons after outcomes, `decide` for consequential branch choices,
  and `memory` / `learning` when the need is fact storage or study practice.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🪞","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"self-criticism":"Insert compact mid-task critique at branching or friction breakpoints; use reflection for heavier post-task retrospectives.","self-improving":"Compound durable execution lessons after outcomes; reflection owns the 7-dimension loop and pattern log.","decide":"Log consequential branch choices; reflection logs how work was evaluated, not which option to pick.","memory":"Long-term factual continuity; reflection stores evaluation lessons, not durable world facts.","learning":"Study and spaced practice; reflection captures agent performance lessons from corrections."}'
---

# Reflection

Pause before delivery, capture corrections, and surface recurring patterns so
the same miss does not return. State lives under a resolved `<state_root>`
outside this package. Never write runtime state into the skill tree.

## State location

Reflection state may exist in `<workspace>/reflection/`,
`<workspace>/memory/reflection/`, or `~/reflection/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/reflection/`, `<workspace>/memory/reflection/`, `~/reflection/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable state must be created, default to
   `<workspace>/reflection/` when `<workspace>` is available; otherwise ask for
   a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.
Typical layout (create children only when needed):

```text
<state_root>/
├── memory.md        # Status, preferences, streak, category counts
├── reflections.md   # Correction log (most recent first)
├── patterns.md      # Detected recurring blind spots
└── archive/         # Monthly archives of processed reflections
```

If older notes exist only at `~/Clawic/data/reflection/`, propose a
copy/validation/cutover plan and wait for confirmation before any migration.
Never write the literal string `<state_root>` to disk. Create or update state
only after the user opts in. Store evaluation lessons only—no credentials or
unrelated private data.

## When to use

- Pre-delivery QA on code, architecture, strategy, or any deliverable the user
  will act on
- After a user correction (`actually…`, `that's wrong`, frustration signals)
- After five or more logged reflections, on weekly review, or when the same
  category appears three or more times
- When a completed task needs a heavier retrospective than a mid-task critique

Prefer adjacent skills when they fit better:

- Mid-task breakpoint critique before branching → `self-criticism`
- Durable execution lessons after outcomes → `self-improving`
- Consequential branch choices → `decide`
- Long-term fact store → `memory`
- Study / spaced practice → `learning`

## Load order

1. `SKILL.md` state rules and operating path (always)
2. `references/dimensions.md` for the 7-dimension scan
3. `references/prompts.md` when stuck on root-cause or weekly review wording
4. `references/setup.md` and `assets/data-templates.md` only on first setup
5. `references/sources.md` when verifying research provenance

## Operating path

1. Detect the trigger: pre-delivery, post-mistake, or pattern review.
2. Resolve `<state_root>`; if missing and durable logging is needed, follow
   `references/setup.md` with explicit approval.
3. Before significant work, scan `<state_root>/patterns.md` and surface any
   relevant active lesson in one short line.
4. For pre-delivery, run the 7-dimension checklist from
   `references/dimensions.md` (~30 seconds). Any dimension below 7/10 → fix
   before delivering.
5. On user correction: acknowledge, analyze root cause, then append to
   `<state_root>/reflections.md` using the Miss / Root / Fix shape. Categories:
   `technical`, `communication`, `assumptions`, `process`, `scope`.
6. After five reflections, or when a category repeats three or more times,
   promote a prevention rule into `<state_root>/patterns.md` and track streak.
7. Archive processed entries to `<state_root>/archive/YYYY-MM.md` when the live
   log exceeds the archive threshold (default 20). Keep
   `<state_root>/reflections.md` lean.

## Quick reference

| Topic | File | Load when |
|-------|------|-----------|
| 7-dimension checklist | `references/dimensions.md` | Pre-delivery scan |
| Analysis prompts | `references/prompts.md` | Root-cause or weekly review |
| First activation | `references/setup.md` | Missing state or first use |
| File templates | `assets/data-templates.md` | Seeding memory / reflections / patterns |
| Sources | `references/sources.md` | Verifying research provenance |

## Core rules

1. **Check lessons before acting.** Scan `<state_root>/patterns.md` before
   significant work and mention a relevant prevention rule naturally.
2. **Score before sending.** Use the seven dimensions; fix any score below 7/10
   before delivery.
3. **Log every correction.** Pause, acknowledge, write Miss / Root / Fix to
   `<state_root>/reflections.md` before the session ends.
4. **Promote patterns.** Same category three or more times → create or update a
   prevention rule in `<state_root>/patterns.md`.
5. **Archive monthly.** Move processed reflections to
   `<state_root>/archive/YYYY-MM.md`.
6. **Track streaks.** Days since repeated mistake; reset on recurrence.

## Common traps

| Trap | Better move |
|------|-------------|
| Reflecting without logging | Write the Miss / Root / Fix entry before the session ends |
| Vague root causes | Name the assumption and the missed signal |
| Description without prevention | Add the smallest rule that would have blocked the miss |
| Ignoring repeats | Treat three same-category hits as a pattern, not noise |
| Over-scanning | Keep pre-delivery to ~30 seconds; deepen only when a score is low |
