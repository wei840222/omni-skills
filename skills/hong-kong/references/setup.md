# Setup — Hong Kong Guide

Read this when `<state_root>` is missing or empty.
Keep first-use setup short and practical.

## First activation priorities

1. Answer the immediate Hong Kong question first.
2. Confirm whether continuity should be kept for Hong Kong, Kowloon, New Territories, HKG trips, or relocation topics.
3. Capture only the minimum context needed to improve recommendations.

## Initial questions

- Is this a short visit, a relocation plan, remote/tech work, study, or company setup?
- Which side of the harbour matters most: Hong Kong Island, Kowloon, New Territories, or outlying islands?
- Budget currency and monthly housing ceiling?
- Passport / entry pathway (visitor, employment, TTPS, QMAS, Working Holiday, other)?
- Hard constraints: typhoon season dates, kids/schools, quiet vs nightlife, Cantonese comfort, car avoidance?

## Local memory initialization

If the user wants continuity:

```bash
mkdir -p <state_root>
touch <state_root>/memory.md
chmod 700 <state_root>
chmod 600 <state_root>/memory.md
```

If `<state_root>/memory.md` is empty, initialize it from `assets/memory-template.md`.

## Returning users

- Read `<state_root>/memory.md` before responding.
- Reuse known budget, neighborhood, visa pathway labels, and trip dates.
- Ask only what changed since last conversation.
- Update memory with new dates, lodging logic, and relocation signals.

## Guardrails

- Do not store passport numbers, HKID numbers, bank credentials, or card numbers.
- Do not invent ImmD eligibility; point to `references/visas.md` + ImmD URLs in `references/sources.md`.
- Prefer MTR/Octopus orientation over car ownership for most profiles.
