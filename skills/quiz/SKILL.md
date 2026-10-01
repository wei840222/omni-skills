---
name: quiz
description: >
  Design effective knowledge, personality, assessment, lead-gen, or trivia
  quizzes with clear stems, plausible distractors, scoring logic, progress UX,
  and actionable results. Use when creating, reviewing, or implementing a quiz
  (questions, outcomes, scoring, or quiz UI). Not for flashcard decks
  (`flashcards` / `anki` / `quizlet`), live adaptive tutoring sessions
  (`learning` / `school`), multi-week study plans (`studying`), or general form
  field validation without quiz outcomes (`forms`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"❓"}'
  related-skills: '{"learning":"Live adaptive teaching and misconception repair rather than one-shot quiz design.","flashcards":"Atomic recall cards and deck authoring when the deliverable is SRS cards, not a scored quiz.","quizlet":"Quizlet set/mode workflows rather than generic quiz design.","studying":"Exam calendars and multi-session revision grids outside a single quiz artifact.","forms":"Form fields, validation, and submissions when there is no quiz scoring or outcome mapping.","school":"K-12 tutoring with parental controls when the primary task is homework help, not authoring a quiz."}'
---

## State location

Quiz is primarily a **stateless design skill**. Optional draft quiz specs may live in `<workspace>/quiz/`, `<workspace>/memory/quiz/`, or `~/quiz/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/quiz/`, `<workspace>/memory/quiz/`, `~/quiz/`.
3. If multiple candidates exist, keep the highest-priority one, leave others independent, and tell the user which location was selected.
4. If none exists and persistent drafts must be created, default to `<workspace>/quiz/` with brief consent on first write.

Use the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Skill resources stay under `references/`.

## When to load

Load this skill when the user wants to **create, critique, or implement a quiz**:

- knowledge / certification / exam-style items with one correct answer
- personality or “which type are you” outcome mapping
- assessment diagnostics across competency dimensions
- lead-gen / lead generation quizzes that gate results behind contact capture
- trivia / entertainment quizzes with score or leaderboard framing
- question stems, distractors, scoring, progress UX, or results copy

Route away when the primary task is:

- Anki/Quizlet card decks or study modes → `flashcards` / `anki` / `quizlet`
- live teach-me / Socratic tutoring → `learning` / `school`
- multi-week exam grids → `studying`
- plain form fields without outcomes/scoring → `forms`

## When to load references

Keep this file as the entry point; load the smallest matching reference.

| Need | File |
|------|------|
| Verified source URLs (Gate 6) | `references/sources.md` |
| Quiz type patterns (knowledge, personality, assessment, lead-gen, trivia) | `references/types.md` |
| Stems, distractors, item types, difficulty | `references/questions.md` |
| Data model, UX, platforms, gamification, accessibility | `references/implementation.md` |

## Operating loop

1. **Clarify goal** — learning assessment, engagement, diagnosis, lead capture, or entertainment; note audience and length budget.
2. **Pick type + scoring** — percentage, weighted, multi-dimension rubric, or outcome trait mapping; write that choice down before drafting items.
3. **Draft items** — one concept per stem; plausible distractors; positive framing; no “all/none of the above” unless the product explicitly requires it.
4. **Define results** — score bands or outcome descriptions that feel personal and end with a concrete next action.
5. **UX pass** — progress visibility, mobile tap targets, feedback timing (immediate vs end), save-on-interrupt if long.
6. **Review** — run the question checklist and red-flag scan before shipping; store durable drafts under `<state_root>/` only when the user wants them kept.

## Core rules

- **One concept per question.** Split double-barreled stems.
- **Plausible distractors.** Wrong options must come from common misconceptions or near-miss concepts, not jokes.
- **Personal, actionable results.** Prefer typed outcomes or competency feedback over bare “7/10”.
- **Progress visibility.** Show position in the set (count or bar); long quizzes without progress drive abandonment.
- **Test the objective, not reading tricks.** Prefer positive stems; avoid obscure trivia that is off the stated learning goal.
- **Mobile-first interaction.** Large tap targets, vertical scroll, no hover-only controls.

## Red flags

- Correct answers always in the same option letter
- One obviously wrong distractor among three lookalikes
- Results with no “now what” action
- Lead-gen gate whose result value is weaker than the email friction
- Mobile UI with tiny buttons or horizontal scroll for options

## Safety

- Do not invent certification cut-scores, legal/medical pass criteria, or vendor pricing from memory; cite a live source or mark unverified.
- For graded/high-stakes exams, prefer end-of-quiz feedback over leaking answers mid-attempt when assessment purity matters.
- Treat quiz answers and PII (email for lead-gen) as sensitive; do not commit real respondent data into the skill package.
