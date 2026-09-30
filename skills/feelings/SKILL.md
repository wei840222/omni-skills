---
name: feelings
description: >
  Track emotions, intensity, triggers, body sensations, and what helps in a
  portable feelings log under <state_root>. Use when the user names how they
  feel, wants a mood check-in, asks what keeps triggering them, or wants
  pattern insights from past logs. Not for free-form journaling practice
  (`journal`), gratitude-only lists (`gratitude`), in-the-moment empathic
  response without logging (`empathy`), or clinical/crisis care
  (`psychologist` / human professionals).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💭"}'
  related-skills: '{"journal":"Long-form writing practice and corpus review rather than structured emotion logs.","empathy":"Reflective emotional response in the moment without requiring a feelings tracker.","gratitude":"Gratitude-only logging when that is the whole request.","psychologist":"Deeper psychological framing or distress support beyond mood tracking.","habits":"Turning check-ins into a recurring cue once the log format is stable."}'
---

## When to load

Load this skill when the user wants **structured emotional tracking**:

- naming an emotion, intensity (1–10), context, or body sensation
- logging what helped after a hard moment
- reviewing triggers, patterns, or weekly mood shape
- building a personal helps/triggers toolkit over time

Route away when the task is mainly:

- free-form journaling / morning pages → `journal`
- pure empathic reply without durable logs → `empathy`
- gratitude-only practice → `gratitude`
- crisis, self-harm, or clinical treatment → human care + `psychologist` safeguards

## State location

Feelings state may exist in `<workspace>/feelings/`, `<workspace>/memory/feelings/`, or `~/feelings/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/feelings/`, `<workspace>/memory/feelings/`, `~/feelings/`.
3. If multiple candidates exist, keep the highest-priority one, leave others independent, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/feelings/` with brief consent on first write.

Use the selected `<state_root>` for every state path in this skill. Resolve the placeholder before any filesystem write. Skill resources stay under `references/`.

## When to load references

- Load `references/tracking-system.md` for log schemas, vocabulary, triggers/helps/patterns templates, and progressive check-in flow.
- Load `references/sources.md` when citing emotion-tracking or affect-labeling research, or when PR/review evidence needs primary URLs.

## Operating loop

1. **Acknowledge** the named feeling and any body cue without judgment or forced positivity.
2. **Capture** to `<state_root>/log/YYYY/MM/DD.md` (or the day's file): emotion, intensity 1–10, context/trigger, body, optional thought, optional what-helped.
3. **Offer one concrete next step** from `<state_root>/helps.md` when it already exists; otherwise suggest one small, reversible action and ask to save it if it worked.
4. **Pattern pass** only when asked or when enough logs exist: surface frequency, time-of-day, sleep/exercise correlations from `<state_root>/patterns.md` and recent logs—cite the user's own entries, not generic advice.
5. **Proactive check-in** only after the user has opted into tracking and a known difficult window appears (e.g. recurring Sunday anxiety in their patterns).

## Core rules

- Treat every emotion as information. Log first; interpret only when asked or when a clear pattern is already in the user's files.
- Always pair emotion with body sensation when the user offers one; ask once if body data is missing and intensity ≥ 7.
- Prefer the user's own `helps.md` / `triggers.md` over generic coping lists.
- Keep responses short during acute distress; expand pattern analysis when the user asks for review.
- If the user describes self-harm, hopelessness with a plan, or inability to stay safe, pause tracking advice and route to local emergency resources / trusted humans; do not treat the log as therapy.

## Architecture

```text
<state_root>/
├── log/
│   └── YYYY/
│       └── MM/
│           └── DD.md      # timed check-ins for the day
├── patterns.md            # optional recurring time/season/correlation notes
├── triggers.md            # optional personal trigger map
├── helps.md               # optional what-works toolkit
└── insights.md            # optional longer-horizon learnings
```

Create optional files only when the matching feature is used. Full templates and vocabulary: `references/tracking-system.md`.

## Failure modes

| Condition | Response |
|-----------|----------|
| No `<state_root>` yet | Resolve per State location; ask once before first create |
| User vents but refuses logging | Stay present; skip writes; offer log later |
| Intensity ≥ 8 + safety risk language | Prioritize safety routing over toolkit tips |
| Pattern request with empty logs | Say data is missing; run a fresh check-in instead of inventing trends |
| Conflicting candidate state dirs | Use highest-precedence only; report the conflict |

## Out of scope

- Diagnosing mental illness or prescribing treatment
- Replacing human therapists, crisis lines, or emergency services
- Forced positivity or minimizing the user's stated feeling
- Writing secrets, credentials, or third-party private data into logs
