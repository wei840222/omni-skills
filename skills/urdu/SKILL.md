---
name: urdu
description: Write natural, expressive Urdu that prefers تم over آپ by default, uses native particles/fillers, and avoids stiff ادبی register. Use when drafting, replying to, or reviewing casual Urdu text (Nastaliq or Roman). Not for Pakistan trip logistics or formal legal drafting.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇵🇰"}'
  related-skills: '{"arabic":"Shares script similarities and some vocabulary.","english":"Used alongside Urdu in online/romanized contexts.","hindi":"Shares spoken similarities with Urdu but uses a different script.","persian":"Shares script and vocabulary with Urdu.","translate":"General translation skill that this skill refines for Urdu."}'
---

This skill is stateless and does not store local configuration or persistent user state.

## When to Use

Help the user draft or review **casual Urdu** that would pass a native speaker's ear: correct register (`تم`/`آپ`/`تو`), Nastaliq vs Roman script choice, particles, fillers, expressive wording, and Urdu–Hindi script/vocabulary boundaries.

## Quick Reference

| Resource | When to load |
|---|---|
| `references/formality-and-pronouns.md` | Load for `آپ` / `تم` / `تو` register choice and consistency. |
| `references/script-and-language.md` | Load for Nastaliq vs Hindi script boundaries and Persian/Arabic vocabulary flavor. |
| `references/flow-and-particles.md` | Load for particles, softeners, fillers, and conversational flow. |
| `references/expressions-and-reactions.md` | Load for expressive upgrades and natural reactions. |
| `references/romanized-urdu.md` | Load when the user wants SMS / social / Roman Urdu. |
| `references/domain-knowledge.md` | Load for source-backed register, script, and bilingual-contact facts. |
| `references/output-gates.md` | Load as final checks before sending casual Urdu text. |

## The "Native Test"

Before sending: would an Urdu speaker screenshot this as "AI-generated"? If yes, lower the register, add casual warmth/particles, and avoid stiff ادبی textbook phrasing.
