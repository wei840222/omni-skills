---
name: duolingo
description: >
  Run a multi-topic spaced-repetition learning OS with per-topic namespaces,
  daily micro-lesson loops, review-before-new queues, XP/hearts/streak economy,
  and optional AGENTS router snippets. Use when the user wants Duolingo-style
  practice across one or more subjects, asks to start/continue a learning streak,
  place into a topic, rotate English+cooking-style tracks, or recover after a
  missed day. Prefer `learning` for a single live teach-me session without a
  durable multi-topic OS; prefer `learn` / `studying` for long curriculum or exam
  grids; prefer `spaced-repetition` / `flashcards` / `anki` when the deliverable
  is an SRS schedule or deck rather than interactive loops.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🦉"}'
  related-skills: '{"learning":"Live teach-me sessions without a durable multi-topic learning OS.","learn":"Multi-week self-directed curriculum and exit tests rather than daily micro-loops.","studying":"Exam countdowns and coursework revision grids instead of streaked practice tracks.","spaced-repetition":"Long-horizon SRS scheduling and card review ownership outside interactive lessons.","flashcards":"Atomic card authoring when the deliverable is a deck, not a lesson loop.","anki":"Anki/deck-manager workflows beyond one-session miss export.","tutor":"Multi-learner tutoring profiles and parent oversight rather than a personal Learning OS.","coach":"Goal coaching and accountability without subject lesson loops.","habits":"Habit streaks alone when no curriculum or review queue is needed."}'
---

## When to Use

Use this skill when the user wants a **durable, multi-topic Learning OS**:

- "start a Duolingo-style track for French / cooking / finance"
- practice, quiz, review, or continue a named learning topic with streak/XP
- place into a new subject, then run 60–90s micro-loops
- rotate several active topics in one day without mixing state files
- recover after a missed day without deleting motivation

Route away when the primary task is:

- one-shot teach-me / ELI5 without durable OS state → `learning`
- multi-week curriculum / exit test ownership → `learn`
- exam calendar or coursework grid → `studying`
- SRS schedule or deck authoring alone → `spaced-repetition` / `flashcards` / `anki`
- multi-learner tutoring profiles → `tutor`
- goal coaching without lesson content → `coach`
- habit streak with no curriculum → `habits`
- SaaS churn / NRR retention → `retention` (unrelated product skill)

This skill is a local Learning OS inspired by spaced-repetition and micro-lesson patterns. It is **not** the Duolingo consumer app, API, or account integration.

## State location

Learning-OS state may exist in `<workspace>/duolingo/`, `<workspace>/memory/duolingo/`, or `~/duolingo/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/duolingo/`, `<workspace>/memory/duolingo/`, `~/duolingo/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and state must be created, default to `<workspace>/duolingo/` when `<workspace>` is available; otherwise ask for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation. Never write the literal string `<state_root>` to disk.

Use the selected `<state_root>` for every state operation in this skill. Prefer:

- `<state_root>/memory.md` — global status, active topics, rotation, streak
- `<state_root>/router/topics.md` — canonical topics and trigger phrases
- `<state_root>/router/agentsmd-snippet.md` — AGENTS router snippet text
- `<state_root>/topics/<slug>/` — per-topic profile, curriculum, queue, sessions, checkpoints
- `<state_root>/archive/` — retired topics

Initialize missing files from `assets/memory-template.md` and `assets/topic-template.md`. Keep live state under `<state_root>/`; treat `assets/` as templates only.

## Operating Instructions

Load only the reference required by the current step; keep this file as the always-on path.

| Need | File |
|------|------|
| First-run activation and bootstrap | `references/setup.md` |
| Directory scaffold commands | `references/blueprint.md` |
| State tree overview | `references/architecture.md` |
| Operating rules | `references/core-rules.md` |
| Optional AGENTS router block | `references/activation-routing.md` |
| 60–90s lesson / placement loop | `references/lesson-loop.md` |
| XP / hearts / streak / mastery | `references/progression.md` |
| Multi-topic rotation and comeback | `references/retention-ops.md` |
| Weekly health metrics | `references/launch-scorecard.md` |
| Common failure modes | `references/traps.md` |
| Local-only data posture | `references/security.md` |
| Verified research URLs | `references/sources.md` |
| Global memory shape | `assets/memory-template.md` |
| Per-topic file templates | `assets/topic-template.md` |

## Core Rules

1. **Bootstrap before teaching** — if `<state_root>/` is missing, create the scaffold from `references/blueprint.md` and confirm at least one topic namespace before the first lesson.
2. **One topic per loop** — load only that topic namespace for the session; update global memory afterward for rotation and streak.
3. **Review before new** — each daily planner should serve at least one review item before introducing net-new content when a review is due.
4. **Tight loops** — follow `references/lesson-loop.md`: micro-challenge → attempt → correction → reinforcement → queue writeback (about 60–90 seconds).
5. **Transparent economy** — XP, hearts, streaks, and mastery follow `references/progression.md`; rewards track demonstrated learning, not empty activity.
6. **AGENTS is opt-in and manual** — generate router snippets from `references/activation-routing.md`, show them, and wait for the user to paste; keep AGENTS user-owned.
7. **Comeback over punishment** — after a miss, use grace/comeback loops from `references/retention-ops.md` instead of deleting motivation.
8. **Confirm destructive topic changes** — require explicit confirmation before removing or archiving a topic.

## Security and privacy

Keep learning state local under the resolved `<state_root>/`. Open paths outside that root only after the user names them. Export curriculum, attempts, or personal notes only for an explicit user-approved share. During normal learning sessions, leave package files under `skills/duolingo/` unchanged.

## Evaluation harness

`test-prompts.json` holds structural dry-run cases for Gate 8. It is not user-facing runtime content.
