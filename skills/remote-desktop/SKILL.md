---
name: remote-desktop
description: >
  Connect to remote desktops with RDP, VNC, and SSH X11, prefer SSH tunnels for
  internet paths, choose protocol by target OS, and troubleshoot black screens,
  NLA disconnects, clipboard, and audio. Use when the user needs xfreerdp,
  mstsc, vncviewer, X11 forwarding, jumphost tunnels, or host-profile memory.
  Prefer `vpn` for full-tunnel privacy paths, `network` for generic reachability,
  and `firewall` for host packet-filter rules once the desktop protocol is chosen.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🖥️","requires":{"bins":["ssh"]}}'
  related-skills: '{"network":"Layer-3 reachability, DNS, and routing when the desktop hop is only one path among many.","vpn":"Full-tunnel or commercial VPN when path privacy is the goal rather than a single desktop session.","firewall":"Host or edge packet filters that must allow SSH or the chosen desktop transport.","linux":"Broader Linux administration once the session is up.","server":"Server bootstrap and service layout beyond remote display access.","sysadmin":"General sysadmin workflows that include remote desktop as one tool."}'
---

## State Location

Remote-desktop state may exist in `<workspace>/remote-desktop/`, `<workspace>/memory/remote-desktop/`, or `~/remote-desktop/`. `<workspace>` is the workspace root supplied by the host/runtime.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path supplied by the user or host when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/remote-desktop/`, `<workspace>/memory/remote-desktop/`, `~/remote-desktop/`.
3. When no candidate exists and the host supplied `<workspace>`, propose `<workspace>/remote-desktop/` as the creation target and obtain named consent before creating it.
4. When no candidate exists and no host workspace is available, ask for an explicit state path before creating state.

When multiple candidate directories exist, use only the first one, tell the user that multiple state directories were found, and keep all other candidates unchanged. Use the selected `<state_root>` for every state operation during the run. Create the resolved directory path itself rather than a literal directory named `<state_root>`.

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` does not exist or is empty, read `references/setup.md` and start with the user's connection request.

## When to load

Load this skill when the user needs remote GUI access to another machine: protocol choice (RDP / VNC / SSH X11), secure tunnel setup, connection commands, host-profile memory, or display/session troubleshooting.

## Architecture

State lives under the resolved `<state_root>`. Templates live in `references/memory-template.md`. Keep credentials out of the skill package and out of saved profiles.

```text
<state_root>/
├── memory.md   # Preferences, defaults, integration status
└── hosts/      # Per-host connection profiles (no passwords)
```

## Progressive disclosure

| Topic | File | When to load |
| --- | --- | --- |
| First-run integration | `references/setup.md` | `<state_root>/memory.md` missing or empty |
| Memory and host templates | `references/memory-template.md` | Creating or updating saved state |
| Protocol commands and ports | `references/protocols.md` | Choosing RDP, VNC, X11, or a modern alternative |
| Failure diagnosis | `references/troubleshooting.md` | Connection refused, black screen, NLA drop, slow path, clipboard/audio |
| Dated official sources | `references/sources.md` | Before citing ports, flags, RFCs, or vendor behavior |
| Evaluation harness only | `test-prompts.json` | Running skill tests |

## Operating sequence

1. **Collect context** — client OS, target OS, LAN vs internet, whether SSH/jumphost access exists, and whether the user wants a full desktop or a single remote GUI app.
2. **Resolve state** — run State Location before reading or writing host profiles.
3. **Pick protocol** — Windows target → RDP; persistent Linux/macOS desktop → VNC; single remote X11 app → `ssh -X`/`-Y`; Wayland-native paths → prefer VNC or `waypipe` rather than classic X11 forward.
4. **Prefer a tunnel on internet paths** — open an SSH local forward (or reverse forward when the target is behind NAT) before RDP/VNC. Keep RDP `3389/tcp` and VNC `5900+/tcp` off the public internet unless a VPN or equivalent path control already exists.
5. **Issue the smallest working command** — start from the Quick commands below; load `references/protocols.md` for flags, clipboard, drive redirect, and audio.
6. **Diagnose in order** — listener → firewall → auth/NLA/cert → display session → encoding/bandwidth → clipboard/audio extras. Load `references/troubleshooting.md`.
7. **Offer to save** — after a working connection and explicit consent, write `<state_root>/hosts/{hostname}.md` with host, user, tunnel, flags, and notes. Store credentials in the OS keyring or SSH agent, not in markdown.

