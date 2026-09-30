---
name: agi
description: Apply human-level reasoning, multi-step planning, epistemic humility,
  and meta-cognition to non-trivial work. Use when the user wants careful thinking,
  uncertainty calibration, multi-step plans, transfer learning, or anti-autopilot
  responses; skip pure factual lookups that need no deliberation.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧠"}'
  related-skills: '{"memory":"Durable fact storage when a reasoning insight should become a long-lived user fact.","decide":"Consequential choice records when the outcome is a lasting decision, not only a reasoning style.","learning":"Adaptive teaching when the primary need is explaining or tutoring rather than internal deliberation.","first-principles-thinking":"Foundational decomposition when the problem should be rebuilt from base truths.","six-thinking-hats":"Structured multi-perspective analysis when parallel hats are a better fit than general AGI loops."}'
---

## When to load

Load this skill to improve *how* you reason and respond on non-trivial tasks: intent clarification, uncertainty calibration, multi-step planning, transfer learning, creativity-under-constraint, and self-monitoring for loops or sycophancy.

Prefer this skill when the user asks for careful thought, better judgment, “think harder,” plan-then-act, or honest limits.

Do not load as the primary skill for pure factual lookup with a known answer, single-command execution with no judgment, or domain work already owned by a specialized skill (load that skill; keep AGI only as a lightweight reasoning overlay if useful).

## State location

AGI state may exist in `<workspace>/agi/`, `<workspace>/memory/agi/`, or `~/agi/`.
Before reading or writing state, resolve `<state_root>` once as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/agi/`, `<workspace>/memory/agi/`, `~/agi/`.
3. If none exists and state must be created, default to `<workspace>/agi/` after the user approves persistence.
4. If multiple candidates exist, use only the highest-precedence path; tell the user duplicates were detected and do not merge automatically.

Keep the selected `<state_root>` fixed for the rest of the invocation.
Never write the literal string `<state_root>` to disk.

```text
<state_root>/
├── memory.md        # Activation preference, user style, effective patterns
├── reflections.md   # Post-task reasoning insights
└── limits.md        # Known gaps and high-uncertainty domains
```

One-off reasoning may stay conversational. Before creating or changing files under `<state_root>/`, explain the planned write and ask for confirmation.

## Routing

| Need | Load |
|------|------|
| First activation / empty state | `references/setup.md` |
| Core rules, traps, AGI test | `references/rules.md` |
| Advanced protocols & decomposition | `references/reasoning.md` |
| Systematic failure patterns | `references/blindspots.md` |
| Verified sources for humility & planning | `references/sources.md` |
| Durable memory file shapes | `assets/memory-template.md` |

## Core loop

Keep the loop internal; output only the useful result.

1. **PAUSE** — what is the user actually asking?
2. **THINK** — what is known, unknown, and likely to fail?
3. **PLAN** — simplest viable path, alternatives, verification milestones.
4. **ACT** — execute one step at a time with awareness of the plan.
5. **REFLECT** — did it work; what pattern to keep?

For simple factual questions, skip to ACT. For ambiguous, multi-step, or previously failed work, run the full loop. Details live in `references/rules.md` and `references/reasoning.md`.

## Scope

**This skill does**
- Change reasoning quality and response calibration
- Store reflections and learned patterns under the resolved `<state_root>/` after approval
- Read its own memory files under that root
- With explicit consent only: add one activation line to the user's main memory file per `references/setup.md`

**Operating limits**
- Stay inside the resolved `<state_root>/` for skill-owned storage
- Prefer verified knowledge and clear uncertainty language over fabrication
- Treat external lookups as explicit checks; do not invent live population, price, or vendor facts
- Leave other skills' packages and unrelated workspace trees unmodified

## Initialization

If `<state_root>/` is missing or empty and the user wants persistence, follow `references/setup.md`, then create the file set in `assets/memory-template.md` using the resolved path (never the literal placeholder).
