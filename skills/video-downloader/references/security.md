# Security & Privacy

**Data that leaves your machine:**
- Only the target media URL and standard downloader request headers sent by `yt-dlp`.

**Data that stays local:**
- Downloaded files in the selected output folder.
- Optional memory notes under `<state_root>/`.

**Allowed boundary:**
- Keep credentials out of plain-text memory notes.
- Write only inside the user-approved output directory.
- Download a single video by default; expand to playlist mode only after an explicit user request.
- Restrict network access to the target media host implied by the provided URL.
