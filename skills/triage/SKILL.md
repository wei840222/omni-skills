---
name: triage
description: >
  Prioritize competing tasks, bugs, tickets, and interruptions into P0-P3 by
  cost of delay and working-hours slack. Use when work piles up, a request
  arrives mid-task, deadlines conflict, alerts need a priority, or the user
  says urgent, ASAP, EOD, drop everything, or no rush. Learns confirmed
  priority rules from corrections. Not for effort estimation or roadmap planning.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🚦"}'
  related-skills: '{"inbox":"Processes message streams before items become triaged tasks.","task-list":"Maintains the durable queue once triage has assigned levels.","productivity":"Diagnoses whole-life capacity and sustainable plans when triage alone cannot absorb the load.","time-management":"Protects day plans and deep-work blocks that P2/P3 must not interrupt."}'
---

# Triage

Classify incoming work into P0-P3 by **cost of delay**, decide what interrupts
now, and learn the user's real priority rules only after explicit confirmation.

## State location

Triage state may exist in `<workspace>/triage/`, `<workspace>/memory/triage/`,
or `~/triage/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/triage/`, `<workspace>/memory/triage/`, `~/triage/`.
3. If multiple candidates exist, use only the highest-precedence directory,
   report the split state, and leave lower-precedence directories unchanged.
4. If none exists and the user confirms a standing rule or stated preference
   that must persist, create `<workspace>/triage/`.
5. If the host cannot supply `<workspace>`, use an existing `~/triage/` only;
   otherwise ask for a state location before creating data.
6. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.

Learned rules and stated preferences live under `<state_root>/` (created on
first confirmed rule or stated preference). Nothing is stored without the
user's explicit yes. If older data exists only at `~/clawic/triage/` or
`~/Clawic/data/triage/`, move it into the resolved `<state_root>/` after the
user confirms, and say in one line that you moved it and from where.

```text
<state_root>/
├── config.yaml    # working_hours, triage_mode, interrupt_floor, …
└── patterns.md    # confirmed rules, override log, sender calibration
```

## When to use

- Several tasks compete and an order must be chosen
- A new request arrives mid-task and interrupt vs park must be decided
- A pile needs sorting: inbox after time away, ungroomed backlog, ticket queue
- A bug, ticket, alert, or security report needs a priority
- Priority language appears: "urgent", "ASAP", "drop everything", "no rush"
- The user reorders the queue — treat that as training data for the ladder
- Exclude effort estimation and roadmap planning: triage decides *when*, not *how long*

## Quick reference

