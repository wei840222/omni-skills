---
name: biology
description: Explain biology for children, students, researchers, and teachers. Use when the user asks about biological concepts, experiments, organisms, physiology, genetics, ecology, or biology education.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧬"}'
---

## Use this skill

1. Identify the audience from the question; when it is unclear, start with a short accessible explanation and offer a deeper layer.
2. Load `references/core-rules.md` for every response.
3. Load exactly the audience reference that fits: `references/children.md`, `references/students.md`, `references/researchers.md`, or `references/teachers.md`.
4. State what is established, what is uncertain, and what depends on species, conditions, or study design.
5. For health, diagnosis, or treatment questions, provide general education and direct the user to an appropriately qualified clinician for personal decisions.

## Quick reference

| File | Load when |
|---|---|
| `references/core-rules.md` | Every biology request. |
| `references/children.md` | Explaining biology to children or using foundational analogies. |
| `references/students.md` | Supporting coursework, exam preparation, mechanisms, or lab interpretation. |
| `references/researchers.md` | Discussing research, nomenclature, study design, statistics, or literature. |
| `references/teachers.md` | Designing lessons, assessments, demonstrations, or lab activities. |
| `references/sources.md` | Verifying a factual claim, current guidance, or a primary source. |

## Guardrails

- Lead with the supported explanation, then state uncertainty and context-dependent exceptions only when they change the answer.
- Distinguish educational explanation from individualized medical, veterinary, or laboratory safety advice.
- Use age-appropriate, scientifically correct language for reproduction and anatomy.
