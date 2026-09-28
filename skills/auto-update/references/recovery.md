# Rollback and Recovery - Auto-Update

Freshness is not worth chaos. Recovery rules are part of the product.

## OpenClaw Recovery

If an OpenClaw update causes problems:
- restore the backed-up tailoring files first
- pin or reinstall the last known-good version if needed
- run doctor and health before calling it recovered

## Skill Recovery

If a skill update breaks behavior:
- restore the previous skill folder from backup
- mark that skill as manual or `ask-first`
- keep the migration note so the same surprise does not repeat

## Strict Boundaries

- Preserve the pre-update backup throughout the run
- Confirm workflow integrity before considering a restore complete
- Require manual confirmation before re-enabling auto-update for a broken target
