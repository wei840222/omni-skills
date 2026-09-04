---
name: remind
description: Manage reminders for commitments the user already knows about. Use when the user asks for a reminder or nudge, mentions a dated commitment or renewal, changes reminder timing, or needs help with a recurring obligation.
metadata:
  version: "1.0.4"
  openclaw: '{"emoji":"⏰"}'
  related-skills: '{"alerts":"Handles new or urgent information the user did not already know.","memory":"Stores durable context beyond reminder preferences.","notify":"Selects delivery channels, batching, and notification-fatigue controls.","schedule":"Executes scheduled work rather than recalling a user commitment."}'
---

## State location

This skill stores reminder preferences and active reminder records. Before a state operation, resolve `<state_root>` once:

1. Use an explicit user- or host-configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/remind/`, `<workspace>/memory/remind/`, `~/remind/`.
3. If none exists and the user has asked to save a reminder or preference, create `<workspace>/remind/`.

Use the selected `<state_root>` for the full invocation. When multiple candidates exist, use the highest-precedence directory, tell the user that independent copies exist, and leave lower-precedence copies unchanged. If `<workspace>` is unavailable and `~/remind/` is absent, obtain a state root before creating data. Existing legacy paths are migration sources only: propose a copy-and-verify migration; do not move or delete data automatically.

## When to use

A reminder surfaces something the user already knows when it becomes actionable:

- planned events, deadlines, promises, renewals, and recurring obligations;
- a direct request to remind, nudge, ping, snooze, or reschedule;
- feedback such as “too early,” “too late,” or “I forgot.”

Apply this test: if the user could have written it in their calendar, it is a reminder. If the world has just changed, route it to an alert. If the request is to perform work on a schedule rather than recall a commitment, route it to a scheduling workflow.

## Workflow

1. Identify the commitment, its action, due time, timezone, and whether the user already knows it. Read `references/triggers.md` for an ambiguous or implicit commitment.
2. Resolve `<state_root>` before reading or changing preferences or active records. Use `<state_root>/preferences.md` for learned timing and `<state_root>/reminders.md` for active entries; create only the file needed for the requested operation.
3. Apply precedence: explicit instruction, then a confirmed learned preference, then the default in `references/timing.md`.
4. Phrase the reminder as the action that remains possible, not merely the event. Read `references/timing.md` for lead-time, quiet-hour, timezone, travel, or multi-stage decisions.
5. Before delivery, verify that the user knows the commitment, can still act, has not acknowledged this occurrence, and is not covered by a Skip preference or quiet hours. For a missed window, lead with the remaining recovery action.
6. After delivery, treat one acknowledgment as complete unless the entry explicitly says **Always**. Propose a learned-preference change in one line before storing it; store direct instructions as `(confirmed)`, and promote an observed pattern after two consistent signals.

## Quick reference

| Situation | Response |
|---|---|
| “Remind me to X at/in Y” | Create the reminder exactly as stated; the explicit time overrides learned defaults. |
| “Don’t let me forget X” | Add an earlier action stage while keeping the final reminder actionable; see `references/timing.md`. |
| Dated commitment without a request | For the first two accepted reminders in that category, offer a nudge before creating one. |
| Recurring obligation | Confirm cadence, anchor, end condition, and delivery channel before recording it. |
| “Later” or no response | Ask once for a time; otherwise use the next natural delivery window and preserve the original commitment. |
| Timing feedback | Adjust one lead-ladder step only after the signal threshold; see `references/timing.md`. |
| Several reminders are due | Combine up to three, hard deadlines first; deliver the rest as the next digest when configured. |
| Still unclear | For high stakes, ask one targeted question; for low stakes, do not create a speculative reminder. |

## Core rules

1. Remind only about commitments the user already knows.
2. Explicit instructions override learned preferences, which override defaults. A one-off override does not rewrite a category preference.
3. Count back from when the action must start: `remind at = event time − process − transition − prep`.
4. Keep each multi-stage reminder action-distinct so it adds agency rather than repetition.
5. Preserve delivery choices: apply `quiet_hours`, existing Skip preferences, and the user's timezone before sending.
6. Keep persistent data minimal. Record a reminder only when the user has requested it or accepted the offered nudge; obtain the host's required authorization before using an external calendar, scheduler, or notification channel.

## Configuration and state

Store user-specific settings in `<state_root>/config.yaml` and learned category timing in `<state_root>/preferences.md`.

| Variable | Default | Effect |
|---|---|---|
| `quiet_hours` | 22:00–07:00 local | Defers delivery unless the action itself must start in that window. |
| `morning_slot` | 07:00–08:00 local | Delivery window for morning-of and daily-habit reminders. |
| `digest_slot` | unset | Batches low-priority reminders when configured. |
| `lead_bias` | `standard` | Shifts an unlearned category by one lead-ladder step. |

Preferences may cover tone, proactivity, workday shape, exclusions, and systems that already alert the user. Keep adjacent systems as Skip preferences to avoid duplicate notifications.

## Reference routing

- Read `references/triggers.md` to classify an explicit, implicit, or near-miss reminder request.
- Read `references/timing.md` to select or adjust a lead time, calculate travel timing, handle quiet hours, timezone changes, DST, or multi-stage reminders.
- Read `references/research.md` only when the evidence behind the prospective-memory guidance is needed.
