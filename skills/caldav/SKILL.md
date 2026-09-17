---
name: caldav
description: Sync, inspect, and safely modify CalDAV calendars with vdirsyncer and
  khal. Use for local-first event queries, verified writes, recurrence-aware edits,
  and stale-sync troubleshooting on standards-based servers.
metadata:
  openclaw: '{"emoji":"📅","requires":{"bins":["vdirsyncer","khal"]}}'
  related-skills: '{"calendar-planner":"Cross-calendar conflict repair and defended weekly planning beyond raw CalDAV CRUD.","schedule":"Job timing and cron-style execution when the need is scheduled work, not calendar event state.","fastmail-api":"Provider-specific Fastmail mail and calendar APIs when CalDAV alone is insufficient.","remind":"Lead-time nudges for known commitments rather than direct CalDAV event mutation."}'
---

## State location

This skill is operationally local-first but does **not** own a skill-private state tree. Calendar credentials, `vdirsyncer` config, `khal` config, and the on-disk `.ics` collections already live outside the package.

- Treat the user's existing `vdirsyncer` storage path and `khal` database as host-owned data.
- Do not invent a new `<state_root>/caldav/` tree unless the user explicitly asks to persist operator notes separate from the live calendar store.
- If operator notes are requested, resolve `<state_root>` once: explicit config first; otherwise the first existing of `<workspace>/caldav/`, `<workspace>/memory/caldav/`, `~/caldav/`; create `<workspace>/caldav/` only with consent.

## When to load

Load this skill when the user needs CalDAV work through a local `vdirsyncer` + `khal` stack, especially for iCloud, Fastmail, Nextcloud, DAViCal, Radicale, or other standards-based calendar servers.

Typical requests:
- list or search events in a bounded window
- create a one-off event and verify it landed
- safe edit/delete with duplicate-title risk
- troubleshoot stale cache, discovery, TLS, or auth failures
- decide whether a recurring series is safe to touch

Load only the reference needed for the current task:
- `references/sync-discipline.md` for discover/sync order and freshness rules
- `references/query-and-scope.md` for windows, calendars, and ambiguous time phrases
- `references/write-and-verify.md` for create/edit/delete plus read-back checks
- `references/recurrence-and-limits.md` when series, DST, or `khal edit` TTY limits matter
- `references/troubleshooting.md` for empty collections, TLS, auth, and cache traps
- `references/sources.md` when verifying CalDAV / tool claims against primary docs

## Requirements

- `vdirsyncer` and `khal` must be installed and available in `PATH`.
- The CalDAV account and collection config must already exist outside this skill.
- A TTY is required for interactive `khal edit` workflows.

## Default operating model

Prefer inspect → bounded query → explicit calendar scope → write → sync → read-back. Keep private connection details out of summaries unless the user asks for them. When the safest action is read-only, say so and stop.

## Core workflow

1. Confirm binaries and that the target calendar collection is already configured.
2. Sync (or discover, then sync) before trusting any `khal` listing when freshness matters. See `references/sync-discipline.md`.
3. Resolve the time window, timezone assumption, and calendar name before searching or writing. See `references/query-and-scope.md`.
4. For writes, capture the pre-change window, apply the smallest safe mutation, sync again, then read back title + time + calendar (or UID). See `references/write-and-verify.md`.
5. For recurring or timezone-sensitive events, load `references/recurrence-and-limits.md` and prefer inspect-first / recreate-with-approval over bulk series surgery.
6. End every answer with calendar scope, window, action taken or proposed, and whether another sync is still needed.

## Hard stop rules

- Do not present `khal edit` as a non-interactive batch primitive.
- Do not edit or delete by title alone when duplicates are possible.
- Do not treat a one-sided `conflict_resolution` policy as harmless.
- Do not delete `khal`'s cache database as a first fix for every mismatch.
- Certificate and TLS errors block further writes until the trust chain is fixed.
- Bulk recurring surgery requires an explicit user go-ahead after the risk is stated.

## Related skills

- `calendar-planner` — week repair, focus protection, multi-calendar planning
- `schedule` — durable job firing rather than calendar event CRUD
- `fastmail-api` — Fastmail-native APIs beyond CalDAV
- `remind` — commitment nudges, not direct calendar mutation