| Situation | Play |
|-----------|------|
| "Drop everything and X" | Interrupt when it passes the P0 test; name what gets paused |
| Two tasks both claim P0 | Escalate sequencing — two "drop everything" cannot both win |
| Must interrupt mid-task | Park first: resume note + WIP preserved, then switch (`references/interrupts.md`) |
| Sounds urgent, no deadline, no accumulating damage | Cap at P1; one closed question: "Is anyone blocked right now?" |
| Mixed signals ("urgent but no rush") | Ask — the contradiction is the signal; pick one reading |
| Deadline exists but looks far | Compute slack (Core Rules #2); slack under one working day → P1 today |
| Deadline looks fake or negotiable | Find what consumes the output (`references/deadlines.md`) |
| Slack already negative | Negotiate scope → sequence → time (`references/deadlines.md`) |
| Bug or ticket arrives | Severity ≠ priority: severity × reach × trend (`references/bugs.md`) |
| Pile of unsorted items | Two-pass sweep: classify all, then order (`references/batch.md`) |
| User corrects a priority | Record it; on the 2nd same-direction correction, propose a standing rule (`references/patterns.md`) |
| Confirmed rule matches | Apply and cite: "Deploy issue → P0 (your standing rule)" |
| New fact arrives | Re-triage the whole queue |
| Else | Run level tests top-down; torn between adjacent levels → Core Rules #3 |

Depth on demand: `references/signals.md` · `references/patterns.md` ·
`references/interrupts.md` · `references/batch.md` ·
`references/deadlines.md` · `references/bugs.md` · `references/sources.md`.

## Priority levels

Run tests top-down; first yes wins. Score verifiable states, not tone.

| Level | Test (yes → this level) | Response | Examples |
|-------|-------------------------|----------|----------|
| P0 | Does damage accumulate every minute this waits? | Interrupt current work now | Production down, active breach, data loss in progress |
| P1 | Is a person or deliverable stalled today? | Next work-unit boundary, same day | Blocked teammate, client waiting, due-today deadline |
| P2 | Dated or clearly valuable, but nobody stalls today? | Scheduled queue, with a date | Reviews, planning, deadlines beyond today |
| P3 | Would anyone notice if this were skipped? (barely) | Backlog, batch-processed | Ideas, "someday", minor optimizations |

## Core rules

1. **Priority = cost of delay.** Effort and loudness are separate inputs. A hard task nobody waits on is P2; a 5-minute unblock for a stalled teammate is P1. Within a level, prefer highest cost of delay per unit of effort (WSJF); when costs look equal, shortest job first. See `references/sources.md`.
2. **Deadline urgency is slack in working hours.** Slack = working time until deadline − remaining work, counted only inside `working_hours`. Friday deadline + 3 days of work, seen Wednesday = negative slack = P1 today. Recompute when scope grows; edge cases in `references/deadlines.md`.
3. **Misclassification is asymmetric.** A false P0 costs one interruption; a missed P0 costs the whole damage window. Torn between adjacent levels *with* concrete evidence → take the higher. Tone only → take the lower and label it: "Queued as P2 — say the word if it's blocking."
4. **Ask only at the P0/P1 boundary.** One closed question there beats a wrong guess. At P2/P3, pick, state the assumption, move on.
5. **Learn only through observe → propose → confirm.** One correction = record. Two same-direction corrections = propose. Apply automatically only after an explicit yes, and cite the rule. Full ladder in `references/patterns.md`.
6. **P0 is rare by construction.** If over a week more than ~1/3 of items land P0/P1, the bar drifted — re-anchor on the level tests.
7. **Re-triage on state change.** Triggers: deadline revealed or moved, blocker cleared, scope change, new P0. Each re-sorts the whole queue.

## Queue discipline

- P0 interrupts mid-task (`interrupt_floor` can extend this to P1). P1 waits for the current unit of work to finish. If current work is P2/P3, switch at the next safe point. Mechanics: `references/interrupts.md`.
- Order within a level: confirmed user rules first, then ascending slack, then arrival order.
- Announce changes, not steady state: "New P0 — pausing X. Queue now: [incident, review, docs]."
- A dated P2 gets scheduled when it enters the queue. A P2 that ages into a P0 without new facts is a triage failure — log it.
- When demand exceeds capacity, propose drops by name (`references/batch.md`, Overflow).

## Output gates

Before emitting a priority or reordered queue:

- Is every P0 justified by accumulating damage or a level test?
- Did I check `<state_root>/patterns.md` for a confirmed rule before defaults?
- Am I auto-applying any rule the user has not confirmed? If yes → propose instead.
- If queue order changed, did I name what got bumped?
- If interrupting, does the paused task have a resume note (`references/interrupts.md`)?

## Configuration

Defaults apply until the user states a preference; store them in
`<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| working_hours | text (e.g. "Mon-Fri 09:00-18:00") | Mon-Fri 09:00-18:00 | Hours slack counts (Core Rules #2) |
| triage_mode | interrupt \| batch | interrupt | batch defers non-P0 classification to sweeps (`references/batch.md`) |
| interrupt_floor | P0 \| P1 | P0 | Lowest level allowed to interrupt mid-task |
| sweep_times | list of times | none | With batch mode: when sweeps run; empty = on request |
| announce_style | full \| minimal | full | full names every bumped item; minimal reports only the new top |

Preference areas recorded in `config.yaml` when stated:

- **Labels**: reporting scheme (P0-P3, High/Normal/Low, MoSCoW) — announcement only
- **Risk posture**: tie-break when torn without evidence — Core Rules #3 default
- **Sources**: paging-grade vs digest channels — overrides `references/signals.md`
- **Cadence**: grooming day, drift-check day, aging thresholds — `references/batch.md`
- **Escalation**: whether the P0/P1 question goes to the user or a named delegate

## Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| Sender rank as urgency | Rank predicts importance, not cost of delay | Run the level tests; learn sender rules only via the ladder |
| Severity as priority | Impact alone misorders the queue | Score severity × reach × trend (`references/bugs.md`) |
| Newest-task pull | Arrival time ≠ cost of delay | Slot by test result, re-sort, report position |
| Doing work mid-triage | Each quick fix restarts sweep context | Classify everything first, then work the ordered queue |
| Averaging mixed signals | "Urgent but no rush" as P1.5 satisfies neither | Ask; pick one reading |
| Escalating on repetition | A third mention is frustration | Acknowledge, give queue position and expected start |
| Demoting polite requests | Soft phrasing can still mean "today" | Check for a date; calibrate per sender (`references/signals.md`) |
| Rolling a passed date forward | Hides a decision from the user | Re-triage the day the date passes (`references/batch.md`) |

## Where experts disagree

- **Interrupt-driven vs batch triage.** Batch wins when true P0s are rare and deep work dominates; interrupt-driven wins for on-call. Record the choice as `triage_mode`.
- **FIFO vs WSJF within a level.** FIFO reads as fair to watchers; WSJF delivers more value when only outcomes matter. Choose by who is watching.

## Routing to sibling skills

- Message-stream sorting before tasks exist → `inbox`
- Durable list capture, views, recurrence → `task-list`
- Whole-life overwhelm / sustainable plan → `productivity`
- Day plan and deep-work protection → `time-management`

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/signals.md` | Urgency language, senders, sources, time modifiers |
| `references/patterns.md` | Learning ladder, memory format, drift, override log |
| `references/interrupts.md` | Safe switch, parking/resume, stacked P0s, two-minute rule |
| `references/batch.md` | Sweeps, piles, grooming, overflow |
| `references/deadlines.md` | Slack edge cases, real vs stated, negotiation |
| `references/bugs.md` | Bug/ticket/SLA/alert priority |
| `references/sources.md` | Before restating WSJF, interruption recovery, or GTD two-minute facts |
| `test-prompts.json` | Evaluation harness only — not runtime guidance |
