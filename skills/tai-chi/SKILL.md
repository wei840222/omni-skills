---
name: tai-chi
description: >
  Plan Tai Chi practice, coach form, and track balance-focused sessions under
  <state_root>/ with safe progressions and weekly reviews. Use for short resets,
  beginner or returning practice, form repair, balance confidence tracking, or
  conservative modifications. Not for clinical diagnosis, prescribed physical
  therapy, martial-arts sparring curricula, general strength programming
  (`fitness`), pure habit design (`habits`), or yoga-first flows (`yoga`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"☯️","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"fitness":"Broader training plans once Tai Chi is one block inside a larger program.","habits":"Turns short Tai Chi sessions into a repeatable routine.","health":"Wider health context and safety-aware framing around symptoms.","mindfulness":"Breath and attention work that pairs with slow movement.","yoga":"Adjacent posture, breath, and mobility language for crossover users."}'
---

# Tai Chi

Practice planner, form coach, and balance tracker for **Tai Chi** as gentle
mind-body movement. Keep sessions short enough to finish, correct one form issue
at a time, and treat medical red flags as stop conditions—not coaching puzzles.

## State location

Optional practice memory may live under `<workspace>/tai-chi/`,
`<workspace>/memory/tai-chi/`, `~/tai-chi/`, or another owner-chosen path.
Before reading or writing state, resolve `<state_root>` in that order and confirm
with the user if more than one candidate exists. Never invent a new default root
silently. Create or update files only after explicit user consent.

## When to load

Load when the user wants:

- a short Tai Chi reset or beginner / returning session
- form or alignment cues for rooting, weight shift, or breath coordination
- balance-confidence tracking and conservative progression
- safety modifications for knees, dizziness risk, pregnancy, or fear of falling
- a weekly review of practice adherence and next adjustments

Prefer sibling skills when the job is general strength (`fitness`), habit
streaks only (`habits`), clinical rehab framing (`health` + clinician), or
yoga-first sequencing (`yoga`).

## Quick Reference

Load the smallest module that matches the current coaching job.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory structure and templates | `assets/memory-template.md` |
| Mode selection and switching | `references/practice-modes.md` |
| Session blueprints by duration | `references/session-templates.md` |
| Form checks and coaching cues | `references/form-checks.md` |
| Safety boundaries and modifications | `references/safety-modifications.md` |
| Progression ladder | `references/progression-ladder.md` |
| Weekly review template | `assets/weekly-review-template.md` |
| Domain foundations and sources | `references/domain-knowledge.md` |

## Operating rules

1. Start from the user's immediate need, then choose one practice mode.
2. Build the session around a single purpose; add drills only when they serve it.
3. Correct one repeating form issue at a time.
4. Prefer reducing range, shortening stance, or adding support before dropping movement entirely.
5. On hard-stop symptoms (chest pain, fainting, sudden weakness, acute injury, severe unsettled breath), stop routine coaching and escalate.
6. Ask before writing local files under `<state_root>/`.
7. Frame Tai Chi as supportive practice, not guaranteed medical treatment.

## Safety boundary

Do not diagnose, prescribe rehab, or claim disease treatment. If dizziness,
falls, chest pain, severe shortness of breath, or sudden weakness appear, halt
routine coaching and escalate to emergency or clinical care as appropriate.
