---
name: galician
description: Write, translate, edit, and linguistically review text in natural Galician (galego). Use when the user needs Galician-language copy, a Galician translation, or a Galician grammar, vocabulary, register, or orthography review.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🌐"}'
---

## Scope and state

This is a language-only skill. It creates no persistent state and writes no files unless the user separately requests an artifact.

## Default workflow

1. Identify the task: write, translate, edit, or explain a linguistic choice. Preserve names, quotations, technical terms, and any requested format.
2. Identify the requested variety and register. Honor an explicitly requested regional or reintegrationist spelling. Otherwise, write clear standard Galician; use the source text and audience to set the register.
3. Translate or revise for meaning first, then make grammar, spelling, and vocabulary internally consistent. For uncertain normative choices, read `references/authorities.md` and use the linked Real Academia Galega resources.
4. Deliver only the requested text by default. Add a brief note on material choices when the user asks for an explanation, review, or alternatives.

If the intended audience, register, or variety would materially change the result, ask one focused question. When a default is sufficient, use neutral standard Galician rather than adding invented regional or colloquial markers.

## Register and address

- Derive formality from the audience, purpose, and source text; a greeting such as `Ola` or `Bo día` can be appropriate in different contexts.
- Use `ti` when the context establishes familiar address. Use `vostede` for courtesy address or when the user requests formal treatment. Keep the chosen address form consistent.
- Preserve source-language code-switching only when the user requests it or it is meaningful to the source. Otherwise, produce coherent Galician rather than adding Spanish words or fillers for effect.

## Accuracy checks

Before sending text, check:

1. **Meaning:** The translation or edit preserves the source intent, constraints, and names.
2. **Agreement:** Articles, nouns, adjectives, pronouns, and verbs agree in gender, number, and person.
3. **Galician choices:** Prefer established Galician spelling and vocabulary when standard Galician is requested. For example, use `grazas`; use `rapaz` and `rapaza` when those meanings fit.
4. **Consistency:** Keep the chosen orthography, address form, and register stable throughout the output.
5. **Audience fit:** Read the result as the target recipient would; remove unexplained formality, slang, or dialect signals that the request does not support.

## Common risks

| Situation | Reliable approach |
| --- | --- |
| Formality is unspecified | Use neutral, clear standard Galician and let the content determine the greeting and tone. |
| `ti` or `vostede` is unclear | Ask who the recipient is when the distinction changes the text; otherwise keep the source’s address form. |
| A word may be Spanish, Portuguese, regional, or nonstandard | Check the RAG dictionary through `references/authorities.md`; preserve an explicitly requested variety. |
| An authority is unavailable or leaves a form unresolved | State that the normative check is unresolved, preserve the supplied form when possible, and ask a focused question before making a meaning-changing substitution. |
| The user asks for reintegrationist spelling | Follow the user’s stated convention and keep it consistent; ask for a model text when the convention is not specified. |
| The source mixes languages | Retain meaningful source code-switching or explain a standard-Galician normalization when requested. |

## Review output

For a language review, return:

1. the corrected Galician text;
2. the material corrections, grouped by grammar, vocabulary, spelling, or register; and
3. one alternative only when it represents a genuine register or variety choice.
