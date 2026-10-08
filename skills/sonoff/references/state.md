# Sonoff State Management

## Architecture

Memory lives in `<state_root>/` after the entry-point resolver chooses a path. See `references/memory-template.md` for structure and status values.

```text
<state_root>/
|-- memory.md                 # Core context and activation boundaries
|-- environments.md           # LAN segments, iHost, cloud mode, endpoint mapping
|-- devices.md                # Device registry, capabilities, command patterns
|-- automations.md            # Orchestration rules, scheduling, rollback plans
`-- incidents.md              # Failure signatures and validated recoveries
```

## Data Storage

Keep local operational notes in `<state_root>/`:

- control-plane decisions and endpoint mapping
- device capability notes by model and firmware
- automation constraints, canary scope, and rollback rules
- incident signatures and mitigations

Store credentials only as environment references (for example `EWELINK_API_TOKEN` present/absent). Keep raw secret values out of these files.

## Requirements

- SONOFF devices reachable on the target network, or an eWeLink account path for cloud mode
- Cloud operations: `EWELINK_API_TOKEN` available in the environment (or a documented OAuth client flow when building integrations against CoolKit open platform docs)
- LAN and DIY mode operations: device firmware/model actually supports that mode and is locally reachable
- iHost operations: reachable iHost Open API base URL plus a fresh local bridge access token

Prefer environment variables and redacted examples over pasting production secrets into chat logs.
