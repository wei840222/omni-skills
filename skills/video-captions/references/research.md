# Caption Delivery Constraints

## Verification Sources

- **Netflix Timed Text Style Guide** — review the delivery partner requirements for timing, line treatment, and text placement before preparing Netflix assets: https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-Timed-Text-Style-Guide-General-Requirements
- **YouTube Help: Subtitle file formats** — choose a supported caption format and upload path for YouTube delivery: https://support.google.com/youtube/answer/2734698
- **FFmpeg subtitles filter documentation** — verify `libass` support and `force_style` behavior before burn-in: https://ffmpeg.org/ffmpeg-filters.html#subtitles

## Netflix Timing and Styling Requirements
- **Duration Requirements**: Minimum duration of 5/6 second (0.833s) per subtitle event. Maximum duration is 7 seconds.
- **Character Limits**: Maximum of 42 characters per line.
- **Line Count**: Maximum of 2 lines per subtitle event.
- **Gap Specifications**: Minimum of 2 frames gap between consecutive subtitle events.
- **Placement**: Bottom center by default, moved to top when on-screen text exists at bottom.

## Social Media Guidelines (TikTok/Instagram Reels)
- **Formatting**: Short phrases (1-4 words per line), highly dynamic.
- **Styling**: Center-aligned, high contrast (thick outlines or background blocks), usually sans-serif bold.
- **Location**: Middle third or lower middle of screen to avoid native UI elements (captions, like buttons).
- **Pacing**: Rapid succession, perfectly synced to word timestamps to maintain viewer retention.

## General Best Practices
- Keep linguistic units together (ensure adjectives/nouns and prepositional phrases remain contiguous).
- Indicate non-speech audio (e.g. `[music playing]`, `[door slams]`) when writing SDH or accessibility subtitles.
