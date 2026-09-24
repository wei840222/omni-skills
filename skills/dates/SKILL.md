---
name: dates
description: >
  Track dating connections, plan dates, and remember private details in local
  notes. Use when the user mentions someone they are seeing, asks for a date
  idea, or wants to log how a date went. Not for relationship therapy, medical
  advice, or sending messages on the user's behalf.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"💜"}'
  related-skills: '{"daily-planner":"Place a chosen date into the day plan after the user picks a time.","habits":"Turn a user-chosen dating rhythm, such as a weekly check-in, into a trackable routine.","journal":"Hold free-form feelings that should not live in a person profile.","remind":"Schedule a reminder the user already asked for, such as a birthday or a planned date."}'
---

## When to load

Load this skill when the user names a new connection, asks what to do on a date, or wants notes after a date. Load `references/sources.md` before repeating a safety or communication claim. Load the matching reference only for the task at hand.

## State location

Dating notes may exist in `<workspace>/dates/`, `<workspace>/memory/dates/`, or `~/dates/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/dates/`, `<workspace>/memory/dates/`, `~/dates/`.
3. If more than one exists, use only the highest-precedence directory and tell the user that other copies were found. Do not merge them.
4. If none exists and the user wants notes saved, create `<workspace>/dates/`.
5. If `<workspace>` cannot be resolved and `~/dates/` is also missing, ask for a state root before creating files.

Use that `<state_root>` for every state operation in this invocation. Keep notes local to that directory. A legacy `~/Clawic/data/dates/` tree is a migration source only; copy it only after the user asks, then leave the original in place.

## Workflow

1. Name the task: new profile, date idea, after-date log, reflection, or deletion.
2. Resolve `<state_root>` before the first read or write.
3. Read only the files the task needs. See `references/file-structure.md`.
4. Confirm any fact that will be stored as the user's words, not an inference.
5. Write the smallest update, then surface one useful reminder from existing notes.

## Core behavior

- Someone new: offer a profile using `references/person-profile.md`. Create it after the user wants it saved.
- Date planning: read that person's interests and history, then suggest from `references/date-ideas.md`. Offer two or three options and let the user choose.
- After a date: capture vibe, topics, details to reuse, flags, and whether they want to see the person again. Format is in `references/after-date.md`.
- Patterns over time: update `references/history-log.md` and `references/reflections.md` only when the user is recording a pattern, not after every aside.
- Pace and intent stay with the user. Advice appears only when they ask for it.

## What to surface

When notes already contain it, surface one concrete item:

- a place or food they said they wanted to try
- a birthday or other dated detail
- time since the last logged date
- a date type not tried yet with this person

## Privacy and safety

- Store notes only under the resolved `<state_root>`. Do not sync, upload, or quote them outside this task.
- Record money requests, pressure to leave the app, or a refusal to meet as flags. The practical rule from FTC guidance is: do not send money or gifts to someone not met in person. Details: `references/sources.md`.
- If notes show control, coercion, or fear, pause planning and point to the WHO intimate-partner-violence definition in `references/sources.md`. Offer deletion of the profile.
- Delete a profile, history rows, and date-idea notes that name that person when the user asks to stop. Confirm the paths removed.
- Keep a neutral tone. Describe what was said; do not diagnose the other person.

## Related handoffs

- A chosen time goes to `daily-planner`.
- A reminder the user already requested goes to `remind`.
- A free-form feeling that is not a profile fact goes to `journal`.
- A recurring check-in the user wants to track goes to `habits`.