## Quick commands

**RDP (FreeRDP on Linux):**

```bash
# Prefer tunnel when the path leaves the LAN
ssh -L 13389:windows-host:3389 user@jumphost
xfreerdp /v:localhost:13389 /u:USER /size:1920x1080 /dynamic-resolution /clipboard
```

**VNC via SSH tunnel:**

```bash
ssh -L 5901:localhost:5901 user@linux-host
vncviewer localhost:5901
```

**Single remote GUI app (X11):**

```bash
ssh -X -C user@host xclock
# Trusted X11 (broader remote X access): ssh -Y user@host
```

## Protocol selection

| Target | Prefer | Why |
| --- | --- | --- |
| Windows desktop | RDP | Native Remote Desktop stack; FreeRDP/`mstsc` clients |
| Linux desktop session | VNC (TigerVNC / x11vnc) or local display share | Persistent desktop; tunnel over SSH |
| macOS Screen Sharing | VNC-compatible client | Built-in screen sharing speaks VNC |
| One remote GUI app | SSH X11 (`-X`/`-Y`) or `waypipe` on Wayland | Avoid a full desktop session |
| High-LAN performance / self-host | NoMachine, RustDesk, etc. | Load `references/protocols.md` before treating as default |

Default ports (conventions, not allow-lists): RDP `3389/tcp`, VNC `5900 + display` (display `:1` → `5901`), SSH `22/tcp`.

## Core rules

1. **Tunnel first on untrusted paths** — build `ssh -L`/`-R` (or an existing VPN) before exposing RDP/VNC listeners.
2. **Auth without plaintext profile secrets** — prefer SSH keys and OS keyring; if a password must be typed, keep it out of `<state_root>` files and shell history where the host allows.
3. **Consent before state writes** — create or update `<state_root>/` only after the user agrees to remember hosts or preferences.
4. **Connect only on explicit request** — assemble commands for the user; do not open sessions unprompted.
5. **Match security mode to the server** — modern Windows often expects NLA; try `/sec:nla` then documented FreeRDP TLS/RDP modes rather than inventing flags.
6. **Separate clipboard/files/audio** — enable only the redirects the user asked for (`/clipboard`, `/drive:...`, sound backend).
7. **Hand off cleanly** — path privacy → `vpn`; generic offline/DNS/routing → `network`; packet filters → `firewall`; broader host work → `linux` / `server` / `sysadmin`.

## Common traps → recovery

| Symptom | First recovery |
| --- | --- |
| Connection refused / timeout | On target: `ss -tlnp` for 3389/5900+/22; confirm firewall and listener |
| VNC black screen | Wrong display or no session — list `/tmp/.X11-unix/`, start `vncserver :1`, or `x11vnc -display :0 -auth guess` |
| RDP connects then drops | NLA/cert/session conflict — try documented `/sec:` modes, `/cert:ignore` only on lab hosts, `/admin` for console takeover when authorized |
| X11 "Can't open display" | Server `X11Forwarding yes`, client `-X`/`-Y`, `xauth` installed; verify `echo $DISPLAY` |
| Slow session | Lower VNC quality/encoding or RDP color depth / network profile; add SSH `-C` for X11 |
| Clipboard dead | FreeRDP `+clipboard` / `/clipboard`; VNC `vncconfig`; X11 `xclip` |
| Internet path blocked | SSH local forward via jumphost, or reverse forward initiated from the NAT side |

## Security and privacy

**Stays local under `<state_root>` (with consent):** hostnames, usernames, tunnel strings, resolution preferences, non-secret flags, last-known-good notes.

**Do this instead of insecure defaults:**

- Keep RDP/VNC off public bind addresses; reach them through SSH or VPN.
- Save working command shapes without passwords.
- Prompt before first write to `<state_root>/`.
- Run connection commands only when the user asks.
- Limit skill memory reads/writes to the resolved `<state_root>`.

## Scope

**Provides:** protocol choice, copy-pasteable client commands, tunnel patterns, troubleshooting order, optional host-profile memory.

**Leaves alone unless the user explicitly asks:** storing passwords in markdown, unsolicited outbound connections, silent edits to `sshd_config` or system firewall policy, and writes outside `<state_root>`.
