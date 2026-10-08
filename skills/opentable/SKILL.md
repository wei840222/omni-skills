---
name: opentable
description: >
  Guide OpenTable availability, booking flows, guest messaging, listing conversion,
  pacing, and incident response for restaurants and hospitality venues. Use when
  adjusting OpenTable inventory or daypart strategy, reducing no-shows, rewriting
  listing/policy copy, handling overbooking or outages, or setting up local
  reservation operations memory. Not for general booking workflows outside OpenTable
  (`booking`), pure CRM lifecycle (`crm`), multi-channel support queues
  (`customer-support`), travel itineraries (`travel`), or analytics system design
  without a reservation operations question (`analytics`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍽️"}'
  related-skills: '{"booking":"Booking workflows and reservation operations in adjacent channels.","customer-support":"Guest communication quality and service recovery patterns.","analytics":"Metric design and experiment readouts for operational decisions.","crm":"Guest segmentation and lifecycle handling beyond single reservations.","travel":"Broader travel planning context that intersects with dining reservations."}'
---

## State location

OpenTable operations state may exist in `<workspace>/opentable/`, `<workspace>/memory/opentable/`, or `~/opentable/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/opentable/`, `<workspace>/memory/opentable/`, `~/opentable/`.
3. If none exists and the user wants persistent tracking, create `<workspace>/opentable/`. If `<workspace>` is unavailable, ask for a state root instead of guessing from the current directory.
4. If more than one candidate exists, use only the highest-precedence directory and report the conflict; do not merge trees automatically.

Use the selected `<state_root>` for every state operation in this skill. Prefer portable `<state_root>` paths; never hard-code host-specific absolute roots. Skill resources stay under `references/` and `assets/`; never treat the literal string `<state_root>` as a filesystem path.

```text
<state_root>/
├── memory.md            # Current strategy, goals, and integration state
├── reservation-log.md   # Demand patterns, pacing changes, and outcomes
├── guest-signals.md     # No-show patterns, special requests, and friction points
└── incidents.md         # Overbooking, outage, and recovery records
```

Create or update state only after the user opts in. Store operational decisions and trends only—no full guest personal datasets or credentials.

## When to use

Load for **OpenTable reservation operations and guest-facing booking quality**:

- Daypart inventory, pacing, and table-mix adjustments
- Listing conversion and policy copy that reduces booking friction
- No-show mitigation via reminders and cancellation clarity
- Overbooking, confirmation failure, or platform outage response
- Weekly experiments with one measurable hypothesis at a time
- Local ops memory for strategy, reservation log, guest signals, and incidents

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| Booking flows outside OpenTable | `booking` |
| Support queue / case handling patterns | `customer-support` |
| Metric frameworks without a live ops question | `analytics` |
| Guest lifecycle beyond a single reservation | `crm` |
| Broader trip planning around dining | `travel` |

## Core rules

1. Anchor every availability or policy change to a stated service goal (covers, yield, no-shows, or guest experience).
2. Keep inventory honest: open only slots kitchen and floor can actually seat; separate peak, shoulder, and off-peak strategy.
3. Prefer pacing and table mix as primary levers before blanket blocks; document expected impact before broad slot changes.
4. Design guest messaging to reduce uncertainty with explicit cancellation windows and deliverable special-request language.
5. Run one controlled weekly experiment with hypothesis, change, measurement window, and keep/rollback decision.
6. Prepare failure paths before peaks: detect fast, offer fallback booking/waitlist options, message clearly, log cause and prevention.
7. Use least-privilege access; never ask users to paste OpenTable credentials or private tokens into chat.

## Quick reference

Load only what improves the current answer.

| Need | File |
|------|------|
| First-run setup and opt-in state init | `references/setup.md` |
| Domain rules, traps, and trust boundary | `references/domain.md` |
| State tree and security defaults | `references/state.md` |
| Daily reservation operating loop | `references/reservation-playbook.md` |
| Listing conversion checklist | `references/listing-optimization.md` |
| Overbooking / outage playbook | `references/incident-response.md` |
| Memory field templates | `references/memory-template.md` |
| Continuity starter template | `assets/memory-template.md` |

## Security and privacy

- Opt-in local state only under the resolved `<state_root>/`.
- This skill does not configure or execute authenticated OpenTable API access by itself.
- Do not persist credentials in markdown notes or run undeclared network destinations.
- Keep guest notes high-signal and operational; avoid long-lived sensitive personal data.
