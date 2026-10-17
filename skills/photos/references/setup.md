# Remote Libraries and Environment Setup

Load for NAS mounts, latency, and vendor thumbnail directories.

## Prerequisites

- `exiftool` on `PATH` (required by `metadata.openclaw.requires.bins`).
- Optional: `sips` (macOS) or `heif-convert` (libheif) for HEIC conversion.
- Optional vision/face tooling provided by the host — this skill caches results
  but does not ship models.

## NAS / remote mounts

- Work on the mounted path; expect network latency on Synology/QNAP/SMB.
- Probe before bulk work: `ls /Volumes/photos | head -1` (or the user path).
- On slow links, keep a local index cache under `<state_root>/.photo-index/` and
  sync periodically rather than re-walking the mount every query.
- Skip vendor noise while indexing:
  - Synology `@eaDir` thumbnail/EA directories
  - macOS `.DS_Store`
- Prefer VPN/mounted paths already authorized by the user; do not invent new
  remote credentials.
