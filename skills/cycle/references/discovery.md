# Discovery questions

Ask only what unblocks a concrete cycle design. Prefer one short cluster over
an interview dump.

## Required clarity

1. **Trigger** — What starts this process (request, schedule, event, alert)?
2. **Done** — What artifact or state means finished?
3. **Always steps** — Which steps already happen every time?
4. **Skipped steps** — Which necessary steps get dropped under pressure?
5. **Bottleneck** — Where is time or risk concentrated?
6. **Human gates** — Which decisions must stay with the user vs automate?

## Red flags → response

| Signal | Response |
|--------|----------|
| Vague goal ("better results") | Push for a measurable done-definition |
| More than 6 proposed phases | Split into multiple cycles or nest loops |
| No validation points | Add an explicit check before each handoff |
| "Automate everything" | Keep gated handoffs for irreversible actions |
| Missing trigger | Refuse to invent a schedule; ask for the real start signal |

## Exit criteria for discovery

Stop questioning when you can state: trigger, done artifact, 3–6 candidate
phases, and which handoffs are gated.
