---
name: sync
description: >
  Synchronize files and directories with rsync, rclone, or Unison across local
  disks, SSH remotes, and cloud object storage. Use when the user needs dry-run
  first transfers, trailing-slash-safe copies, --delete mirror decisions,
  exclude-from ignore files, SSH/rsync resume, rclone sync vs copy, checksum
  verification, or true bidirectional sync. Prefer `backups` for retention and
  restore drills, `cloud-storage` for multi-provider browse/cost ops, and
  `storage` for capacity planning outside a live transfer.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔄","requires":{"anyBins":["rsync","rclone"]},"os":["linux","darwin","win32"],"displayName":"Sync"}'
  related-skills: '{"backups":"Versioned/immutable backup and restore design when the need is recovery, not live mirroring.","cloud-storage":"Multi-provider cloud file ops, auth, and egress-cost checks once destinations are chosen.","storage":"Capacity and media planning outside a concrete transfer command.","files":"Local filesystem inspection and path hygiene before constructing sync commands.","linux":"Host paths, mounts, permissions, and SSH quirks that affect remote rsync.","s3":"S3 bucket, Object Lock, and key-layout details when the destination is object storage."}'
---

# Sync

Operational skill for **one-way and bidirectional file synchronization**. Keep credentials out of the package; inject cloud remotes and SSH keys at runtime.

## When to load

Load for transfer work:

- local folder mirror with `rsync -avz` and optional `--delete`
- remote-over-SSH rsync with key auth, non-default ports, or resume (`--partial`)
- cloud object sync/copy with `rclone` (`sync` vs `copy`, progress, S3 chunk size)
- exclude lists, checksum verification, audit logs
- true bidirectional needs (`unison`) when both sides may change

Prefer other skills when the ask is mainly:

- retention, immutability, restore drills → `backups`
- multi-cloud browse, sharing models, egress estimates → `cloud-storage`
- pure capacity / durability class → `storage`

## State location

Optional ignore files and audit logs may live under `<workspace>/sync/`, `<workspace>/memory/sync/`, or `~/sync/`. `<workspace>` is the host/runtime workspace root, never the shell cwd.

Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/sync/`, `<workspace>/memory/sync/`, `~/sync/`.
3. If none exists and persistent state must be created, default to `<workspace>/sync/` only with brief first-write consent.
4. When more than one candidate exists, use only the highest-precedence path, report the conflict, and leave other copies unchanged.

Use only the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Keep cloud tokens, SSH private keys, and live credentials **out of git** and out of the skill package.

```text
<state_root>/
|-- .syncignore     # exclude patterns (optional)
|-- sync.log        # audit trail from rsync/rclone runs (optional)
`-- remotes.md      # non-secret remote names and notes only (optional)
```

## Routing

Keep this file as the router (progressive disclosure); load depth only when needed:

- **Exclusions, cloud flags, verification, bidirectional, remote SSH, pitfalls** → `references/sync-rules.md`
- **Gate 6 primary sources** → `references/sources.md`

## Execution routine

1. **Scope** — Identify source, destination, direction (one-way vs bidirectional), and whether deletes are required.
2. **Safety preflight** — Confirm mounts exist, paths are correct, and trailing slashes match intent. Prefer `--dry-run` / `rclone ... --dry-run` before any destructive or `--delete` run.
3. **Tool choice** — `rsync` for POSIX/SSH trees; `rclone` for cloud/object remotes; `unison` only for true bidirectional updates.
4. **Draft command** — Apply baseline flags, excludes via `<state_root>/.syncignore` when useful, and progress/resume options.
5. **Execute and verify** — Run the transfer; verify with checksum/`rclone check` or spot size/count; append logs to `<state_root>/sync.log` when audit is requested.
6. **Report** — Summarize what changed, deletes performed or skipped, and residual risk (for example same-disk “backup”).

## Core operations

### 1. Trailing slash is part of the path contract

