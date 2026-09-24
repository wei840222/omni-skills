---
name: finnish
description: >
  Compose, translate, and revise natural Finnish for messages, posts, and
  everyday copy. Use when Finnish text needs a register choice, puhekieli
  shortcuts, pronouns, particles, or a less formal translation; keep
  kirjakieli for official, academic, or professional recipients. Not for
  Estonian, legal translation, or a full language course.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇫🇮"}'
  related-skills: '{"copywriting":"Shape persuasive marketing copy after the Finnish register is chosen.","english":"Draft or revise the English source before translating it into Finnish.","norwegian":"Apply the same register-first writing method to Norwegian instead of Finnish.","swedish":"Handle Swedish requests that share Nordic context but not Finnish pronouns or compounds.","writing":"Plan structure and argument before polishing the Finnish wording."}'
---

## When to load

Load this skill to write, rewrite, or translate Finnish that should sound like a person, not a textbook. Load `references/sources.md` before repeating a register label, a pronoun mapping, or a particle gloss.

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify the audience, relationship, channel, source text, and requested tone. If the request names no register, choose Helsinki-leaning puhekieli and say so in one short note.
2. Pick one register and keep it for the whole draft. Match a sample the user already supplied when one exists.
3. Choose pronouns, spoken shortcuts, and particles that fit that register. Preserve names, numbers, dates, commitments, and how sure the source is.
4. Run the delivery check, then return the Finnish text first.

## Register

| Situation | Default | Delivery rule |
| --- | --- | --- |
| Official, academic, news, or unfamiliar institution | Kirjakieli | Use full forms (`minä`, `sinä` or a title, `hän`), standard spelling, and no spoken shortcuts. |
| Work chat with known colleagues | Everyday professional | Stay clear and polite; add light particles only if that workplace already does. |
| Friend, peer chat, or social post to people who already talk that way | Puhekieli | Use `mä` / `sä`, spoken shortcuts, and a few particles. |
| Public or mixed audience | Neutral everyday | Stay readable; skip intimate slang and profanity. |
| Dialect named by the user | That dialect's voice | Keep one dialect system for the whole draft. |

Online chat is mostly puhekieli. Pure kirjakieli in a casual chat reads robotic. An explicit formal request stays formal. Do not treat one urban puhekieli as every Finnish dialect.

## Pronouns

Pronouns set the social distance. Helsinki-area casual forms are the default only when no dialect is named:

- `minä` → `mä` (also `mää`, `mie`, `miä` by dialect). Possessive stem `minun` → `mun`.
- `sinä` → `sä` (also `sää`). Possessive stem `sinun` → `sun`.
- `hän` (he / she) → `se` in most spoken Finnish outside Southwestern Finland. `se` here is not an insult.
- `he` (they) → `ne` in the same spoken register.
- `te` as formal you is rare: elderly addressees or a very formal setting. Default to `sinä` / `sä`, not `te`.

If the speaker's preferred form is unknown, use `mä` / `sä` for an unspecified casual draft, or `minä` / `sinä` for kirjakieli. State the assumption when it changes the social effect.

## Shortcuts, particles, and flow

Use spoken shortcuts in puhekieli, not in kirjakieli:

- `minä` / `sinä` → `mä` / `sä`
- `olet` → `oot`; `olen` → `oon`
- `eikö` → `eiks`
- `minulla on` → `mulla on`

Particles and clitics shape tone. Add one when it matches the voice:

- `-han` / `-hän`: shared knowledge or emphasis (`sehä on`)
- `-pa` / `-pä`: softens or nudges (`katopa`)
- `-ko` / `-kö`: makes a question (`tuutko`)
- `ni` / `nii`: filler or agreement

Casual flow can use `nii`, `niinku`, `sillee`, `tota`, `siis`, `no`, `joo`, and `niin`. Use a few, not a pile. Peer-chat reactions include `Oikeesti?`, `Mitä?`, `Eikä!`, `Jes!`, `Siistii!`, and `Aivan!`. `hitto`, `paska`, and `helvetisti` are casual intensity; keep them out of formal and mixed-audience drafts.

Prefer a specific casual word over a safe textbook word when the register is puhekieli: `hyvä` → `mahtava` / `siistii`; `paljon` → `tosi` / `ihan`. In kirjakieli, keep `hyvä`, `paljon`, and full verb forms.

## Compounds and fidelity

Keep Finnish compound words intact. Do not split a compound into separate English-like words, and do not invent an extreme compound to sound native. Natural wording does not add a promise, a place, or a time that the source did not give.

## Delivery check

- Register, pronouns, shortcuts, and particles agree with each other and with the audience.
- Facts, names, numbers, and commitments come from the source.
- One dialect voice runs through the draft. Helsinki-leaning `mä` / `sä` is the default only for unspecified casual chat.
- For legal, medical, financial, or publication-sensitive Finnish, keep the requested formality and recommend a qualified native-speaker review.

## Related boundaries

Swedish and Norwegian are separate skills. A Swedish request belongs to `swedish`. Marketing structure belongs to `copywriting` after the register is chosen. English source polishing belongs to `english`.
