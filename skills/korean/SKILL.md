---
name: korean
description: >
  Compose, translate, and revise natural Korean for messages, posts, emails,
  and everyday copy. Use when Korean needs a clear 합쇼체/해요체/반말 choice,
  consistent speech level, contractions, particles, or less textbook wording;
  keep explicitly formal Korean for professional, institutional, older, or
  unfamiliar recipients. Prefer `translate` for multi-pair localization jobs
  and `japanese`/`chinese` when those languages are the target—not a full
  language course or Korea travel planner.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇰🇷"}'
  related-skills: '{"japanese":"Write Japanese when Korean is not the target language.","chinese":"Write Mandarin Chinese when Korean is not the target language.","traditional-chinese":"Write Traditional Chinese when Korean is not the target language.","translate":"Translate an existing source text into Korean across formats and locales.","writing":"Shape broader prose once the Korean-language decision is settled.","english":"Draft or revise the English source before translating it into Korean.","copywriting":"Shape persuasive marketing copy after the Korean register is chosen."}'
---

Research notes for speech levels, honorifics, and authoritative resources live in `references/sources.md` (progressive disclosure).

Expanded register tables, contractions, particles, slang boundaries, and delivery checks live in `references/domain.md` (progressive disclosure).

## When to load

Load this skill to write, rewrite, or translate **Korean** that should sound like a person, not a textbook. Prefer this skill over generic `translate` when speech-level choice (합쇼체 / 해요체 / 반말), particle dropping, contractions, fillers, internet slang, or casual Korean tone change the draft. Load references on demand rather than dumping every table into the first reply.

For Japanese, Mandarin, or Traditional Chinese targets, load `japanese`, `chinese`, or `traditional-chinese` as the primary skill instead. Hand multi-pair localization catalogs to `translate`.

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify audience, relationship, channel, source text, and requested tone. When those details are missing, write neutral 해요체 Korean and state the register assumption in one short note when the choice matters.
2. Choose one speech level and keep it for the whole draft:
   - 합쇼체 (-습니다): news, presentations, highly formal institutions
   - 해요체 (-아/어요): polite default for strangers, mixed audiences, work chat
   - 반말/해체 (-아/어): friends, peers, or an explicit casual request
3. Draft for the selected register. Preserve names, numbers, dates, commitments, and how sure the source is. For casual text, use direct phrasing and add at most a few contractions, fillers, particles, or light slang that fit the speaker and channel.
4. Read `references/domain.md` for human-facing Korean drafts, rewrites, and reviews; use its register, contractions, particles, expressiveness, and delivery guidance.
5. Run the delivery check, then return the Korean text first.

## Formality default

Casual Korean is warm and direct online among peers. Unless the audience is professional, institutional, older, unfamiliar, or explicitly formal, lean casual only when the relationship supports 반말. For unknown recipients, default to 해요체 rather than inventing intimacy.

| Situation | Default | Delivery rule |
| --- | --- | --- |
| Official, academic, news, or unfamiliar institution | 합쇼체 or careful 해요체 | Full greetings, complete sentences, no slang or heavy particle drop |
| Work chat with known colleagues | 해요체 | Clear and polite; light contractions only if that workplace already uses them |
| Friend, peer chat, or social post | 반말 when relationship is clear | Short lines, natural fillers, selective ㅋㅋ / reactions |
| Public or mixed audience | Neutral 해요체 | Stay readable; skip intimate 반말 and dense slang unless requested |

## Address and speech level

- **해요체:** safe default for most written Korean, mixed audiences, and professional contexts.
- **합쇼체:** reserved for news-style, ceremonial, or highly formal institutional copy.
- **반말:** intimate or peer. Use only when the user or supplied sample clearly wants that relationship; do not invent 반말 for strangers or formal recipients.
- Keep verb endings, pronouns, and honorifics aligned with the chosen level for the whole draft. Mid-text level drift is a Required failure.

## Scope boundary

Use this skill for Korean-language writing, rewrites, and translations. Keep an explicitly formal or professional request formal. For a mixed or public audience, use neutral language rather than assuming familiarity or a speaker identity. This skill is not a travel planner, legal advisor, or full language course.

## Delivery check

Before sending:

1. Speech level is consistent end to end.
2. Facts, commitments, and uncertainty from the source are preserved.
3. Slang, 애교 endings, and crude intensifiers appear only when the channel and relationship support them.
4. A native reader would not screenshot the draft as stiff textbook Korean for the chosen register.
