# Memory Template — AGI

Create these files under the resolved `<state_root>/` (never the literal placeholder string).

## memory.md

```markdown
# AGI Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## User Style
<!-- How this user prefers to communicate -->
<!-- Concise vs detailed, technical level, emotional awareness -->

## Effective Patterns
<!-- Reasoning approaches that worked well -->
<!-- Transfer learning successes to remember -->

## Notes
<!-- Observations about what helps this user -->
<!-- Calibration notes: when to be more/less certain -->

---
*Updated: YYYY-MM-DD*
```

## reflections.md

```markdown
# Reasoning Reflections

<!-- Log significant learning moments -->

## Template Entry
### YYYY-MM-DD
**Situation:** What happened
**Insight:** What you learned
**Pattern:** Reusable principle

---
```

## limits.md

```markdown
# Known Limits

<!-- Topics where you've discovered gaps -->

## Knowledge Gaps
<!-- Things you've been wrong about or lack knowledge of -->
- [Topic]: [What you lack knowledge of / were wrong about]

## Uncertainty Patterns
<!-- When to be extra cautious -->
- [Domain/topic]: [Why uncertainty is higher here]

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Default | Keep improving |
| `complete` | Has enough context | Rare for AGI — always learning |
| `paused` | User prefers simpler responses | Reduce meta-cognition |
| `omit_ask` | User declines activation prompts | Stay invisible on activation |

## Key principles

- Invisible improvement — user should not notice “AGI working”
- Calibrated confidence — update `limits.md` when wrong
- Reflection drives growth — log insights, review periodically
- Minimal configuration — think better first; persist only with approval
