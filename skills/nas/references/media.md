## Media server and photo layout

### Folder structure for Plex / Jellyfin

Paths are **on the NAS volume**, not inside this skill package. Replace
`<nas_volume>` with the live share root (for example `/volume1`).

```text
<nas_volume>/media/
├── movies/
│   └── Movie Name (2024)/
│       ├── Movie Name (2024).mkv
│       └── Movie Name (2024).srt
├── tv/
│   └── Show Name/
│       └── Season 01/
│           └── Show Name - S01E01 - Title.mkv
├── music/
│   └── Artist/
│       └── Album (Year)/
│           └── 01 - Track.flac
└── photos/
    └── 2024/
        └── 2024-06-15 Event Name/
```

### Common traps

1. **Wrong naming breaks metadata matchers** — Follow scanner conventions or
   expect manual matching.

2. **Mixed libraries confuse agents** — Keep movies and TV under separate roots.

3. **Transcoding melts weak CPUs** — Low-power Celeron/ARM units struggle with
   4K HEVC transcode. Prefer direct play or hardware transcode (Quick Sync /
   vendor GPU options) when available.

4. **First photo index is slow** — Tens of thousands of photos can take days on
   first Immich/Synology Photos pass; let it finish before declaring failure.

5. **Native NAS photo AI is often mediocre** — Face/object features vary; Immich
   is a common self-hosted alternative when users want stronger photo workflows.

### Hardware transcoding (planning)

| Need | Practical approach |
| --- | --- |
| 4K HEVC | Intel Quick Sync class NAS, capable clients, or accept direct-play-only |
| Many concurrent streams | Stronger CPU/GPU or fewer transcodes |
| Budget ARM NAS | Direct play clients (Infuse, Kodi, Shield, etc.) |

### Photo workflow sketch

```text
Phone  → auto-upload (Immich / vendor photos app)
Camera → import under photos/YYYY/
RAW    → separate photos-raw/ tree when masters must stay lossless
```

### Storage planning (order-of-magnitude)

| Content | Per-item ballpark | Example library |
| --- | --- | --- |
| 1080p movie | ~5–15 GB | 500 titles ≈ several TB |
| 4K movie | ~20–80 GB | 100 titles ≈ several TB |
| TV episode | ~1–4 GB | Large series libraries add TB quickly |
| Photo RAW | ~25–50 MB | 10k photos ≈ hundreds of GB |
| FLAC album | ~300–600 MB | Hundreds of albums ≈ tens–hundreds of GB |

Plan headroom (often ~2× current library) and re-check encoder/bitrate assumptions
against the user's actual files.