- `rsync src/ dest/` copies **contents** of `src` into `dest`.
- `rsync src dest/` copies the **directory node** `src` as a child of `dest`.
- `rclone` treats `source:path` as “contents of that path” when the path is a directory — do not assume rsync slash rules map 1:1; confirm with a dry-run listing.

### 2. Baseline one-way rsync

Default local or SSH shape:

```bash
rsync -avz --info=progress2 --dry-run SRC/ DEST/
# after dry-run review:
rsync -avz --info=progress2 SRC/ DEST/
```

- `-a` archive (permissions/times/links as documented for the platform)
- `-v` verbose, `-z` compress in flight
- Add `--delete` **only** when destination must exactly mirror source
- Add `--checksum` when clocks skew or size/time is untrusted
- Remote example: `rsync -avz -e "ssh -i ~/.ssh/key -p 22" SRC/ user@host:DEST/`

### 3. Cloud: prefer copy until delete intent is explicit

- `rclone copy` adds/updates without deleting extras on the destination.
- `rclone sync` makes destination match source **including deletes**. Official docs warn this can cause data loss — always dry-run first.
- Useful extras for large object stores: `-P` / `--progress`, `--fast-list` when appropriate, `--s3-chunk-size 64M`, tuned `--transfers`.
- Verify with `rclone check source: dest:` (hashes/sizes per remote capabilities).

### 4. Excludes and audit

- Prefer `--exclude-from=<state_root>/.syncignore` over long ad-hoc flag lists.
- Common code excludes: `.git/`, `node_modules/`, `__pycache__/`, `.venv/`, `*.pyc`, `.DS_Store`, `Thumbs.db`.
- Patterns are relative to the source root; leading `/` anchors to top-level only.
- Log when asked: `rsync ... | tee -a <state_root>/sync.log`.

### 5. Bidirectional is not rsync

rsync is one-way. When both sides may change, use **Unison** (`unison dir1 dir2`), resolve conflicts deliberately (`-auto` only for non-conflicts; `-prefer` / `-copyonconflict` with care). Native bidirectional services (Syncthing, Dropbox-class tools) beat hand-rolled dual rsync.

### 6. Safety boundaries

- Verify the mount or remote is still present before writing into a path that used to be a mountpoint.
- Double-check source vs destination before `--delete` or `rclone sync`.
- `rsync --delete` / cloud sync is **mirroring**, not a versioned backup — route recovery requirements to `backups`.
- Never embed cloud credentials in scripts committed to the skill tree; configure remotes interactively or via host secrets (`rclone config`, env, or secret store).

## Quick command cheatsheet

| Intent | Starting point |
| ------ | -------------- |
| Local mirror preview | `rsync -avz --info=progress2 --dry-run SRC/ DEST/` |
| Exact mirror | add `--delete` only after dry-run sign-off |
| Resume large SSH copy | `rsync -avz --partial --progress -e "ssh -i KEY" SRC/ user@host:DEST/` |
| Cloud add/update only | `rclone copy SRC remote:path -P --dry-run` then drop `--dry-run` |
| Cloud exact sync | `rclone sync SRC remote:path -P --dry-run` then drop `--dry-run` |
| Cloud verify | `rclone check SRC remote:path` |
| Bidirectional | `unison DIR1 DIR2` |

## Failure recovery

| Symptom | Action |
| ------- | ------ |
| Wrong tree layout after copy | Re-check trailing slashes; dry-run a corrective rsync; do not `--delete` until listing matches intent |
| Partial transfer / dropped SSH | Re-run with `--partial` / `-P`; confirm free space on destination |
| Deletes surprised the user | Stop; restore from versioned backup if available; re-run without `--delete` / switch to `rclone copy` |
| Clock-skew false skips | Use `--checksum` or align NTP, then re-run |
| Mount vanished mid-job | Abort; fix mount; ensure destination is not a leftover empty directory with the mount name |
