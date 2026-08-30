# Disk-Full Triage

Run in this order and stop at the first one that explains the gap. Detail and the safe reclaim order live in `disk-space.md`.

| # | Check | Catches |
|---|---|---|
| 1 | `df -hT` | Which filesystem is actually full — the error names a path, not a device |
| 2 | `df -i` | Inode exhaustion: "No space left on device" with free space showing |
| 3 | `lsof +L1` | Deleted files still held open — `rm` freed nothing |
| 4 | `mount --bind / /mnt && du -xh --max-depth=1 /mnt` | Files shadowed under a mount point, invisible to every `du` |
| 5 | `tune2fs -l <dev> \| grep -i 'reserved block'` | The ext4 5% root reserve — 50 GB on a 1 TB volume, "full" for users |
| 6 | `lvs -o +snap_percent`, `zfs list -t snapshot`, cloud snapshots | Deleted data kept alive by a snapshot |
| else | `du -xh --max-depth=1 / \| sort -h \| tail` | Ordinary growth — descend into the winner |
