---
name: estonian
description: >
  Compose, translate, and revise natural Estonian for messages, posts, and
  everyday copy. Use when Estonian text needs sina/Teie, understatement,
  particles (noh, ju, küll), fillers, or a less formal translation; keep Teie
  and standard register for official or unfamiliar recipients. Prefer
  finnish/swedish for those languages and translate for multi-locale jobs—not
  a full language course.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇪🇪"}'
  related-skills: '{"finnish":"Write Finnish when Estonian is not the target language.","swedish":"Write Swedish when Estonian is not the target language.","translate":"Translate an existing source text into Estonian across a broader localization job.","writing":"Shape broader prose once the Estonian-language decision is settled.","english":"Draft or revise the English source before translating it into Estonian.","copywriting":"Shape persuasive marketing copy after the Estonian register is chosen."}'
---

Research notes for sina/Teie, particles, and understatement live in `references/sources.md`.

Expanded particle tables, expressiveness swaps, and reaction templates live in `references/estonian-style-guide.md` (progressive disclosure).

## When to load

Load this skill to write, rewrite, or translate **Estonian** that should sound like a person, not a textbook. Prefer this skill over generic `translate` when sina/Teie, understatement, particles, fillers, or casual Estonian tone change the draft.

Do **not** load as the primary skill for Finnish (`finnish`), Swedish (`swedish`), or a multi-file localization pipeline that only needs generic MT post-editing (`translate`).

This skill is stateless. It does not store local configuration or persistent user state.

## Workflow

1. Identify audience, relationship, channel, source text, and requested tone. If no register is named, choose casual sina-address Estonian and say so in one short note when the choice matters.
2. Pick one register and keep it for the whole draft. Match a sample the user already supplied when one exists.
3. Choose pronouns, particles, fillers, and expressive vocabulary that fit that register. Preserve names, numbers, dates, commitments, and how sure the source is.
4. Run the delivery check, then return the Estonian text first.

## Formality default

Default AI register is too high. Everyday Estonian is understated and direct. Unless the user explicitly wants formal or official copy:

- Prefer `Tere` / `Hei` over `Tere päevast`
- Prefer `Jah` / `Jep` / `Okei` over stiff full affirmations
- Prefer particles and understatement over literary completeness

## Sina vs Teie

Critical social distance:

- `Teie`: elderly addressees, unfamiliar institutions, marked professional distance
- `sina`: friends, peers, most internet, casual workplaces
- Estonian internet is overwhelmingly `sina`
- Overusing `Teie` online reads stiff and foreign

Keep `sina` unless the user explicitly requests formal address or the audience is clearly institutional.

## Particles, fillers, and flow

These markers make Estonian sound native. Add one when it matches the voice—do not stack many:

| Particle / filler | Effect | Example |
| --- | --- | --- |
| `ju` | shared knowledge | `Sa ju tead` |
| `küll` | reassurance | `Küll saab` |
| `ikka` | still / emphasis | `Ikka tuleb` |
| `noh` | soft filler / "well" | `Noh, vaatame` |
| `vist` | "probably" | `Vist tuleb` |
| `nagu` | hedge / softener | `nagu okei` |

Casual flow can also use `siis`, `tead`, `kuule`, `tegelikult`, `muide`, `nii-öelda`, and `onju`. Use a few, not a pile.

## Understatement and expressiveness

Estonian culture is reserved. Calibrate enthusiasm downward rather than upward:

- High praise often sounds like `päris hea`, not `suurepärane`
- Prefer `Lahe` / `Äge` / `Kõva` over exaggerated cheer
- Soften negatives with `Kehv` / `Jama` rather than theatrical outrage unless asked

Natural reactions: `Tõesti?`, `Päriselt?`, `Ei või olla!`, `Oih!`, `Vau!`, `Jumal!`, `Äge!`, `Lahe!`. Light English mixing such as `Nice!` or `lol` can stay when it matches the channel.

## Fidelity and boundaries

Natural wording does not add a promise, place, time, or certainty the source did not give. Marketing structure belongs to `copywriting` after register is chosen. English source polishing belongs to `english`. Finnish or Swedish targets belong to those skills. Broader localization catalogs belong to `translate`.

For legal, medical, financial, or publication-sensitive Estonian, keep the requested formality and recommend a qualified native-speaker review.

## Delivery check (Native Test)

Before sending:

- Register, pronouns (`sina` vs `Teie`), particles, understatement, and fillers agree with the audience
- Facts, names, numbers, and commitments come from the source
- One voice runs through the draft; casual default is `sina` with light particles
- Ask: would an Estonian screenshot this as "AI-generated"? If yes—too formal, too enthusiastic, or too stiff—tone down, shorten, and add a natural particle such as `noh` without stuffing
