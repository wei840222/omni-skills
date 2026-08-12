# Productivity operating model

Read this reference after the entry workflow identifies a productivity diagnosis, or when the user needs a complete plan, system repair, capacity review, recurring review, or explanation of the method. It preserves the skill's detailed operating model while keeping `SKILL.md` an executable entry point.

## When to use this skill

Use the skill to recover from overwhelm, procrastination, scattered priorities, missed deadlines, broken habits, attention fragmentation, or a productivity system that is no longer trusted. It turns a goal into a project and then into a physical next action, plans a realistic week, and adapts to role-specific constraints such as study, management, caregiving, freelance work, remote work, creative work, ADHD accommodations, burnout, or rest guilt.

Do not use it to operate a calendar API, a live task application, or a single narrow routine when the underlying diagnosis is already known. Route those cases to `calendar-planner`, `task-list`, `time-management`, or `habits` as appropriate.

## Quick diagnostic reference

| Situation | First play |
| --- | --- |
| Overwhelmed or drowning | List commitments, compare them with capacity, then cut or renegotiate one item today. |
| Has time but cannot start | Shrink the work to a two-minute physical action and identify the avoided feeling or ambiguity. |
| Busy but nothing ships | Audit meeting, message, and context-switch load before changing the task list. |
| Everything is urgent | Apply a strict priority order and a WIP limit; urgency belongs to a request, not automatically to the work. |
| List is untrusted | Restore one capture point, a weekly sweep, and explicit removal of stale commitments. |
| Missed deadline | Treat it as an estimation problem; use recorded estimate/actual pairs. |
| Habit keeps collapsing | Define a minimum version and restart after one miss rather than treating the miss as failure. |
| Tired or crashing | Treat recovery and sleep as capacity constraints; see `safety-and-contexts.md` when severe or persistent. |
| Too much on one person's plate | Delegate an outcome with criteria and decision rights, or decline / renegotiate it. |
| Tool or method churn | Diagnose the failure mode before changing apps, methods, or rituals. |
| Emotional rather than structural problem | Use the relevant context guide; do not solve rest guilt or burnout with a bigger schedule. |

For capacity planning, weekly reviews, WIP, estimates, recovery-aware scheduling, and a small planning sequence, also read `workflow-details.md`. For role-specific conditions, read the matching guide in this directory.

## Core rules

1. **Diagnose the bottleneck, then give the smallest intervention.** The common causes are overcommitment, unclear next action, weak boundaries, fragmented attention, bad estimates, and depleted energy. Do not prescribe a whole system when one deadline needs renegotiation.
2. **Capacity is arithmetic, not optimism.** Weekly focus capacity is `focused hours per day × working days − fixed meeting hours`. Measure committed work against that number before making a plan.
3. **Multiply estimates by a calibration ratio.** `ratio = sum(actual) ÷ sum(estimated)` across comparable recent work. Until enough local pairs exist, use 1.5 and label it a placeholder rather than a finding.
4. **Cap work in progress.** Default to three active projects unless the person has chosen another limit. Starting a fourth requires explicitly finishing, parking, delegating, or declining something else.
5. **Use one capture point.** Capture must take less than 30 seconds and be swept at least weekly. Multiple inboxes undermine trust and leave open loops in working memory.
6. **A goal without a next physical action is a wish.** The chain is goal → project → next action; each active item needs an owner and horizon. “Figure out”, “look into”, and “think about” are not startable actions.
7. **Protect one block, not the whole day.** Put demanding work in the user's observed peak window and shallow coordination work in lower-energy windows. A plan that assumes an uninterrupted eight-hour day is invalid.
8. **Never miss twice.** A single miss is normal variation. Restart with the minimum version, not the full version that failed.
9. **Judge the system at review time.** A weekly review that happens is better than a sophisticated system that does not. After repeated skipped reviews, simplify the system instead of adding another tool.

## Bottleneck table

| What the person says | Likely mechanism | First response |
| --- | --- | --- |
| “I am overwhelmed” | Commitments exceed capacity. | Do the capacity arithmetic and cut scope, date, or commitment. |
| “I procrastinate” | High initiation cost or avoided emotion. | Make the first action visible and physical. |
| “I am busy but nothing ships” | Meetings, interruption, or switching fragmentation. | Protect one block and reduce reactive windows. |
| “I keep replanning” | Planning has become avoidance. | Freeze the plan and execute the next physical action. |
| “Everything is a priority” | No priority function or WIP cap. | Rank strictly and park the losers. |
| “I miss deadlines” | Estimates ignore actual experience. | Apply the calibration ratio and buffer. |
| “My list is a graveyard” | Capture is detached from review. | Sweep it, close or defer stale work, and restore a review cadence. |
| “I start strong and quit” | The plan assumes peak energy or lacks a minimum version. | Reduce the habit and plan for recovery. |
| “I cannot rest” | Worth is fused to output. | Use `guilt.md`; do not turn rest into another optimization target. |
| “Normal advice does not work” | Executive function or role constraints invalidate generic advice. | Read the matching context guide. |
| “I do not own my calendar” | The constraint is organizational. | Work on decision rights, influence, and meeting structure rather than personal scheduling. |

