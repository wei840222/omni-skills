# Sync sources (Gate 6)

Checked 2026-10-02. Re-open the live page before restating flag defaults, backend limits, or product behavior.

## rsync

- **rsync man page (Debian bookworm)** — trailing-slash semantics, `--archive`/`-a`, `--delete` family, `--checksum`, `--dry-run`, `--partial` / `-P`.
  - https://manpages.debian.org/bookworm/rsync/rsync.1.en.html
- **rsync man page (samba.org publication)** — upstream-published manual text for cross-check.
  - https://download.samba.org/pub/rsync/rsync.1
- **rsync NEWS** — release notes when flag behavior may have changed across versions.
  - https://download.samba.org/pub/rsync/NEWS

## rclone

- **rclone documentation hub** — command index and global flags.
  - https://rclone.org/docs/
- **rclone sync** — destination made identical to source; includes deletes; dry-run warning.
  - https://rclone.org/commands/rclone_sync/
- **rclone copy** — copy without deleting destination extras.
  - https://rclone.org/commands/rclone_copy/
- **rclone check** — compare sizes/hashes between source and dest.
  - https://rclone.org/commands/rclone_check/
- **rclone S3** — S3-compatible backend options including chunked uploads.
  - https://rclone.org/s3/
- **rclone filtering** — include/exclude filter language (not identical to rsync patterns).
  - https://rclone.org/filtering/

## Bidirectional

- **Unison project page (UPenn)** — bidirectional user-level file synchronization overview.
  - https://www.cis.upenn.edu/~bcpierce/unison/
- **Unison man page (Debian bookworm)** — CLI flags including conflict-related options.
  - https://manpages.debian.org/bookworm/unison/unison.1.en.html
- **Unison GitHub mirror** — upstream repository entry point.
  - https://github.com/bcpierce00/unison

## Skill format authority

- **Agent Skills specification** — package format and progressive-disclosure expectations.
  - https://agentskills.io/specification
- **agentskills / skills-ref** — reference validator used by this repository.
  - https://github.com/agentskills/agentskills/tree/main/skills-ref

## What this skill does not treat as live measurement

Cloud egress pricing, provider-specific rate limits, and exact S3 multipart defaults change often — read the provider/rclone page for the active version. Mount health, disk free space, and SSH reachability must be observed on the live host. This skill’s command shapes are operational starting points, not a substitute for dry-run output on the real trees.
