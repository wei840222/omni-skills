# Setup - OpenTable

Read this when `<state_root>/` is missing or empty.
Keep setup practical and non-blocking.

## Operating Priorities

- Answer the immediate reservation or operations question first.
- Confirm how OpenTable is used today before suggesting structural changes.
- Keep recommendations implementable by the current team.

## First Activation Flow

1. Confirm business context:
- single venue or multi-venue operation
- service model (casual, fine dining, hybrid)
- current booking lead time and peak windows

2. Confirm success criteria for this cycle:
- occupancy target
- no-show reduction target
- guest satisfaction objective
- revenue mix objective

3. Confirm operational constraints:
- seating capacity and turn assumptions
- staffing limits by daypart
- cancellation policy and communication standards
- event or holiday exceptions already scheduled

4. If context is approved, resolve `<state_root>` per `SKILL.md`, then initialize local workspace:

```bash
mkdir -p "<state_root>"
touch "<state_root>/memory.md" \
  "<state_root>/reservation-log.md" \
  "<state_root>/guest-signals.md" \
  "<state_root>/incidents.md"
chmod 700 "<state_root>"
chmod 600 "<state_root>/memory.md" \
  "<state_root>/reservation-log.md" \
  "<state_root>/guest-signals.md" \
  "<state_root>/incidents.md"
```

Replace the literal `<state_root>` placeholder with the resolved path. Never create nested `<state_root>/opentable/` when the root already is the opentable directory.

5. If `memory.md` is empty, initialize it from `assets/memory-template.md` and extend with fields from `references/memory-template.md` as needed.

## Integration Defaults

- Start with one optimization objective per week.
- Prefer reversible changes first.
- Track outcomes before expanding rollout.
- Keep incident handling templates ready before peak windows.

## What to Save

- current objective and active constraints
- recent pacing and inventory changes
- no-show and guest friction signals
- incident causes, mitigations, and open prevention tasks

## Guardrails

- Ensure raw credentials and private tokens remain out of chat.
- Claim impact only with measurable before/after evidence.
- Recommend capacity expansions only if operations can support them.
