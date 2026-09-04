---
name: habits
description: Design, track, and repair recurring habits, routines, completion rates, and relapse plans. Use when the user wants to start or resume a daily practice, log a completion or miss, review a streak or 28-day rate, diagnose a failing routine, or change an unwanted habit. Route goal-setting to `goals`, whole-life capacity planning to `productivity`, and exercise programming to `fitness`.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"✅"}'
  related-skills: '{"coach":"Provides accountability conversations when a habit problem is not primarily mechanical.","fitness":"Designs the exercise program once the recurring exercise habit is stable.","goals":"Turns outcomes and milestones into goals; habits owns the recurring behavior layer.","journal":"Captures reflective context and the narrative portion of reviews.","productivity":"Handles whole-life capacity, priorities, and overwhelm beyond one recurring behavior."}'
---

## State location

Resolve `<state_root>` before reading or writing habit data:

1. Use a host- or user-configured habit-state path when one is explicitly supplied.
2. Otherwise use the first existing directory in this order: `<workspace>/habits/`, `<workspace>/memory/habits/`, then `~/habits/`.
3. If none exists and the user asks to persist habit data, create `<workspace>/habits/`.

Use only the selected `<state_root>` for this invocation. If more than one candidate exists, use the highest-precedence directory and report the conflict; keep the directories separate rather than merging or moving data.

```text
<state_root>/
├── config.yaml                 # Optional preferences; create after the user states one
├── memory.md                   # Required when a durable habit record is created
└── logs/
    └── YYYY-MM.md              # Create when recording a completion or miss
```

External shared records, such as an accountability contact, health measurement, or paid stake, are outside this state tree. Write one only after the host provides its path and the user consents to that specific external write; name the destination and minimum content before writing.

## Core workflow

1. Resolve `<state_root>`. Read `<state_root>/config.yaml`, `<state_root>/memory.md`, and the current `<state_root>/logs/YYYY-MM.md` only when they exist. Treat an absent state tree as a blank start, not as evidence of performance.
2. If the request includes hazardous substance withdrawal, disordered-eating signals, self-harmful tracking, injury-driven exercise, or persistent low mood, load `references/red-flags.md` and use its safety route before habit coaching.
3. For a new or redesigned habit, define the six fields in **Habit anatomy**. For status questions, read the current log before reporting a rate, streak, or trend. For a failure diagnosis, load `references/traps.md`; change one condition at a time.
4. Record a durable completion, miss, definition, pause, retirement, review, or plan in the selected state tree. Load `references/output-gates.md` before closing a check-in, status report, or new-habit design.
5. Load the matching reference only when its branch applies:

| Reference | Load when |
|---|---|
| `references/configuration.md` | Setting tracking preferences, cadence, or defaults. |
| `references/domain.md` | Explaining the evidence behind habit design or checking the cited source material. |
| `references/output-gates.md` | Reporting a number, proposing a habit, or closing a check-in. |
| `references/red-flags.md` | A health, withdrawal, distress, or compulsive-tracking signal appears. |
| `references/traps.md` | A routine is failing or the user proposes a tracking/streak tactic. |
| `references/where-experts-disagree.md` | The user asks to weigh rate versus streak, identity framing, abstinence, or rewards. |

## When to use

- Turn a vague outcome into a recurring, observable behavior with a cue.
- Log completions and misses; calculate a completion rate or streak from the log.
- Repair a broken streak, long lapse, routine, or unwanted habit.
- Run a daily check-in, weekly review, or retirement decision.
- Maintain a habit through travel, illness, shift work, caregiving, or changing capacity.

This skill owns recurrence, not general goal-setting, whole-life productivity, sleep treatment, clinical care, or workout programming.

## Habit anatomy

Define these six fields before tracking a new habit:

| Field | Requirement |
|---|---|
| Name | An observable action, such as "walk 20 minutes," rather than an outcome. |
| Type | `do` for an action or `avoid` for a clean day plus a substitution. |
| Cue | An existing action with a place and time. |
| Minimum | The worst-day version, small enough to start in under two minutes. |
| Frequency | `daily`, `weekdays`, `N×/week`, `weekly`, or `every-N-days`. |
| Why | One sentence in the user's own words that still matters on a hard day. |

Use the cue form: *after `<existing anchor>`, I will `<minimum>` in `<location>`*.

## Operating rules

1. Track behavior rather than an outcome. Convert "lose 5 kg" into an observable action, or hand the outcome to `goals`.
2. Use the minimum as the tracked unit. More effort remains welcome, but it does not turn one completion into a larger score.
3. Lead status reports with the rolling 28-day completion rate: `completions ÷ scheduled days`; state the streak as secondary context. With fewer than 14 scheduled days, report that the sample is still small.
4. A single miss is data. After two consecutive misses, diagnose one failure class and adjust one condition. After three consecutive misses, redefine or pause the habit instead of silently accumulating misses.
5. Start one new habit at a time. Keep no more than three active habits by default; add another only after every active habit is at least 80% over the relevant review window.
6. Make a weekday pattern claim only after four samples of that weekday. Present automaticity as individually variable rather than assigning a fixed date.

## Failure classes

| Signal in the log | First repair |
|---|---|
| The person keeps forgetting | Replace the missing cue with a specific existing action. |
| The pattern fades late in the week | Move it earlier or create a smaller late-week version. |
| It collapses after the first weeks | Reduce the floor to the actual worst-day version. |
| Misses cluster on a weekday | Create a context-specific minimum for that day. |
| Every habit drops together | Enter maintenance mode with one keystone habit and reassess capacity. |
| The behavior is resented | Test a substitute that serves the same `Why` while retaining the cue and minimum. |

Use `references/traps.md` for the fuller decision guidance and `references/red-flags.md` whenever the signal is clinically sensitive.
