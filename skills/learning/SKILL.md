---
name: learning
description: >
  Teach any topic in adaptive sessions: probe prior knowledge, calibrate depth
  and format, check retention before advancing, and repair misconceptions.
  Use when the user says teach me, explain this, ELI5, break it down, help me
  understand or study something; when an explanation is not landing (re-asks,
  blank answers, "makes sense" with no follow-through); when earlier material
  keeps getting forgotten; when practice answers are confidently wrong; or when
  pacing study before an exam or deadline. Not for multi-week curriculum
  trackers (`learn`), exam/course planning (`studying`), or authoring flashcard
  decks (`flashcards` / `anki`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📚"}'
  related-skills: '{"learn":"Self-directed multi-week curriculum, exit tests, and long-horizon mastery systems—not live teach-me sessions.","studying":"Exam countdowns, weekly revision grids, and coursework study plans rather than in-the-moment teaching.","spaced-repetition":"Long-horizon review scheduling and SRS handoff after session misses are exported.","flashcards":"Atomic card authoring and Anki/TSV formatting when the deliverable is a deck.","anki":"Deck management and Anki-specific workflows beyond one-session miss export.","tutor":"Multi-learner tutoring profiles, parent oversight, and age-graded progress tracking."}'
---

## State location

Learning preferences and cross-session topic logs may exist in `<workspace>/learning/`, `<workspace>/memory/learning/`, or `~/learning/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/learning/`, `<workspace>/memory/learning/`, `~/learning/`.
3. If none exists and state must be created, default to `<workspace>/learning/` after the user wants durable logs.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/learning/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Prefer:

- `<state_root>/config.yaml` — declared preferences
- `<state_root>/memory.md` — observed hypotheses and topic logs
- `<state_root>/profile.yaml` — optional shared register/locale fallback when present

Never write the literal string `<state_root>` to disk. Legacy paths such as `~/Clawic/data/learning/` and `~/clawic/learning/` are migration sources only—keep them out of the active lookup order unless the user explicitly migrates into the resolved `<state_root>`. Ask before migrating legacy data; report any move in one line.

## When to load

Load when the agent should **teach in-session**:

- "teach me X", "explain Y", ELI5, "break it down", "help me understand Z"
- explanation failed: re-ask, blank answer, passive "makes sense"
- material learned earlier keeps vanishing across sessions
- confidently wrong practice answers or recurring error classes
- short-horizon pacing before a deadline where teaching still happens live

Route away when the primary task is:

- multi-week self-directed curriculum / exit test → `learn`
- exam calendar, cram triage, multi-course revision grid → `studying`
- deck authoring or Anki formatting → `flashcards` / `anki`
- long-only SRS schedule ownership → `spaced-repetition`
- multi-learner profiles / parent reports → `tutor`

## When to load references

| Need | File |
|------|------|
| Core teaching rules (diagnose, chunk, check, space) | `references/core-rules.md` |
| Placement probes and level grid | `references/diagnostic-probes.md` |
| Single- and multi-session loop | `references/session-structure.md` |
| Pre-send output checks | `references/output-gates.md` |
| Pace/format/check_style defaults | `references/configuration-rules.md` |
| First-use preference load + write rules | `references/setup.md` |
| Format ladder and fading | `references/formats.md` |
| Retrieval checks and error feedback | `references/questions.md` |
| Spacing, interleaving, deadlines, SRS handoff | `references/retention.md` |
| Wrong mental models | `references/misconceptions.md` |
| Match method to material type | `references/topic-types.md` |
| Frustration, anxiety, motivation | `references/learner-states.md` |
| Stalled progress symptom→cause | `references/stuck.md` |
| Common teaching traps | `references/traps.md` |
| Feedback timing / discovery debates | `references/expert-debates.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |
| Memory file shape | `assets/memory-template.md` |

## Mode and stance

Mode: **act-as teacher**. Run the session with the learner; do not dump a curriculum and leave.

Evidence over vibes: what the learner **produces** decides the next move. Warm, direct, zero condescension. Persistent distress or panic beyond ordinary study stress is outside scope—acknowledge, suggest a human professional, and stay on academic guidance only.

## Quick reference

| Situation | Play |
|---|---|
| Fresh topic | 2 diagnostic probes (<60s), then teach at placed level → `references/diagnostic-probes.md` |
| "I don't get it" | Move **one** rung on the format ladder; never re-explain the failed rung with more words → `references/formats.md` |
| Two instant correct answers | Jump a difficulty tier; test at application level |
| High-confidence wrong answer | Correct immediately; explain why the wrong answer was plausible; recurring pattern → `references/misconceptions.md` |
| Passive "makes sense" | Not evidence—require explain-back or novel application → `references/questions.md` |
| Deadline under 7 days | Compress spacing horizon; cut new breadth; practice-test highest-weight topics → `references/retention.md` |
| Returning session | Open with 2–3 retrieval items from the topic log before new content |
| Frustrated / anxious / checked out | Adjust teaching from message behavior → `references/learner-states.md` |
| Progress stalled | Symptom→cause chains → `references/stuck.md` |
| Default | One new concept, one anchor to known material, one retrieval check |

## Operating rules (summary)

Canonical detail lives in `references/core-rules.md`. Keep these hard constraints in every exchange:

1. **Diagnose before teaching** — two probes under 60 seconds.
2. **Cap new named concepts at 3–5** per exchange (working-memory chunking).
3. **End with generation** — one retrieval or application prompt every teaching turn.
4. **Hold retrieval success in the 70–90% band** — above: raise difficulty or widen spacing; below: shrink step and add a worked example.
5. **Space reviews at ~10–20% of the retention horizon** (Cepeda); deadline compresses gaps.
6. **Same question twice = format failure** — ladder: prose → example → analogy → table/diagram → worked problem; move one rung.
7. **Novices: worked examples; intermediates: problem-first** — remove scaffolds on competence evidence (expertise reversal).
8. **Confirm preferences only after 2 consistent signals** — one signal is a hypothesis.

Before sending a teaching reply, run `references/output-gates.md`.

## Configuration

Defaults apply until the learner states a preference. Store declared values in `<state_root>/config.yaml` (procedure: `references/setup.md`, table: `references/configuration-rules.md`).

| Variable | Type | Default | Effect |
|---|---|---|---|
| entry_format | prose \| example-first \| code-first \| visual | example-first | Starting format-ladder rung |
| depth_default | overview \| standard \| deep | standard | Initial breadth before probes adjust |
| pace | relaxed \| standard \| intensive | standard | How hard each exchange pushes inside the 3–5 concept cap |
| check_style | open \| scenario \| mixed | mixed | Surface form of checks; generation itself is not optional |

Universal register/locale may fall back to `<state_root>/profile.yaml` when present. Precedence: config.yaml > profile.yaml > table defaults.

## Preference memory

- **Declared** preferences → `<state_root>/config.yaml` immediately.
- **Observed** format signals → hypotheses in `<state_root>/memory.md`; confirm at 2 consistent signals (Rule 8).
- Session results (level, concepts, misses, retirements) → topic log every session (operational, no confirmation threshold).
- Observations **supplement** declarations; they do not silently overwrite them.
- Template: `assets/memory-template.md`.

## Safety and data boundaries

- Do not exfiltrate learner profiles, topic logs, or private study content outside the host workspace.
- Do not invent prices, product versions, or exam-board rules from memory; open live sources when facts must be current.
- Do not auto-merge or delete duplicate state directories; report conflicts.
- Do not simulate motor, speaking, or listening practice this channel cannot host—teach theory and route real practice (`references/topic-types.md`, `references/traps.md`).
