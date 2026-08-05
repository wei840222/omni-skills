---
name: galician
description: Write natural, human-sounding Galician (galego) that avoids AI-sounding formality. Use when the user asks to write, translate, edit, or review text in Galician, mentions Galician language or galego, or references Galicia in a linguistic context.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌐"}'
---

## The Real Problem

AI Galician is technically correct but sounds off. Too formal. Too literary. Natives write more casually, with warmth. Match that.

## Dialectal Awareness

Galician has regional variation (eastern, western, central dialects). Unless the user specifies a dialect or region:
- Default to standard normative Galician (RAG norm)
- Keep vocabulary and pronunciation consistent
- If the user writes in a specific dialect, match it

## Formality Default

Default register is too high. Casual Galician is warm and melodic. Unless explicitly formal: lean casual. "Ola" not "Bo día". "Si" not "Si, por suposto".

## Ti vs Vostede

Distinction:
- Vostede: formal, elderly, respect
- Ti: friends, peers, casual
- Galician casual uses ti widely
- Vostede in formal contexts only

## Galician vs Spanish vs Portuguese

Galician is distinct:
- Not Spanish, not Portuguese
- Own vocabulary and patterns
- "Grazas" not "Gracias"
- Don't mix with Spanish

**Code-switching reality**: Galicians often mix Galician and Spanish in casual speech. In formal writing, keep it pure Galician. In casual contexts, light mixing is natural but lean toward Galician vocabulary.

## Grammar Traps

Common AI mistakes:
- **Gender agreement**: Ensure adjectives match noun gender (o home alto / a muller alta)
- **Number agreement**: Plurals must agree (os homes altos / as mulleres altas)
- **False friends**: Avoid Spanish cognates (use "rapaz" not "chico", "rapaza" not "chica")
- **Verb conjugation**: Check irregular verbs (ser, ir, ter, haber)

## Particles & Softeners

These make Galician natural:
- Pois: "well", "so"
- Non si: tag question
- Home/Muller: casual address
- Logo: "then"

## Fillers & Flow

Real Galician has fillers:
- Pois, logo, ben
- Sabes, entendes
- Ou sexa, vamos
- Mira, escoita

## Expressiveness

Don't pick the safe word:
- Ben → Xenial, Estupendo, Dabuti
- Mal → Fatal, Moi mal
- Moito → Abondo, Unha chea

## Common Expressions

Natural expressions:
- Vale, Ben, Dabondo
- Non pasa nada, Tranquilo
- De verdade?, En serio?, Que?
- Xenial!, Estupendo!, Moi ben!

## Reactions

React naturally:
- De verdade?, En serio?, Que dis?
- Carai!, Carallo!, Miña nai!
- Xenial!, Dabuti!, Moi ben!
- Jajaja in text

## Reintegrationism

Some use Portuguese-aligned spelling:
- Reintegrationist vs normative
- Most use normative (RAG standard)
- Stay consistent

## Anti-Patterns: What to Avoid

| ❌ Wrong | ✅ Right | Why |
|---|---|---|
| "Bo día, como está vostede?" (casual context) | "Ola, que tal?" | Default to casual unless told otherwise |
| "Gracias" | "Grazas" | Galician, not Spanish |
| "chico/chica" | "rapaz/rapaza" | Galician vocabulary |
| "Estupendo, moi ben, si" (all safe words) | "Xenial! Dabuti!" | Use expressive vocabulary |
| Mixing Spanish syntax with Galician words | Pure Galician sentence structure | Galician has its own syntax patterns |
| Overly literary tone in casual chat | Warm, melodic casual register | Match native speech patterns |

## Pre-Output Validation

Before delivering Galician text, run through this checklist:

1. **Register check**: Is the formality level appropriate for the context? (Default: casual)
2. **Vocabulary check**: Any Spanish words that should be Galician? (gracias→grazas, chico→rapaz)
3. **Agreement check**: Do adjectives match noun gender and number?
4. **Naturalness check**: Does it sound like something a native would actually say, or does it read like a textbook?
5. **Consistency check**: Is the dialect/normative standard consistent throughout?

If any check fails, revise before outputting.

## The "Native Test"

Before sending: would a Galician speaker screenshot this as "AI-generated"? If yes—too formal, sounds Spanish, too literary. Add Galician warmth.
