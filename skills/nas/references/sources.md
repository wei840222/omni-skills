# Sources (Gate 6)

Full URLs checked while refactoring this skill (2026-10-14). Re-verify before
restating product defaults, pricing, or UI labels.

## Agent skill format

- Agent Skills specification: https://agentskills.io/specification
- Agent Skills llms.txt: https://agentskills.io/llms.txt
- skills-ref validator: https://github.com/agentskills/agentskills/tree/main/skills-ref

## Backup and 3-2-1

- Backblaze — "The 3-2-1 Backup Strategy" (industry-popular restatement of
  multi-copy backup practice):
  https://www.backblaze.com/blog/the-3-2-1-backup-strategy/
  Takeaways: three copies, two media types, one off-site; RAID is not a
  substitute for backup; test restores.
- United States CISA — Data Backup Options (PDF):
  https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf
  Takeaways: regular backups, offline/off-site copies, and restore testing
  reduce ransomware and disaster impact.
- CISA StopRansomware hub:
  https://www.cisa.gov/stopransomware
  Takeaways: backups are part of ransomware resilience; keep offline/immutable
  copies where practical.

## Object storage / off-site (pricing changes — verify live)

- Backblaze B2 Cloud Storage product page:
  https://www.backblaze.com/cloud-storage
  Use only for product existence and current published pricing; do not hardcode
  stale $/TB figures into answers without re-check.
- Amazon S3 documentation home:
  https://docs.aws.amazon.com/s3/
  S3-compatible off-site patterns; lifecycle and encryption are operator choices.

## Remote access and exposure

- Tailscale product documentation:
  https://tailscale.com/kb/
  Overlay VPN without inbound port forward is a common NAS remote-access pattern.
- WireGuard official site:
  https://www.wireguard.com/
  Modern VPN protocol commonly self-hosted on NAS or edge router.
- Cloudflare Tunnel documentation:
  https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/
  Outbound tunnel alternative to WAN port forward for selected HTTP apps.

## Vendor NAS documentation (platform-specific detail)

- Synology DSM documentation portal:
  https://kb.synology.com/
- QNAP documentation:
  https://www.qnap.com/en/how-to/
- TrueNAS documentation:
  https://www.truenas.com/docs/
- Unraid documentation:
  https://docs.unraid.net/

## Media stack

- Jellyfin documentation:
  https://jellyfin.org/docs/
- Plex support articles:
  https://support.plex.tv/
- Immich documentation:
  https://immich.app/docs

## Containers on limited hosts

- Docker documentation — volumes and bind mounts:
  https://docs.docker.com/engine/storage/bind-mounts/
- Docker multi-arch / platform considerations:
  https://docs.docker.com/build/building/multi-platform/
