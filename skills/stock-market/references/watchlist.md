# Watchlist Structure — Stock Market

Create `<state_root>/watchlist.md` using the Watchlist Template in `assets/templates.md` (a path rooted at this skill package) only when persistent state is enabled and the user approves creation.

## Ranking Rules

Apply ranking changes in the response by default. Modify `<state_root>/watchlist.md` only when persistent state is enabled and the user approves that update.

1. Rank by setup quality and catalyst clarity, not only recent price momentum.
2. Keep Priority A small enough for the user's review capacity, and state the selection criterion.
3. Move symbols between tiers whenever evidence changes.
4. Remove stale names after catalyst passes with no valid trigger.

## Quick Health Checks

- Does each Priority A ticker have both trigger and invalidation?
- Are you duplicating correlated names with the same risk driver?
- Is a no-trade list maintained to prevent revenge entries?
