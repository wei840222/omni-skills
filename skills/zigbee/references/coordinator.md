# Coordinator

## Hard constraints

- Only one coordinator per Zigbee network. Two coordinators create two separate networks, not a redundant pair.
- Coordinator stick placement matters. USB ports beside dense PC noise are common failure points; use a short USB extension and move the stick away from the chassis and large metal surfaces when RF is weak or unstable.
- Coordinator migration can lose all pairings. Backup before switching hardware, and only use the stack's supported migrate/restore path.
- Some sticks need a firmware flash before they are useful. Sonoff and CC2531 class adapters often require a known-good coordinator firmware rather than factory defaults.

## Selection checklist

1. Confirm the target software stack (Zigbee2MQTT, ZHA, Hubitat, etc.) officially supports the adapter.
2. Prefer maintained coordinator firmware over abandoned forks.
3. Record IEEE/network identity and backup files before any hardware swap.
4. Keep the stick on a powered host that will stay up; a sleeping laptop is a bad coordinator host.

## Migration workflow

1. Export/backup the live network if the stack supports it.
2. Flash and verify the new stick offline first.
3. Restore only through the documented path for that stack.
4. If restore is unavailable, rebuild: routers first, then end devices.
5. Validate a sample command on near and far devices before declaring cutover done.

## Operational notes

- Do not hot-swap coordinators during active pairing storms.
- After reboot, wait for the mesh table to settle before mass reconfiguration.
- If two sticks were plugged "just to test," shut down the unused one and rejoin orphans deliberately.
