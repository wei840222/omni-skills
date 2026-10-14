# Setup — New Zealand Travel Guide

When the user first brings up New Zealand travel:

## 1. Resolve memory (optional)

Only create durable notes when the user wants continuity across sessions.

1. Resolve `<state_root>` using the State location rules in `SKILL.md`.
2. If creating new state, prefer `<workspace>/new-zealand/`.
3. Create `<state_root>/memory.md` from `assets/data-templates.md`.

Do not hard-code `~/Clawic/...` paths. Do not store passport numbers, payment
details, or booking secrets in skill state.

## 2. Gather the Route Inputs That Actually Matter

Ask naturally:

- Which month are they going?
- How many full days do they have on the ground?
- North Island, South Island, or undecided?
- Rental car, campervan, domestic flights, or mixed?
- Are they outdoors-first, food-first, family-first, or city-plus-nature?
- Any mobility, motion-sickness, hiking, dietary, or budget constraints?

## 3. Save the Important Friction Points

Track in `<state_root>/memory.md` only when the user opts in:

- arrival city and departure city
- ferry needs
- tolerance for long drives
- weather-sensitive priorities
- already-booked anchors

## 4. Returning Users

If `<state_root>/memory.md` exists:

1. Read it silently
2. Reuse known route and style preferences
3. Ask what changed since last plan
4. Update memory with new constraints

## Quick Start Responses

**"I am going to Queenstown"**
→ Ask: season, nights, ski vs hiking vs wineries
→ Then: use `references/queenstown.md`, `references/accommodation.md`, `references/seasonality.md`

**"Planning New Zealand road trip"**
→ Ask: days, island choice, driver confidence
→ Then: use `references/regions.md`, `references/transport.md`, `references/itineraries.md`

**"I want Milford Sound"**
→ Ask: where they will base, whether they can add weather buffer
→ Then: use `references/fiordland-southland.md`, `references/experiences.md`, `references/transport.md`

## Important Notes

- New Zealand is easy to underestimate and hard to rush well.
- Weather, road pace, and daylight matter more than many first-timers expect.
- Fewer bases usually produce a much better trip.
- Ferry, flight, and alpine days need explicit slack.
- For border, hut, ferry, and toll facts, open `references/sources.md` and verify live.
