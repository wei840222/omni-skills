---
name: basque
description: >
  Compose, translate, and revise natural Basque for messages, posts, and
  everyday copy. Use when Basque needs a clear zu/hi choice, batua vs dialect
  flavor, particles, or less formal wording; keep formal register for
  professional, institutional, older, or unfamiliar recipients. Prefer
  spanish/french/catalan/galician for those languages and translate for
  multi-pair localization—not a full language course.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"spanish":"Write Spanish when Basque is not the target language.","french":"Write French when Basque is not the target language.","catalan":"Write Catalan when Basque is not the target language.","galician":"Write Galician when Basque is not the target language.","translate":"Translate an existing source text into Basque across formats and locales.","writing":"Shape broader prose once the Basque-language decision is settled.","english":"Draft or revise the English source before translating it into Basque.","copywriting":"Shape persuasive marketing copy after the Basque register is chosen.","spain":"Plan Spain travel logistics rather than Basque-language phrasing.","france":"Plan France travel logistics rather than Basque-language phrasing."}'
---

Research notes for zu/hi, batua, dialects, and authoritative resources live in `references/sources.md` (progressive disclosure).

Expanded particle tables, expressiveness, and delivery checks live in `references/style-guide.md` (progressive disclosure).

## When to load

Load this skill to write, rewrite, or translate **Basque** that should sound like a person, not a textbook. Prefer this skill over generic `translate` when zu/hi choice, batua vs dialect flavor, particles (`ba`, `ala`, `bada`, `ezta`), fillers, Spanish/French code-switching, or casual Basque tone change the draft.

For Spanish, French, Catalan, or Galician targets, load `spanish`, `french`, `catalan`, or `galician` as the primary skill instead. Hand off Spain/France travel logistics to `spain` or `france`.

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify audience, relationship, channel, source text, and requested tone. When those details are missing, write neutral batua-leaning Basque and state the register assumption in one short note when the choice matters.
2. Choose one address form and keep it for the whole draft: `zu` for standard, mixed, professional, or unfamiliar contexts; `hi` (hika) only when the user or sample clearly wants intimate regional informality.
3. Draft for the selected register. Preserve names, numbers, dates, commitments, and how sure the source is. For casual text, use direct phrasing and add at most a few particles, fillers, or light code-switching that fit the speaker and channel.
4. Read `references/style-guide.md` for human-facing Basque drafts, rewrites, and reviews; use its register, particles, expressiveness, and authoritative-resource guidance.
5. Run the delivery check, then return the Basque text first.

## Formality default

Casual Basque is warm and direct. Unless the audience is professional, institutional, older, unfamiliar, or explicitly formal, lean casual.

| Situation | Default | Delivery rule |
| --- | --- | --- |
| Official, academic, news, or unfamiliar institution | Formal batua | Prefer full greetings such as `Egun on` / `Arratsalde on`, keep `zu`, avoid slang and heavy code-switching. |
| Work chat with known colleagues | Everyday professional | Stay clear and polite; light particles only if that workplace already uses them. |
| Friend, peer chat, or social post | Casual | Prefer `Kaixo`, direct `Bai` / `Ez`, a few particles, and natural reactions. |
| Public or mixed audience | Neutral everyday batua | Stay readable; skip intimate hika and dense dialect unless the user asked for it. |

## Address: zu vs hi

- **`zu`:** safe default for most written Basque, mixed audiences, and professional contexts.
- **`hi` / hika:** intimate and regional. Use only when the user or supplied sample clearly wants that relationship; do not invent hika for strangers or formal recipients.
- Keep pronouns, verb forms, greeting, and closing in the same address system for the whole draft.

## Batua vs dialects

- **Batua (standard Basque)** is the default for online, mixed-audience, and interregional writing.
- Dialect flavor (Bizkaiera, Gipuzkera, and others) may appear lightly when the user names a region or supplies a dialect sample.
- Do not invent dense dialect grammar the user did not request. Prefer clear batua with optional local vocabulary over unreadable purity.

## Code-switching and bilingual flow

Basque speakers often mix Spanish or French in casual channels. Light, natural mixing can fit peer chat:

- Example shape: `Oso interesting da.`
- Keep pure Basque when the user asks for it, when the channel is formal, or when mixing would obscure meaning.
- Match the bilingual flow of the source rather than forcing textbook monolingual output.

## Delivery check

Before sending:

1. Confirm `zu` or `hi` matches the recipient and stays consistent.
2. Confirm batua vs dialect intensity matches the request.
3. Remove any filler, slang, intensifier, or code-switch that changes the implied relationship or clarity.
4. Keep names, dates, quantities, commitments, and safety-sensitive wording faithful to the source.
5. For publication, legal, medical, or brand-critical text, label the result as a draft and route it to a qualified native reviewer when one is available.
6. Native test: would a Basque speaker screenshot this as stiff AI-generated batua? Prefer natural warmth over formal correctness theater.

## Output shape

Return the Basque text first. Add a one-line register note only when the address form, dialect choice, or formality assumption is material.