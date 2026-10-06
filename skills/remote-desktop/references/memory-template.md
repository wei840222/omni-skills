# Memory Template — Remote Desktop

Create files only under the resolved `<state_root>` after named user consent. Never create a literal directory named `<state_root>`.

## `memory.md`

Create `<state_root>/memory.md` with this structure:

```markdown
# Remote Desktop Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
<!-- Client OS, common targets, network situation -->

## Preferences
<!-- Default protocol, resolution, tunnel-by-default -->

## Saved Hosts
<!-- Pointers into hosts/ — name, protocol, last connected -->

---
*Updated: YYYY-MM-DD*
```

## Host profile template

For each host, create `<state_root>/hosts/{hostname}.md`:

```markdown
# {Hostname}

## Connection
host: 192.0.2.10
protocol: rdp | vnc | ssh-x11
user: username
port: default | custom

## Tunnel (if needed)
tunnel: ssh -L 13389:192.0.2.10:3389 user@jumphost

## Command
<!-- Working command without password -->
xfreerdp /v:localhost:13389 /u:USER /size:1920x1080 /dynamic-resolution /clipboard

## Notes
<!-- OS version, NLA quirks, last working date -->

---
*Last connected: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
| --- | --- | --- |
| `ongoing` | Still learning the setup | Ask before saving new facts |
| `complete` | Common hosts are known | Reuse profiles; confirm before overwriting |
| `paused` | User deferred memory | Work from the live request only |

## Write rules

1. Resolve `<state_root>` once per invocation (see `SKILL.md` State Location).
2. Obtain consent before the first create/update under `<state_root>/`.
3. Store host, user, ports, tunnel strings, and flags — not passwords or private keys.
4. Prefer updating an existing `hosts/{hostname}.md` over duplicating profiles.
