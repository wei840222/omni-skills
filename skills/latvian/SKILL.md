---
name: latvian
description: >
  Compose, translate, and revise natural Latvian for messages, posts, and
  everyday copy. Use when Latvian needs a clear tu/jūs choice, casual particles,
  or less formal wording; keep formal register for professional, institutional,
  older, or unfamiliar recipients. Prefer lithuanian/russian/polish for those
  languages and translate for multi-pair localization—not a full language course.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇱🇻"}'
  related-skills: '{"lithuanian":"Write Lithuanian when Latvian is not the target language.","russian":"Write Russian when Latvian is not the target language.","polish":"Write Polish when Latvian is not the target language.","translate":"Translate an existing source text into Latvian across formats and locales.","writing":"Shape broader prose once the Latvian-language decision is settled.","english":"Draft or revise the English source before translating it into Latvian.","copywriting":"Shape persuasive marketing copy after the Latvian register is chosen."}'
---

Research notes for tu/jūs, particles, and official resources live in `references/sources.md` (progressive disclosure).

Expanded particle tables, expressiveness, and delivery checks live in `references/style-guide.md` (progressive disclosure).

## When to load

Load this skill to write, rewrite, or translate **Latvian** that should sound like a person, not a textbook. Prefer this skill over generic `translate` when tu/jūs choice, particles (`nu`, `jau`, `vai`, `gan`), fillers, or casual Latvian tone change the draft.

Do **not** load as the primary skill for Lithuanian (`lithuanian`), Russian (`russian`), or Polish (`polish`).

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify audience, relationship, channel, source text, and requested tone. When those details are missing, write neutral-standard Latvian and state the register assumption in one short note when the choice matters.
2. Choose one address form and keep it for the whole draft: `tu` for a known peer or clearly casual context; `jūs` for professional, institutional, older, unfamiliar, or explicitly formal recipients.
3. Draft for the selected register. Preserve names, numbers, dates, commitments, and how sure the source is. For casual text, use direct phrasing and add at most a few particles or fillers that fit the speaker and channel.
4. Read `references/style-guide.md` for human-facing Latvian drafts, rewrites, and reviews; use its register, particles, expressiveness, and authoritative-resource guidance.
5. Run the delivery check, then return the Latvian text first.

## Formality default

Default AI register is too high. Everyday Latvian is warm and direct. Unless the user explicitly wants formal or official copy:

- Prefer `Čau` / `Sveiks` / `Sveika` over bare `Labdien` in peer chat
- Prefer short replies such as `Jā`, `Labi`, `Okei`, `Sapratu`
- Prefer light particles and natural intensity over stiff full sentences

## Tu vs jūs

Critical address distinction:

| Form | Use when |
| --- | --- |
| `tu` | friends, peers, internet, clearly casual chat |
| `jūs` | professional, institutional, older, unfamiliar, or explicitly formal recipients |

Keep greeting, verbs, pronouns, and closing in the same register. Latvian internet writing usually defaults to `tu`; overusing `jūs` with peers sounds stiff and distant.

## Particles and softeners

These markers make casual Latvian sound native. Add one when it matches the voice—do not stack many:

| Particle | Effect | Example |
| --- | --- | --- |
| `nu` | filler / soft lead-in ("well") | `Nu, labi.` |
| `jau` | "already" / mild emphasis | `Es jau zinu.` |
| `tak` | emphasis / insistence | `Dari tak.` |
| `vai` | question particle | `Vai tu nāksi?` |
| `gan` | "quite" / soft emphasis | `Gan jau izdosies.` |

## Fillers and flow

Casual Latvian uses light fillers. Keep a few, not a pile:

- `nu`, `tā`, `labi`
- `tipa`, `kā`
- `zini`, `klau`
- `vispār`, `starp citu`

## Expressiveness

Choose expressive vocabulary when the register is informal:

- Labi → `Super`, `Forši`, `Lieliski`
- Slikti → `Šausmīgi`, `Briesmīgi`
- Ļoti → `Mega`, `Baigi`, `Pilnīgi`

Natural reactions and set phrases: `Tiešām?`, `Nopietni?`, `Nu nē!`, `Oho!`, `Vau!`, `Nav problēmu`, `Mierīgi`, `Forši!`.

Keep intensity out of formal and mixed-audience drafts unless the user asks for it.

## Fidelity and boundaries

Natural wording does not add a promise, place, time, or certainty the source did not give. Marketing structure belongs to `copywriting` after register is chosen. English source polishing belongs to `english`. Lithuanian, Russian, or Polish targets belong to those skills. Multi-format localization catalogs belong to `translate`.

For legal, medical, financial, or publication-sensitive Latvian, keep the requested formality and recommend a qualified native-speaker review. Prefer current entries in Tēzaurs or Latviešu valodas aģentūra guidance when orthography or terminology is contested.

## Delivery check (Native Test)

Before sending:

- Register, `tu`/`jūs`, particles, fillers, and intensity agree with the audience
- Facts, names, numbers, and commitments come from the source
- One voice runs through the draft; casual default is warm `tu` with light particles
- Ask: would a Latvian screenshot this as "AI-generated"? If yes—too formal, missing `nu`/`jau`, too stiff—shorten, warm the register, and add at most one natural particle without stuffing
