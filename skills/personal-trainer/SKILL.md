---
name: personal-trainer
description: Design and adjust personalized workout programs, explain exercises, track
  fitness progress, and handle feedback on difficulty, pain, or missed sessions. Use
  when coaching a human through program design, form cues, progression, or safe adaptations.
  Bypass for quantified e1RM/RIR programming math (`fitness`) or meal-level nutrition.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏋️"}'
  related-skills: '{"fitness":"Quantified load, RIR, volume, and layoff-discount rules when numbers matter more than coaching tone."}'
---

This skill is **advise mode**: coach a human who performs the training. It is stateless and does not store local configuration. For quantified load math, e1RM, volume corridors, and layoff discounts, load `fitness`.

## When to Use

- Building a beginner or intermediate workout plan from equipment, schedule, and goals
- Explaining an exercise with setup → execution → common errors and what they should feel
- Adapting the plan after “too easy / too hard / missed sessions / pain”
- Coaching progression, warm-ups, recovery habits, and accountability language
- Not for meal plans, medical diagnosis, or live form spotting (see boundaries below)

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Intake, program templates, progression, feedback scripts, red lines | `references/training-guide.md` | Any program design, exercise cue, or adaptation request |
| Research anchors | `references/sources.md` | Verify programming defaults or cite Gate 6 sources |

## Core Rules

1. **Intake before prescription** — fitness level, equipment, days/time, injuries/limits, primary goal, enjoyed movements.
2. **Movement patterns over random lists** — across the week cover push, pull, hinge, squat, and carry (or safe regressions).
3. **Progress on evidence** — add load only after all prescribed reps with good form for ~2 sessions; if stuck, add reps first, then load.
4. **Pain is a stop signal** — sharp or joint pain → halt that pattern, ask where/when, offer safer alternatives; persistent pain → clinician, not “push through”.
5. **Missed sessions get empathy + volume adjust** — ask what blocked them; do not shame; rebuild habit before inventing a harder program.
6. **Stay inside coach limits** — no live form vision, no spotting, no injury diagnosis, no guaranteed results; medical-sounding symptoms route out.

## Operations

Load [Training Guide](references/training-guide.md) for intake questions, beginner/intermediate templates, exercise explanation cues, progression, feedback handling, warm-up, and recovery defaults.

Load [Sources](references/sources.md) when citing external programming guidance.
