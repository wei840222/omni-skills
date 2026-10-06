# Sources — Remote Desktop

Dated research notes for Gate 6. Re-open the live URL before restating version-specific flags or policy.

## Agent Skills format

- **Agent Skills specification** — frontmatter, progressive disclosure, optional directories, file references — https://agentskills.io/specification
- **Agent Skills document index** — https://agentskills.io/llms.txt
- **skills-ref / agentskills validator** — reference validation tooling — https://github.com/agentskills/agentskills/tree/main/skills-ref

## RDP / FreeRDP

- **Debian `xfreerdp(1)` (freerdp2-x11, bookworm)** — `/v:`, `/u:`, `/p:`, `/size:`, `/dynamic-resolution`, `/clipboard`, `/drive:`, `/cert:` client syntax — https://manpages.debian.org/bookworm/freerdp2-x11/xfreerdp.1.en.html
- **Debian `xfreerdp3` manpage (testing/freerdp3-x11)** — FreeRDP 3 client manpage presence for package naming checks — https://manpages.debian.org/testing/freerdp3-x11/xfreerdp3.1.en.html
- **FreeRDP project site** — upstream project home — https://www.freerdp.com/
- **FreeRDP CommandLineInterface wiki** — additional CLI orientation — https://github.com/FreeRDP/FreeRDP/wiki/CommandLineInterface
- **Microsoft Learn: Remote Desktop clients** — vendor client family overview (URL may redirect within Learn) — https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients

## VNC / RFB

- **RFC 6143 — The Remote Framebuffer Protocol** — normative RFB/VNC protocol — https://www.rfc-editor.org/rfc/rfc6143
- **TigerVNC project** — common open VNC server/viewer family — https://tigervnc.org/
- **TigerVNC GitHub** — issue/release tracking — https://github.com/TigerVNC/tigervnc
- **LibVNC/x11vnc** — share an existing X display — https://github.com/LibVNC/x11vnc

## SSH, X11, Wayland

- **OpenBSD `ssh(1)`** — `-X`, `-Y`, `-C`, `-L`, `-R`, X11 forwarding flags — https://man.openbsd.org/ssh.1
- **RFC 4254 — SSH Connection Protocol** — channels and TCP forwarding architecture — https://www.rfc-editor.org/rfc/rfc4254
- **waypipe (freedesktop GitLab)** — Wayland session forwarding helper — https://gitlab.freedesktop.org/mstoeckl/waypipe

## Research dispositions applied in this refactor

| Claim area | Disposition |
| --- | --- |
| FreeRDP `/v:/u:/size:/dynamic-resolution:/clipboard:/drive:/cert:` | Retained; confirmed on Debian freerdp2 manpage |
| `/sec:nla|tls|rdp` recovery order | Retained as practical recovery; confirm against the installed FreeRDP build when behavior differs |
| VNC weak native security → SSH tunnel | Strengthened with RFC 6143 citation and explicit tunnel-first guidance |
| Default ports 3389 / 5900+display / 22 | Retained as conventions, labeled non-allow-list |
| Wayland + X11 forward limitation | Retained; waypipe pointed at live freedesktop GitLab project |
| Vendor catalog homepage / star-feedback URLs | Removed (Gate 5) |
| Password examples in saved profiles | Removed; keyring/agent guidance replaces plaintext `/p:` in templates |
