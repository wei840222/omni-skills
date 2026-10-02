---
name: hungarian
description: >
  Compose, translate, and revise natural Hungarian for messages, posts, and
  everyday copy. Use when Hungarian text needs a register choice, te/ön forms,
  particles, fillers, conjugations, or a less formal translation; keep irodalmi
  or Ön/Maga for official, academic, or unfamiliar recipients. Not for a full
  language course, legal translation certification, or non-Hungarian languages.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇭🇺"}'
  related-skills: '{"copywriting":"Shape persuasive marketing copy after the Hungarian register is chosen.","english":"Draft or revise the English source before translating it into Hungarian.","polish":"Apply the same register-first casual-writing method to Polish instead of Hungarian.","speak":"Handle spoken delivery cues after the Hungarian wording is settled.","writing":"Plan structure and argument before polishing the Hungarian wording."}'
---

## When to load

Load this skill to write, rewrite, or translate Hungarian that should sound like a person, not a textbook. Load `references/sources.md` before repeating a register label, a te/ön mapping, or a particle gloss that needs a primary source.

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify the audience, relationship, channel, source text, and requested tone. If the request names no register, choose warm casual te-register and say so in one short note.
2. Pick one register and keep it for the whole draft. Match a sample the user already supplied when one exists.
3. Choose pronouns, conjugations, particles, and fillers that fit that register. Preserve names, numbers, dates, commitments, and how sure the source is.
4. Run the native delivery check, then return the Hungarian text first.

## The Real Problem

AI Hungarian is often technically correct but sounds off: too formal, too *irodalmi* (literary), and thin on particles. Natives write more casually, with warmth and flow. Match that unless formality is required.

## Register

| Situation | Default | Delivery rule |
| --- | --- | --- |
| Official, academic, news, or unfamiliar institution | Irodalmi / formal | Prefer `Ön`/`Maga`, full polite forms, and standard spelling; skip intimate slang. |
| Work chat with known colleagues | Everyday professional | Stay clear and polite; add light particles only if that workplace already does. |
| Friend, peer chat, or social post | Casual te | Use `te`, natural fillers, and a few particles. |
| Public or mixed audience | Neutral everyday | Stay readable; skip intimate slang and heavy profanity. |
| Explicit formal request | That formal voice | Keep one formal system for the whole draft. |

Casual Hungarian is warm. Unless the user asks for formal language, lean casual: `Szia` not `Jó napot kívánok`; `Oké` not `Rendben van`. Online Hungarian is mostly `te`. Pure `Ön` in casual chat reads robotic and distant.

## Te vs Ön/Maga

Pronouns set the social distance:

- `Ön` / `Maga`: strangers, elderly addressees, professional or formal settings.
- `te`: friends, peers, internet, most casual workplaces.
- Hungarian internet uses `te`. Default casual drafts to `te`, not `Ön`.
- State the assumption when the choice changes the social effect.

## Conjugation

Hungarian verbs mark formality and object definiteness. Keep one system for the draft:

- Definite vs indefinite conjugation must match the object.
- `-lak` / `-lek` marks "I … you" forms; get these right when addressing `te`.
- Do not mix polite `Ön` morphology with casual peer slang in the same sentence.

## Particles, fillers, and flow

These make Hungarian natural in casual drafts:

- `Hát`: "well" filler (`Hát, nem tudom`)
- `Csak`: "just" (`Csak kérdeztem`)
- `Már`: emphasis or mild impatience
- `Ugye`: "right?" tag
- `Azért`: "still" / "though"

Casual flow can use `hát`, `szóval`, `na`, `tudod`, `érted`, `nézd`, `asszem`, `szerintem`, `mondjuk`, and `viszont`. Use a few, not a pile.

## Expressiveness and reactions

Prefer a specific casual word over a safe textbook word when the register is casual:

- `Jó` → `Szuper`, `Király`, `Zsír`, `Frankó`
- `Rossz` → `Gáz`, `Szar`, `Béna` (keep vulgar options out of formal and mixed-audience drafts)
- `Nagyon` → `Tök`, `Bazi`, `Irtó`

Natural expressions and reactions:

- `Király!`, `Zsír!`, `Szuper!`
- `Semmi gond`, `Nem para`
- `Komolyan?`, `Tényleg?`, `Nocsak`
- `Oké`, `Ja`, `Aha`
- `Hú!`, `Basszus!`, `Jesszus!`
- `Haha` / `lol` in text chat when the channel already uses them

## Word order and suffixes

Hungarian has flexible, topic-focus word order. Use position for natural emphasis without inventing facts. Hungarian is agglutinative: keep suffixes attached (`Házamban` stays one word). Do not split compounds or suffix chains into English-like fragments.

## Fidelity and boundaries

Natural wording does not add a promise, place, time, or certainty the source did not give. Marketing structure belongs to `copywriting` after register is chosen. English source polishing belongs to `english`. Spoken delivery cues belong to `speak`. Polish requests belong to `polish`.

For legal, medical, financial, or publication-sensitive Hungarian, keep the requested formality and recommend a qualified native-speaker review.

## Delivery check (Native Test)

Before sending:

- Register, pronouns, conjugations, particles, and fillers agree with each other and with the audience.
- Facts, names, numbers, and commitments come from the source.
- One voice runs through the draft; unspecified casual chat defaults to warm `te`.
- Ask: would a Hungarian screenshot this as "AI-generated"? If yes—too formal, no `hát`, too stiff—add natural particles such as `na` and `szóval` without stuffing.
