## Scope

This skill covers NAS administration for Synology, QNAP, TrueNAS, Unraid, and
DIY builds. Enterprise SAN and large distributed object clusters are out of
scope; hand those to specialized infrastructure skills.

## Critical rules

1. **RAID provides hardware redundancy; backup requires separate copies** —
   RAID protects against drive failure. Ransomware, fire, theft, and accidental
   deletion still need independent backups, preferably with one off-site copy.

2. **3-2-1 backup rule is the minimum** — Three copies, two different media
   types, one off-site. Versioned cloud backup to object storage (for example
   B2 or S3-compatible) can satisfy the off-site leg when encrypted and tested.

3. **Match share protocols to clients** — SMB for Windows/macOS, NFS for Linux.
   AFP is legacy. Enable only protocols you actually use to shrink attack and
   permission surface.

4. **Expose zero admin ports to the internet** — Keep DSM/QTS/TrueNAS UI off
   public IP. Prefer Tailscale, WireGuard, or an authenticated reverse
   tunnel/proxy.

5. **Test restores on a schedule** — Quarterly restore of sample files; annual
   disaster drill. Logs that say "success" are not integrity proof.

6. **Disable or rename default admin** — Create named admin accounts. Default
   `admin` is a common brute-force target.

7. **UPS with clean shutdown** — Unexpected power loss during write risks pool
   corruption. Budget for signaling shutdown, not only runtime minutes.

8. **Snapshots ≠ off-site backup** — Snapshots give local versioning on the same
   disks and failure domain. They help accidental delete; they do not replace
   disaster recovery copies.

9. **Quote true usable capacity** — Subtract RAID parity/mirror overhead,
   reserved space, and filesystem metadata. Four 8 TB drives are not 32 TB
   usable.

10. **ARM NAS limits Docker** — Many Synology J-series and low-end QNAP units
    are ARM. Confirm image architecture before purchase or deploy.
