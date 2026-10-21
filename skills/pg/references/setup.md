# Setup — PostgreSQL

Read this on first use to load user preferences. Rely on stored configuration without prompting.

## Your Attitude

Postgres punishes guesses and rewards evidence. Read the plan, the lock, or the statistics view before proposing a change, and say which number would prove the fix worked. Default to the least destructive path that answers the question.

## How To Load Preferences

1. Resolve `<state_root>` using the State location rules in `SKILL.md`.
2. Read `<state_root>/config.yaml` if it exists. Apply its values.
3. For anything absent, use the defaults in the Configuration table of `SKILL.md` — use the defaults without asking.
   - `server_version: 16`, `deployment: self-hosted`, `client: psql`, `pooler: app-pool`, `id_style: bigint-identity`, `naming_convention: snake_plural`, `lock_timeout_default: 2s`, `destructive_confirm: true`.
4. Read `<state_root>/memory.md` for prior context (their schema shape, recurring pain points). Absence is fine; proceed without comment.
5. Universal values (units, locale, timezone) fall back to a host-shared profile only when the host supplies one and the user has consented to that shared path.

If the live server is reachable, `SHOW server_version` and `SELECT current_setting('is_superuser')` beat any stored value — the stored one is a fallback for when it is not.

Work from defaults immediately. Start from stored preferences and the Configuration table; ask about stack, scale, or proactivity only when a missing fact blocks a safe recommendation.

## Recording Preferences (only when the user declares one)

Write to config or memory **only** when the user states a preference in the course of the work — never as a preflight questionnaire.

- User names a version, provider, client, pooler, key style, or naming convention → update the matching key in `<state_root>/config.yaml`.
- User expresses a habit or stance (migration tooling, whether DDL may be run directly, how much plan detail they want, which extensions are unavailable to them) → record it under the relevant preference area (tooling, thresholds, conventions, platform, risk posture, output format, integrations, restrictions, cadence) in `<state_root>/memory.md`.
- User corrects earlier guidance → update the stored value so it is not repeated.

If the user has said nothing, store nothing.

## What Memory Holds

See `assets/data-templates.md` for the file format. Track their schema shape and scale, the incidents they have hit, the extensions available to them, and how much explanation they want — but only from what they actually reveal.
