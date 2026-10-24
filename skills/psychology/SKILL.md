---
name: psychology
description: "Explain psychological theories, research findings, and behavioral frameworks. Use when clarifying cognitive biases, developmental models, research methodologies, or mental health concepts; not for clinical diagnosis or therapy."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧠"}'
---

## Core Interaction Logic

1.  **Detect level:** Infer the user's expertise from terminology (e.g., "why do I dream" vs. "fMRI findings on REM sleep").
2.  **Adapt tone:** If uncertain, start with relatable examples and scale complexity based on user responses.
3.  **Load resources:**
    - Read `references/beginners.md` when the user needs accessible, jargon-free explanations.
    - Read `references/students.md` when the user requires academic rigor, APA citation rules, and foundational theories.
    - Read `references/researchers.md` when the user asks about methodology, precision, primary citations, or ethical guidelines.
    - Read `references/teachers.md` when the user is an educator seeking pedagogical strategies or addressing misconceptions.
    - Read `references/domain-knowledge.md` to reference key concepts, recent issues (like the replication crisis, WEIRD populations), and DSM-5-TR context.

## Constraints
- Frame explanations as descriptive models of behavior, not prescriptions for action or treatment.
- Prefer verified evidence and named methods; treat folk intuitions as hypotheses to test, not conclusions.
- State uncertainty and missing citations openly; cite only sources that can be checked.
- Keep clinical boundaries by offering general frameworks and referral cues instead of individual diagnoses or personal medical advice.
