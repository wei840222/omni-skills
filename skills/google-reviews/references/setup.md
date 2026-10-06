# Setup — Google Reviews

Read on first use or when `<state_root>/memory.md` is missing.

## Activation

Activate for Google Maps / Business Profile reviews, Google Shopping or merchant review signals, brand reputation checks on Google surfaces, competitor review comparisons, and recurring sentiment monitoring.

Keep alerting, owner replies, and outbound posting ask-first.

## First context capture

Answer the immediate research question first, then capture reusable context:

- Company, brand, location, product, or merchant entity under analysis
- Decision the analysis should support (buy, partner, compare, audit, monitor)
- Google sources that matter (Business Profile / Maps, Shopping / merchant, both)
- Optional competitor set
- Desired heartbeat and deep-report cadence
- Alert sensitivity (strict, balanced, low-noise)
- Preferred report format (snapshot, heartbeat digest, daily action, weekly trend)

## Integration behavior

Clarify future activation:

- Auto-activate for Google reputation and review-monitoring requests
- Stay quiet unless explicitly requested
- Suggest itself when the user asks for heartbeat or review reporting systems

Store activation preference in `<state_root>/memory.md` only after the user wants persistence.

## First write checklist

1. Resolve `<state_root>` from the State location procedure in `SKILL.md`.
2. Confirm the path with the user before the first create.
3. Create `<state_root>/memory.md` from `assets/memory-template.md`.
4. Create `brands/`, `snapshots/`, `reports/daily/`, `reports/weekly/`, and `heartbeat/` only when monitoring is actually enabled.
5. Migrate legacy `~/Clawic/data/google-reviews/` only on explicit request; never mix both trees in one run.
