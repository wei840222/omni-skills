---
name: danish
description: >
  Write casual, natural-sounding Danish with particles, fillers, egalitarian
  du-address, and expressive vocabulary. Use when drafting messages, translating
  conversational text, or polishing informal Danish; keep formal register only
  for official audiences. Prefer norwegian/swedish for those languages and
  denmark for travel logistics—not a full language course.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇩🇰","displayName":"Danish"}'
  related-skills: '{"norwegian":"Write Norwegian when Danish is not the target language.","swedish":"Write Swedish when Danish is not the target language.","translate":"Translate an existing source text into Danish.","writing":"Shape broader prose once the Danish-language decision is settled.","denmark":"Plan Denmark travel or local logistics rather than Danish-language phrasing.","english":"Draft or revise the English source before translating it into Danish.","copywriting":"Shape persuasive marketing copy after the Danish register is chosen."}'
---

Research notes for register, particles, and Scandinavian adjacency live in `references/sources.md`.

## When to load

Load this skill to write, rewrite, or translate **Danish** that should sound like a person, not a textbook. Prefer this skill over generic `translate` when particles, du-address, fillers, or Danish humor change the draft.

Do **not** load as the primary skill for Norwegian (`norwegian`), Swedish (`swedish`), or Denmark travel logistics (`denmark`).

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify audience, relationship, channel, source text, and requested tone. If no register is named, choose casual egalitarian Danish and say so in one short note when the choice matters.
2. Pick one register and keep it for the whole draft. Match a sample the user already supplied when one exists.
3. Choose pronouns, particles, fillers, and expressive vocabulary that fit that register. Preserve names, numbers, dates, commitments, and how sure the source is.
4. Run the delivery check, then return the Danish text first.

## Formality default

Default AI register is too high. Everyday Danish is informal and egalitarian. Unless the user explicitly wants formal or official copy:

- Prefer `Hej` over `Goddag`
- Prefer plain `Ok` / short replies over stiff full sentences
- Prefer particles and understatement over textbook completeness

## Du is universal

Denmark uses **du** almost everywhere:

- `du`: default for strangers, colleagues, bosses, and elders in ordinary writing
- `De` (formal you): rare, old-fashioned, or ironic outside highly ceremonial contexts
- Do not upgrade to `De` unless the user explicitly requests formal address

## Particles and softeners

These markers make Danish sound native. Add one when it matches the voice—do not stack many:

| Particle | Effect | Example |
| --- | --- | --- |
| `jo` | shared knowledge | `Det ved du jo` |
| `vel` | soft uncertainty | `Du kommer vel?` |
| `da` | emphasis / nudge | `Kom så da!` |
| `nok` | "probably" / soft prediction | `Det går nok` |
| `altså` | "so" / "I mean" | `Altså, det er fint` |

## Fillers and flow

Casual Danish uses light fillers. Keep a few, not a pile:

- `altså`, `ligesom`, `sådan`
- `øh`, `hmm`
- `bare`, `egentlig`, `faktisk`
- `i hvert fald`, `forresten`

## Sentence fragments

Danes are concise in chat:

- `Kommer du?` → `Ja` / `Nej`
- `Hvad så?` → `Ikke så meget`
- Short answers are natural; over-complete replies read stiff

## Expressiveness

Choose expressive vocabulary when the register is informal:

- God → `Fedt`, `Skønt`, `Vildt godt`
- Dårlig → `Nederen`, `Lortet`, `Pisse dårlig`
- Meget → `Mega`, `Sygt`, `Pisse-`

Keep intensity out of formal and mixed-audience drafts unless the user asks for it.

## Humor and reactions

Danish casual voice often uses dry understatement and light irony:

- `Det er da fint` can be sincere **or** sarcastic—match context
- Prefer understatement over forced enthusiasm in peer chat
- Natural reactions: `Seriøst?`, `Virkelig?`, `Hvad?`, `Hold da op!`, `Ej!`, `Fedt!`, `Vildt!`
- Light English mixing is common and should stay seamless: `Det var mega awkward`, `Super nice`

## Delivery check

- Register, pronouns (`du` vs rare `De`), particles, and intensity agree with the audience
- Facts, names, numbers, and commitments come from the source—do not invent place, time, or promises
- One voice runs through the draft; casual default is egalitarian `du` with light particles
- Before send: would a Dane screenshot this as "AI-generated"? If yes—too formal, too complete, missing particles—loosen register and shorten
