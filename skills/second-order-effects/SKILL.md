---
name: second-order-effects
description: Analyze decisions by tracing consequences beyond immediate outcomes to second and third-order effects. Trigger this skill when the user asks to analyze a decision, evaluate long-term impacts, or apply systems thinking.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔮"}'
  related-skills: '{"first-principles-thinking":"break problems to fundamentals","six-thinking-hats":"parallel thinking modes","strategy":"strategic planning frameworks"}'
---

## Setup

If `<state_root>/second-order-effects/` doesn't exist, or user's memory file shows setup incomplete, read `references/setup.md` first.

## When to Use

User faces a decision with non-obvious downstream effects. Agent traces consequences through multiple orders, identifies hidden risks and opportunities, and stress-tests assumptions.

## Architecture

Memory lives in `<state_root>/second-order-effects/`. See `references/memory-template.md` for structure.

```
<state_root>/second-order-effects/
├── memory.md          # Preferences + past analyses
├── decisions/         # Archived decision analyses
│   └── YYYY-MM-DD_topic.md
└── patterns.md        # Learned consequence patterns
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | When `<state_root>/second-order-effects/` does not exist or user memory indicates setup is incomplete |
| Memory template | `references/memory-template.md` | When reading or writing to the decision archive in `<state_root>/second-order-effects/` |
| Analysis framework | `references/framework.md` | When structuring a new consequence chain analysis |
| Common patterns | `references/patterns.md` | When reviewing past decisions to identify recurring patterns |
| Domain knowledge | `references/domain-knowledge.md` | When needing definitions of systems thinking or unintended consequences |

## Core Rules

### 1. Always Go Three Levels Deep
First-order: What happens immediately?
Second-order: What does that cause?
Third-order: What does THAT cause?

Most people stop at first-order. Competitive advantage lives in second and third.

### 2. Consider All Stakeholders
Map who is affected at each order:
- Direct participants
- Indirect observers
- Market/ecosystem
- Future self

Each stakeholder creates new consequence chains.

### 3. Invert the Question
After mapping positive outcomes, ask: "What could go wrong at each level?"

| Order | Optimistic | Pessimistic |
|-------|------------|-------------|
| 1st | Direct benefit | Obvious risk |
| 2nd | Compounding gain | Hidden cost |
| 3rd | Strategic advantage | Systemic risk |

### 4. Time-Weight Consequences
Near-term consequences feel larger than they are. Apply discount:
- 1st order (now): weight 0.5
- 2nd order (weeks/months): weight 1.0
- 3rd order (years): weight 1.5

Decisions that sacrifice 2nd/3rd order for 1st are usually wrong.

### 5. Document Predictions
Every analysis should include falsifiable predictions with timestamps. Review quarterly. Update `references/patterns.md` when patterns emerge.

## Consequence Chain Format

Use this structure for every analysis:

```markdown
## Decision: [One sentence]

### First Order (Immediate)
- Effect 1 → leads to...
- Effect 2 → leads to...

### Second Order (Weeks-Months)
- [Effect 1] causes → ...
- [Effect 2] causes → ...

### Third Order (Months-Years)
- [Second-order effect] causes → ...

### Stakeholder Map
| Who | 1st Order | 2nd Order | 3rd Order |
|-----|-----------|-----------|-----------|

### Inversion (What Could Go Wrong)
- Risk at 2nd order: ...
- Risk at 3rd order: ...

### Decision: [Proceed/Pause/Reject] because [reason tied to 2nd/3rd order]
```

## Common Traps

- Stopping at first order → miss compounding effects
- Ignoring negative second-order effects → blindsided by hidden costs
- Over-weighting immediate pain → sacrifice long-term position
- Analysis paralysis → set time limit (15-30 min), then decide
- Confident predictions → use probability ranges, not certainties

## Scope

- Focus entirely on analyzing decisions using consequence chains.
- Store analyses in `<state_root>/second-order-effects/`.
- Learn patterns from past decisions.
- Wait for the user's final judgment rather than making decisions for them.
- Only access external data when explicitly requested.
- Maintain the integrity of your SKILL.md file by leaving it unmodified.

## Security & Privacy

**Data Boundaries:**
- Keep all decision analyses within `<state_root>/second-order-effects/`.
- Keep learned patterns and preferences local.
- Restrict file access to this skill's directory.
- Operate entirely offline without external network requests.
