---
name: sociology
description: >
  Support sociological thinking from everyday observation to academic research
  by adapting to user level, connecting theory to evidence, keeping theoretical
  pluralism, and prioritizing structural explanations. Use when the user asks
  about social stratification, culture, institutions, inequality, classical or
  contemporary theory, methods, teaching sociology, or applying the sociological
  imagination. Not for individual clinical diagnosis (psychology), pure
  first-principles rebuilds without social structure (first-principles-thinking),
  or long multi-order consequence chains alone (second-order-effects).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"👥"}'
  related-skills: '{"psychology":"Individual cognition and clinical frameworks when the question is person-level rather than structural.","writing":"Academic or public writing craft after the sociological argument is clear.","journal":"Free-form field notes and reflections outside structured analysis.","decide":"Log a chosen research design or policy option after analysis.","six-thinking-hats":"Parallel stakeholder lenses when facilitation needs multiple roles.","second-order-effects":"Trace multi-order consequences of a social intervention after the structural diagnosis.","first-principles-thinking":"Strip assumptions when a social problem is stuck in convention and needs fundamentals rebuild."}'
---

## When to load

| Need | Resource |
| --- | --- |
| Level detection and always-on rules | `references/guidelines.md` |
| Beginner framing and jargon translation | `references/beginners.md` |
| Student theory–evidence and writing moves | `references/students.md` |
| Researcher rigor, methods, IRB, journals | `references/researchers.md` |
| Teacher scaffolding and sensitive topics | `references/teachers.md` |
| Verified domain facts and dated sources | `references/domain-knowledge.md` |
| Evaluation harness only | `test-prompts.json` |

## Operating sequence

Load at most one audience branch per turn after `references/guidelines.md`; pull `domain-knowledge.md` only when citing facts.


1. **Detect level** from terminology, theorists named, method awareness, and assignment constraints. When unclear, start with observable patterns and scale up from the user’s replies. Load `references/guidelines.md` first.
2. **Choose the audience branch**: beginners → `references/beginners.md`; coursework/papers → `references/students.md`; design/analysis/publication → `references/researchers.md`; classroom facilitation → `references/teachers.md`.
3. **Keep the sociological imagination on**: connect personal troubles to public issues; pair individual explanations with structural ones; separate description from endorsement.
4. **Ground claims** before citing theorists, statistics, or methods. Load `references/domain-knowledge.md` for stratification, classical/contemporary theory anchors, methods pluralism, and source URLs. Flag uncertainty; do not fabricate citations.
5. **Match depth to the ask** (one concept with an everyday example vs. epistemology, coding, or journal norms). Prefer evidence over common sense; challenge essentialist language with social-construction reframes.
6. **Hand off when needed**: person-level clinical framing → `psychology`; multi-order policy consequences → `second-order-effects`; assumption-stripping rebuild → `first-principles-thinking`; writing polish → `writing`.

## Scope

- This skill is reasoning guidance only: no persistent skill state, no network calls required by the package, no package-local writes.
- Explain social patterns; do not prescribe illegal action, discriminatory targeting, or individual clinical treatment.
- Maintain theoretical pluralism (functionalism, conflict, interactionism, feminist and critical traditions, and others named by the user) without declaring a single default “correct” theory.
- Statistics and method advice stay interpretive and hedged; report what a coefficient or design *means*, not fake precision.

## Near-misses

| Request shape | Better skill |
| --- | --- |
| “Why do I keep procrastinating / is this anxiety?” | `psychology` |
| “Rebuild this org from physics-level fundamentals.” | `first-principles-thinking` |
| “What happens 2–3 orders out if we ban X?” | `second-order-effects` |
| “Polish this essay’s prose only.” | `writing` |
| “Log how we chose the research design.” | `decide` |
