---
name: expedia
description: >
  Search Expedia stays, packages, cars, and activities; compare real trip costs;
  and run partner-safe booking workflows in public web, Travel Redirect, or Rapid
  modes. Use when Expedia inventory, packaging logic, deeplinks, total-cost
  checks, or partner API constraints matter more than generic travel advice.
  Not for deep flight routing (`flight`), multi-platform lodging search
  (`booking`), broader trip systems (`travel`), or destination sentiment
  (`tripadvisor`).
license: Apache-2.0
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧳","requires":{"bins":["curl","jq","openssl","xxd"]}}'
  related-skills: '{"booking":"Extend Expedia options into broader accommodation comparison across other booking surfaces.","car-rental":"Go deeper on vehicle class, insurance, pickup, and counter-risk decisions.","flight":"Hand off route quality, misconnect risk, baggage traps, and fare-family judgment when flight complexity dominates.","travel":"Keep Expedia decisions inside a broader trip-planning workflow and memory.","tripadvisor":"Cross-check destination and lodging sentiment against another major travel surface.","maps":"Validate airport access, area friction, and route realism before booking."}'
---

## State location

Expedia state may exist in `<workspace>/expedia/`, `<workspace>/memory/expedia/`, or `~/expedia/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/expedia/`, `<workspace>/memory/expedia/`, `~/expedia/`.
3. If none exists and durable state must be created, default to
   `<workspace>/expedia/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell
   cwd. An existing `~/expedia/` may be read; otherwise ask before creating
   data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.
Treat prior Clawic paths as migration sources only; migrate them only through
a user-approved copy, validation, and cutover.

## When to Use

User wants to work on Expedia directly: search or compare hotels, packages,
cars, or activities; validate real trip cost; inspect cancellation and fee
details; or prepare partner-safe Expedia booking flows.

Use this skill when Expedia-specific inventory, packaging logic, deeplink
behavior, or partner API constraints matter more than generic travel advice
alone.

## Architecture

If `<state_root>/` does not exist, run `references/setup.md`. See
`references/memory-template.md` for structure.

```text
<state_root>/
├── memory.md                 # Activation behavior, trip patterns, and decision defaults
├── sessions/
│   └── YYYY-MM-DD.md         # Current search context and shortlisted options
├── stays/
│   └── {city-or-trip}.md     # Lodging and package candidates with tradeoffs
├── partners/
│   ├── auth-notes.md         # Which partner surfaces are available in this workspace
│   └── request-log.md        # Redacted endpoint, mode, status, timestamp
└── bookings/
    └── {trip-name}.md        # Confirmed selections, deadlines, and weak points
```

## Quick Reference

Load only the file needed for the current Expedia task.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory schema and status model | `references/memory-template.md` |
| Rapid lodging partner workflows | `references/rapid-lodging.md` |
| Travel Redirect search and deeplink workflows | `references/travel-redirect.md` |
| Public web search and verification flows | `references/web-navigation.md` |
| Total-cost and package comparison logic | `references/total-cost.md` |
| Booking-safety gates before execution | `references/booking-gates.md` |
| Access boundaries and compliance rules | `references/access-boundaries.md` |
| Core rules, common traps, and scope | `references/rules.md` |
