# Troubleshooting — Remote Desktop

Work top-down: **reachability → auth → session/display → extras (clipboard/audio) → performance**.

## Connection refused or timeout

**Checks on the target (authorized shell):**

```bash
ss -tlnp | grep -E '3389|5900|5901|22'
sudo ufw status
sudo iptables -L -n | grep -E '3389|5900|5901'
```

**Fixes:**

- Start the service (Windows Remote Desktop setting; `vncserver :1`; ensure `sshd` is up).
- Open the port only on the intended interface, or keep it localhost-only and use SSH.
- Confirm client is aiming at the forwarded local port when a tunnel is in use.

```bash
sudo ufw allow 22/tcp          # preferred outer path
# Only if a deliberate direct lab listener is required:
sudo ufw allow from 192.168.1.0/24 to any port 3389 proto tcp
```

## VNC black / blank screen

**Likely causes:** no desktop session, wrong display, display-manager conflict.

```bash
ls /tmp/.X11-unix/
vncserver :1 -geometry 1920x1080
x11vnc -display :0 -auth guess
```

Try display `:1` when `:0` is the local seat. Confirm the viewer port matches **5900 + display**.

## RDP connects then drops

**Likely causes:** NLA mismatch, certificate prompt loop, existing interactive session policy.

```bash
xfreerdp /v:HOST /u:USER /sec:nla
xfreerdp /v:HOST /u:USER /sec:tls
xfreerdp /v:HOST /u:USER /sec:rdp
xfreerdp /v:HOST /u:USER /sec:nla /cert:ignore   # lab hosts only
xfreerdp /v:HOST /u:USER /admin                  # console takeover when authorized
```

If the drop happens only across the internet, rebuild with an SSH tunnel to rule out middleboxes interfering with bare 3389.

## X11 forwarding failures

**Symptom:** `Can't open display` or silent no-window.

Server:

```bash
# sshd_config
X11Forwarding yes
# then: sudo systemctl restart sshd   # or equivalent
which xauth || sudo apt install xauth
```

Client:

```bash
ssh -X user@HOST 'echo $DISPLAY && xclock'
ssh -vvv -X user@HOST xclock 2>&1 | grep -i x11
```

`DISPLAY` should look like `localhost:10.0` (offset may vary). Prefer `-X` first; use `-Y` only when the app needs trusted X11.

## Slow performance

**VNC:**

```bash
vncviewer -encoding tight -quality 3 HOST:1
vncviewer -depth 8 HOST:1
```

**RDP:**

```bash
xfreerdp /v:HOST /u:USER /bpp:16 /network:modem -themes -wallpaper
```

**X11:**

```bash
ssh -X -C user@HOST app-name
```

Also verify the path is not hairpinning through an unintended VPN or congested jumphost.

## Clipboard not syncing

- **RDP:** pass `/clipboard` or `+clipboard`; on Windows confirm `rdpclip` is running in the session.
- **VNC:** run `vncconfig &` inside the remote session when the server expects it.
- **X11:** install/use `xclip` (or toolkit clipboard) on both ends as needed.

## Audio missing

**RDP:**

```bash
xfreerdp /v:HOST /u:USER /sound:sys:alsa
xfreerdp /v:HOST /u:USER /sound:sys:pulse
```

**VNC:** native RFB does not define remote audio. Use a separate agreed audio path, or switch to a product that bundles audio, rather than assuming VNC will carry it.

## NAT / firewall traversal

**Local forward via jumphost:**

```bash
ssh -L 3389:windows-pc:3389 user@jumphost
xfreerdp /v:localhost /u:USER
```

**Reverse forward (target initiates):**

```bash
# on target behind NAT
ssh -R 13389:localhost:3389 user@reachable-server
# on reachable-server
xfreerdp /v:localhost:13389 /u:USER
```

When the real need is a persistent encrypted path for all traffic, hand off to `vpn` rather than stacking ad-hoc reverse forwards.

## Decision order cheat sheet

1. Does `ss` show the expected listener on the expected interface?
2. Does a tunnel to `localhost` work while direct remote fails? → path/firewall issue.
3. Does auth fail fast? → NLA/password/key/cert before display tuning.
4. Does the session connect with a black screen? → display/session, not TCP.
5. Are only extras broken (clipboard/audio/drive)? → enable explicit redirects last.
