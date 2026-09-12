---
name: dreams
description: Record, organize, and analyze personal dreams to track symbols, recurring themes, people, emotions, waking triggers, and lucid-dream practice. Use when the user describes a dream on waking, wants a quick fragment capture, asks what keeps recurring, needs a weekly pattern review, explores a symbol without forcing one meaning, practices lucid dreaming techniques, or migrates an old dream journal. Not for clinical sleep-disorder coaching (`sleep`), free-form life journaling (`journal`), live emotional support (`psychologist`), or general note retrieval (`notes`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌙","requires":{"config":["<state_root>/dreams/"]}}'
  related-skills: '{"journal":"Broader reflective writing and life reviews beyond dream capture.","sleep":"Sleep quality, insomnia, jet lag, and clinical sleep red flags rather than dream content.","habits":"Daily cue and streak tracking once a morning dream-log slot is chosen.","psychologist":"In-the-moment emotional support; dream logging is not therapy.","voice-notes":"Turn groggy spoken fragments into text before filing a dream entry.","notes":"Retrieval-oriented notes unrelated to dream journaling.","mindfulness":"Waking awareness practices adjacent to dream recall and lucidity prep."}'
---

## State location

Resolve `<state_root>` once per invocation before any dream read or write:

1. Use an explicitly configured dream-state path when the host or user supplies one.
2. Otherwise use the first existing directory in this order: `<workspace>/dreams/`, `<workspace>/memory/dreams/`, `~/dreams/`, then migrate-from candidates `~/Clawic/data/dreams/` and `~/clawic/dreams/` only when moving legacy data.
3. If multiple candidates exist, keep the highest-precedence directory, leave others independent, and tell the user which location was selected.
4. If none exists and the user asks to persist a dream, create `<workspace>/dreams/` and use it as `<state_root>`.

Use only the selected `<state_root>` for every state path in this skill. Skill resources stay under `references/`; never treat the literal string `<state_root>` as a filesystem path. If legacy data sits only under `~/Clawic/data/dreams/` or `~/clawic/dreams/`, move it into the selected `<state_root>` and say in one line that you moved it and from where.

```text
<state_root>/
├── journal/
│   └── YYYY/
│       └── MM/
│           ├── YYYY-MM-DD-title.md   # full entries
│           └── YYYY-MM-DD.md         # quick captures
├── patterns/
│   ├── symbols.md
│   ├── themes.md
│   └── people.md
├── lucid/
│   └── techniques.md
└── insights.md
```

## When to use

- User describes a dream, night fragment, recurring symbol, or lucid attempt
- User asks what keeps showing up, wants a weekly review, or needs help expanding a groggy capture
- User wants portable templates for entries, pattern files, or lucidity practice logs
- Not for diagnosing sleep apnea/insomnia protocols (`sleep`), processing waking life as a journal (`journal`), or crisis/clinical support (`psychologist`)

## Operating loop

1. **Capture first** — if the user is describing a dream, write the entry before interpreting. Prefer full template when details are available; otherwise quick capture.
2. **Resolve state** — select `<state_root>`, create missing folders only when writing.
3. **File the entry** under `<state_root>/journal/YYYY/MM/` using `references/templates.md`.
4. **Update patterns only with evidence** — when the user asks about patterns or after enough entries exist, load `references/patterns.md` and update `symbols.md` / `themes.md` / `people.md` from logged entries, not from invention.
5. **Lucidity branch** — load `references/lucid.md` only when the user practices reality checks, MILD/WBTB, or logs a lucid episode.
6. **Surface lightly** — offer one concrete pattern or next capture tip; interpret only when asked, and keep multiple meanings open.
7. **Safety route** — recurring trauma nightmares, sleep paralysis with distress, dream enactment/injury risk, or self-harm content: stay non-judgmental, keep the log if the user wants it, and route clinical/sleep concerns to `sleep` or real-world care rather than dream interpretation.

## Quick reference

| Need | Action | Load |
|---|---|---|
| New dream with detail | Write full entry under `journal/YYYY/MM/` | `references/templates.md` |
| Groggy fragment | Quick capture file; expand later on request | `references/templates.md` |
| Pattern / recurrence question | Read `patterns/*` and summarize from counts | `references/patterns.md` |
| Symbol curiosity | List observed contexts; offer plural readings | `references/patterns.md` |
| Lucid practice | Reality checks, MILD/WBTB, dream-sign list | `references/lucid.md` |
| Weekly review | Scan last 7–14 days; update `insights.md` | templates + patterns |
| Domain sources | Verify recall/lucidity guidance claims | `references/sources.md` |

## Capture rules

- Log immediately on waking when possible; fragments beat perfect prose.
- Record date/time, narrative, emotions, symbols, recurring flags, possible waking triggers, and lucidity.
- Emotions are first-class data, not optional color.
- Voice-to-text is fine; route heavy audio cleanup through `voice-notes` when needed, then file here.
- Never invent dream content the user did not provide.

## Pattern rules

- Counts and recurrences come only from stored entries or explicit user history.
- Prefer “Flying appeared 3 times this month, twice with landing anxiety” over fixed symbolic dictionaries.
- People tags may note relationship context the user stated (e.g. deceased relative); do not diagnose the user.
- Weekly: refresh `insights.md` with 1–3 checkable observations and one gentle next step (capture streak, expand a fragment, or one lucidity check).

## Interpretation stance

- Offer flexible, plural readings when asked; keep ambiguity available.
- Separate dream description (what happened) from waking advice (what to do).
- Do not force meaning onto every image, dismiss fragments, or judge dream content.
- Dream work supports reflection; it is not therapy, legal advice, or medical diagnosis.

## Failure modes

| Signal | Response |
|---|---|
| User is half-awake and dumping fragments | Quick capture now; defer analysis |
| Asks “what does X mean?” with no journal | Answer tentatively from stated dream only; invite logging for patterns |
| Wants clinical sleep fix via dream skill | Hand off scope boundary to `sleep` |
| Trauma nightmare loop or safety risk | Supportive logging + real-world help path; no forced decoding |
| Legacy Clawic path still in use | Migrate once to `<state_root>` and confirm |

## Guardrails

- No credentials, secrets, or third-party account tokens in dream files.
- Do not publish private dream content externally unless the user explicitly asks to export a specific entry.
- Keep skill resources (`references/`) separate from user state (`<state_root>/`).
- Positive practice framing: log fragments, keep plural meanings, and route clinical sleep issues to the right skill.
