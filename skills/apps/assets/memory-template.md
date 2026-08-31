# Apps state templates

Use these templates only after resolving `<state_root>` and obtaining consent to create or modify persistent state. Create only the files needed for the user's requested tracking.

## `memory.md`

Create `<state_root>/memory.md`:

```markdown
# Apps — Preferences

## Platform
<!-- iOS | Android | Both -->

## Pricing Preferences
<!-- free-only | freemium-ok | paid-ok | no-subscriptions -->

## Dislikes
<!-- Apps or patterns to avoid -->
-

## Notes
<!-- Privacy, offline use, accessibility, cross-platform needs, or other preferences -->

---
*Last updated: YYYY-MM-DD*
```

## `favorites.md`

Create `<state_root>/favorites.md`:

```markdown
# Favorite Apps

## Productivity
| App | Platform | Why it fits |
|-----|----------|-------------|

## Notes & Writing

## Health & Fitness

## Finance

## Photo & Video

## Social

## Utilities

## Entertainment

---
*Last updated: YYYY-MM-DD*
```

## `tried.md`

Create `<state_root>/tried.md`:

```markdown
# Apps Tried

## Kept
| App | Category | Notes |
|-----|----------|-------|

## Dropped
| App | Category | Why |
|-----|----------|-----|

---
*Last updated: YYYY-MM-DD*
```

## `wishlist.md`

Create `<state_root>/wishlist.md`:

```markdown
# Apps to Try

| App | Category | Why interested | Added |
|-----|----------|----------------|-------|

---
*Last updated: YYYY-MM-DD*
```
