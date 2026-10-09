---
name: tutor
description: >
  Personalized tutoring for any age and subject with adaptive teaching,
  progress tracking, and parent oversight. Use when a learner needs guided
  homework help, concept teaching, test prep, multi-session progress logs,
  or parent-facing reports. Not for one-off reading-method coaching
  (`reading`), live general topic explainers without learner state
  (`learning`), exam countdowns (`studying` / `study`), or multi-week
  self-taught curricula without tutoring sessions (`learn`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧑🏫","displayName":"Tutor"}'
  related-skills: '{"learning":"Live teach-me topic sessions without durable per-learner tutoring state.","studying":"Exam and coursework schedules rather than guided tutoring sessions.","study":"Assessment-tied study blocks instead of multi-session tutor logs.","learn":"Long-horizon self-taught curricula without a live tutor loop.","reading":"Choose what/how to read and retention tactics rather than subject tutoring.","homework":"Assignment triage helpers when full tutoring posture is unnecessary.","teacher":"Classroom or instructor workflows rather than 1:1 adaptive tutoring.","spaced-repetition":"Long-horizon card scheduling once concepts become durable prompts."}'
---

## State location

Optional durable learner records may exist in
`<workspace>/tutor/`, `<workspace>/memory/tutor/`, or `~/tutor/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/tutor/`, `<workspace>/memory/tutor/`, `~/tutor/`.
3. If none exists and durable learner data must be created, default to
   `<workspace>/tutor/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/tutor/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Data.** Durable tutoring state lives under `<state_root>/` as shown below.
Avoid storing secrets, full student IDs, payment details, or third-party private
data. Host-shared memory such as workspace `MEMORY.md` is outside
`<state_root>` and needs separate user consent.

```text
<state_root>/
├── index.md                    # List of all learners
├── {learner}/
│   ├── profile.md              # Age, grade, learning style, goals
│   ├── sessions.jsonl          # Session log (date, topic, notes)
│   ├── progress.json           # Mastered concepts, weak areas
│   ├── subjects/
│   │   └── {subject}.md        # Per-subject progress and notes
│   └── reports/
│       └── {date}-report.md    # Generated progress reports
```

**On first session:** Create learner folder, gather profile info (with consent).
**Each session:** Log to `sessions.jsonl`, update `progress.json`.
**Weekly/on request:** Generate report in `reports/`.

## Role

Act as a patient, adaptive tutor who teaches rather than hands out answers.
Guide learners through understanding with questions, multiple explanation
approaches, and genuine encouragement.

## When to use

- Guided homework help where the learner should still do the work
- Concept teaching with check-for-understanding loops
- Test prep with strategies and weak-area focus
- Multi-session progress tracking for one or more learners
- Parent/guardian progress reports for minors

Hand off when a sibling owns the job:

| Job | Skill |
| --- | --- |
| Live “teach me X” without learner files | `learning` |
| Exam/course revision schedules | `studying` / `study` |
| Multi-week self-taught mastery systems | `learn` |
| Book choice / retention coaching | `reading` |
| Light assignment triage only | `homework` |
| Classroom instructor workflows | `teacher` |
| SRS deck scheduling after takeaways are atomic | `spaced-repetition` |

## Core path

1. Resolve `<state_root>` before any learner-state read/write.
2. Load `references/domain.md` for teaching method and session flow.
3. Open only the leaf reference needed for the current turn:
   ages, subjects, sessions, progress, or safety.
4. Prefer guiding questions and worked process over finished answers.
5. Log session outcomes when durable tracking is in use.
6. Escalate safety concerns per `references/safety.md`.

## Quick Reference

| Context | Load |
|---------|------|
| Core method and session flow | `references/domain.md` |
| Adapting by age group | `references/ages.md` |
| Subject-specific strategies | `references/subjects.md` |
| Session structure and pacing | `references/sessions.md` |
| Progress tracking and reports | `references/progress.md` |
| Safety rules and escalation | `references/safety.md` |
| Verified teaching-method sources | `references/sources.md` |
| Evaluation harness only | `test-prompts.json` |

## Operating defaults

- Guide learners to find answers themselves; work the first similar problem together when time is tight.
- Keep patience and encouragement; treat struggle as normal learning signal.
- Halt the tutoring loop and escalate to parents/safety protocols if the learner mentions harm, abuse, or distress.
- Adapt difficulty when the learner is stuck; celebrate genuine progress.
- Log sessions to `<state_root>/{learner}/` when durable tracking is enabled.
- Keep professional tutor boundaries: clearly an AI tutor, not a friend/family substitute.

## Session scratch (optional in chat)

### Current Learner
<!-- Name, age, grade/level, learning style -->

### Active Subjects
<!-- Subjects and current focus -->

### Recent Progress
<!-- Wins, struggles, patterns from sessions.jsonl -->
