---
name: arabic
description: >
  Write natural, human-sounding Arabic that blends dialect (عامية) and MSA
  (فصحى) appropriately, locks one regional variety when known, and avoids
  robotic pure-MSA tone unless the user asks for formal writing. Use when
  drafting, replying to, or reviewing casual Arabic messages, social posts,
  or chat in Arabic script or Arabizi. Not for pure translation pipelines
  (`translate`) or non-Arabic languages.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇸🇦"}'
  related-skills: '{"urdu":"Shares Perso-Arabic script contact and some vocabulary flavor.","persian":"Shares script and historical vocabulary contact with Arabic.","english":"Used alongside Arabic in bilingual or Arabizi contexts.","translate":"Translate an existing source text into Arabic.","writing":"Shape broader prose once the Arabic-language decision is settled.","french":"Write French when Arabic is not the target language."}'
---

This skill is stateless and does not store local configuration or persistent user state.

## When to Use

Help the user draft or review **Arabic that would pass a native ear**: correct MSA vs dialect register, one locked regional variety when the region is known, natural fillers and reactions, Arabizi vs Arabic-script choice, and expressive (not safe-textbook) wording.

## Quick Reference

| Resource | When to load |
|---|---|
| `references/guide.md` | Load for MSA vs dialect, regional varieties, greetings, fillers, reactions, Arabizi, and politeness particles. |
| `references/sources.md` | Load for Gate 6 source-backed register, dialect, and script facts. |
| `references/output-gates.md` | Load as final checks before sending casual Arabic text. |

## The Real Problem

AI Arabic is often technically correct but sounds off: too formal, too pure فصحى, missing يعني and other discourse glue. Natives blend registers and use colloquial naturally. Match that.

## Defaults

1. Prefer dialect or light MSA for casual chat, social, and SMS unless the user asks for formal/news/academic/religious register.
2. If the region is known (Egyptian, Levantine, Gulf, Moroccan, …), lock that variety and do not mix dialect vocabulary in one reply.
3. If the region is unknown and the choice materially changes wording, ask once; otherwise use a light pan-dialect / MSA mix that stays casual.
4. Keep script consistent: full Arabic script by default; Arabizi only when the channel or user clearly wants Latin chat spellings.
5. Before sending, run the native test in `references/output-gates.md`.

## Workflow

1. Detect target register (casual vs formal) and region from the request; ask once only when region changes wording and is missing.
2. Load `references/guide.md` for dialect markers, fillers, reactions, and script choice; load `references/sources.md` when a domain fact must be justified.
3. Draft in the locked variety; prefer short turns, natural fragments, and one warm particle over complete textbook sentences.
4. Run `references/output-gates.md` (register, dialect lock, fillers, script, native screenshot test, scope).
5. If the native test fails, rewrite once toward warmer عامية — do not add more MSA gloss.

## The "Native Test"

Before sending: would an Arab screenshot this as "AI-generated"? If yes — too MSA, no fillers, too complete/formal — lower the register and add عامية flavor.
