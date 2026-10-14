---
name: question
description: >
  Craft better questions with Socratic moves, SPIN discovery, funneling,
  bias/leading detection, and context-aware follow-ups. Use when drafting
  interview or research questions, running sales discovery, coaching 1:1s,
  journalism probes, learning through questioning, rewriting leading or
  compound questions, or when the user asks for SPIN, Socratic, open-ended,
  or neutral phrasing. Not for full coaching arcs (`coach`), decision logging
  (`decide`), bulk idea generation (`brainstorm`), or multi-option scoring
  (`compare`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"❓"}'
  related-skills: '{"coach":"Full coaching session arcs, commitments, and accountability beyond question craft.","decide":"Log consequential choices after questioning surfaces the decision.","brainstorm":"Generate option volume when the need is ideas, not interview or discovery questions.","collaborate":"Bounded critique exchanges once a position exists to challenge.","compare":"Weighted multi-option scoring after criteria are clear.","empathy":"One-shot reflective support without structured questioning.","ux-researcher":"Broader UX research programs when questioning is only one method.","market-research":"Market and demand research beyond interview question design.","writing":"Prose craft for non-question deliverables."}'
---

# Question

Improve **question craft**: open/neutral phrasing, framework selection, follow-ups,
and anti-bias checks across research, sales, coaching, journalism, and learning.

## State location

Optional session notes may exist in `<workspace>/question/`,
`<workspace>/memory/question/`, or `~/question/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/question/`, `<workspace>/memory/question/`, `~/question/`.
3. If multiple candidates exist, use only the highest-precedence directory,
   report the split, and leave lower-precedence directories unchanged.
4. If none exists and the user wants persistent session notes, create
   `<workspace>/question/`. If `<workspace>` is unavailable, ask for a state
   root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation. Prefer portable
`<state_root>` paths; keep host-specific absolute roots out of the skill text.
Skill resources stay under `references/`; treat the token `<state_root>` as a
placeholder, not a literal filesystem path.

Create or update state only after the user opts in. Store context labels,
topics, and assumptions only—no third-party secrets or credentials.

Defaults and the JSON shape live in `references/state.md`.

## When to use

- Draft or rewrite interview, discovery, coaching, journalism, or learning questions
- Detect leading, compound, closed-too-early, or solution-fishing phrasing
- Choose a framework: Socratic, SPIN, funnel, 5 Whys, ladder, scaling, pre-mortem
- Generate one next follow-up from the last answer (not a five-question dump)
- Route away when the job is a full coaching arc, decision log, idea dump, or scored comparison

## Core path

1. Name the **context**: research | sales | coaching | journalism | learning
   (`references/contexts.md`).
2. Load the matching techniques (`references/techniques.md`) and quality checklist
   (`references/domain.md`).
3. Scan the draft against anti-patterns (`references/anti-patterns.md`); rewrite
   leading or compound wording before adding volume.
4. Deliver **one primary question** (or a short ordered sequence with a clear stop),
   plus at most one follow-up trigger based on likely answers.
5. If the user opted into session state, update `<state_root>` with context, topic,
   and key assumptions only.

## Quick reference

| Need | See |
|------|-----|
| Core behaviors and quality checklist | `references/domain.md` |
| Context playbooks | `references/contexts.md` |
| Frameworks and moves | `references/techniques.md` |
| Failure modes and rewrites | `references/anti-patterns.md` |
| Session state shape | `references/state.md` |

## Non-negotiables

1. **One thing at a time** — Prefer a single question; wait before the next.
2. **Neutral before clever** — Strip embedded answers, praise, or blame from the stem.
3. **Past behavior over hypotheticals** in research and qualification contexts.
4. **Framework fits context** — SPIN for sales discovery; Socratic for coaching/learning;
   funnel for unknown interviews; journalism gets contradiction and evasion tools.
5. **Silence is a tool** — After a high-value question, allow space before rephrasing.
