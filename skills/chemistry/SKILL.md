---
name: chemistry
description: Teach and check chemistry from kitchen-level ideas to mechanisms, spectroscopy, stoichiometry, and computational method choice. Use when the user asks about reactions, equations, naming, lab safety, or level-adapted chemistry help. Not for synthesizing controlled substances, bypassing precursor controls, or giving an unverified exposure limit.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧪"}'
  related-skills: '{"science":"Broader science explanations when the question is not chemistry-specific.","biology":"Organism-level life science when the question leaves molecular chemistry.","physics":"Mechanics, energy, and quantitative physical derivations.","math":"Algebra, calculus, or proof checks that a chemistry calculation depends on."}'
---

# Chemistry

## When to use

Use this skill for chemistry learning and technical explanation: concepts, balanced equations, mechanisms, spectroscopy reading order, naming, computational method choice, and instructional support.

Stay inside education and explanation. Do not provide a synthesis route, quantities, or conditions for a controlled substance, listed precursor diversion, or an explosive. For a hazardous procedure, state the hazard and the institutional safety authority before any step.

## State location

This skill is stateless. Do not write local files.

## Route

1. State safety considerations before any reaction or procedure. Verify stoichiometry and say when an equation is not yet balanced.
2. Load `references/pedagogy.md` and follow the matching level: beginner, student, researcher, or teacher.
3. Load `references/sources.md` before citing a safety rule, an IUPAC name, a DOI, or a computational recommendation that depends on current guidance.
4. Mark a simplified model as simplified. Distinguish an accepted mechanism from one proposed pathway.

## Always

- Safety before steps.
- Balanced equations, or an explicit note that the equation is unchecked.
- Respect the user's level: concrete first for beginners, precise conditions for researchers.
