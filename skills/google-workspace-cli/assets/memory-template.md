# Memory Template — Google Workspace CLI

Files live in `<state_root>/`. Split: `<state_root>/config.yaml` holds what the user DECLARED (the Configuration table in SKILL.md); `<state_root>/memory.md` holds what the agent OBSERVED. An observation overwrites a declared preference only after the user confirms.

## config.yaml

```yaml
default_account:            # email; falls back to `gws auth default`
write_policy: dry-run-first # dry-run-first | confirm-only | open
output_format: json         # json | table | yaml | csv
sanitize_mode: warn         # warn | block | off
mcp_services: [drive, gmail, calendar]
# preference areas — keys added as the user states preferences:
# accounts_and_tenants: {}
# scope_policy: {}
# safety_posture: {}
# conventions: {}
# automation_cadence: {}
# no_go_zones: []
```

## memory.md

```markdown
# Google Workspace CLI Memory

## Status
status: ongoing
last: YYYY-MM-DD

## Environment Context
- accounts seen and their tenants
- tenant_type: personal | team | enterprise
- admin privileges available: yes | no | unknown

## Scope Profiles
- profile name -> scopes and allowed services
- recorded scope expansions and why

## Working Templates
- known-good command templates (stable id placeholders)
- recurring failure signatures and their fixes

## Open Risks
- unresolved auth issues
- API enablement gaps
- policy or compliance blockers

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Context still evolving | Keep refining boundaries and templates |
| `complete` | Stable operating baseline | Focus on optimization and reliability |
| `paused` | User paused this workflow | Keep context read-only until resumed |
| `implicit_setup` | User does not want setup prompts | Follow recorded preferences; ask an integration question only when the user requests one |

## Companion Files

- `<state_root>/command-log.md` — command template, required placeholders, expected output fields, known side effects, run counts (`references/automation.md`)
- `<state_root>/change-control.md` — the mutation evidence log; entry template in `references/change-control.md`
- `<state_root>/incidents.md` — failures, root causes, prevention actions
- `<state_root>/mcp-profiles.md` — service bundles per workflow family and tool budget decisions (`references/mcp-integration.md`)
