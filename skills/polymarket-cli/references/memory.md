# Preference state lifecycle

Read when the user enables persistence or updates an existing tracking preference.
Use the State location resolver in SKILL.md before accessing `<state_root>/memory.md`.
Create this file only after the user confirms what may persist; use the directly
routed asset `assets/memory-template.md`. Read existing content before updating it.

## Status values

- `ongoing`: learning the user's workflow; ask relevant preference questions.
- `complete`: workflow is known; apply confirmed preferences normally.
- `paused`: suspend feature suggestions until the user resumes.
- `never_ask`: query-response only; keep additional setup questions out of the exchange.

## Integration values

- `pending`: activation preference has not been confirmed.
- `automatic`: user approved activation for relevant Polymarket requests.
- `on-demand`: activate only on direct requests.
- `tracking`: user identified specific markets to track. This value neither creates
  a schedule nor grants trading permission; a monitor requires a separate explicit
  request and the host's scheduling authorization.

## Updates

Use natural-language preference questions rather than exposing internal enum names.
Keep the user read-only until an explicit trade request. Save observed interests,
tracked slugs, dated quotes, and voluntarily shared risk preferences only within the
confirmed persistence scope; update `last` after an authorized meaningful change.
Label recorded prices with their timestamp and outcome, rather than treating them
as current across sessions. Preserve unrelated content and an incomplete plan.

The CLI's credential config is separate user-managed state, not skill memory.
Shared-memory pointers are optional external writes: require the actual host-supplied
path and separate consent, and record only the minimal activation pointer. Private
keys, API credentials and account secrets are outside the permitted memory fields.
Legacy data migration is a separate copy/verify/cutover/rollback transaction with
explicit consent; active lookup does not search or alter old marketplace paths.
Reset/deletion is outside the normal workflow. If separately requested, confirm the
exact child under the selected root and require a resolved non-root allowlisted
path with at least two nonempty path components before any destructive action.
