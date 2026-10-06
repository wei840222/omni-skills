# Heartbeat Recipes — Google Reviews

Use these cadence patterns as defaults, then tune by risk and volume.

## Cadence profiles

| Profile | Heartbeat | Deep report | Best for |
| --- | --- | --- | --- |
| Watch | Every 12h | Weekly | Low-volume brands |
| Balanced | Every 6h | Twice weekly | Most SMB monitoring |
| Critical | Every 1–2h | Daily | High-stakes launches or incidents |

## Heartbeat payload

Keep each cycle lightweight:

- New review count by brand/source
- Rating deltas versus baseline
- Negative-theme spike detection
- Connector health status (`active` / `degraded` / `blocked`)

If nothing meaningful changed, emit a compact no-change status and skip long narrative.

## Cooldown rules

- Default duplicate-alert cooldown: 24h per brand + theme pair
- Escalate immediately when severity upgrades from medium to high
- Reset cooldown when a new root-cause theme appears

## Failure handling

1. Mark the failing connector `degraded` with last-error and timestamp
2. Continue with remaining sources
3. Surface coverage gaps in the heartbeat digest
4. Retry on the next cycle with bounded backoff; do not loop indefinitely inside one run
