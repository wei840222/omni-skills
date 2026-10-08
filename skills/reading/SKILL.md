---
name: reading
description: >
  Coach better reading: match book or article choice to goals and available
  time, pick skim vs deep-read vs linear flow, raise retention with active
  recall, and decide when to quit or switch formats. Use when the user wants
  book recommendations, help finishing books, reading plans for short daily
  windows, retention after reading, audiobook vs print choices, or permission
  to stop a slog. Not for literary theory essays (`literature`), live teach-me
  sessions (`learning`), exam/course study plans (`studying` / `study`), or
  long-horizon self-taught curricula (`learn`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📚"}'
  related-skills: '{"literature":"Scholarly close reading, theory lenses, and critical essays rather than everyday reading coaching.","learning":"In-session teaching and misconception repair when the goal is understanding a topic live.","studying":"Exam countdowns, coursework schedules, and retrieval blocks tied to assessments.","learn":"Multi-week self-directed curriculum and mastery systems without a course or exam.","bookmarks":"Saving and organizing links or read-later queues after a title is chosen.","book-writing":"Planning and drafting long-form manuscripts rather than reading existing works.","spaced-repetition":"Long-horizon review scheduling once reading takeaways become durable cards or prompts."}'
---

# Reading coach

Stateless coaching skill for **choosing what and how to read**, raising retention, and exiting books that no longer serve the goal. It does not store reading lists or progress files.

## When to load

Load when the user needs:

- a next book or article matched to goal, taste, time, and format
- a reading method (skim, deep study, linear entertainment, research cross-read)
- retention tactics after chapters (explain-back, spaced revisit, one takeaway)
- help quitting a slog, switching level/format, or replacing a 600-page commitment
- audiobook vs print/ebook fit for commute, caregiving, or focus limits

Hand off when a sibling owns the job:

| Job | Skill |
| --- | --- |
| Literary theory, close reading, critical essays | `literature` |
| Live “teach me X” explanation sessions | `learning` |
| Exam/course revision schedules | `studying` / `study` |
| Multi-week self-taught mastery systems | `learn` |
| Save/search read-later links | `bookmarks` |
| Drafting a book manuscript | `book-writing` |
| SRS deck scheduling after takeaways are atomic | `spaced-repetition` |

## Core path

1. **Context before titles** — past likes, *why* this topic (learn / entertainment / solve), daily minutes, and format constraints.
2. **One next read** — curate ruthlessly; one strong pick beats a list of ten.
3. **Match method to goal** — load `references/domain.md` for skim vs deep vs linear vs research patterns.
4. **Retention on purpose** — explain-back, link to prior knowledge, one actionable takeaway, spaced revisit; prefer own-words summary over highlighting.
5. **Exit rules** — after a fair sample (about 50+ pages or equivalent), disengagement, level mismatch, or a faster path to the goal are enough reason to stop or switch.
6. **Cite carefully** — load `references/sources.md` when quoting study techniques or comprehension guidance so dated windows stay attached.

## Depth on demand

| Need | Load |
| --- | --- |
| Recommend / method / retention / quit / common mistakes | `references/domain.md` |
| Verified research and format sources | `references/sources.md` |
| Evaluation harness only | `test-prompts.json` |

## Operating defaults

- Prefer questions that unlock a fit over dumping classics “everyone should read.”
- Treat time cost honestly: 200 pages ≠ 600 pages; short chapters and audio can be the correct primary format.
- Keep entertainment linear; interrupt deep-learning reads with retrieval, not the reverse.
- Label uncertainty on specific title fit; ask which angle of the topic matters most before locking a pick.
- No secrets, accounts, or purchase automation—recommendations stay informational unless the user asks to act.
