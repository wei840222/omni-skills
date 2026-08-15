---
name: grammar
description: Correct grammar, spelling, punctuation, and agreement while preserving intended meaning, voice, formatting, language variety, and register. Use when a user asks to proofread, correct, or explain errors in text.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"✏️"}'
---

## Correct text

1. Identify the text's language, regional variety, register, and intended meaning before editing.
2. Correct actual spelling, grammar, punctuation, and agreement errors.
3. Preserve the author's voice, word choices, sentence structure, capitalization, and formatting. Treat intentional fragments, dialect, informal constructions, code-switching, and loanwords as valid unless the user asks to standardize them.
4. Keep regional conventions consistent with the source text, such as British or American spelling.
5. When a possible correction could change meaning, ask a focused clarification question or retain the original wording.

## Output

- Return the corrected text only unless the user asks for explanations.
- For a longer text, use the interface's supported diff or change-highlighting format when the user asks to see edits.
- Match the original formatting, including intentional capitalization choices.
- State that no corrections are needed when the text contains no actual errors.

## Explanations and learning support

Load `references/grammar-guidelines.md` when explaining corrections, reviewing mixed language varieties, or deciding whether an apparent error is intentional style.

When the user asks why, explain each correction in plain language and identify its type, such as spelling, subject-verb agreement, tense, or punctuation. For a language learner, describe the relevant rule at an appropriate level without changing the requested correction into a broader rewrite.
