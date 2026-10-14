## Docker and applications on NAS

### Architecture awareness

| NAS CPU class | Typical arch | Docker reality |
| --- | --- | --- |
| Intel Celeron / Pentium NAS | x86_64 | Broad image support |
| AMD Ryzen NAS | x86_64 | Broad image support |
| ARM Cortex (many J-series) | arm64/arm | Many images missing or slow |
| Budget Realtek-class | arm | Very limited containers |

**Before buying or promising an app stack:** confirm CPU architecture and
vendor container support (Container Manager, Container Station, etc.).

### Docker networking sketch (Synology-style)

```yaml
# Prefer bridge isolation; bind published ports to a LAN IP when possible
networks:
  nas-apps:
    driver: bridge

ports:
  - "192.168.1.10:8080:80"  # example LAN bind — replace with real host IP
```

Hand deep Compose/publish debugging to the `docker` skill.

### Common traps

1. **Volume ownership** — Map PUID/PGID (or equivalent) to the NAS user that
   owns the share. Do not assume `1000:1000` on every appliance.

2. **Memory limits** — NAS RAM is shared with the OS and scrub/index jobs. Set
   container limits or one runaway app OOMs the box.

3. **Databases on SMB/spinners** — Heavy Postgres/MySQL on SMB-backed or slow
   HDD arrays perform poorly. Prefer SSD/NVMe datasets or external DB hosts;
   SQLite may be acceptable for light apps.

4. **Host path ≠ container path** — Example: host
   `/volume1/docker/appdata/immich` maps explicitly to container `/config` (or
   the app's documented path). Vendor volume roots differ (`/volume1`,
   `/share`, datasets under TrueNAS, etc.).

5. **`:latest` breaks weekends** — Pin image tags/digests for anything you care
   about recovering quickly.

### Resource-friendly app classes

- **Jellyfin / Plex** — Media server; transcode needs CPU/GPU headroom
- **Paperless-ngx** — Document OCR/archive
- **Immich** — Self-hosted photo backup/index
- **Home Assistant** — Smart home (sometimes better on a dedicated SBC)
- **Pi-hole / AdGuard Home** — DNS filtering
- **Nginx Proxy Manager / Caddy** — Reverse proxy with TLS

### Suggested host layout (illustrative)

Use the vendor volume root (examples: Synology `/volume1`, QNAP `/share`,
TrueNAS dataset mount). Do not treat these as skill-package paths.

```text
<nas_volume>/docker/
├── appdata/      # container config (prefer SSD/NVMe when available)
├── media/        # shared library binds
└── downloads/    # scratch / incomplete
```

Keep busy container configs off pure spinning parity arrays when the hardware
allows a faster pool or cache.
