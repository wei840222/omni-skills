---
name: turkish
description: >
  Draft, translate, and revise natural Turkish for messages, posts, emails,
  and everyday copy. Use when Turkish needs a clear sen/siz choice, casual
  particles and fillers (ya, yani, işte, hani), spoken reductions (naber,
  napıyon, di mi), or a less textbook wording; keep explicitly formal Turkish
  for professional, institutional, older, or unfamiliar recipients. Prefer
  `turkey` for itinerary planning, `translate` for multi-pair localization
  jobs, and `arabic`/`persian` when those languages are the target—not a full
  language course.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇹🇷","displayName":"Turkish"}'
  related-skills: '{"turkey":"Plan Turkey travel clusters and logistics rather than composing Turkish text.","translate":"Translate an existing source text into Turkish across formats and locales.","writing":"Shape broader prose once the Turkish-language decision is settled.","english":"Draft or revise the English source before translating it into Turkish.","copywriting":"Shape persuasive marketing copy after the Turkish register is chosen.","arabic":"Write Arabic when Turkish is not the target language.","persian":"Write Persian when Turkish is not the target language."}'
---

Research notes for sen/siz, particles, greetings, and authoritative resources live in `references/sources.md` (progressive disclosure).

Expanded register tables, fillers, expressiveness, reactions, and delivery checks live in `references/domain.md` (progressive disclosure).

## When to load

Load this skill to write, rewrite, or translate **Turkish** that should sound like a person, not a textbook. Prefer this skill over generic `translate` when sen/siz choice, particles (`ya`, `yani`, `işte`, `hani`), fillers, spoken reductions, internet reactions, or casual Turkish tone change the draft.

For Turkey travel routing, load `turkey` instead. Hand multi-pair localization catalogs to `translate`. For Arabic or Persian targets, load `arabic` or `persian` as the primary skill.

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify audience, relationship, channel, source text, and requested tone. When those details are missing, write warm casual peer Turkish with **`sen`** and state the register assumption in one short note when the choice matters.
2. Choose one address form and keep it for the whole draft:
   - **`siz`**: strangers initially, elderly, professional, or explicitly formal
   - **`sen`**: friends, peers, internet, and most casual channels
3. Draft for the selected register. Preserve names, numbers, dates, commitments, and how sure the source is. For casual text, use direct phrasing and add at most a few particles, fillers, reductions, or light reactions that fit the speaker and channel.
4. Read `references/domain.md` for human-facing Turkish drafts, rewrites, and reviews; use its formality, particles, expressiveness, and delivery guidance. Load `references/sources.md` when a sen/siz or lexical claim needs verification.
5. Run the delivery check, then return the Turkish text first.
6. If address form is unclear after drafting, rewrite once toward casual **`sen`** for peer chat or careful **`siz`** for unfamiliar recipients, and state the assumption briefly rather than stopping without a draft.

## Formality default

Casual Turkish is warm and direct. Unless the audience is professional, institutional, older, unfamiliar, or explicitly formal, lean casual among peers and on the open internet. For unknown recipients in work or institutional settings, prefer **`siz`** rather than inventing intimacy.

| Situation | Default | Delivery rule |
| --- | --- | --- |
| Official, academic, or unfamiliar institution | `siz` + clearer greetings | Complete sentences; avoid heavy slang and intimate particles |
| Work chat with known colleagues | soft `siz` or established `sen` by workplace norm | Clear and friendly; light particles only if that chat already uses them |
| Friend, peer chat, or social post | `sen` | Short lines, natural fillers, selective reactions |
| Public or mixed audience | Neutral everyday | Stay readable; skip intimate slang stacks unless requested |

## Address and sen/siz

- **`sen`:** safe default for friends, peers, and most Turkish internet writing.
- **`siz`:** reserved for strangers initially, elders, and explicitly formal or institutional copy.
- Keep pronouns, verb agreement, and greetings aligned with the chosen address for the whole draft. Mid-text sen/siz drift is a Required failure.

## Scope boundary

- In scope: drafting, translating, and revising Turkish phrasing for messages, comments, posts, and short copy.
- Out of scope: Turkey travel planning (`turkey`), legal advice, full grammar courses, or Arabic/Persian-first writing (`arabic` / `persian`).

## Delivery check

Before sending:

1. Confirm one sen/siz choice and matching greetings or verb forms.
2. Facts, names, numbers, dates, commitments, and uncertainty from the source are preserved.
3. Particles, fillers, reductions, and slang appear only when the channel and relationship support them.
4. A native reader would not screenshot the draft as stiff textbook Turkish for the chosen register.
5. For legal, medical, financial, or publication-sensitive Turkish, keep the requested formality and recommend a qualified native-speaker review.
