# Setup — Listen

Read this on first use to load user preferences. Load preferences silently without interviewing.

## Your Attitude

Voice users chose the channel because their hands or eyes are busy. Every repair either saves them a re-dictation or silently gets it right; every unnecessary question spends the convenience they came for. Be invisible when the transcript is clean, surgical when it is not.

## How To Load Preferences

1. Read `<state_root>/config.yaml` if it exists. Apply its values.
2. For anything absent, use the defaults in the Configuration table of `SKILL.md` — use defaults without asking.
   - `dictation_mode: cleaned`, `number_echo: actions-only`, `confirmation_posture: standard`, `languages: [en]`, `lexicon_ttl_days: 90`.
3. Read `<state_root>/lexicon.md` for stored pairs, patterns, and the Never list (`lexicon.md` for format and application order). Absence is fine; proceed without comment and create it at the first logged pair.

Work from defaults immediately. Open silently without questions about languages, engines, or how much to confirm.

## Recording Preferences (only when the user declares one)

Write to config **only** when the user states a preference in the course of the work — skip preflight questionnaires.

- User names their dictation style, echo tolerance, confirmation appetite, or languages → update the matching key in `<state_root>/config.yaml`.
- User reveals their field, artifact formatting habits, STT engine, channel mix, or spelling convention → record it under the relevant preference area (SKILL.md Configuration) as a config comment or key.
- User corrects earlier behavior ("stop echoing numbers") → update the stored value to prevent repeating it.

If the user has said nothing, store nothing.

## What the Lexicon Holds

Observed corrections, not declared preferences — keep the two distinct (`lexicon.md`). Correction pairs and Never-list entries accumulate from real exchanges only; an observation requires confirmation before overwriting a declared preference without confirmation.
