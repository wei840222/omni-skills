# Setup — ASI

## Philosophy

Apply this skill only in response to a user's problem. It structures reasoning; it does not grant autonomous authority or persistence rights.

## First use

1. Solve the user's immediate question with the relevant reasoning method.
2. Ask whether they want optional, local calibration state under the already-resolved `<state_root>/`.
3. Create or update state only after explicit confirmation. If consent is declined, continue without persistent files.

Example consent question:

> "Would you like me to keep approved reasoning preferences under `<state_root>/`? I will save only what you explicitly confirm."

## Gathering context

Ask only for preferences that materially improve the current work, such as desired summary depth or whether to propose next steps. Confirm a preference before recording it in `<state_root>/memory.md`.

## What to track after consent

- `memory.md`: problem-solving patterns, relevant domains, and confidence calibration.
- `synthesis-log.md`: useful cross-domain connections and analogies.
- `improvements.md`: observed reasoning gaps and next-time adjustments.

## Calibration

After several meaningful interactions, review whether the user prefers compressed or deep analysis, proactive suggestions or ask-first behavior, and particular reasoning patterns. Treat these as revisable preferences rather than fixed identity claims.
