# Setup - Game Development

Read this when `<state_root>/` is missing or empty, or on first activation.
Keep setup concise and oriented to a fast first-playable outcome.

## Operating priorities

- Ship a playable loop early.
- Align technical profile with user constraints.
- Preserve decisions so later sessions continue without rediscovery.

## First activation flow

1. Clarify what the user wants to ship **now**:
   - one playable browser prototype
   - a reusable game framework
   - a production-ready game with roadmap
2. Confirm delivery profile and constraints:
   - Browser Instant (no build) or Browser Structured (TS/bundler)
   - 2D, 2.5D, or 3D scope
   - single-player only or online features
   - target devices and performance expectations
3. Confirm design direction:
   - genres and references
   - visual/camera style
   - complexity and timeline
4. Resolve `<state_root>` using `SKILL.md` State location (configured path → existing candidates → consent before create).
5. After named consent, create only the files needed for this milestone under the **resolved concrete path** (never the literal `<state_root>` string):

```bash
# Example after resolution to a real directory stored in STATE_ROOT
mkdir -p "$STATE_ROOT"
touch "$STATE_ROOT/memory.md" \
  "$STATE_ROOT/concept-briefs.md" \
  "$STATE_ROOT/user-preferences.md" \
  "$STATE_ROOT/system-decisions.md" \
  "$STATE_ROOT/playtest-log.md" \
  "$STATE_ROOT/roadmap.md" \
  "$STATE_ROOT/release-notes.md"
chmod 700 "$STATE_ROOT"
chmod 600 "$STATE_ROOT"/*.md
```

6. If `memory.md` is empty, initialize structure from `assets/memory-template.md`.

## Integration defaults

- Prefer Browser Instant for the first playable iteration.
- Keep the first milestone to one core loop and one win/lose condition.
- Apply performance budgets before expanding assets.
- Add backend dependencies only when user goals require them.

## What to save

- selected delivery profile and platform scope
- concept pillars and target player fantasy
- technical decisions and rejected alternatives
- test outcomes and balancing changes
- release risks and next milestone

## Guardrails

- Start with lightweight infrastructure for simple prototypes.
- Ensure at least one complete playtest cycle before claiming readiness.
- Document major pivots in local memory files under the resolved state root.
