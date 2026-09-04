# Setup and preference capture

Load this when the user asks to configure HomePod support or wants persistent notes. Resolve `<state_root>` using `SKILL.md` before reading or writing notes.

## Gather only decision-relevant context

- HomePod models and software versions.
- Active home hub and its status.
- Network topology, SSID policy, and router constraints.
- Desired outcome: reliable automation, stable multiroom playback, or Siri response quality.
- Tolerance for temporary disruption and the preferred escalation path before a reset.
- Whether direct-control commands require per-command confirmation.

## Persist only with confirmation

After the user agrees, use `<state_root>/memory.md` for activation preferences, control boundaries, open incidents, confirmed fixes, and validation evidence. Use `<state_root>/homes.md` for the device and room topology. Keep records concise, factual, and free of pairing secrets or household content.
