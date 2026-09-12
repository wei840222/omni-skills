---
name: science
description: Explain science for children, students, researchers, and teachers across physics, chemistry, earth science, space, and general scientific reasoning. Use when the user asks science questions, needs level-adapted explanations, experimental design help, science-literacy checks, or lesson support; load audience references and sources before answering.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔬"}'
  related-skills: '{"biology":"Organism-level life science, physiology, genetics, ecology, and biology education.", "chemistry":"Matter, reactions, stoichiometry, and lab chemistry depth.", "physics":"Mechanics, energy, waves, fields, and quantitative physics derivations.", "math":"Mathematical methods, proofs, and quantitative checks that science explanations depend on.", "computer-science":"Algorithms, computation, and programming reasoning adjacent to scientific computing."}'
---

## State location

This skill is completely stateless. It does not store or read local configuration or state.

## Use this skill

1. Identify the audience from vocabulary, goals, and question complexity; when unclear, start with a short accessible explanation and offer a deeper layer.
2. Load `references/core-rules.md` for every response.
3. Load exactly one audience reference that fits: `references/children.md`, `references/students.md`, `references/researchers.md`, or `references/teachers.md`.
4. For factual claims, current guidance, or primary literature checks, load `references/sources.md` and prefer the primary source over memory.
5. State what is established consensus, what is active debate, and what is unknown or knowledge-cutoff limited when that distinction changes the answer.
6. For personal medical, clinical, or hazardous lab decisions, give general science education only and direct the user to a qualified professional or institutional safety authority.

## Quick reference

| File | Load when |
|---|---|
| `references/core-rules.md` | Every science request. |
| `references/children.md` | Explaining science to children or using wonder-first analogies. |
| `references/students.md` | Coursework, mechanisms, lab reasoning, or exam preparation. |
| `references/researchers.md` | Research framing, methods critique, uncertainty, or literature. |
| `references/teachers.md` | Lessons, demos, differentiation, or assessment design. |
| `references/sources.md` | Verifying a claim, current guidance, or a primary source. |

## Guardrails

- Lead with the supported explanation, then add uncertainty and caveats only when they change the answer.
- Prefer checkable quantities, units, and order-of-magnitude sanity checks over vague adjectives.
- Separate scientific description (what is) from policy or value choices (what should be done).
- Do not invent citations, DOIs, or study results; point to Scholar/PubMed or the sources list for verification.
- Route deep specialty requests to related skills when the user clearly needs biology, chemistry, physics, math, or computer-science depth beyond general science education.
