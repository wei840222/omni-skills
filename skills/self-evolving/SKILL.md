---
name: self-evolving
description: >
  Improve a repeated agent workflow with one-lever experiments, three-win
  promotion gates, and portable local pattern memory under `<state_root>/`.
  Use when a workflow keeps failing the same way, the user wants to test one
  mutation before making it durable, or tentative experiments must be promoted
  or discarded with evidence. Prefer `self-improving` for correction logs and
  durable execution lessons, `memory` for long-term facts, `learning` for study
  plans, `decide` for consequential branching, and `proactivity` for follow-through
  after a better pattern is chosen.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧬","configPaths":["<state_root>/"]}'
  related-skills: '{"self-improving":"Log corrections and compound execution lessons; self-evolving owns one-lever experiment promotion.","memory":"Durable facts and diary continuity; self-evolving stores workflow mutation evidence.","decide":"Choose among options once; self-evolving tests a single lever across comparable runs.","learning":"Deliberate practice plans; self-evolving promotes proven workflow mutations.","proactivity":"Carry the next step after a promoted pattern exists."}'
---

# Self-Evolving

Turn repeated friction into portable local rules: detect one bottleneck, mutate
one lever, evaluate against a baseline, then promote only after three comparable
wins.

## State location

Optional evolution notes are persistent user state. Resolve `<state_root>` once
per invocation before any read or write:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/self-evolving/`, `<workspace>/memory/self-evolving/`, then
   `~/self-evolving/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicates; do not merge them.
4. If none exists and the user confirms saving evolution notes, create
   `<workspace>/self-evolving/`. If `<workspace>` is unavailable, ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation. Never write the literal string
   `<state_root>` to disk.

```text
<state_root>/
|-- memory.md        # HOT: stable rules, guardrails, activation cues
|-- experiments.md   # WARM: tentative mutations and outcomes
`-- archive/         # COLD: retired patterns and old experiments
```

If older notes exist under a legacy Clawic self-evolving data directory, migrate
them into the resolved `<state_root>/` on first write and say in one line that
you moved them and from where. Seed new memory from
`assets/memory-template.md` and new experiment logs from
`assets/experiments-template.md`.

## When to use

- A repeated workflow fails, needs correction, or shows a measurable bottleneck
- The user wants to try one mutation and keep evidence before making it durable
- Tentative experiments need promotion, narrowing, or discard decisions
- Local pattern memory should compound without rewriting the installed skill

Prefer adjacent skills when they fit better:

- correction logs / durable execution lessons → `self-improving`
- long-term facts, people, dates, diary continuity → `memory`
- study plans or deliberate practice curricula → `learning`
- one-shot consequential branching → `decide`
- follow-through after a better pattern is chosen → `proactivity`

## Progressive disclosure

Keep `SKILL.md` as the always-on contract. Load at most one reference or asset for the current need.

| Topic | File | Load when |
|-------|------|-----------|
| First activation / setup | `references/setup.md` | No `<state_root>/memory.md`, empty state, or first session |
| Memory template | `assets/memory-template.md` | Creating or reshaping `<state_root>/memory.md` |
| Experiment log template | `assets/experiments-template.md` | Creating or reshaping `<state_root>/experiments.md` |
| Evolution loop | `references/evolution-loop.md` | Detect → mutate → evaluate → promote/discard |
| Safety boundaries | `references/boundaries.md` | Before storing data or changing behavior |
| Verified sources | `references/sources.md` | Before changing promotion thresholds or memory claims |

## Core rules

1. **Start from real friction** — open an experiment only after a failed attempt,
   repeated correction, or measurable bottleneck.
2. **Change one lever** — test one prompt pattern, decision rule, retrieval step,
   or file habit per experiment so the winning variable stays obvious.
3. **Gate by value** — promote only when speed, quality, or reliability improves
   across at least three comparable uses; keep unproven ideas in
   `<state_root>/experiments.md`.
4. **Keep local evidence** — record trigger, baseline, mutation, outcome, and
   next move. Before the first persistent write, tell the user this skill keeps
   concise local notes for repeat improvement.
5. **Promote over rewrite** — convert winners into short rules, checklists, or
   retrieval triggers; compound by accumulation.
6. **Stay inside boundaries** — follow `references/boundaries.md`; limit durable
   writes to resolved `<state_root>/` notes and leave installed skill files
   unchanged.

## Common traps

| Trap | Why it fails | Better move |
|------|--------------|-------------|
| Rewrite the whole workflow after one mistake | Winning variable stays unknown | Test one mutation against the previous baseline |
| Promote after one good run | Lucky wins become noisy defaults | Wait for three comparable wins |
| Log vague lessons like "be smarter" | Future retrieval becomes useless | Write the exact trigger, decision, and expected outcome |
| Optimize for novelty | The system churns without compounding | Keep only behaviors that save time or reduce errors |
| Treat silence as proof | Lack of complaint is weak evidence | Require explicit feedback or repeated success |

## Security and privacy

**Data that leaves the machine**

- Excluded by default; this skill does not call external APIs.

**Data that stays local**

- Stable rules and activation notes in `<state_root>/memory.md`
- Tentative experiments in `<state_root>/experiments.md`
- First-time local storage is announced before the first write

**Out of scope**

- Reading or storing credentials, financial identifiers, medical diagnoses,
  biometrics, or third-party private data
- Modifying installed skill files (`SKILL.md`, references, assets)
- Reading unrelated files outside the active task context and `<state_root>/`
