---
name: productivity
description: Diagnose a failing personal productivity practice and create the smallest sustainable plan. Use for overwhelm, procrastination, missed deadlines, scattered work, weekly planning, focus, habits, or workload triage; not for calendar API automation or operating a task app.
metadata:
  version: "1.0.6"
  openclaw: '{"emoji":"⚡"}'
  related-skills: "{\"calendar-planner\":\"Automates calendar services after this skill has defined the work and time blocks.\",\"goals\":\"Extends goal and milestone design beyond this skill's goal-to-project-to-action chain.\",\"habits\":\"Operates a narrow habit-tracking practice when diagnosis is already complete.\",\"task-list\":\"Operates a day-to-day task list after this skill has repaired priorities and workflow.\",\"time-management\":\"Runs time-blocking mechanics when the user needs scheduling rather than diagnosis.\"}"
---

## State location

Productivity state may exist in `<workspace>/productivity/`, `<workspace>/memory/productivity/`, or `~/productivity/`.

Before a state read or write, resolve `<state_root>` once for the invocation:

1. Use a user- or host-configured state path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/productivity/`, `<workspace>/memory/productivity/`, `~/productivity/`.
3. If multiple candidates exist, use only the highest-precedence directory, report the split state, and leave lower-precedence roots unchanged.
4. If none exists and the user explicitly wants persistent notes, create `<workspace>/productivity/`.

If the host cannot identify `<workspace>`, use an existing `~/productivity/` only; otherwise request a state location before creating notes. Keep all state operations in the selected `<state_root>`.

## Workflow

1. Establish the immediate outcome: one decision, one next action, or a bounded plan. Read existing `<state_root>/memory.md` only when it exists and materially changes the advice.
2. Diagnose one primary bottleneck: capacity, unclear action, weak boundary, attention fragmentation, estimation, or depleted energy.
3. State the arithmetic when load is involved. `committed load = sum(estimate × calibration ratio)`; compare it with available focused hours. Use a provisional 1.5 ratio until enough local estimate/actual pairs exist.
4. Choose the smallest intervention that changes the bottleneck: cut or renegotiate work, write a physical next action, protect one focus block, reduce WIP, or repair recovery.
5. Deliver an executable plan with an owner, time horizon, and first physical action. A plan with no action possible in the next two minutes is incomplete.
6. When the user asks to persist a result, read `references/state-format.md` and make the smallest requested update under `<state_root>`; report the exact file and change.

## Missing-input fallback

Use the available facts first; collect only the missing input that changes the next decision.

| Missing input | Provisional action | Next question when needed |
| --- | --- | --- |
| Focused hours | Reserve one protected block and defer detailed allocation. | "How many focused hours are actually available before the deadline?" |
| Estimates | Choose one must-win outcome and split it into a two-minute action. | "What is the smallest deliverable that counts as done this week?" |
| Calibration pairs | Apply the 1.5 provisional ratio and label it as a placeholder. | "Which two recent completed tasks have both an estimate and an actual duration?" |
| Deadline or consequence | Keep the item out of the committed plan. | "When is it due, and what changes if it moves?" |

## Plan validity

Treat a plan as ready when it meets all of these conditions:

- The committed load, including the calibration ratio, fits available focused hours and leaves a buffer.
- Every active outcome has one owner, one horizon, and one two-minute physical next action.
- Sleep, care, health, and stated non-negotiables are represented as capacity constraints.
- Persistent notes are written only after the user requests them and the selected `<state_root>` is known.
- Clinical, crisis, HR, legal, and employment-risk signals are routed to the relevant human support before productivity tactics.

## Safety boundary

Pause productivity coaching and use `references/safety-and-contexts.md` when the user describes self-harm, broad loss of interest, severe exhaustion, panic, or a workplace process that needs clinical, emergency, HR, legal, or managerial support. The skill can support planning around professional care; it does not diagnose or replace it.

## Reference routing

Load one reference only after the workflow identifies the relevant branch; the entry workflow remains the default for a straightforward request.

- Read `references/workflow-details.md` for capacity planning, weekly reviews, WIP, estimates, or recovery-aware scheduling.
- Read `references/state-format.md` only for persistent notes, migrations, or reviewing an existing local productivity record.
- Read `references/safety-and-contexts.md` for role constraints (student, manager, executive, parent, freelancer, founder, remote, creative), ADHD accommodations, burnout, or rest guilt.
- Read `references/knowledge-sources.md` only when auditing or explaining the factual basis for the safety and context guidance.

## Boundaries

Use `calendar-planner` only after the work and blocks are already defined. Use `task-list`, `habits`, or `time-management` when a user wants a narrow mechanism operated rather than diagnosis of a failing system. Keep credentials, financial account details, private third-party notes, clinical inferences, and unrelated external state out of `<state_root>`.
