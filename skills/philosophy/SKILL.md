---
name: philosophy
description: Guide philosophical inquiry from first questions to scholarly debate. Use when the user wants to discuss philosophical concepts, evaluate arguments, or design pedagogy.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🤔"}'
  related-skills: '{"in-depth-research": "Provides deep research strategies for tracking philosophical debates."}'
---

This skill is stateless and does not store local configuration or persistent user state.

## Core Directives
- **Detect Level, Adapt Everything**: Context reveals level (terminology, thinkers mentioned, argument structure). When unclear, start with intuitions and adjust based on response. Always match the complexity of the response to the user's level of expertise.
- **Always**:
  - Clarify the question before answering — philosophical disputes often hide verbal disagreements.
  - Distinguish descriptive from normative — what is vs what ought to be.
  - Arguments matter more than conclusions — how you get there is the philosophy.

## Progressive References

Load the appropriate reference based on the user's identified level:

| Reference | When to load |
|---|---|
| `references/beginners.md` | The user is exploring basic intuitions or asking introductory questions. |
| `references/students.md` | The user is studying formal arguments, fallacies, or writing philosophy papers. |
| `references/researchers.md` | The user is engaging with academic literature, exegesis, or scholarly debate. |
| `references/teachers.md` | The user is teaching, assessing, or designing philosophical curricula. |
