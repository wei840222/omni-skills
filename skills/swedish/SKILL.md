---
name: swedish
description: >
  Compose, translate, and revise natural Swedish for messages, posts, and
  everyday copy. Use when Swedish text needs casual register, du-address,
  particles, fillers, lagom understatement, or a less formal translation; keep
  formal register only for official or unfamiliar recipients. Prefer
  norwegian/danish for those languages and sweden for travel logistics—not a
  full language course.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇸🇪"}'
  related-skills: '{"norwegian":"Write Norwegian when Swedish is not the target language.","danish":"Write Danish when Swedish is not the target language.","translate":"Translate an existing source text into Swedish.","writing":"Shape broader prose once the Swedish-language decision is settled.","sweden":"Plan Sweden travel or local logistics rather than Swedish-language phrasing.","english":"Draft or revise the English source before translating it into Swedish.","copywriting":"Shape persuasive marketing copy after the Swedish register is chosen.","finnish":"Handle Finnish requests that share Nordic context but not Swedish particles or lagom tone."}'
---

Research notes for du-reform, particles, lagom tone, and Scandinavian adjacency live in `references/sources.md`.

Expanded particle tables and lagom examples live in `references/conversational-rules.md` (progressive disclosure).

## When to load

Load this skill to write, rewrite, or translate **Swedish** that should sound like a person, not a textbook. Prefer this skill over generic `translate` when particles, du-address, fillers, lagom understatement, or casual Swedish tone change the draft.

Do **not** load as the primary skill for Norwegian (`norwegian`), Danish (`danish`), Finnish (`finnish`), or Sweden travel logistics (`sweden`).

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify audience, relationship, channel, source text, and requested tone. If no register is named, choose casual egalitarian Swedish and say so in one short note when the choice matters.
2. Pick one register and keep it for the whole draft. Match a sample the user already supplied when one exists.
3. Choose pronouns, particles, fillers, and expressive vocabulary that fit that register. Preserve names, numbers, dates, commitments, and how sure the source is.
4. Run the delivery check, then return the Swedish text first.

## Formality default

Default AI register is too high. Everyday Swedish is informal. Unless the user explicitly wants formal or official copy:

- Prefer `Hej` / `Tja` over `God dag`
- Prefer `Okej` and short replies over stiff full sentences
- Prefer particles and lagom understatement over textbook completeness

## Du-reform

Modern Swedish almost always uses **du**:

- `du`: default for strangers, colleagues, and ordinary writing
- `ni`: rare as polite singular; can sound sarcastic, ceremonial, or old-fashioned
- Keep *du* unless the user explicitly requests formal address; only then consider marked polite `ni`

## Particles and softeners

These markers make Swedish sound native. Add one when it matches the voice—do not stack many:

| Particle | Effect | Example |
| --- | --- | --- |
| `ju` | shared knowledge | `Det vet du ju` |
| `väl` | soft uncertainty / hope | `Du kommer väl?` |
| `nog` | "probably" / soft prediction | `Det går nog bra` |
| `då` | emphasis / nudge | `Gör det då` |
| `visst` | confirmation seeking | `Det var visst bra?` |

## Fillers and flow

Casual Swedish uses light fillers. Keep a few, not a pile:

- `typ`, `liksom`, `alltså` / `asså`
- `eh`, `öh`, `mm`
- `ja` / `nej` as soft fillers, not only yes/no
- `i alla fall`, `hur som helst`

## Sentence fragments

Swedes are concise in chat:

- `Kommer du?` → `Aa` / `Nej`
- `Läget?` → `Bra`
- Short answers are natural; over-complete replies read stiff

## Expressiveness

Choose expressive vocabulary when the register is informal:

- Bra → `Grymt`, `Fett`, `Najs`, `Asbra`
- Dåligt → `Kasst`, `Skit`, `Drygt`
- Mycket → `Jätte-`, `As-`, `Mega-`

Keep intensity out of formal and mixed-audience drafts unless the user asks for it.

## Lagom and reactions

Swedish understatement is cultural. Calibrate enthusiasm downward rather than upward:

- `Inte så dumt` often means actually good
- `Helt okej` often means pretty good
- Natural reactions: `Vad?`, `Seriöst?`, `Oj!`, `Herregud!`, `Skönt!`, `Najs!`
- Light English mixing is common and should stay seamless: `Det var så awkward`, `Super nice`

Natural expressions: `Lugnt`, `Ingen fara`, `Inga problem`, `Vad schysst!`, `Kul!`, `Orka` (can't be bothered).

## Fidelity and boundaries

Natural wording does not add a promise, place, time, or certainty the source did not give. Marketing structure belongs to `copywriting` after register is chosen. English source polishing belongs to `english`. Norwegian or Danish targets belong to those skills. Sweden logistics belong to `sweden`.

For legal, medical, financial, or publication-sensitive Swedish, keep the requested formality and recommend a qualified native-speaker review.

## Delivery check (Native Test)

Before sending:

- Register, pronouns (`du` vs rare polite `ni`), particles, lagom intensity, and fillers agree with the audience
- Facts, names, numbers, and commitments come from the source
- One voice runs through the draft; casual default is egalitarian `du` with light particles
- Ask: would a Swede screenshot this as "AI-generated"? If yes—too formal, missing particles, too enthusiastic—tone down, shorten, and add a natural particle such as `typ` without stuffing
