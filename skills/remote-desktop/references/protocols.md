# Protocols — Remote Desktop

Load this file when choosing clients, flags, ports, or modern alternatives. Cite `references/sources.md` before restating vendor-specific behavior as fact.

## RDP (Remote Desktop Protocol)

**Best for:** Windows targets and many enterprise desktops.

### Clients

| Tool | Platform | Notes |
| --- | --- | --- |
| FreeRDP (`xfreerdp` / `xfreerdp3`) | Linux | Common CLI; Debian packages `freerdp2-x11` / `freerdp3-x11` |
| Remmina | Linux GUI | Wraps FreeRDP and other plugins |
| Microsoft Remote Desktop | macOS / mobile | Vendor client |
| `mstsc` | Windows | Built-in Remote Desktop Connection |

### FreeRDP command shape

Flags below match FreeRDP client documentation (syntax uses `/name:value`). Prefer interactive password entry or the OS keyring over embedding `/p:` in shell history.

```bash
xfreerdp /v:HOST /u:USER \
  /size:1920x1080 \
  /dynamic-resolution \
  /clipboard \
  /drive:share,/home/user/share \
  /cert:ignore
```

Useful extras when the environment supports them:

- `/sound:sys:alsa` or `/sound:sys:pulse` for audio redirection
- `/admin` to request the console session when the user is authorized to take it over
- Security negotiation: try the server's required mode rather than guessing — many modern Windows hosts expect NLA

NLA-oriented recovery attempts (lab-safe order):

```bash
xfreerdp /v:HOST /u:USER /sec:nla
xfreerdp /v:HOST /u:USER /sec:tls
xfreerdp /v:HOST /u:USER /sec:rdp
```

Use `/cert:ignore` only on known lab hosts; production paths should validate the certificate chain.

### Internet path

```bash
ssh -L 13389:windows-host:3389 user@jumphost
xfreerdp /v:localhost:13389 /u:USER /size:1920x1080 /dynamic-resolution /clipboard
```

Default listener convention: **3389/tcp**.

## VNC (RFB)

**Best for:** Linux desktops, macOS Screen Sharing clients, persistent graphical sessions.

RFB/VNC is specified in [RFC 6143](https://www.rfc-editor.org/rfc/rfc6143). Native VNC transport is not a substitute for a vetted encrypted tunnel on untrusted networks.

### Servers

| Server | Role |
| --- | --- |
| TigerVNC | Common Linux VNC server/viewer family |
| x11vnc | Share an existing X display |
| vino / gnome-remote-desktop | GNOME-integrated paths |
| wayvnc | Wayland compositor sharing |
| macOS Screen Sharing | Built-in VNC-compatible service |

### Start / connect

```bash
# TigerVNC-style new display (display :1 → TCP 5901)
vncserver :1 -geometry 1920x1080
vncviewer HOST:5901

# Share the existing local display
x11vnc -display :0 -forever -shared

# Stop a TigerVNC display
vncserver -kill :1
```

Viewer tuning on slow links:

```bash
vncviewer -encoding tight -quality 5 HOST:5901
vncviewer -fullscreen HOST:5901
```

### Always-on tunnel pattern

```bash
ssh -L 5901:localhost:5901 user@HOST
vncviewer localhost:5901
```

Port convention: **5900 + display number** (display `:0` → 5900, `:1` → 5901).

## SSH X11 forwarding

**Best for:** one remote GUI application rather than a full desktop.

OpenSSH client flags (see `ssh(1)`):

```bash
# Untrusted X11 forwarding
ssh -X user@HOST app-name

# Trusted X11 forwarding (broader remote X access)
ssh -Y user@HOST app-name

# Enable compression on slow links
ssh -X -C user@HOST app-name
```

Server side requires `X11Forwarding yes` (and typically working `xauth`) in `sshd_config`, then a reload of `sshd`.

### Wayland note

Classic X11 forwarding does not replace a Wayland-native remote path. Practical options:

1. Run the app under XWayland when the toolkit allows (`GDK_BACKEND=x11` for some GTK apps).
2. Prefer VNC/wayvnc for a full desktop.
3. Use [waypipe](https://gitlab.freedesktop.org/mstoeckl/waypipe) for Wayland app forwarding when both sides support it.

SSH connection sharing and TCP forwarding semantics also sit under the SSH architecture in [RFC 4254](https://www.rfc-editor.org/rfc/rfc4254).

## Modern alternatives (not defaults)

| Tool | When to consider |
| --- | --- |
| NoMachine (NX) | LAN performance, existing NX deployments |
| Parsec | Low-latency / media-oriented sessions |
| AnyDesk / Chrome Remote Desktop | Quick cross-platform access with vendor trust trade-offs |
| RustDesk | Self-hosted open path when the user already chose it |

Treat these as explicit product choices. Confirm install source, relay topology, and trust boundary before replacing SSH-tunneled RDP/VNC.

### RustDesk self-host sketch

```bash
docker run -d --name rustdesk-hbbs -p 21115:21115 -p 21116:21116 -p 21116:21116/udp -p 21118:21118 rustdesk/rustdesk-server hbbs
docker run -d --name rustdesk-hbbr -p 21117:21117 -p 21119:21119 rustdesk/rustdesk-server hbbr
```

Verify current image tags and required ports on the upstream project before production use.

## Clipboard, files, audio

| Path | Clipboard | Files | Audio |
| --- | --- | --- | --- |
| FreeRDP | `/clipboard` or `+clipboard` | `/drive:name,/path` | `/sound:sys:alsa` or `pulse` |
| VNC | often needs `vncconfig` on the session | use `scp`/`sftp` alongside | not native — use a separate audio path if required |
| SSH X11 | `xclip` / toolkit clipboard | `scp`/`sftp` | local audio unless separately forwarded |

## Port quick reference

| Service | Common port | Notes |
| --- | --- | --- |
| SSH | 22/tcp | Preferred outer transport for tunnels |
| RDP | 3389/tcp | Keep off public bind when possible |
| VNC | 5900+/tcp | Display offset |
| NoMachine | 4000/tcp | Product-specific |

These are service conventions for diagnosis, not firewall allow-lists. Prefer allowing only SSH (or VPN) from untrusted networks, then forward inwardly.
