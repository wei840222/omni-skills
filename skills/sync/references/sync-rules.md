# Detailed synchronization rules

Load this file for complex exclusions, cloud object transfers, verification, bidirectional sync, SSH remotes, or pitfall review. Keep secrets out of commands logged to chat when possible.

## Exclusions

- Prefer an exclude file: `rsync -avz --exclude-from=<state_root>/.syncignore SRC/ DEST/`
- Standard code-project excludes: `.git/`, `node_modules/`, `__pycache__/`, `.venv/`, `*.pyc`, `.DS_Store`, `Thumbs.db`
- Patterns are relative to the source root — `/logs/` excludes only top-level `logs`; `logs/` excludes `logs` directories anywhere under the tree
- `rclone` filtering uses its own filter language; see official filtering docs before translating rsync patterns 1:1
- Excluded paths are not deleted on the destination unless an explicit delete-excluded mode is enabled for that tool

## Cloud storage (rclone)

- `rclone sync` makes the destination match the source and **can delete** destination files that are gone from the source. Official guidance: test with `--dry-run` first
- `rclone copy` only adds/updates — prefer it when delete intent is unclear
- Configure remotes with `rclone config` or host-provided secrets; never commit access keys into the skill package
- Progress: `-P` / `--progress`
- Large S3-compatible objects: consider `--s3-chunk-size 64M` (confirm against current rclone S3 docs for the provider)
- Listing performance: `--fast-list` can reduce API chatter on some remotes; validate cost/compatibility per backend
- Parallelism: raise `--transfers` only after watching API rate limits and bandwidth
- Destination identity: wrong region/endpoint or remote name is a common silent mis-route — dry-run listings first

## Verification

- rsync checksum mode: `rsync -avzc` (or `--checksum`) compares checksums instead of size/modtime — slower, stronger against clock skew
- rclone: `rclone check source: dest:` compares sizes/hashes when the backends support them; `--size-only` is a faster weaker check
- Spot-check large jobs with file counts, sampled checksums, and free-space reports
- Audit: `rsync -avz SRC/ DEST/ | tee -a <state_root>/sync.log` or rclone log flags when the operator needs a trail

## Bidirectional sync

- rsync remains one-way even if run twice; two opposing rsync jobs do **not** equal safe bidirectional merge
- Unison (`unison dir1 dir2`) detects updates on both sides and surfaces conflicts
- Use Unison non-conflict automation carefully; prefer explicit conflict resolution over blind `-prefer` on production trees
- For continuous multi-device sync, prefer purpose-built tools (for example Syncthing) over custom dual-rsync cron

## Remote sync (SSH)

- Key-based auth: `rsync -avz -e "ssh -i ~/.ssh/key -o IdentitiesOnly=yes" SRC/ user@host:DEST/`
- Non-default port: `-e "ssh -p 2222"`
- Large/unreliable links: `--partial` and/or `-P` (`--partial --progress`) to keep partials and show progress
- Confirm remote disk space and path permissions before `--delete`
- Do not pass private key material into chat logs; reference key paths only

## Common pitfalls

- Writing into a path that used to be a mountpoint after the mount silently dropped creates a local directory with the mount name — verify mounts first
- Repeated sync **without** `--delete` accumulates deleted source files on the destination forever (may be desired or not — decide explicitly)
- Time-based skip with skewed clocks misses updates — use `--checksum` or fix time sync
- `rsync --delete` / `rclone sync` mirrors ransomware-encrypted or wiped trees just as faithfully as good data — this is not a backup
- Trailing-slash mistakes invert “contents vs directory node” layout; always dry-run after path edits
- Mixing `cloud-storage` cost/auth concerns: for bulk cloud egress estimates and provider auth traps, load `cloud-storage` instead of reinventing pricing tables here

## Positive operating defaults

- Dry-run before first destructive or delete-enabled command
- State excludes and logs under the resolved `<state_root>`
- Prefer `copy` until the user explicitly wants destination extras removed
- After critical jobs, verify before declaring success
- Route versioned recovery requirements to the `backups` skill
