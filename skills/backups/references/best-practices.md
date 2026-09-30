# Backup best practices and failure traps

Load when designing policy, choosing tools, or reviewing an existing backup estate.

## The only rule that matters

- Untested backups are not backups — schedule regular restore tests alongside backup jobs.
- Test restores to different hardware or a clean location — validates both backup and restore procedure.
- Time the restore — know recovery duration before an incident, not during one.

## 3-2-1-1-0 strategy

Modern threats favor **3-2-1-1-0**:

- **3** copies of data (production + 2 backups)
- **2** different media types or storage technologies
- **1** offsite copy
- **1** offline, air-gapped, or immutable copy (ransomware-critical)
- **0** errors verified through restore testing

Classic **3-2-1** remains useful vocabulary; add immutability/offline and verified-zero-error when ransomware or silent corruption is in scope.

## 3-2-1 rule violations

- Same disk as source data — disk failure loses both.
- Same server as source — ransomware, fire, or theft can take both.
- Same cloud account without strong separation — account compromise or provider issue can hit both.
- Cloud sync (Dropbox, Drive, similar) is not backup — it syncs deletions and corruption.

## Ransomware protection

- Backups reachable with production credentials often get encrypted too — require air gap or immutable storage.
- Append-only / immutable storage resists deletion — for example S3 Object Lock, retention-locked object stores.
- Offline rotation (USB, tape, disconnected media) for critical sets — keep offsite media disconnected.
- Test restoring from the immutable tier — prove ransomware cannot rewrite the recovery path.

## Database backup traps

- File copy of a running database often yields a corrupted image — use engine-native exporters (`pg_dump`, `mysqldump`, `mongodump`) or supported physical methods.
- Point-in-time recovery needs WAL/binlog (or equivalent) archiving — a dump alone loses recent transactions.
- Large PostgreSQL: long `pg_dump` locks or load may be unacceptable — consider `pg_basebackup` and continuous archiving.
- Always test restore on a different server — proves the backup is self-contained.

## Incremental backup pitfalls

- Incrementals depend on the chain — one broken link can invalidate later restores.
- Long chains slow restores — schedule periodic full backups.
- Deduplication saves space but concentrates risk — repository corruption can affect many snapshots.
- Verify integrity regularly — bit rot and partial writes happen; checksums catch them.

## Retention mistakes

- No retention policy fills storage — define and automate cleanup.
- Over-aggressive retention cannot recover old latent corruption — keep monthly tiers for at least a year when feasible.
- Legal/compliance may mandate longer retention — check before shortening policy.
- Grandfather-father-son style tiers (daily/weekly/monthly) remain a practical pattern.

## Filesystem traps

- Permissions and ownership are easy to lose — verify restore preserves them or document expected state.
- Symlink behavior differs by tool (follow vs copy link) — test explicitly.
- Sparse files may inflate in some formats.
- Extended attributes and ACLs are not universally preserved — confirm tool flags.

## Cloud and remote

- Encrypt before upload when provider breach must not expose plaintext.
- Bandwidth and first-seed cost matter — physical seed is sometimes rational for large datasets.
- Region placement matters for disaster recovery — same region as production does not survive regional outage.
- Egress fees can dominate restore cost — estimate before emergency.

## Tool-specific notes

- `rsync --delete` on the wrong direction destroys the intended source — double-check paths every time.
- `restic` / `borg` repository passwords are single points of failure — store in a password manager; loss means permanent lockout.
- Uncompressed tarballs trade CPU for size — choose deliberately.
- Snapshots (LVM, ZFS, cloud) share the production failure domain — treat as operational rollback, not the sole offsite backup.

## Documentation

- Write the restore procedure for stressed operators, not for the author on a calm day.
- Store the procedure outside the backup repository (printout, alternate host, password manager).
- Include identities, paths, approval steps, and expected duration.

## Related sources

Canonical URLs and verification notes live in `references/sources.md`.
