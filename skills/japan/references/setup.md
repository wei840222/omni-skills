# Setup — Japan Travel Guide

## First-Time Setup

When user mentions Japan travel for the first time:

### 1. Resolve State Root
Follow the `## State location` rules in `SKILL.md`. Do not treat the literal
string `<state_root>` as a filesystem path.

### 2. Create Memory Structure (only with consent)
```bash
mkdir -p "$RESOLVED_STATE_ROOT"
```

### 3. Initialize Memory File
Create `<state_root>/memory.md` using the template from
`references/memory-template.md`.

### 4. Gather Trip Context
Ask naturally (not as a form):
- Which month are you going? (season heavily affects crowds and weather)
- How long is the trip?
- Which bases matter most? (Tokyo, Kyoto, Osaka, Hiroshima, Hokkaido, Okinawa, other)
- Food-first, culture-first, nightlife-first, nature-first, or mixed?
- Any mobility, dietary, or budget constraints?
- Rail-focused, domestic flights, or mixed transport?

### 5. Save to Memory
Update `<state_root>/memory.md` with their answers.

## Returning Users

If `<state_root>/memory.md` exists:
1. Read it silently
2. Reuse known preferences
3. Ask what changed since last plan
4. Update memory with new priorities and constraints

## Quick Start Responses

**"I am going to Tokyo"**
→ Ask: nights, neighborhood preference, food and nightlife priorities
→ Then: use `references/tokyo.md` + `references/accommodation.md`
→ For Greater Tokyo-only depth, prefer the `tokyo` skill

**"I want temples and culture"**
→ Ask: Kyoto-only depth vs Kyoto plus Nara/Uji split
→ Then: use `references/kyoto.md` + `references/culture.md` + `references/itineraries.md`

**"Planning Japan trip"**
→ Ask: one-region depth vs multi-city route
→ Then: use `references/regions.md` and `references/transport.md` before final itinerary
→ Verify rail-pass math and weather from `references/sources.md`

## Important Notes

- Japan rewards fewer bases with better pacing.
- Rail logistics define trip quality more than map distance.
- Peak seasonal windows need early bookings.
- Etiquette and timing details improve both value and experience.
- Do not lock non-refundable bookings from package memory alone.