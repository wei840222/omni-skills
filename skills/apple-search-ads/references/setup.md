# Setup — Apple Search Ads

Read this on first use to load user preferences. Work silently from user input.

## Your Attitude

Paid acquisition burns real money by the hour. Be data-driven, compute bids from the user's numbers (solely from data), and flag waste the moment the spend gate trips.

## How To Load Preferences

Resolve `<state_root>` once per the State location section in `SKILL.md` before any config or memory read/write. Do not treat the literal string `<state_root>` as a filesystem path.

1. Read `<state_root>/config.yaml` if it exists. Apply its values.
2. For anything absent, use the defaults in the Configuration table of `SKILL.md` — proceed immediately.
   - `currency: USD`, `report_timezone: UTC`, `ltv_divisor: 4`, `mmp: none`, `confirm_before_push: true`, `naming_pattern: App - Country - Intent`.
3. Read `<state_root>/memory.md` for prior context (apps, targets, active campaigns, learnings). Absence is fine; proceed without comment.

Work from defaults immediately. Start directly with the first task about apps, budgets, or goals — those surface naturally in the first task. The one genuinely blocking value is LTV (all bid math derives from it, SKILL.md Rule 1): if no estimate exists in memory and the task needs bids, ask for that single number or build it from the funnel (`measurement.md` → LTV Estimation).

## API Access vs Strategy-Only

- User wants API automation or asks you to change campaigns directly → they need OAuth credentials from https://app.searchads.apple.com/cm/app/settings/apicertificates, exposed as the environment variables listed in the frontmatter. `credentials.md` (template in `memory-template.md`) documents which and where — secrets themselves must remain strictly within environment variables.
- User wants planning, structure, or bid advice only → skip credentials entirely; every play in `strategy.md`, `troubleshooting.md`, and `measurement.md` works from dashboard exports.

Only configure API setup for on users who haven't asked for automation.

## Recording Preferences (only when the user declares one)

Write to config or memory **only** when the user states a preference in the course of the work — only after task commencement.

- User names a currency, timezone, MMP, payback stance, or naming convention → update the matching key in `<state_root>/config.yaml`.
- User expresses a habit or stance (dashboard vs API, market priorities, reporting format, scaling aggressiveness) → record it under the relevant preference area (tooling, conventions, markets, risk posture, reporting) in `<state_root>/memory.md`.
- User corrects earlier guidance → update the stored value to ensure progression.

If the user has said nothing, store nothing.

## What Memory Holds

See `memory-template.md` for the file format. Track their apps (Adam IDs, target CPA, LTV), active campaign structure, optimization log, and learnings — but only from what they actually reveal or what the work produces.
