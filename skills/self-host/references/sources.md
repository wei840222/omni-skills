# Sources — self-host

Gate 6 research anchors for self-hosting operations. Prefer primary vendor and project docs over listicles. Re-verify UI paths, default ports, and ACME flows before quoting exact clicks.

## Docker and Compose

- [Docker Engine — volumes](https://docs.docker.com/engine/storage/volumes/) — named volumes vs bind mounts and data durability.
- [Docker Compose — restart policies](https://docs.docker.com/reference/compose-file/services/#restart) — `no`, `always`, `on-failure`, `unless-stopped`.
- [Docker Compose — networking](https://docs.docker.com/compose/networking/) — project networks and service DNS.
- [Docker logging drivers](https://docs.docker.com/engine/logging/configure/) — log rotation and max-size options to prevent disk fill.

## Reverse proxy and TLS

- [Caddy — automatic HTTPS](https://caddyserver.com/docs/automatic-https) — ACME defaults and on-demand TLS caveats.
- [Traefik — Docker provider / routers](https://doc.traefik.io/traefik/routing/providers/docker/) — labels, entrypoints, and service ports.
- [Let's Encrypt — challenge types](https://letsencrypt.org/docs/challenge-types/) — HTTP-01 vs DNS-01 selection for LAN/home setups.

## Security and access

- [CIS Docker Benchmark (overview)](https://www.cisecurity.org/benchmark/docker) — host and container hardening baseline categories (use current edition).
- [WireGuard quick start](https://www.wireguard.com/quickstart/) — VPN alternative to broad port forwarding.
- [Tailscale — subnet routers / exit nodes docs](https://tailscale.com/kb/) — zero-config remote admin patterns (verify current KB article for the exact feature used).

## Backups and reliability

- [3-2-1 backup rule (industry practice summary via US-CERT / CISA continuity guidance)](https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf) — multiple copies and offsite considerations; adapt to home-lab scale.
- Project-specific volume backup docs for the chosen engine (Docker volume backup utilities, restic, borg) — always confirm restore flags against current upstream README.

## Monitoring

- [Uptime Kuma documentation](https://github.com/louislam/uptime-kuma/wiki) — self-hosted uptime checks (verify wiki pages for current setup).
- [Prometheus documentation](https://prometheus.io/docs/introduction/overview/) — metrics-based resource monitoring when the stack warrants it.

## Practice notes for this skill

- Defaults in `self-host-rules.md` (pin tags, private DB ports, restore drills) are operational starting points, not compliance certifications.
- Prefer `docker`, `caddy`, `traefik`, `sysadmin`, `home-server`, and `backups` skills for deep product-specific procedures.
- Obsolete packaging removed in this refactor: Clawic homepage, top-level `slug`/`homepage`/`version`, clawdbot metadata block, and `_meta.json`.
