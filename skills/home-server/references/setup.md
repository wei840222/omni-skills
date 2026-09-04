# First-time setup

Use this reference when the user wants persistent home-server context or asks to create the inventory files.

1. Resolve `<state_root>` with the State location procedure in `SKILL.md`; inspect all candidate roots before proposing a new directory.
2. Explain the exact files that are relevant to the requested work and request confirmation before creating them.
3. After approval, create only the required files:
   - `<state_root>/memory.md` for reusable context;
   - `<state_root>/services.md` when recording a service inventory;
   - `<state_root>/backup-status.md` when reviewing backup coverage; and
   - `<state_root>/incidents.md` during or after an incident.
4. Confirm the user’s activation preference: proactive security/backup warnings, request-only guidance, or a mixed mode. Summarize every saved item in plain language so it can be corrected or removed.

Build a small baseline before collecting deeper detail: host platform and hardware constraints, service/exposure model, backup/monitoring posture, deployment tooling, maintenance cadence, and incident communication preference. Stop at the level of detail the user finds useful.
