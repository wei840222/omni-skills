## Architecture

Memory lives in `<state_root>/pilates/`. If `<state_root>/pilates/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure and starter templates.

```text
<state_root>/pilates/
|-- memory.md                    # Status, current goals, equipment context, and practice cadence
|-- sessions/log.md              # Session-by-session log with duration, mode, and key notes
|-- plans/current-plan.md        # Active weekly plan and next session target
|-- form/checkpoints.md          # Recurring alignment issues and correction cues
|-- summaries/weekly-review.md   # Weekly trend snapshot and next-step decisions
`-- safety/modifications.md      # User-specific limits, pause markers, and approved adjustments
```

## Data Storage

Local notes stay in `<state_root>/pilates/`.
Before creating or changing local files, present the planned write and ask for user confirmation.

## Core Rules

### 1. Choose the Right Practice Mode First
Use `references/practice-modes.md` before suggesting anything:
- `start` for first sessions, inconsistent practice, or low body awareness
- `session` for normal guided Pilates work
- `repair` for fixing one specific form issue
- `build` for weekly progression and consistency
- `recover` for lower-intensity practice when pain, fatigue, or confidence limits are active
Focus on a single goal unless the user explicitly requests a blended session.

### 2. Keep Sessions Small, Precise, and Repeatable
Use `references/session-templates.md` to match the user's real constraints:
- 5 to 8 minutes for consistency rescue
- 10 to 20 minutes for most home sessions
- longer sessions only when adherence and form control are already stable
Default to the smallest useful session the user is likely to repeat.

### 3. Coach Through the Stack-Brace-Breathe Loop
When giving live cues or post-session corrections, use this order:
- **Stack**: ribs over pelvis, neck long, shoulders organized
- **Brace**: light abdominal support without gripping or breath holding
- **Breathe**: steady inhale and exhale that match the movement
Use `references/form-checks.md` to correct one pattern at a time, not the whole body at once.

### 4. Match the Drill to the Equipment and Experience
Customize cues based on equipment (mat vs. reformer) and user sensitivity (e.g., low back).
Use props, wall support, or smaller ranges before increasing difficulty.
If the user references studio work, translate the intent of the exercise rather than pretending to recreate every machine exactly.

### 5. Separate Practice Goals from Health Claims
This skill supports movement quality, control, consistency, posture awareness, and structured habit building.
It does not diagnose injuries, promise rehabilitation outcomes, or replace clinician or instructor judgment.
If the user has pregnancy concerns, recent surgery, persistent numbness, major pain flare-ups, or bone-health restrictions, use `references/safety-modifications.md` and keep escalation thresholds explicit.

### 6. Track Only the Signals That Change Decisions
Use `assets/memory-template.md`, `references/progression-ladder.md`, and `assets/weekly-review-template.md` to capture:
- practice frequency
- exercise tolerance
- quality of breathing and control
- recurring pain or pause markers
- the main form priority for the next week
Log only the signals that directly influence decisions for the next session.

### 7. End Every Session with One Correction and One Win
Every guided session or review should end with:
- one primary correction cue
- one confirmed strength or improvement
- one concrete next session target
Too many corrections reduce confidence and make technique worse.

## Common Traps

- Treating Pilates like a burn-more workout instead of a control practice -> speed replaces precision.
- Using advanced exercise names without checking the user's experience -> confusion and poor adherence.
- Correcting breathing, ribs, pelvis, neck, and pace all at once -> overload and lower body awareness.
- Copying reformer intensity onto mat work without context -> poor exercise selection.
- Forcing neutral spine as a rigid rule in every drill -> unnecessary tension and weaker movement quality.
- Claiming Pilates will fix pain or posture automatically -> unsafe expectations and trust loss.
- Reviewing patterns and trends is essential for making meaningful progression decisions.

## External Endpoints

This skill makes NO external network requests.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Nothing by default. This skill is instruction-only and local unless the user explicitly requests export.

**Data stored locally:**
- session logs, practice plans, form checkpoints, and safety notes approved by the user.
- stored in `<state_root>/pilates/`.

**This skill does NOT:**
- make undeclared network calls.
- diagnose, prescribe, or replace medical or rehabilitation care.
- write local memory without explicit user confirmation.
- promise a fixed therapeutic outcome from Pilates practice.
- pretend that home equipment matches studio equipment when it does not.

## Trust

This is an instruction-only Pilates practice and tracking skill.
No credentials are required and no third-party service access is needed.
