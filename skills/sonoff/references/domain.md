# Sonoff Domain Knowledge

## Core Rules

### 1. Select Control Plane Before Any Command

- Choose eWeLink cloud, LAN control, DIY mode, or iHost local API first.
- Block execution when the plane is ambiguous because results and state consistency differ across planes.

### 2. Validate Device Capability and Mode Eligibility

- Confirm whether each device supports LAN control or DIY mode before local commands.
- Treat unsupported mode assumptions as hard errors, not retryable transient failures.

### 3. Discover Before Write

- Read current status and device metadata before generating command payloads.
- Build writes only with model-valid fields and method paths.

### 4. Use Read-Before-Write and Read-After-Write Loops

- Capture baseline state before every write action.
- Verify final observed state after command execution and halt rollout on mismatch.

### 5. Enforce Explicit Safety Gates for High-Impact Actions

- Start in read-only inspection and dry-run planning mode.
- Require explicit confirmation for power relays, heating circuits, locks, alarms, or bulk updates.

### 6. Keep Cloud and LAN Views Reconciled

- If cloud and LAN states diverge, resolve identity and sync assumptions before more writes.
- Prefer directly observed LAN state for immediate local decisions when reachable and policy allows.

### 7. Design Automations as Idempotent and Observable

- Use deterministic run ids, bounded retries, and hard halt conditions.
- Record each step with expected state checks to prevent duplicate or partial transitions.

### 8. Preserve Security and Privacy Boundaries

- Use least-privilege credentials and only declared endpoints.
- Read `EWELINK_API_TOKEN` from the environment and keep raw tokens out of notes.

## Common Traps

- Assuming every SONOFF model supports LAN or DIY mode → local calls fail by design.
- Mixing cloud and LAN writes without precedence rules → conflicting state transitions.
- Sending commands before mode/capability checks → rejected requests and wrong remediations.
- Running batch updates without canary checks → broad blast radius on invalid payloads.
- Treating command acknowledgment as final success → desired state not actually reached.
- Storing cloud tokens in plaintext notes → unnecessary credential exposure.
- Hard-coding a single cloud hostname from memory → region/app routing drift versus current CoolKit docs.

## External Endpoints

| Endpoint / surface | Data sent | Purpose |
|--------------------|-----------|---------|
| `http://<device-ip>:8081/zeroconf/*` (common DIY pattern) | Device id and command payload fields | SONOFF DIY mode local control and status retrieval on compatible firmware |
| `http://<ihost-ip>/open-api/v2/rest/*` | Local token and control payloads | SONOFF iHost / eWeLink CUBE local REST control |
| `http://<ihost-ip>/open-api/v2/sse/*` | Event subscription parameters | Local iHost event stream and status updates |
| CoolKit eWeLink open platform / API Center hosts (see `references/sources.md`) | Account-scoped API requests and device command payloads | Documented cloud/integration control surfaces; pick region and paths from current docs |
| SONOFF Help Center / product docs | Documentation query terms only | Validate product, DIY, and iHost operational guidance |

Send only the minimum operational data required for the approved action. Stay on declared SONOFF/eWeLink/iHost endpoints listed above.

## Security & Privacy

Data that may leave the machine:

- local LAN requests or cloud API payloads needed for requested SONOFF operations
- optional local event subscription traffic for iHost SSE workflows

Data that stays local:

- environment mapping, device notes, and playbooks under `<state_root>/`
- incident timelines and rollback decisions

This skill does **not**:

- use undeclared third-party endpoints
- request bypass or evasion techniques
- store `EWELINK_API_TOKEN` in local skill package files
- execute bulk writes without user confirmation and a verification strategy

## Trust

This skill sends operational data to SONOFF devices and optionally eWeLink cloud services when execution is approved.
Only install if you trust your LAN environment, iHost deployment, and eWeLink account scope with this automation data.
