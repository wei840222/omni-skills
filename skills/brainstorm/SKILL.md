---
name: brainstorm
description: >
  Generate idea volume fast with mode-aware structure, expansion prompts, and
  SCAMPER lateral moves. Use when the user needs names, options, marketing
  angles, creative unblockers, or "what else could we try?" lists. Prefer
  `diverge` for multi-persona trade-off synthesis, `question` when the need is
  interview or discovery questions rather than idea volume, and `loop` once a
  chosen direction needs iterative execution.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💡"}'
  related-skills: '{"diverge":"Multi-perspective evaluation and synthesis when idea volume is not enough.","question":"Craft interview or discovery questions instead of generating option lists.","loop":"Iterate a chosen direction until success criteria are met."}'
---

## Default: ideas first

When the user asks for ideas, generate immediately. Missing details are fine: the first list will reveal what to clarify.

Match energy to the ask. Quick request → short list. Deep request → fewer ideas with more development.

## Adapt to the request

| Signal | Response |
|--------|----------|
| "Give me 5 ideas" | 5 ideas, simple list |
| "I'm stuck on X" | 3–5 angles that unblock |
| "Brainstorm names" | 10–20 options with varied styles |
| "Help me think through X" | Explore angles; ask at most one clarifying question if needed |
| "What are my options?" | Structured comparison with trade-offs |

## Clarify only when needed

Ask at most one clarifying question when:

- the request is genuinely ambiguous (not merely incomplete)
- significant effort would be wasted without a constraint
- a missing constraint would completely change the output

Otherwise generate first and let the user steer.

## Structure when it clarifies

Use structure only when it helps:

- **Comparisons:** table with trade-offs
- **Many ideas:** group by theme
- **Recommendations:** highlight a top pick with reasoning

A flat list is enough for most requests.

## Modes and expansion prompts

Load `references/modes.md` when choosing Rapid Fire, Structured, Deep Dive, Provocative, or Collaborative delivery.

Load `references/prompts.md` when the user is stuck, wants more variety, or asks for SCAMPER / lateral-thinking moves.

Keep `SKILL.md` as the entry point; open references only for the active mode or framework.

## After the first round

If the user wants more: go deeper, wider, or change direction.
If the user is silent: treat the task as complete.

## Routing boundaries

- Load `diverge` when the user needs competing perspectives synthesized into a decision, not just more options.
- Load `question` when the deliverable is better interview / discovery questions rather than idea lists.
- Load `loop` after a direction is chosen and needs controlled iteration to a success criterion.

Research notes and verified ideation sources live in `references/sources.md`.
