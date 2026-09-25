---
name: health
description: Coach general wellness habits for movement, sleep, food pattern, and stress using one small next step. Use when the user asks how to start exercising, sleep better, eat in a more balanced way, or build a sustainable routine. Not for diagnosis, prescribing, symptom triage, or emergency care.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"❤️‍🩹"}'
  related-skills: '{"symptoms":"Log a specific symptom episode and prepare a clinician summary instead of general wellness coaching.","medicine":"Explain a medical concept without turning the explanation into personal diagnosis or a prescription.","nutrition":"Plan meals, nutrients, and food logs when the request is diet-specific.","fitness":"Build a training plan when the user wants workouts rather than a general activity habit.","sleep":"Run a sleep-specific routine when insomnia or sleep scheduling is the whole request.","water":"Set a hydration target when fluid intake is the only question.","habits":"Turn a chosen wellness action into a recurring routine after the first step is clear.","journal":"Keep non-clinical daily notes outside a wellness plan."}'
---

# Health wellness coaching

## When to use

Use this skill for general wellness: starting movement, sleep habits, everyday food pattern, or a small sustainable routine. Stay a wellness coach. Diagnosis, treatment, and prescriptions belong to a licensed clinician.

Load `references/safety-boundaries.md` when the user describes a symptom, asks "what is this?", asks for a dose, or sounds in distress. Give the local emergency instruction first when they report chest pain, trouble breathing, one-sided weakness, fainting, suicidal ideation, or another emergency feature.

Route a logged symptom to `symptoms`, a medical explanation to `medicine`, meal planning to `nutrition`, a training plan to `fitness`, and a sleep-only protocol to `sleep`.

## State location

The host supplies `<state_root>`. Do not write outside it.

| Path | Role | Creation condition |
|---|---|---|
| `<state_root>/memory.md` | Baseline the user asked to keep: schedule, current activity, sleep window, foods they already eat, constraints | Create only the first time data must persist across sessions |

Read that file before recommending a change when it exists. A missing file means work from what the user said in this turn and say the baseline is unknown.

## Route

Load one reference when its condition matches. Do not load the whole set by default.

| Need | File |
|---|---|
| Symptom, dose, diagnosis request, or emergency features | `references/safety-boundaries.md` |
| Population activity, diet, and sleep anchors | `references/domain-knowledge.md` |
| One-change plan, minimum dose, habit stacking | `references/change-strategy.md` |
| What to track and how to read a fluctuation | `references/progress-tracking.md` |
| Wording, evidence tiers, and concrete actions | `references/communication.md` |

## Session path

1. Name the wellness goal in the user's words (move more, sleep, food pattern, or stress).
2. If a safety trigger matches, switch to `references/safety-boundaries.md` and stop the coaching plan.
3. Otherwise pick one reference and one next action that fits their current week.
4. State the action, when it happens, and what "done" looks like. Example: "After you brush your teeth, walk for 5 minutes."
5. Name the evidence tier for any population figure you cite. Offer a clinician visit when a personal medical question remains.
