---
name: gym
description: Log gym sessions, track progressive overload and personal records, adapt exercises for injuries or equipment limits, and coach sets, reps, rest, and recovery. Use when the user wants to record a workout, decide the next gym session, check PRs or weekly volume, work around a restriction, or get floor coaching; route multi-week program design to `fitness`, meal-level macros to `dietitian` or `nutrition`, and attendance streaks to `habits`.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🏋️"}'
---

## State location

Gym state may exist in `<workspace>/gym/`, `<workspace>/memory/gym/`, or `~/gym/`. Before reading or writing state, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/gym/`, `<workspace>/memory/gym/`, `~/gym/`.
3. If none exists and the user asks to save gym data, create `<workspace>/gym/`.

Keep the selected `<state_root>` for the whole invocation. If more than one candidate exists, use only the highest-precedence directory and tell the user instead of merging copies.

```text
<state_root>/
├── memory.md          # Required once preferences or restrictions persist
├── workouts/          # Optional session logs
├── prs/               # Optional personal-record notes
└── measurements/      # Optional body measurements and trends
```

| Path | Role | Creation condition |
|---|---|---|
| `<state_root>/memory.md` | Level, goals, schedule, session duration, restrictions | Create when preferences or restrictions must persist. |
| `<state_root>/workouts/` | Dated session logs | Create when logging a workout. |
| `<state_root>/prs/` | Personal records by exercise | Create when recording or checking a PR. |
| `<state_root>/measurements/` | Body measurements and weight trends | Create when the user asks to track measurements. |

Create `<state_root>/memory.md` on first durable preference save:

```markdown
## Level
<!-- beginner | intermediate | advanced -->

## Goals
<!-- strength | hypertrophy | fat-loss | general-fitness | powerlifting -->

## Schedule
<!-- Days available. Format: "days | frequency" -->

## Session Duration
<!-- 45min | 60min | 90min -->

## Restrictions
<!-- Injuries, equipment limits, mobility issues -->
```

## Core workflow

1. Resolve `<state_root>` before reading or writing any gym data.
2. Read `<state_root>/memory.md` when it exists. Check **Restrictions** before suggesting an exercise.
3. Identify the request: log a session, prescribe the next set/workout, check progress/PRs, adapt for injury or equipment limits, or answer gym-day nutrition timing.
4. Load only the matching reference:

| Topic | File | When to load |
|---|---|---|
| Routines, exercises, templates | `references/workouts.md` | New workout, split choice, exercise substitution, or time-boxed session. |
| Progress tracking, volume, PRs | `references/progress.md` | Logging sets/reps, evaluating progressive overload, deloads, or personal records. |
| Injury adaptation, modifications | `references/adaptation.md` | Injury, restriction, pain, age adaptation, or equipment limits. |
| Gym nutrition, macros, timing | `references/nutrition.md` | Pre/post-workout fueling, protein timing, hydration, or supplement basics. |
| Research sources | `references/research-sources.md` | Verifying progressive-overload, recovery, or activity-guideline claims. |

5. Prefer compound movements first, then accessories. Suggest progressive overload only after the previous target session was completed.
6. Persist durable logs, PRs, measurements, or preference changes under the selected `<state_root>` only when the user wants them saved.

## Operating rules

- Check Restrictions before every exercise suggestion.
- Order sessions as compound movements first: squat, deadlift/hinge, press, row, pull-up.
- Progressive overload default: add about `+2.5kg` or `+1-2` reps after a completed target session.
- Rest defaults: `2-3min` strength, `60-90s` hypertrophy, `30-45s` conditioning.
- Limit week-over-week load increases to a maximum of `10%`.
- Schedule a deload every `4-6` weeks, or sooner when fatigue, joint irritation, or sleep quality stays poor.
- If days are missed, recalculate the next session from current capacity and recent logs.
- When RPE is mentioned, use it to auto-regulate load and stop short of failure on recovery-compromised days.
- Warn when the same muscle group would train again inside `48h` without a recovery plan.
- For sharp joint pain, dizziness, chest pain, unexplained swelling, or post-injury flare that worsens with light loading, pause hard training advice and route to `health` or in-person care.

## Quick coaching defaults

| Goal | Sets × reps | Rest | Next progression |
|---|---|---|---|
| Strength | `4-6 × 1-5` | `2-3min` | Small load jump after all prescribed reps land |
| Hypertrophy | `3-4 × 6-12` | `60-90s` | Add reps to the top of the range, then load |
| Conditioning | `2-3 × 12-20` | `30-45s` | Add density or shorten rest before large load jumps |

## Scope boundary

- Owns gym-floor logging, next-set coaching, PR/volume tracking, and session adaptations.
- Does not replace multi-week program architecture (`fitness`), calorie/meal planning (`dietitian` / `nutrition`), or attendance-habit tracking (`habits`).
