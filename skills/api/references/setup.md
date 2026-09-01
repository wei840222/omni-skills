# Setup — API

Read this on first use to load user preferences. Do not interview the user.

## Lookup Procedure

When a user asks about an API, in this order:

1. **Locate the category** — API Categories table in SKILL.md. Service not listed → say so, link its official docs; use official docs links instead of guessing endpoints from memory (they drift).
2. **Read the index only** — `head -20` on the category file gives API name → line number.
3. **Read just that section** — `sed -n 'START,ENDp'`; sections are 50-100 lines. Reading the whole 500-1400 line file wastes context.
4. **Answer with the section's Common Traps included** — the traps are why this reference exists; an answer with only the endpoint repeats what official docs already do.
5. **Version-sensitive claims** (current pricing, current rate limits, model names) — the reference may lag; point to the Official Docs link at the end of the section for anything the user will bill against (`references/versioning.md` Reference Drift).

## How To Load Preferences

1. Resolve `<state_root>` by the State location procedure in `SKILL.md`, then read `<state_root>/config.yaml` if it exists; apply its values.
2. For anything absent, use the defaults from the Configuration table in `SKILL.md` — `example_language: curl`, `client_style: raw`, `default_environment: sandbox`, `retry_max: 4` — do not ask.
3. Read `<state_root>/memory.md` for observed context (services the user integrates, accounts in play, past pain points). Absence is fine; proceed without comment.
4. Treat `~/Clawic/data/api/` and `~/clawic/api/` as legacy migration sources, not active lookup locations. Keep them separate unless the user explicitly asks for a migration; then copy, validate, cut over, and retain a rollback path rather than moving or deleting data automatically.

Work from defaults immediately. Never open with questions about language, accounts, or environments.

## Recording Preferences (only when the user declares one)

- User names an example language, raw-vs-SDK style, or environment → update the matching key in `<state_root>/config.yaml`.
- User reveals a lasting choice (their payments provider, an org timeout policy, an env-var naming scheme) → record it under the relevant preference area in `<state_root>/config.yaml`.
- Patterns you observe but the user did not state (they always ask for Python, they keep using the same account) → `<state_root>/memory.md`. An observation requires confirmation to overwrite a declared preference without confirmation.
- User corrects earlier guidance → update the stored value to ensure accurate future answers.

If the user has said nothing, store nothing.

## What This Skill Does Not Do

- Store or manage API keys
- Make API calls automatically
- Access external services
