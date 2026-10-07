---
name: wedding-planner
description: >
  Plan weddings with budget guardrails, guest-list scenarios, vendor scorecards,
  payment tracking, and deadline-driven coordination. Use when the user is newly
  engaged or mid-planning and needs venue/date sequencing, guest-count decisions,
  budget control, vendor comparison, contract/payment tracking, RSVP handling, or
  day-of run-of-show. Not for general daily time-blocking (`daily-planner`),
  calendar multi-adapter repair (`calendar-planner`), wardrobe styling (`outfits`),
  pure expense ledgers (`expenses`), or generic multi-session task plans (`plan`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💍"}'
  related-skills: '{"calendar-planner":"Multi-calendar conflict repair and focus protection when wedding logistics land on shared calendars.","daily-planner":"Day-level time blocking when wedding tasks compete with ordinary work.","expenses":"Generic spend ledger and split settlements outside wedding budget lanes.","outfits":"Attire and wardrobe combinations once dress code and fittings are set.","plan":"Multi-session task plans when the work is not wedding-domain planning."}'
---

## When to use

Load for **operational wedding planning**: date/venue frame, guest-count scenarios, budget commitments, vendor shortlists, payment deadlines, RSVP control, and day-of execution.

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| Shared calendar repair / multi-adapter conflicts | `calendar-planner` |
| Ordinary day time-blocking | `daily-planner` |
| Non-wedding expense splits and reimbursements | `expenses` |
| Wardrobe catalog and outfit combos | `outfits` |
| Generic multi-session task planning | `plan` |

## State location

Wedding-planner state may exist in `<workspace>/wedding-planner/`, `<workspace>/memory/wedding-planner/`, or `~/wedding-planner/`. `<workspace>` means the workspace root provided by the host/runtime, not the shell CWD.

Before any state read or write, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/wedding-planner/`, `<workspace>/memory/wedding-planner/`, `~/wedding-planner/`.
3. If none exists and the user asks to save durable wedding notes, create `<workspace>/wedding-planner/` only after consent.
4. If multiple candidates exist, use only the highest-precedence path, report the duplicates, and leave the others untouched.

Use the selected `<state_root>` for every state operation in this skill. Create only the resolved filesystem path; the placeholder name `<state_root>` is documentation-only.

Legacy path `~/Clawic/data/wedding-planner/` is a migration source only. Propose copy, validation, cutover, and rollback; do not move or delete automatically.

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` is missing or empty, read `references/setup.md`. Confirm before the first write to `<state_root>`.

## Primary workflow

Execute in order. Stop early only when a step already blocks progress.

1. **Role and stage** — Ask which planning role is active (couple, family organizer, planner, shared team) and the stage (just engaged → day-of). Read `references/setup.md` when state is empty.
2. **Lock the frame** — Approximate date, location/radius, event-size scenarios, and budget ceiling before decor-level decisions. Read `references/domain.md`.
3. **Bottleneck routing** — Load only the reference that owns the current pain:

| Bottleneck | Load |
|------------|------|
| State tree, privacy, path safety | `references/state.md` |
| Core rules and traps | `references/domain.md` |
| First-run activation and attitude | `references/setup.md` |
| Memory schema | `references/memory-template.md` |
| Budget math, deposits, cash-flow | `references/budget-and-payments.md` |
| Vendor shortlist and contracts | `references/vendor-scorecards.md` |
| Guest tiers, RSVP, seating | `references/guest-list-and-seating.md` |
| Backward milestones and run-of-show | `references/timeline-and-run-of-show.md` |
| Verified sources | `references/sources.md` |

4. **Scenarios over false precision** — Keep A/B/C guest and budget scenarios until venue, headcount, and ceiling stabilize.
5. **Confirm before external impact** — Draft only for vendor messages, deposits, contract acceptance, or final guest communication; never send, sign, or pay without explicit current-task authorization.
6. **Write durable notes** — After consent, update `<state_root>/memory.md` and the relevant `weddings/{event}/` files named in `references/state.md`.

## Requirements

- No credentials are required.
- Prefer ranges and scenarios while constraints are still moving.
- Culture-specific etiquette and legal claims are not universal; name the culture or jurisdiction being assumed.
- Keep payment card data, full contract PDFs, passport/ID details, and deeply personal family-conflict detail out of durable notes unless the user explicitly asks and it is operationally necessary.

## Scope

This skill ONLY:

- plans weddings through local notes, timelines, and decision systems
- organizes budget, guest, vendor, and coordination information under `<state_root>/`
- turns ambiguous wedding choices into structured trade-offs and next actions

This skill does NOT:

- sign contracts, place deposits, or contact vendors on its own
- claim etiquette or legal advice is universal across cultures or jurisdictions
- store payment credentials or full contracts in durable notes by default
- read files outside `<state_root>/` for its memory
- modify its own `SKILL.md`
