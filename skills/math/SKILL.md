---
name: math
description: Explain mathematical concepts, solve problems with checkable steps, generate practice, and discuss proofs at an appropriate level. Use when a user needs help learning, verifying, teaching, or exploring mathematics.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔢"}'
---

This skill is stateless and does not store local configuration or persistent user state.

## Adapt the response

1. Infer the user's level from their vocabulary, problem complexity, and prior work. When the level is unclear, begin with an accessible explanation and calibrate from the reply.
2. State the goal, known quantities, assumptions, and the method before presenting a multi-step solution.
3. Show enough intermediate work for the user to check each transformation. Label an intuitive explanation separately from a formal proof.
4. End with a result check: substitute an answer where possible, verify units and domains, and test whether the magnitude is plausible.

## Teach and collaborate by audience

### Children

- Celebrate effort and use concrete objects, diagrams, number lines, or small groups before abstract notation.
- Present one small step, check understanding, and then continue.
- Treat mistakes as information: identify what was right before correcting the next idea.

### Students and homework

- Ask what the student has tried, then guide the next useful step while explaining why it works.
- Scaffold proofs with definitions, candidate strategies, and a clear structure.
- Connect recurring concepts across courses and name the intended rigor level.

### Experts and open questions

- Distinguish established theorems, conjectures, heuristics, and open problems.
- State uncertainty and the boundary of available knowledge. Use precise LaTeX and offer counterexamples or stress tests when useful.
- Frame work on open problems as exploratory reasoning rather than a claimed resolution.

### Teachers

- Generate graduated problem sets with answer keys and multiple representations: visual, algebraic, and contextual.
- Surface likely misconceptions, then use formative questions to locate the student's current model.
- Read `references/math-education-research.md` when designing instruction around common misconceptions or research-backed intervention choices.

## Diagnose and recover

- Check for common errors such as distributing an exponent across a sum, invalid fraction addition, division by zero, sign errors, or a formula used outside its domain.
- When a result conflicts with a constraint, re-check the problem statement, units, assumptions, and algebra. Explain whether a typo, missing condition, or ambiguity prevents a unique answer.
- For calculations beyond reliable manual verification, provide a reproducible method or ask for an appropriate tool check rather than presenting unverified precision.
