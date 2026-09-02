# Interior-design project-state templates

Load this reference only after the user has opted into persistent project tracking and `<state_root>` has been resolved.

Create only the state needed for the current project:

```bash
mkdir -p <state_root>/spaces <state_root>/archive
touch <state_root>/memory.md <state_root>/suppliers.md
```

## `<state_root>/memory.md`

```markdown
# Interior Design Memory

## Active Project
Name:
Type: home | rental | office | staging
Budget:
Timeline:
Priority:

## Style Preferences
<!-- Confirmed by user, not inferred -->

## Constraints
<!-- Physical, budget, regulatory, household, and accessibility constraints -->

---
Last updated: YYYY-MM-DD
```

## `<state_root>/spaces/{room}.md`

```markdown
# {Room Name}

## Dimensions
- Floor: L × W
- Ceiling: H
- Doors: position, width, swing, and access route
- Windows: position and size

## Fixed Elements
<!-- Items that cannot move -->

## Current Furniture
<!-- Record items that must remain -->
```

## `<state_root>/suppliers.md`

```markdown
# Suppliers

## Verified options
- Name:
  - Region and delivery area:
  - Checked date:
  - Product or service:
  - Price tier:
  - Availability, delivery, assembly, and return terms:

## Avoid or revisit
<!-- Record a dated reason, such as unavailable delivery or incompatible terms -->
```
