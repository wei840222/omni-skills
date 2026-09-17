# Groups vs Binding

## Groups

- The coordinator fans out one group command to member devices.
- Groups require the coordinator/stack path to remain healthy for that fan-out behavior.
- Useful for app-driven or automation-driven rooms where the hub is the source of truth.

## Binding

- Direct device-to-device linkage, such as a switch bound to one or more bulbs.
- Works with lower latency and can survive coordinator reboot when both ends support the bind.
- Prefer binding for wall-switch survival and local tactile control that must keep working if the hub restarts.

## Decision guide

| Need | Prefer |
|------|--------|
| Hub automations and dashboards own the scene | Groups / hub scenes |
| Switch must still control lights after hub reboot | Binding |
| Mixed devices with weak bind support | Verify capabilities; fall back to hub automation |
| Lowest latency local control | Binding when supported |

## Caveats

- Not all devices support binding. Check the model before promising direct binds.
- Binding a switch to bulbs can survive coordinator reboot; groups generally still need the coordinator online for hub-originated group commands.
- After re-pairing, bindings and group membership usually need to be recreated.
