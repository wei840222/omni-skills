---
name: university
description: >
  Run self-directed degree, career, certification, and multi-course study systems:
  build curricula, weekly calendars, mastery tracking, practice exams, and spaced
  review queues. Use when the user wants an autodidact degree path, university
  course support across a term, career-change upskilling with milestones, exam-board
  prep with weighted topics, or multi-learner tutoring plans that persist across
  weeks. Prefer `learning` for live teach-me sessions, `studying` for short exam
  countdown grids, `course` for authoring/selling courses, and `flashcards`/`anki`
  when the deliverable is only a deck.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎓","requires":{"config":["<state_root>"]}}'
  related-skills: '{"learning":"Live in-session teaching, probes, and format ladders—not multi-week degree trackers.","studying":"Short-horizon exam countdowns and revision grids rather than full degree calendars.","learn":"Self-directed multi-week curriculum systems with exit tests adjacent to university mode.","course":"Designing or selling online courses rather than studying as a student.","school":"K-12 or school-term support when university framing is wrong.","exam":"Single high-stakes exam tactics without full degree architecture.","flashcards":"Atomic card authoring when the only deliverable is a deck.","anki":"Anki deck ops beyond exporting misses from university modules.","spaced-repetition":"Long-horizon SRS ownership after university schedules export review queues.","tutor":"Multi-learner profiles and parent oversight layered on top of university plans."}'
---

## State location

University learning state may exist in `<workspace>/university/`, `<workspace>/memory/university/`, or `~/university/`.
`<workspace>` means the workspace root provided by the host/runtime, not the shell cwd.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/university/`, `<workspace>/memory/university/`, `~/university/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/university/` after brief first-write consent.
5. If `<workspace>` cannot be resolved, read an existing `~/university/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Skill package files stay under `references/`; never write curricula, progress, or preference data into `SKILL.md`.

Legacy path `~/Clawic/data/university/` is a migration source only. It is outside active lookup. Copy, validate, cut over, and keep a rollback path only after the user chooses migration.

```text
<state_root>/
├── degrees/                 # One folder per degree / career / certification
│   ├── index.md             # Active programs with status
│   └── [program-name]/
│       ├── curriculum.md    # Modules, dependencies, resources
│       ├── progress.md      # Completion and mastery
│       ├── calendar.md      # Deadlines, exams, milestones
│       └── modules/         # Per-module notes and materials links
├── resources/               # Uploaded PDFs, slides, recordings indexes
├── exams/                   # Practice-exam history
├── flashcards/              # Spaced-repetition sets exported from modules
└── config.md                # Schedule, formats, goals, communication prefs
```

## When to load

Load this skill for **multi-week academic program management**:

- autodidact full-degree or career replacement curricula
- support for current university classes across a term
- career-change upskilling with portfolio milestones and cert roadmaps
- certification / board / competitive exam prep with weighted syllabi
- tutoring another learner with durable plans and mastery logs

Route away when the primary task is:

- live teach-me / ELI5 / in-session explanation → `learning`
- short exam countdown or weekly revision grid only → `studying`
- authoring or selling a course product → `course`
- K-12 school framing → `school`
- single exam tactics without program architecture → `exam`
- deck-only authoring or Anki ops → `flashcards` / `anki`
- pure SRS schedule ownership → `spaced-repetition`
- multi-learner parent dashboards as the main ask → `tutor`

## Setup

After resolving `<state_root>`, if `<state_root>/config.md` is missing or empty, read `references/setup.md` and follow it while still answering the current academic question first. Confirm before the first durable write.

## When to load references

Keep this file as the router; load the smallest matching reference only.

| Need | File |
|------|------|
| First-use preferences and write consent | `references/setup.md` |
| Hard operating rules | `references/core-rules.md` |
| Degree / career / student / exam / tutor modes | `references/degrees.md` |
| Content extraction and study-material generation | `references/content.md` |
| Practice exams and grading loops | `references/assessment.md` |
| Weekly calendar and capacity planning | `references/planning.md` |
| Mastery, time, and readiness analytics | `references/tracking.md` |
| Flashcards, audio, and study formats | `references/formats.md` |
| Preference schema and feedback loops | `references/feedback.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |

## Operating loop

1. **Resolve state** — pick `<state_root>`; load `config.md` and relevant `degrees/` only after consent rules in setup.
2. **Lock mode** — autodidact, student, career-change, exam-prep, or tutor (see `references/degrees.md`).
3. **Inventory knowns** — current level, hours/week, deadlines, materials already on hand.
4. **Plan** — curriculum + calendar with ≤80% capacity and spaced review slots (`references/planning.md`).
5. **Study cycle** — generate today's session (new + practice + review); track completion (`references/tracking.md`).
6. **Assess** — practice under exam conditions; teach the why before scoring answers as final (`references/assessment.md`).
7. **Adjust** — redistribute missed work supportively; raise or lower difficulty from mastery evidence.

## Core operations (summary)

- **New program:** assess baseline → curriculum with dependencies → time estimate → calendar → store under `<state_root>/degrees/[name]/`.
- **Daily study:** calendar-driven session with new material, exercises, and spaced review; log completion.
- **Content processing:** extract structure from uploads, summarize, map to modules, create flashcards.
- **Assessment:** generate practice exams, grade with explanations, update mastery, schedule weak-area review.
- **Progress review:** completion %, mastery by topic, hours invested, exam-readiness prediction, plan adjustments.

Canonical detail for each operation lives in the matching reference file.

## Critical rules (always)

Canonical wording: `references/core-rules.md`.

1. Teach the concept and the why before treating exam answers as complete deliverables.
2. Separate **studied** from **mastered**; require verification (explain-back, novel problem, or timed drill).
3. Place difficulty from evidence of current level, not assumed credentials.
4. Schedule spaced reviews automatically; passive rereading is not a mastery path.
5. Keep multiple concurrent programs organized under distinct `degrees/` folders.
6. Learn optimal times, formats, and session length from observed patterns, then store them in `config.md`.
7. Prefer official syllabi, exam boards, and primary learning-science sources over memorized numbers (`references/sources.md`).
