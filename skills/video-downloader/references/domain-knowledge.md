# Domain Knowledge - yt-dlp & Video Downloading

## yt-dlp Context
`yt-dlp` is a command-line program to download videos from YouTube and many other sites. It is a maintained fork of `youtube-dl` with faster release cadence for extractor and CDN changes.

## Common Terms & Usage
- **Containers vs. Streams:** Video and audio are often served as separate streams. `yt-dlp` uses `ffmpeg` to multiplex them into one container such as `.mp4` or `.mkv`.
- **Formats (`-f`):** Selecting formats matters because the visually "best" stream may be large or use codecs that are expensive to play or edit (for example AV1).
- **Metadata (`--dump-json` / `--dump-single-json`):** Fetch metadata first to confirm title, duration, and available formats without downloading the full media.

## Limitations and Risks
- **Rate Limiting:** Hosts may rate-limit or temporarily block rapid repeated requests.
- **Dynamic Endpoints:** Hosts change APIs and CDNs frequently; outdated `yt-dlp` commonly fails with `HTTP 403 Forbidden` or extraction errors.
- **Copyright & Policy:** Use must follow local law and platform terms. Prefer fair-use archiving, education, and personal offline viewing with an explicit user-provided URL.

## Verifiable Sources
- **yt-dlp README / usage** — installer, format selection, and output templates via https://github.com/yt-dlp/yt-dlp
- **yt-dlp FAQ** — common extraction and update guidance via https://github.com/yt-dlp/yt-dlp/wiki/FAQ
- **FFmpeg documentation** — muxing / remux expectations used by yt-dlp merges via https://ffmpeg.org/documentation.html
- **YouTube Terms of Service** — platform policy baseline for YouTube URLs via https://www.youtube.com/t/terms
