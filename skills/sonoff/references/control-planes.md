# Sonoff Control Planes

Use this matrix to choose the right control plane per task.

## Available Planes

- **eWeLink cloud API**
  - Best for remote access across networks.
  - Requires valid cloud credentials and account-scoped permissions.
  - Open-platform integration docs live under CoolKit eWeLink API Center (v2 surface and OAuth materials). Region/host selection must follow the current developer docs, not a hard-coded single hostname guess.

- **LAN control mode**
  - Best for low-latency local operations on devices that actually support LAN control.
  - Requires same-LAN reachability and LAN-capable firmware/device. Unsupported models fail closed.

- **DIY mode API**
  - Local HTTP API for compatible SONOFF DIY devices (commonly `/zeroconf/*` style paths on the device).
  - Discovery often relies on mDNS/zero-conf service metadata (historically `_ewelink._tcp` style advertisements). Confirm live service records before assuming paths.

- **iHost Open API V2**
  - Local bridge token + REST and SSE endpoints for iHost / eWeLink CUBE managed systems.
  - Useful for local orchestration and event-driven confirmation without leaving the LAN.

## Selection Rules

1. Prefer LAN or iHost local path for immediate local-state operations when the device is reachable and eligible.
2. Use the cloud path when remote-only control is required or local eligibility fails.
3. Keep one primary plane for a run; change planes only when an explicit fallback policy is already recorded.
4. If device mode support is unknown, resolve capability before command generation.

## Reliability Baseline

- Track command id and expected result for every write.
- Set timeout and retry budget per control plane.
- Log plane-specific failures separately from device logic failures.
- On mixed cloud/LAN estates, define which observation is authoritative for the current step before issuing another write.
