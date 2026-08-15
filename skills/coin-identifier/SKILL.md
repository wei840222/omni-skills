---
name: coin-identifier
description: Identify coins from photos using visual checks, legends, dates, and mint marks. Use when a user needs a ranked coin identification, an evidence checklist, or a precise follow-up photo request.
metadata:
  openclaw: '{"emoji":"🪙"}'
  related-skills: '{"image":"inspect and optimize photos before identification","image-edit":"crop, isolate, and clean up the subject for clearer review","inventory":"maintain a broader catalog once coins are identified","scanner":"improve flat top-down captures of coins, cards, or documents"}'
---

## When to Use

Use when the user wants to identify a coin from one or more photos, narrow down similar issues, log a collection piece, or separate likely type from later grading or pricing work.

## Architecture

Resolve `<state_root>` before reading or writing memory: use `STATE_ROOT` when set; otherwise use `$XDG_STATE_HOME/coin-identifier/` when set; otherwise use `~/.local/state/coin-identifier/`. If the resolved directory does not exist, follow `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/
├── memory.md
├── identifications/
│   └── YYYY-MM/
│       └── {entry-id}.md
└── exports/
```

## State location

Use the resolved `<state_root>` in every path below. Do not create or write it until the user has approved local storage.

## Quick Reference

| Topic | File |
|-------|------|
| Setup guide | Load `references/setup.md` if the state directory does not exist or lacks setup files. |
| Memory template | Load `references/memory-template.md` to understand the state file structures. |
| Coin evidence checklist | Load `references/evidence-guide.md` before deciding on a coin to follow the strict evaluation order. |

## Scope

This skill ONLY:
- identifies coins from visible evidence in user-supplied images
- returns ranked candidates with explicit confidence and missing evidence
- asks for the next best photo or measurement when the evidence is incomplete
- stores local identification notes only if the user approves

Safety Boundaries:
- Always state that photos cannot guarantee authenticity, grade, mint error status, metal purity, or market value.
- Always advise users to keep coins in their current condition rather than cleaning or polishing them.
- Always keep images and coin data local without uploading to external services.

## Security & Privacy

**Data stored locally if approved by the user:**
- activation and response preferences in `<state_root>/memory.md`
- one note per saved identification in `<state_root>/identifications/`

**Skill Boundaries:**
- Keep operations local without making network requests.
- State clearly that identification is provisional and not professional grading or authentication.
- Always ask for explicit user approval before writing local files.

## Core Rules

### 1. Clear the photo gate before naming a coin
- Check subject isolation, glare, blur, crop, orientation, and whether the obverse, reverse, or edge are missing.
- If the coin is angled, reflective, inside a sleeve, or mixed with other coins, ask for a tighter straight-on view first.

### 2. Return ranked candidates with confidence, not one blind guess
- Give one to three candidates with confidence bands: High 85-95, Medium 60-84, Low 35-59.
- For each candidate, cite the visible evidence and the missing evidence.
- If the signal is weak, say the result is an unresolved shortlist instead of pretending certainty.

### 3. Use coin evidence in a fixed order
- Open `references/evidence-guide.md` before deciding.
- Work from country or script, portrait or emblem, denomination, date, mint mark, metal color, shape, rim or edge, then commemorative cues.
- Keep obverse, reverse, and edge evidence separate.

### 4. Ask for the next best view, not generic more photos
- Prefer straight obverse, straight reverse, edge, mint-mark crop, and scale or weight.
- Explain which missing feature would separate candidate A from candidate B.

### 5. Separate identification from value, grading, and authenticity
- Photo identification can narrow the type and likely issue without proving grade, rarity, or authenticity.
- If the user wants value or authenticity, treat identification as step one and keep the rest provisional.

### 6. Keep memory useful and lightweight
- Save only durable preferences and approved identification notes.
- One saved entry should record date, coin label, best match, confidence, evidence, and unresolved questions.
- Write files only after the user explicitly approves local storage.

### 7. Say what could change the answer
- Highlight wear, glare, missing edge data, foreign-script ambiguity, and similar commemoratives when they limit certainty.
- Update the shortlist immediately if a better image or measurement changes the balance.

## Common Traps and Recovery

- For a reflective or angled photo, request a straight-on view before evaluating dates, mint marks, or legends.
- Treat visible silver color as an appearance clue; confirm composition and coin type separately.
- Separate a commemorative theme from the issuing country and denomination before selecting a catalog family.
- Present identification before any value discussion, then state that grade, authenticity, and demand remain unverified.
