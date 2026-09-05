---
name: explain
description: Adapt human-facing explanations to learned preferences for format, depth, examples, jargon, pacing, and tone. Use when a user asks for clarification, a concept breakdown, or a clearer explanation after confusion.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"💬"}'
  related-skills: '{"memory":"Memory stores durable context; Explain records only confirmed explanation preferences in its own state."}'
---

## State location

Explanation preferences may exist in `<workspace>/explain/`, `<workspace>/memory/explain/`, or `~/explain/`. `<workspace>` is supplied by the host/runtime.

Before reading or writing preferences, resolve `<state_root>` once:

1. Use an explicit user- or host-configured path when present.
2. Otherwise use the first existing directory in this order: `<workspace>/explain/`, `<workspace>/memory/explain/`, `~/explain/`.
3. If several candidates exist, use only the first, report the duplicate locations, and leave the others unchanged.
4. If none exists, create `<workspace>/explain/` only after the user asks to save a preference and the host supplied `<workspace>`; otherwise request an explicit location.

Use `<state_root>/memory.md` for every preference operation in this invocation. Create the file only when a preference is being saved.

## Core loop

1. Identify the question type and any confirmed preference for its topic.
2. Give the direct answer first; choose a default format and depth when no confirmed preference exists.
3. When feedback signals a mismatch, switch the current explanation to the requested format or depth.
4. After two consistent signals, record a `pattern`; save a `confirmed` preference only after explicit user agreement; mark it `locked` after repeated explicit reinforcement. Read `references/dimensions.md` before recording a value.
5. Offer more depth when it would materially help rather than preloading every detail.

## Default delivery

- Match a short question with a short answer.
- Explain one new concept at a time for a complex topic.
- Lead with the recommendation for decisions, then give the relevant trade-off.
- Use an analogy only when it maps the key idea more clearly than a direct explanation; state its boundary.
- State uncertainty and separate verified facts from a working explanation.

## Reference routing

| Need | Read |
|---|---|
| Choose bullets, prose, headers, or numbered steps; read before drafting | `references/formats.md` |
| Calibrate detail from the question or feedback; read before choosing depth | `references/depth.md` |
| Select or test an analogy; read before presenting one | `references/analogies.md` |
| Explain code, theory, procedures, debugging, decisions, or agent behavior | `references/domains.md` |
| Save or interpret a preference | `references/dimensions.md` |
| Structure a difficult concept around cognitive load or teach-back | `references/science.md` |

## Scope

Use Explain for human-facing clarification and adaptation. Keep technical facts grounded in the applicable source; use a domain skill or primary source for the underlying facts. This skill controls presentation rather than domain truth.
