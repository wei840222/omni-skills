---
name: self-direction
description: >
  Capture the user's direction system—values, goals, decision criteria, risk
  tolerance, resource priorities, and hard boundaries—then decide and transmit
  that direction to sub-agents as the user would. Use when the agent must act
  without full instructions, explain WHY not only WHAT, keep multiple agents
  aligned to the same priorities, learn preferences over time, or build a
  direction frame before spawning work. Prefer `decide` for logging one
  consequential branch choice, `escalate` for ask-vs-act thresholds,
  `delegate` for spawn mechanics, `reflection` / `self-improving` for
  post-outcome lessons, and `memory` for durable world facts.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧭","requires":{"config":["<state_root>/self-direction/"]}}'
  related-skills: '{"reflection":"Heavier post-task evaluation of work quality; self-direction owns ongoing priority and value capture.","decide":"Log one consequential branch choice; self-direction maintains the broader direction model that informs many choices.","escalate":"Ask-vs-act thresholds by risk and reversibility; self-direction supplies the values and boundaries those thresholds protect.","delegate":"Spawn mechanics, tiers, and verification; self-direction supplies the transmission frame content.","memory":"Durable world facts and diary continuity; self-direction stores preference and decision-direction patterns, not factual memory."}'
---

# Self-Direction

Build a durable model of how the user thinks, prioritizes, and decides, then
use that model to act, explain, and brief sub-agents without constant
re-prompting.

This skill is stateful. Runtime direction data lives under a resolved
`<state_root>/self-direction/` tree outside this package. Never write runtime state
into the skill tree.

## State location

Self-direction state may exist in `<workspace>/self-direction/`,
`<workspace>/memory/self-direction/`, or `~/self-direction/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/self-direction/`, `<workspace>/memory/self-direction/`,
   `~/self-direction/`.
3. If more than one exists, use only the highest-precedence directory, report
   the split copies, and do not merge or cross-write.
4. If none exists and durable direction state must be created, default to
   `<workspace>/self-direction/` when `<workspace>` is available; otherwise ask
   for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the rest of the invocation.

Use the selected `<state_root>` for every path under
`<state_root>/self-direction/` (`direction.md`, `evidence.md`,
`confidence.md`, `conflicts.md`, `transmission.md`). Legacy
`~/Clawic/data/self-direction/` and `~/clawic/self-direction/` copies are
migration sources only — move them into the resolved
`<state_root>/self-direction/` when the user asks, and say in one line that you
moved them and from where. Skill resources stay under `references/` and
`assets/`; never treat the literal string `<state_root>` as a filesystem
directory name.

After resolving `<state_root>`, if this is first use or state is empty, read
`references/setup.md`. Templates live in `assets/memory-template.md`.

## When to use

- The agent must decide without complete step-by-step instructions
- The user wants consistent WHY/WHAT alignment across agents and sessions
- Preferences should compound over time instead of resetting each turn
- A sub-agent needs a faithful direction frame before spawn
- A decision conflicts with a captured boundary or low-confidence inference

Prefer adjacent skills when they fit better (do not stretch this skill to cover them):

- One logged branch choice with outcome → `decide`
- Ask-now vs act-now policy by risk → `escalate`
- Spawn checklist, tier, recovery → `delegate`
- Delivery QA / lesson retention after work → `reflection` / `self-improving`
- Facts, people, dates, diary → `memory`

## Direction system

Capture these components progressively:

| Component | Captures |
|---|---|
| Values | What to optimize, refuse, and trade off |
| Goals | Objectives, reasons, and success signals |
| Criteria | What makes work worth doing or rejecting |
| Resources | Time, money, tokens, and attention priorities |
| Boundaries | Hard limits and actions that need explicit approval |
| Patterns | Mental models and default approach order |

## Progressive disclosure

| Need | Load |
|---|---|
| First use / empty state | `references/setup.md` |
| Direction model schema | `assets/memory-template.md` |
| Raw observation logging | `references/evidence.md` |
| Sub-agent transmission frames | `references/transmission.md` |
| Domain sources for Gate research | `references/sources.md` |

## Capture loop

```text
OBSERVE → CAPTURE → VALIDATE → APPLY
```

**Explicit signals:** stated preferences, reasoning (“because…”), hard
boundaries (“never do X without asking”), and corrections.

**Implicit signals:** option choices, resource allocation, reactions to
outcomes, and rejected suggestions.

Track confidence per element:

| Level | Meaning | Action |
|---|---|---|
| High | Multiple confirmations or explicit statements | Act and report |
| Medium | Inferred or single confirmation | Act and cite evidence |
| Low | Thin observation | Ask first, then capture |
| Conflict | Contradictory signals | Resolve with the user before acting |

## Architecture

```text
<state_root>/self-direction/
├── direction.md       # Values, goals, criteria, resources, boundaries, patterns
├── evidence.md        # Raw observations that informed the model
├── confidence.md      # Per-element confidence
├── conflicts.md       # Contradictions awaiting resolution
└── transmission.md    # Direction frames prepared for sub-agents
```

## Core rules

1. **Capture before acting** on uncovered decisions: check the model, infer only
   within confidence, ask when uncertain, and never guess on high-stakes
   low-confidence choices.
2. **Explain from evidence** — cite the captured value, criterion, or pattern.
3. **Evolve continuously** — update entries, surface contradictions, adjust
   confidence, and let unused patterns decay.
4. **Respect confidence** — low or conflict blocks autonomous action.
5. **Transmit faithfully** — include every relevant boundary, preserve values
   exactly (do not soften or reinterpret), keep the why, and add escalation
   triggers.
6. **Surface gaps early** — say when the model is silent or low-confidence
   before the gap becomes a bad decision.
7. **Validate periodically** — confirm the highest-impact elements and clear
   accumulated conflicts.

## Self-direction in action

- Autonomous decision: act from high-confidence evidence and report the why
- Preference prediction: propose from patterns and ask for confirmation
- Misalignment catch: pause when a task conflicts with a captured boundary
- Honest gap: ask when the model is silent instead of inventing direction

## Operating modes

| Mode | Behavior |
|---|---|
| Learning (default) | Capture signals, ask clarifying questions, deepen the model |
| Autonomous | High-confidence action with cited reasoning |
| Conservative | New relationship or critical domain; ask more, assume less |

## Common traps

| Trap | Fix |
|---|---|
| Acting on low-confidence inference | Ask first |
| Capturing noise as signal | Require repeated evidence for patterns |
| Stale model | Continuous updates + periodic validation |
| Incomplete transmission | Verify boundaries and escalation triggers |
| Assuming universal patterns | Context-tag observations (work vs personal) |

## Related skills

- `reflection` — structured self-evaluation before or after delivery
- `decide` — consequential branch-choice logging
- `escalate` — ask-vs-act thresholds
- `delegate` — spawn mechanics and verification
- `memory` — long-term factual continuity
