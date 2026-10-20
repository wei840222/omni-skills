# Terminology and quality

Load when building glossaries, enforcing do-not-translate lists, or scoring quality.

## Glossary discipline

The first accepted rendering of a term becomes a glossary row with:

- source term
- target rendering
- locale
- part of speech
- reason / domain note
- owner / date

The first rejected rendering becomes a forbidden row for the same locale. Consistency beats elegance: two words for one concept read as two concepts.

## Do-not-translate enforcement

Default DNT classes live in `SKILL.md`. Project additions live under `<state_root>/glossaries/` and are checked at delivery.

## Quality posture

- Define risk-bearing segments before starting (numbers, dosages, negations, obligations, deadlines, names)
- Prefer second-person revision; otherwise delayed self-review with source hidden, plus back-translation on risk segments
- Score with a stated typology/formula (for example MQM-style error classes) rather than an unexplained opinion
- "Correct but not how we say it" is usually register/variant mismatch — fix Rule 7, not only the sentence

## Memory writes

Durable term decisions, rejected renderings, register choices, delivered jobs, and reviewer corrections are written in the same turn using `assets/memory-template.md`.
