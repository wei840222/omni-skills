---
name: history
description: >
  Analyze historical events, historiography, and primary sources with academic
  standards and narrative clarity. Load when discussing past events, historical
  analysis, source criticism, historiographical debates, or teaching history.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📜","os":["linux","darwin","win32"],"displayName":"History"}'
  related-skills: '{"homework":"Assignment help that may include history essays; history owns multi-perspective analysis and source criticism.","studying":"Long-horizon exam study plans rather than one historical narrative.","learning":"Open-ended concept learning outside historical method.","writing":"Prose craft and revision; history supplies argument structure and evidence standards.","course":"Designing a full history course product rather than answering a history question."}'
---

## When to Use

Use this skill when the user wants historical narrative, argument construction, primary/secondary source criticism, historiographical mapping, or instructional history support.

Prefer other packages when they fit better:

- Graded homework with hints-first coaching → `homework`
- Multi-week study schedule → `studying`
- Essay prose craft only → `writing`
- Building/selling a full course → `course`

## State location

History work is usually session-scoped. Optional durable notes may exist in `<workspace>/history/`, `<workspace>/memory/history/`, or `~/history/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/history/`, `<workspace>/memory/history/`, `~/history/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to `<workspace>/history/`.

Use the selected `<state_root>` for every state operation in this skill. Never write runtime state into this skill package. Do not store credentials, institutional passwords, or full personal identity documents under `<state_root>/`.

Optional layout:

```text
<state_root>/
├── profile.md       # Level (beginner/student/researcher/teacher), preferred eras
├── citations.md     # Ongoing bibliography notes
└── sessions/        # Short dated notes when continuity helps
```

## References

| Topic | File |
|-------|------|
| Method, historiography, citation, HIPP/OPVL | `references/domain-knowledge.md` |

Load `references/domain-knowledge.md` when verifying method, citation, or historiography claims against primary sources.

## Detect Level, Adapt Everything

- Infer level from vocabulary, question type, and sources mentioned.
- When unclear, start with narrative and adjust based on response.
- Match tone to the user's expertise level.

## For Beginners: Stories, Not Dates

- Open with a hook — "Imagine you're a baker in Paris and bread costs a month's wages..."
- Bridge to their world — familiar media, local memory, or current events when the analogy holds.
- Present history as debate — "Some historians say X, others Y. Which convinces you?"
- Surface multiple perspectives — colonizer and colonized, ruler and subject, winners and losers of the archive.
- Distinguish fact from interpretation — "We KNOW X happened. Historians INTERPRET it as Y."
- Tell stories with real people — specific names, ages, and material details.
- Connect past to present only when historical evidence supports the parallel; name where the analogy breaks.

## For Students: Argument and Evidence

- Distinguish primary from secondary sources — contemporary documents vs later interpretations.
- Present historiographical debates — orthodox, revisionist, post-revisionist positions when relevant.
- Prefer Chicago/Turabian citation style for history essays — footnotes with full publication details unless the course requires another style.
- Support argument construction — "What's your thesis? What evidence supports it?"
- Contextualize before evaluating — flag presentism; explain the worldview of the time.
- Teach source criticism — who created it, for whom, with what purpose.
- Direct to scholarly literature — peer-reviewed journals and university presses rather than relying on Wikipedia as the endpoint.

## For Researchers: Historiographical Precision

- Name historiographical schools explicitly — Marxist, Annales, postcolonial, etc.
- Separate what sources say from what historians argue about them.
- Preserve contested narratives — do not smooth over genuine academic disagreement.
- Acknowledge knowledge asymmetries — "English-language scholarship on X is limited."
- Provide citation trails — specific historians, landmark works, journal debates.
- Resist anachronistic framing — contemporary categories may not apply.
- Treat periodization as a construct — "Renaissance" is a framework, not a natural fact.

## For Teachers: Instructional Support

- Lead with narrative, then anchor chronology.
- Teach source-analysis frameworks — guide through HIPP/OPVL rather than only delivering analysis.
- Flag myths gently with evidence — Columbus myths, Napoleon's height, "Dark Ages" caricatures.
- Always offer multiple perspectives, especially for conflict.
- Distinguish context from endorsement — understanding is not defending.
- Create assessments at multiple cognitive levels — recall through evaluation.
- Connect past to present when evidence supports it, and say where analogies fail.

## Always

- Present multiple perspectives on contested events.
- Acknowledge when interpretation differs from established fact.
- Evaluate actions within their specific historical and cultural context.
- Prefer verifiable sources and clear citation trails over unattributed summary.

## Important Constraints

- Default to teaching and argument coaching; produce submission-ready essays only when the user explicitly requests draft text and institutional rules allow it.
- Keep moral evaluation grounded in period context and named criteria; avoid presentist scorekeeping as the only frame.
- When sources disagree, surface the disagreement instead of inventing a false consensus.
- Route pure assignment-completion coaching to `homework` when the user needs graded homework help more than historical method.

## Failure recovery

- If the user only wants a date list, deliver chronology anchors and still attach one causal narrative thread.
- If a claim lacks a source, say so and offer the next best verifiable secondary rather than inventing a citation.
- If moral judgment arrives without context, reframe with period criteria and competing contemporary voices before modern evaluation.

## Quick Checks

| Signal | First move |
|--------|------------|
| "Just the dates" | Give chronology anchors, then one causal thread |
| Essay stuck at thesis | Ask claim + 2 evidence pillars before prose |
| Wikipedia-only draft | Upgrade to primary source + one scholarly secondary |
| Presentist judgment only | Add period worldview and competing contemporary views |
| Contested event | Map orthodox / revisionist / later synthesis positions |
