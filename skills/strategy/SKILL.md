---
name: strategy
description: >
  Design robust competitive and product strategies with proven frameworks,
  constraint mapping, cognitive-bias checks, and kill criteria. Use when the
  user needs option maps, trade-offs, competitor-response modeling, scenario
  plans, or prioritization (Porter, Ansoff, Playing to Win, ICE/RICE). Prefer
  `business` for startup validation and unit economics, `competitor-research`
  for competitor audits and gap analysis, `mba` for curriculum-style learning,
  `ceo` for company-level capital/board calls, and `brainstorm` for raw idea
  volume before strategic selection.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"♟️"}'
  related-skills: '{"business":"Startup validation, unit economics, and irreversible decision tracking rather than competitive option maps.","competitor-research":"Competitor audits, positioning, and gap analysis when the ask is research depth.","mba":"MBA curriculum and case learning across finance, strategy, and operations.","ceo":"Company-level pivot, fundraising, layoff, and board decisions.","brainstorm":"Raw idea volume before strategic selection and trade-off ranking.","management":"People-leadership routines rather than market/competitive strategy."}'
---

# Strategy

Constraint-aware strategy craft for competitive positioning, growth options,
prioritization, and scenario planning. Diagnose the real problem before
prescribing frameworks. This skill advises; it does not publish plans, scrape
competitors, or mutate external systems without an explicit user request.

Optional persistent notes live under a resolved `<state_root>/` tree outside
this package. Never write runtime state into the skill tree.

## State location

Strategy state may exist in `<workspace>/strategy/`,
`<workspace>/memory/strategy/`, or `~/strategy/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/strategy/`, `<workspace>/memory/strategy/`, `~/strategy/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable notes, create
   `<workspace>/strategy/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the shell cwd.
5. Prefer portable `<state_root>` paths; never hard-code host-specific absolute
   roots. Skill resources stay under `references/` and `assets/`; never treat
   the literal string `<state_root>` as a filesystem path.

Persistent state is enabled only when the user explicitly requests retention or
approves a named persistent write.

```text
<state_root>/
|-- memory.md     # HOT: constraints, preferences, past decisions
|-- domains/      # Domain-specific patterns (business, product, career)
`-- playbooks/    # Reusable strategy templates
```

See `assets/memory-template.md` for initial setup shapes.

## When to Use

Use this skill when the user needs:

- competitive or growth strategy with explicit trade-offs
- framework selection (Porter, Ansoff, Playing to Win, ICE/RICE, SWOT, PESTEL)
- competitor-response modeling and kill criteria
- bias checks before locking a recommendation

Route away when the ask is mainly:

- startup idea validation / unit economics → `business`
- competitor dossier / niche audit → `competitor-research`
- MBA curriculum learning → `mba`
- company-level capital / board crisis → `ceo`
- raw idea lists without selection → `brainstorm`
- people-management routines → `management`

## When to load what

Load only the matching reference for the current ask.

| Need | Load |
|------|------|
| Framework chooser + deep dives | `references/frameworks.md` |
| Pre-decision bias checklist | `references/biases.md` |
| 4-phase design process / issue trees | `references/process.md` |
| First-principles / second-order techniques | `references/techniques.md` |
| Official source URLs + claim checklist | `references/sources.md` |
| Memory template shapes | `assets/memory-template.md` |

## Core Rules

### 1. Diagnosis Before Prescription

Before proposing a strategy, verify you understand the REAL problem. Ask:

- What are you trying to achieve? (specific, measurable)
- What constraints exist? (time, money, people, politics)
- What have you tried? What failed?
- Who are the stakeholders and what do they want?

If answers are missing, ask the smallest clarifying set first; do not invent
goals or constraints.

### 2. Constraints First

BEFORE any recommendation, map hard constraints:

- Budget (actual numbers, not "limited")
- Timeline (deadlines, milestones)
- Resources (team size, capabilities)
- Political/cultural restrictions

Discard strategies that ignore stated constraints. If a constraint blocks every
attractive option, surface the blockage and reframe rather than forcing a plan.

### 3. Trade-offs Are Mandatory

Every strategy must explicitly state:

- What you're SACRIFICING (not doing Y to do X)
- What could go wrong (risks, not just benefits)
- What success looks like (measurable criteria)

Avoid "Do both" or "Optimize everything"; those are not strategies. When the
user insists on dual goals, force a ranked primary objective.

### 4. Model Competitor Response

For competitive decisions: "If you do X, competitor will likely do A, B, or C.
Your counter-move for each..."

Assume competitors will react and adapt. If competitor data is thin, label the
uncertainty and prefer reversible first moves.

### 5. Multiple Scenarios

Provide at least 3 scenarios:

- **Best case**: Everything works (≈10% weight)
- **Base case**: Realistic execution (≈60% weight)
- **Worst case**: Key assumptions fail (≈30% weight)

Include triggers: "If X happens, switch to plan B."

### 6. Bias Protection

Before finalizing, run the checklist in `references/biases.md`:

- Am I confirming existing beliefs?
- Am I anchored to first data?
- Am I avoiding loss or chasing sunk costs?

### 7. Actionable Next Steps

End every strategy session with:

- 3 concrete actions for this week
- Clear owner for each action
- Success metrics to check in 2–4 weeks

### 8. Challenge the Framing

If the question seems wrong, say so:

"You're asking how to grow faster, but your data suggests retention is the real
problem. Should we reframe?"

### 9. Kill Criteria

Every strategy includes conditions to ABANDON it:

"If metric X drops below Y for Z weeks, stop and reassess."

Missing kill criteria is a defect; add them before locking the plan.

### 10. Progressive Framework Selection

Match framework to problem type — see `references/frameworks.md`:

- Competition analysis → Porter's Five Forces
- Growth options → Ansoff Matrix
- Prioritization → ICE/RICE
- Full strategy design → Playing to Win

Load only the matching deep dive; do not dump every framework.

## Common Traps (recovery-first)

1. **Jumping to a framework before the problem statement** — Stop; write one
   agreed problem sentence, then choose a framework.
2. **Bare `<state_root>` without resolution** — Resolve the State location
   rules above before any read/write; never treat the placeholder as a path.
3. **Copying a competitor move without diagnosis** — Check churn, advantage,
   and response scenarios; prefer a unique wedge over parity theater.
4. **No kill criteria** — Add metric + threshold + time window before
   committing resources.
5. **Clawic / host-absolute paths in templates** — Rewrite to
   `<state_root>/...` only; never recreate `~/Clawic/data/strategy/`.

## Memory Storage

User context persists in `<state_root>/memory.md` only after consent. Create on
first approved use using `assets/memory-template.md`.
