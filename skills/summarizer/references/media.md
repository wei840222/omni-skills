# Audio, Video, and Transcripts

Scope: podcast, lecture, webinar, and video transcripts (text already extracted).

## Procedure

1. Strip sponsor reads, intros/outros padding, and pure filler (often 5–15% runtime).
2. Keep timestamps for quotable or decision-bearing spans.
3. Repair ASR proper nouns against `<state_root>/glossary.md` and known speakers.
4. Prefer content after signal phrases ("so the point is", "the takeaway") and the last minutes for talks.

## Fidelity

- Quotes stay extractive; never paraphrase attributed speech presented as a quote.
- Hedge and negation words in speech are easy ASR errors — verify before upgrading certainty.
