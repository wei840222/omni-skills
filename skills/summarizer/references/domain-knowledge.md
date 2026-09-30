# Domain Knowledge — Summarization

Verified sources used to ground summarization conventions during the Gate 6 research pass.

## Automatic summarization overview

- Wikipedia — Automatic summarization: https://en.wikipedia.org/wiki/Automatic_summarization
- Wikipedia — Abstract (summary): https://en.wikipedia.org/wiki/Abstract_(summary)
- Wikipedia — Executive summary: https://en.wikipedia.org/wiki/Executive_summary

## Position bias and long-context behavior

- Liu et al. — Lost in the Middle: How Language Models Use Long Contexts (arXiv 2307.03172): https://arxiv.org/abs/2307.03172 | https://aclanthology.org/2024.tacl-1.9/
- Key finding: LLMs show degraded performance on information located in the middle of long inputs; lead and tail are retrieved more reliably.

## Journalism and BLUF

- Wikipedia — Inverted pyramid (journalism): https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)
- Wikipedia — BLUF (communication): https://en.wikipedia.org/wiki/BLUF_(communication)
- Digital.gov — Plain language guide: https://digital.gov/guides/plain-language/
- plainlanguage.gov guidelines: https://www.plainlanguage.gov/guidelines/

## Meeting minutes and action items

- Wikipedia — Minutes: https://en.wikipedia.org/wiki/Meeting_minutes

## Application in this skill

- Lead-first strategy for news, press releases, and executive summaries follows the inverted-pyramid and BLUF conventions.
- The "lost in the middle" paper directly informs the explicit middle-handling rule in SKILL.md (Where The Payload Lives) and the chunk-and-merge path in long-sources.md.
- Action-item format (owner + verb + date) is the canonical requirement for meeting minutes.
- Plain-language guidance informs the hedge/quantifier/attribution preservation rules and the Output Gates.
