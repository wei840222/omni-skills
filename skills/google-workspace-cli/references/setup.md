# Setup — Google Workspace CLI

Read this on first use to load user preferences. Answer the immediate request first; configuration accrues as the user reveals it.

Resolve `<state_root>` from the State location section in `SKILL.md` before any read or write. A legacy tree at `~/Clawic/data/google-workspace-cli/` is a migration source only. Copy it into the resolved `<state_root>` when the user asks; do not delete the source in the same step. `~/google-workspace-cli/` is already a candidate root, so do not copy it onto itself.

## How To Load Preferences

1. Read `<state_root>/config.yaml` if it exists. Apply its values.
2. For anything absent, use the defaults from the Configuration table in `SKILL.md`:
   - `default_account`: the `gws auth default` account · `write_policy: dry-run-first` · `output_format: json` · `sanitize_mode: warn` · `mcp_services: drive,gmail,calendar`
3. Read `<state_root>/memory.md` for prior context (tenants, scope profiles, known-good templates). Absence is fine; proceed without comment.

Work from defaults immediately. Integration, boundaries, and proactivity questions wait until the user raises them.

## Initialize the Workspace (silent, on first write need)

```bash
mkdir -p "<state_root>"
touch "<state_root>"/{config.yaml,memory.md,command-log.md,change-control.md,incidents.md,mcp-profiles.md}
chmod 700 "<state_root>"
chmod 600 "<state_root>"/*
```

Substitute the resolved path for `<state_root>` before running the commands. If `<state_root>/memory.md` is empty, seed it from `assets/memory-template.md`. The tight permissions matter: these files name accounts, tenants, and command patterns.

## Recording Preferences (only when the user declares one)

- User names an account, output format, write posture, sanitize stance, or MCP bundle → update the matching key in `<state_root>/config.yaml`.
- User expresses a stance inside a preference area (tenant walls, scope policy, safety posture, conventions, automation cadence, no-go zones) → record it under that area in `<state_root>/config.yaml`; long texts get their own file in the folder, referenced by path.
- User corrects earlier guidance → update the stored value so the next run follows the correction.
- Observed patterns (recurring failure signatures, working templates) go to `<state_root>/memory.md`. An observation overwrites a declared preference only after the user confirms.

If the user has said nothing, store nothing.

## Operating Defaults Until Told Otherwise

- Inspect → dry-run → apply, one account and one tenant per operation batch (SKILL.md Rules 2 and 4).
- Minimal scopes; scope expansion is a recorded decision, not a reflex (`references/auth-playbook.md`).
- Command templates keep stable placeholders for ids so they are reusable from `<state_root>/command-log.md`.
- Every mutation runs through `references/change-control.md` gates.
