---
name: first-principles-thinking
description: >
  Break a stuck or novel problem down to verified fundamentals, strip hidden
  assumptions, and rebuild a solution from physics, logic, or math rather than
  convention. Use when conventional methods fail, the user asks for first
  principles, root-cause redesign, blank-slate thinking, or assumption audits.
  Not for routine optimization with a proven playbook (use analogy), pure
  long-horizon consequence chains (second-order-effects), or logging a past
  decision pattern (decide).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔬"}'
  related-skills: '{"business":"Strategy and commercial constraints once fundamentals are clear.","ceo":"Executive framing when the rebuilt option needs leadership tradeoffs.","decide":"Log the chosen option and approval boundary after fundamentals rebuild.","second-order-effects":"Trace multi-order consequences after a rebuilt option is on the table.","six-thinking-hats":"Parallel thinking modes when multiple stakeholder lenses are needed.","startup":"Zero-to-PMF rebuilds that start from customer fundamentals.","strategy":"Portfolio and positioning choices after the problem is reduced to fundamentals."}'
---

## When to load

| Need | Resource |
| --- | --- |
| Full three-step protocol, traps, output schema | `references/core-rules.md` |
| Five Whys depth, component/cost/constraint maps | `references/decomposition.md` |
| Seven assumption traps and stress tests | `references/assumptions.md` |
| Definitions and dated citations | `references/sources.md` |
| Evaluation harness only | `test-prompts.json` |

## Operating sequence

1. **State the problem in one sentence** with the outcome that matters. Separate stated want from underlying need.
2. **Inventory assumed constraints** and tag each as physics, logic, regulation, convention, or untested assumption. Load `references/assumptions.md` when the phrasing looks like historical, authority, social, or resource lock-in.
3. **Decompose to functions, not implementations.** Keep going until claims rest on physics, logic, math, or a named regulation. Load `references/decomposition.md` for Five Whys depth, component maps, and cost stacks.
4. **Verify each remaining claim.** Ask origin, falsifier, and whether the reason still applies. Prefer primary evidence over analogy.
5. **Rebuild upward** from verified fundamentals only. Generate options per function, score against fundamentals, then combine a minimum-viable solution that can actually be built.
6. **Emit the structured output** in `references/core-rules.md` (problem, assumed constraints, fundamentals, decomposition, rebuilt solution, assumptions challenged). Hand off to `second-order-effects` when multi-order impact matters, or to `decide` when the choice must be logged.
7. **Load `references/sources.md`** before citing definitions, historical examples, or external method claims so dates stay attached.

## Scope

- Reasoning only: no persistent skill state, no network calls, no package-local writes.
- Prefer first principles for novel or stuck problems; prefer analogy when a proven playbook already fits and time is tight.
- Keep implementation constraints visible; a fundamental solution that cannot be built is incomplete.
- Challenge conventions without discarding valid physics or hard legal limits.

## Near-misses

| Request shape | Better skill |
| --- | --- |
| “What happens after we ship X over 1–3 years?” | `second-order-effects` |
| “Log how we chose the database last time.” | `decide` |
| Parallel stakeholder lenses without root rebuild | `six-thinking-hats` |
| Pure strategy portfolio choice after fundamentals are known | `strategy` |
