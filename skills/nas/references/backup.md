## Backup strategy

### 3-2-1 implementation sketch

```text
Primary copy: NAS pool (RAID/mirror protected)
Second copy: External USB or second NAS (rotated or continuous)
Third copy: Off-site object storage or cold drive (encrypted)
```

### Common traps

1. **Sync is not backup** — Bidirectional sync propagates deletes and ransomware
   encryption. Prefer versioned backup jobs with retention.

2. **Cloud-only is fragile** — Provider outage, account lock, or bad sync still
   needs a local recoverable copy for irreplaceable data.

3. **Encrypt before untrusted off-site** — Client-side or NAS-side encryption
   (Hyper Backup encryption, restic/borg, Cryptomator, and similar) before
   upload. Do not treat provider-side encryption alone as complete threat cover.

4. **Test restore quarterly** — Restore random files to a different path and
   verify content, not only job status LEDs.

5. **Retention must match legal and personal needs** — Example starting point
   for personal archives: ~30 daily, ~12 monthly, multi-year annual for
   irreplaceable sets. Adjust to policy; do not invent compliance claims.

### Priority when space is limited

1. **Irreplaceable** — Photos, documents, creative masters
2. **Expensive to recreate** — VMs, configs, databases
3. **Convenient** — Media libraries that can be re-ripped or re-downloaded

### Verification cadence

| Cadence | Action |
| --- | --- |
| Monthly | Read backup job logs and failure alerts |
| Quarterly | Restore at least five random files to another path |
| Annually | Full disaster-recovery drill (new host or empty volume) |

### Off-site options (illustrative)

| Option | Typical tradeoff | Recovery speed |
| --- | --- | --- |
| Object storage (B2/S3-compatible) | Ongoing $/TB; good automation | Hours–days |
| Encrypted external drive off-site | Low recurring cost; manual rotation | Hours |
| Second NAS at another site | Higher upfront | Fast on LAN/VPN |
| Safety-deposit rotation | Low tech; slow logistics | Slow |

Re-check current vendor pricing and APIs via `references/sources.md` before
quoting dollar figures as facts.
