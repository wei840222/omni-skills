---
name: romanian
description: >
  Compose, translate, and revise natural Romanian for messages, posts, and
  everyday copy. Use when Romanian text needs a tu vs dumneavoastră choice,
  casual particles (hai, măi, păi), texting slang (cf, ms, mișto, nașpa), or a
  less formal translation; keep polite dumneavoastră for elderly or very formal
  recipients. Not for Moldovan politics, legal translation, Romania travel
  routing (`romania` / `bucharest`), or a full language course.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇷🇴","displayName":"Romanian"}'
  related-skills: '{"romania":"Plan Romania travel itineraries instead of composing Romanian text.","bucharest":"Navigate Bucharest neighborhoods and logistics rather than language drafting.","translate":"Move an existing source text into Romanian when translation workflow is the main need.","writing":"Shape broader prose once the Romanian-language decision is settled.","english":"Draft or revise the English source before translating it into Romanian.","spanish":"Write Spanish when Romanian is not the target language.","french":"Write French when Romanian is not the target language."}'
---

## When to load

Load this skill to write, rewrite, or translate Romanian that should sound like a person, not a textbook. Prefer `romania` / `bucharest` for travel and city logistics, and `translate` when the main ask is a translation workflow rather than register coaching. Load `references/sources.md` before repeating a register label, a pronoun mapping, or a slang gloss. Load `references/vocabulary.md` when the draft needs texting abbreviations or expressive slang.

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify the audience, relationship, channel, source text, and requested tone. If the request names no register, choose casual `tu` Romanian for peer chat and say so in one short note.
2. Pick one register and keep it for the whole draft. Match a sample the user already supplied when one exists.
3. Choose pronouns, particles, and slang that fit that register. Preserve names, numbers, dates, commitments, and how sure the source is.
4. Run the delivery check, then return the Romanian text first.

## Register

| Situation | Default | Delivery rule |
| --- | --- | --- |
| Elderly addressee, unfamiliar institution, or explicit formal request | Polite | Use `dumneavoastră`, fuller sentences, and little or no slang. |
| Work chat with known colleagues | Everyday professional | Stay clear and polite; add light particles only if that workplace already does. |
| Friend, peer chat, SMS, or social post | Casual `tu` | Use `tu`, particles (`hai`, `măi`, `păi`), and light slang. |
| Public or mixed audience | Neutral everyday | Stay readable; skip intimate slang and profanity. |
| Region named by the user (e.g. Moldova) | That region's voice | Keep one regional voice; do not invent political language labels. |

Romanian internet and peer chat are almost entirely `tu`. Pure textbook formality in a casual chat reads robotic. An explicit formal request stays formal.

## Tu vs dumneavoastră

Pronouns set the social distance:

- `tu`: friends, peers, most internet, casual workplaces.
- `dumneavoastră`: singular and plural polite you for elderly addressees or very formal professional settings.
- Other polite/regional forms such as `dumneata` / `matale` can sound confrontational or marked; do not introduce them unless the user asks.

If the speaker's preferred form is unknown, use `tu` for unspecified casual chat and `dumneavoastră` for formal notes. State the assumption when it changes the social effect.

## Particles, fillers, and flow

These make casual Romanian feel native. Use a few, not a pile:

- `Hai`: "come on" / "let's" (`Hai să mergem`)
- `Măi`: casual address (`Măi, ce faci?`)
- `Bre`: emphasis in casual talk
- `Păi`: "well" filler
- `Deci`: "so", transitional

Casual flow can also use `adică`, `uite`, `auzi`, `stai`, `știi`, `gen`, `parcă`, `mda`, and `mno`. Peer-chat reactions include `Serios?`, `Zici?`, `Nu mai spune!`, `Vai!`, `Ce tare!`, `Mișto!`, and `Grozav!`.

Prefer a specific casual word over a safe textbook word when the register is peer chat: `bine` → `super` / `grozav` / `tare` / `mișto`; `rău` → `nasol` / `groaznic`; `mult` → `foarte` / `mega`. In polite register, keep fuller forms and skip slang.

## Vocabulary and progressive disclosure

Refer to `references/vocabulary.md` for conversational abbreviations and expressive slang (`cf`, `ms`, `fain`, `nașpa`). Keep glosses aligned with `references/sources.md`; do not invent slang the sources do not support.

## Diminutives and regional flavor

Romanian uses diminutives for warmth (`-uț`, `-uță`, `-ică`: `puțin` → `puținel`). Add them when the relationship is close and the channel is informal.

Moldovan Romanian can differ in vocabulary and intonation. If the user names that region, stay consistent with one voice. Do not turn the draft into a language-politics debate; travel or city logistics belong to `romania` / `bucharest`.

## Delivery check

- Register, pronouns, particles, and slang agree with each other and with the audience.
- Facts, names, numbers, and commitments come from the source.
- One regional voice runs through the draft. Casual `tu` is the default only for unspecified peer chat.
- For legal, medical, financial, or publication-sensitive Romanian, keep the requested formality and recommend a qualified native-speaker review.

## Related boundaries

Romania travel routing belongs to `romania`. Bucharest neighborhood and commute depth belongs to `bucharest`. A Spanish or French request belongs to those language skills. Marketing structure belongs to `writing` / adjacent copy skills after the Romanian register is chosen. English source polishing belongs to `english`.

## The "Native Test"

Before outputting, ensure the text has native warmth, uses particles such as `hai` when the register is casual, and keeps conversational fluid.