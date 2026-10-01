# SQL Patterns

- Prefer CTEs over nested subqueries for readability.
- Aggregate before joining when possible — performance and grain both matter.
- Use window functions for running totals, ranks, and period comparisons.
- Use CASE for clean categorization rather than many overlapping filters.
- Comment non-obvious filters — why these rows are excluded.
- Keep filters sargable when the warehouse dialect supports it; push predicates early.
- Name columns and CTEs for the business grain (`daily_active_users`, not `t1`).