When nothing matches, reconstruct one recent day hour by hour. The discrepancy between the reported intent and actual day is often the diagnosis.

## Capacity math

Compute and state these numbers before proposing a plan:

| Number | Formula | Example |
| --- | --- | --- |
| Weekly focus capacity | `focused hours per day × working days − meeting hours` | `3 × 5 − 6 = 9 h` |
| Committed load | `sum(estimate × calibration ratio)` for work due in the horizon | `(2 + 3 + 1) × 1.6 = 9.6 h` |
| Overcommitment | `committed load − capacity` | `9.6 − 9 = +0.6 h`; move one item |
| Safe scheduled hours | `capacity ÷ calibration ratio` | `9 ÷ 1.6 ≈ 5.6 h` |

Unplanned time is buffer, not waste. When the plan exceeds capacity, cut whole items instead of assigning every item an implausible partial allocation.

## Delivery gates

Before delivering advice, a plan, or a system change, verify all of the following:

- The primary bottleneck is named.
- Capacity and committed load are stated when workload is involved; the plan fits by cutting, deferring, delegating, or renegotiating something specific.
- Each estimate uses a calibration ratio whose source is stated.
- Every recommended outcome has a first physical action possible within two minutes.
- Safety, clinical, HR, legal, or employment-risk signals have been routed before productivity tactics.
- Persistent notes are changed only on the user's request and only after `state-format.md` establishes the selected `<state_root>`.

## Defaults and preferences

Until the person states a preference, use these defaults: a weekly horizon; Monday as week start; Friday review; 3 focused hours per workday; one 90-minute deep-work block; WIP limit 3; balanced commitments; and direct, concise coaching.

Adapt the plan to declared preferences for method (GTD, PARA, bullet journal, Kanban, OKR, or none), task tooling, working hours and timezone, hard constraints, safety non-negotiables, desired output detail, review cadence, and willingness to track estimate/actual pairs. Store only a user-confirmed preference, and only when persistence is requested. `state-format.md` owns the portable format and write boundary.

## Traps

| Trap | Why it fails | Do instead |
| --- | --- | --- |
| Building the system before today's problem | System-building becomes productive-looking avoidance. | Solve the live constraint first; persist only the result the user requests. |
| Everything is P1 | A ranking with no losers is not a ranking. | Choose one winner per slot and park the rest. |
| Calendar as task list | A task has no duration until estimated; missed blocks become invisible debt. | Keep actionable work in the chosen state and calendar blocks as time reservations. |
| Ideal-hour estimates | They omit meetings, switching, and recovery. | Apply calibration and compare with actual capacity. |
| Daily replanning | It resets progress tracking and avoids execution. | Plan per horizon; mid-horizon changes are cuts, not complete rewrites. |
| Thirty-day or all-or-nothing streaks | One miss becomes evidence of failure. | Use a minimum version and never-miss-twice restart. |
| Tool churn | Moving tools resets trust without changing the failure mode. | Change tools only when the diagnosed mechanism requires it. |
| Tracking without review | Data becomes another abandoned commitment. | Track only information that has a defined review. |
| Keeping stale commitments | Dead items make the live list untrustworthy. | Maintain an explicit kill / renegotiation list. |
| Cutting sleep to make room | The capacity instrument itself degrades. | Treat sleep as capacity, not a competitor for it. |
| Delegating without decision rights | Work returns for clarification and creates a bottleneck. | Delegate outcome, criteria, authority, and date. |
| Motivation for a structural problem | It locates fault in the person instead of the workload. | Fix the arithmetic, boundaries, or organizational constraint. |
| Optimizing during burnout | More efficiency accelerates depletion. | Subtract demands and seek appropriate support first. |

## Method trade-offs

- **GTD vs OKR:** use bottom-up capture when work leaks; use top-down goals when completed work lacks direction. Do not force both review cadences onto a person who cannot maintain them.
- **Time blocks vs list-driven days:** strict blocks make capacity visible but fail under high interruption rates. Protect one window and use a list for the rest when interruptions are frequent.
- **Pomodoro vs long sessions:** short timers can lower initiation cost; extend them once flow begins, especially for creative or debugging work.
- **Morning routines:** protect the person's actual peak window rather than prescribing an early schedule.
- **Deadline pressure:** acknowledge that it may help initiation while naming its usual costs: no revision pass, recovery debt, and unmeasured error.
- **Measurement:** estimate/actual pairs improve planning, but excessive tracking can become surveillance or a chore. Track only what the person accepts and reviews.

## Privacy and related skills

This skill does not need network access. Do not store credentials, financial account details, clinical inferences, or private third-party information. If the user requests state changes, use the selected `<state_root>` and preserve only the minimum user-confirmed information needed to plan.

Use `task-list` for day-to-day list operation, `calendar-planner` for calendar execution after planning, `goals` for deeper goal design, and `time-management` or `habits` for a narrow mechanism once diagnosis is complete.
