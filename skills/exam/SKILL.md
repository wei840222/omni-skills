---
name: exam
description: Generate practice questions, flashcards, study schedules, and timed mock exams from supplied study material. Use when the user asks to quiz, test, review notes, create study aids, analyze weak topics, or simulate an exam; verify official requirements before modeling a named certification exam. Do not use for proctored-exam assistance or to claim an official blueprint without a verified source.
metadata:
  openclaw: '{"emoji":"📝"}'
---

## State location

Exam state may exist in `<workspace>/exam/`, `<workspace>/memory/exam/`, or `~/exam/`. Before reading or writing state, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/exam/`, `<workspace>/memory/exam/`, `~/exam/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicate locations; do not merge or synchronize them.
4. If none exists and the user asks to persist study data, create `<workspace>/exam/`.

Use the selected `<state_root>` for every state operation. Create a subject directory and only the data files needed for the requested activity; never write runtime state into this skill package.

```text
<state_root>/
└── {subject}/
    ├── questions.jsonl    # Optional question bank
    ├── sessions.jsonl     # Optional practice history
    ├── performance.json   # Optional topic statistics
    └── flashcards.json    # Optional generated-card and review data
```

## What This Skill Does

Complete exam preparation from supplied content:
- **Practice tests** — multiple choice, short answer, and essay questions
- **Flashcards** — key concepts for spaced repetition and Anki export
- **Simulations** — timed mock exams matching verified formats
- **Gap analysis** — identify weak areas and prioritize them
- **Study schedules** — realistic plans based on an exam date and availability
- **Summaries, concept maps, and quick review sheets** — focused study aids

Works for university exams, certifications, standardized tests, and professional licensing.

## Quick Reference

| Task | When to load | Load |
|------|--------------|------|
| Question generation patterns | When generating new practice questions or maintaining a question bank. | `references/questions.md` |
| Flashcard formats and review strategy | When creating, exporting, or reviewing flashcards. | `references/flashcards.md` |
| Timed simulation setup | When the user requests a timed mock exam or names a certification exam. | `references/simulations.md` |
| Performance tracking | When scoring a session, finding weak areas, or reporting progress. | `references/tracking.md` |
| Learning methods | When calibrating difficulty, retention, or a study schedule. | `references/learning-methods.md` |
| Assessment boundaries | Before responding to a live, proctored, or restricted assessment. | Apply the safety boundary below. |

## Assessment boundaries

Support learning before or after an assessment. For a live, proctored, or access-restricted exam, provide conceptual explanations and study practice rather than answers to active test questions. Ask whether the assessment permits external assistance when the status is unclear.

## Core Workflow

1. **Collect the goal and material.** Confirm the subject, assessment format, time available, and whether the user wants persistent tracking. For a named certification, obtain the current official exam guide before matching its format.
2. **Choose the activity.** Generate questions, flashcards, a schedule, a simulation, or a gap analysis. Load the matching reference before using its detailed procedure.
3. **Calibrate.** Match question types and difficulty to the supplied material and the user's target. State assumptions when the source material or exam blueprint is incomplete.
4. **Run and explain.** Present one question or card at a time when practicing; grade with the stated rubric and explain missed concepts.
5. **Persist only on request.** Resolve `<state_root>` before recording questions, sessions, performance, or flashcards. Then use the relevant reference's schema.
6. **Adapt the next step.** Prioritize weak or stale topics, while reserving a smaller maintenance share for stronger topics. When the learner improves, increase complexity gradually rather than abruptly replacing all review material.

## Question Types

| Type | Format | Best for |
|------|--------|----------|
| Multiple choice | 4 options, 1 correct | Quick assessment and certification practice |
| Multiple select | N options, M correct | Complex topics |
| True/False | Statement + T/F | Fast review |
| Short answer | 1–3 sentences | Definitions and explanations |
| Fill blank | Sentence with blank | Terminology |
| Matching | Connect pairs | Relationships |
| Essay | Open response | Deep understanding |

## Practice Session

```text
📝 Practice: AWS S3 (10 questions)

Q1/10 [Medium]
Which S3 storage class has the lowest cost for infrequently accessed data with millisecond retrieval?

A) S3 Standard
B) S3 Intelligent-Tiering
C) S3 Standard-IA
D) S3 Glacier

Your answer: _
```

After an answer, identify the correct answer, explain the relevant concept, and record the result only when persistent tracking is enabled.

## Study Planning

Typical requests:

```text
Create a study schedule — exam in 2 weeks, 3 hours/day available
Summarize chapter 5, focused on examinable concepts
Make a concept map for [topic]
Generate a 1-page quick review sheet for [subject]
Remind me to study at 7pm daily
```

Use the host's scheduling capability only after the user authorizes a reminder.

## Common Requests

```text
Generate 20 questions from [material]
Quiz me on [topic]
Start a timed simulation (50 questions, 60 minutes)
Show my weak areas
Create flashcards for [topic]
Review mistakes from the last session
Grade my essay answer and suggest improvements
```
