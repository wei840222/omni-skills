---
name: welsh
description: Write natural, human-sounding Welsh with appropriate register, regional variation, and bilingual code-switching. Use when the user asks to write, translate, compose, or converse in Welsh (Cymraeg), or needs help with Welsh grammar, formality, dialect choices, or colloquial expressions.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏴󠁧󠁢󠁷󠁬󠁳󠁿"}'
  related-skills: '{"speak":"Supports spoken Welsh practice and pronunciation guidance.","translate":"Handles general translation tasks where Welsh is the target or source language."}'
---

## Core Principle

For direct Welsh writing or translation requests, produce Welsh-only output. Use Welsh–English code-switching when the user supplies or explicitly requests bilingual/Wenglish output, then match that audience's register and mixing density.

## Register Selection

Choose the pronoun from the relationship and number of addressees. Formality and literary-versus-colloquial style are separate choices.

| Audience | Pronoun | Example greeting |
|----------|---------|-----------------|
| Friend, family, or established casual peer | ti (informal singular) | Shwmae / Haia |
| More than one addressee | chi (plural) | Bore da / Prynhawn da |
| A singular stranger, elder, or professional contact | chi (polite singular) | Bore da / Prynhawn da |
| Unclear 1:1 context | chi (polite default) | Bore da |

Use colloquial Welsh for conversation with either pronoun. Use literary Welsh only when the user requests formal written language or the target genre requires it. Move from chi to ti when the relationship or requested audience establishes informal address.

## Regional Variation

Maintain consistency within a single output. Ask which dialect if unclear.

| Feature | North (Gogledd) | South (De) |
|---------|-----------------|------------|
| "He" | fo | fe |
| "I am" (casual) | Dw i | Dw i / Rydw i |
| Tag question | 'te | 'de |
| "Isn't it" | ynde | ynde / 'nde |

## Code-Switching (Wenglish)

Welsh–English mixing is standard in some everyday contexts. Use it when the user requests Wenglish/bilingual output or their input establishes that audience:

- Insert English adjectives, adverbs, or discourse markers: "Mae'n really good", "It's proper brysur heddiw"
- Use English fillers within Welsh sentence structure: "Wel, you know, ti'n gwybod"
- Match the user's mixing density — mirror their ratio of Welsh to English

Welsh-only output can be natural in both formal and casual contexts; match vocabulary and register to the target audience.

## Particles, Fillers & Softeners

These markers signal natural Welsh:

| Marker | Meaning | Region | Usage |
|--------|---------|--------|-------|
| 'de / 'te | tag question | South / North | Sentence-final confirmation |
| ynde | isn't it | Both | Rhetorical agreement |
| felly | so / like | Both | Discourse connector |
| wel | well | Both | Hesitation / opener |
| ia / ie / na | yes / no | Both | Response particles |
| ti'n gwybod / ti'n gweld | you know / you see | Both | Filler phrases |
| gwranda / edrych | listen / look | Both | Attention openers |

## Expressive Vocabulary

Select vivid, specific words over generic ones:

| Generic | Vivid alternatives |
|---------|-------------------|
| da (good) | gwych, bendigedig, ffab, cracking |
| drwg (bad) | ofnadwy, crap, terrible |
| iawn (very/really) | rili, proper, proper mau |

## Common Expressions

| Expression | Meaning | Register |
|------------|---------|----------|
| Iawn, OK, Dim probs | OK / no problem | Casual |
| Dim problem | No problem | Neutral |
| Paid poeni | Don't worry | Casual (ti) |
| Go iawn? | Alright? / OK? | Casual greeting |
| Wir? / Wir yr? | Really? / Seriously? | Casual |
| Be? / Be' ? | What? | Very casual |
| Grêt! / Lyfli! / Ffab! | Great! / Lovely! / Fab! | Casual enthusiasm |

## Natural Reactions

React with the same energy as native speakers:

- Surprise: "Wir yr?!", "Be?!", "Jiw jiw!"
- Affection: "Mam bach!", "Och a!"
- Approval: "Gwych!", "Bendigedig!", "Proper job!"
- Text casual: "Haha", "lol", emoji

## Quality Check

Before finalizing output, verify:

1. Pronoun matches the audience (ti for established informal singular; chi for plural or polite singular)
2. Regional forms are consistent (use one region's forms throughout: fo for North, fe for South)
3. Language choice matches the request: Welsh-only by default; Wenglish only for an explicit bilingual signal
4. Particles and fillers are present where natural
5. Vocabulary is vivid and specific
