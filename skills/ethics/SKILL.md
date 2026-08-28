---
name: ethics
description: Guide moral reasoning, from resolving personal ethical dilemmas to analyzing academic philosophy and contemporary metaethics. Trigger when asked about morality, dilemmas, argument structures, or philosophy teaching protocols.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⚖️"}'
  related-skills: '{"philosophy":"Broader philosophical inquiry beyond applied moral dilemmas","writing":"Essay drafting and voice when ethics is not the primary subject","studying":"Study planning when the user needs exam prep rather than moral analysis"}'
---

## Detect Level, Adapt Everything
- Context reveals level: "is it wrong to..." vs citing Scanlon vs asking about metaethics.
- When unclear, start with their specific situation and adjust.
- Adapt your response to the user's expertise level.

## Progressive Disclosure
Load the appropriate reference based on the user's context:
- For personal dilemmas or introductory questions, read `references/beginners.md`.
- For essay writing, argument structure, or historical interpretation, read `references/students.md`.
- For contemporary debates, methodology, or metaethics, read `references/researchers.md`.
- For curriculum design, classroom protocols, or teaching methods, read `references/teachers.md`.

## Always Check
- Separate empirical from moral disagreements — many disputes dissolve when facts are clarified.
- Define terms precisely — "rights," "justice," "harm" mean specific things in ethics.
- Acknowledge genuine uncertainty — some dilemmas lack clean answers.

## Detect User Errors
- Conflating "legal" with "ethical" — laws can be unjust.
- Appeal to tradition or nature as moral proof — "we've always done it" does not serve as justification.
- False dichotomies — most dilemmas have more than two options.
