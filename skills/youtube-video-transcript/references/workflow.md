# Workflow — YouTube Video Transcript

## 1. Normalize the URL

Accept `youtube.com/watch?v=`, `youtu.be/`, `youtube.com/shorts/`, and playlist/watch URLs that embed a video id. Extract the canonical 11-character id when forming cache filenames and `&t=` deep links.

## 2. Metadata first

```bash
yt-dlp -j "VIDEO_URL"
```

Use JSON fields:

- `id`, `title`, `channel`, `duration`, `upload_date`
- `chapters` (may be null)
- `subtitles` / `automatic_captions` keys (languages present)

Confirm the title with the user when multiple candidates could match a vague paste.

## 3. List subtitle tracks

```bash
yt-dlp --list-subs "VIDEO_URL"
```

Selection order:

1. User-requested language if stated
2. Manual/uploaded track in that language
3. Manual English (or the video's primary language) if unspecified
4. Auto-generated track in the best available language
5. If none: stop and report; do not fabricate speech

## 4. Extract without downloading media

```bash
# Manual / uploaded
yt-dlp --skip-download --write-subs --sub-langs LANG \
  --sub-format "vtt/srt/best" -o "%(id)s.%(ext)s" "VIDEO_URL"

# Auto fallback
yt-dlp --skip-download --write-auto-subs --sub-langs LANG \
  --sub-format "vtt/srt/best" -o "%(id)s.%(ext)s" "VIDEO_URL"
```

Work in a temporary directory owned by the session when possible. Convert VTT/SRV3 cues into Markdown lines:

```markdown
[00:00] Opening line
[00:15] Next segment
```

Use `[MM:SS]` under one hour; `[HH:MM:SS]` otherwise. Merge split cues that are clearly one sentence when readability requires it, without dropping start times.

## 5. Chapters

If `chapters` exists, emit a table of contents with start times, then optionally section the transcript. If absent, optional smart breaks from long pauses or explicit transition phrases — label those as inferred, not official.

## 6. Answer shapes

| User intent | Response shape |
|-------------|----------------|
| Transcribe / read | Title + track quality note + timestamped body (or path if long + cached) |
| Summarize | Chapter or TL;DR bullets **with** supporting timestamps |
| Search topic | Ranked hits with quote, context (±10–15s), deep link |
| Quote / cite | Exact span, speaker if known, timestamp, watch URL with `&t=` |
| Export | Write requested format under `<state_root>/exports/` only with consent, or stream content if no persist |

## 7. Consent and cleanup

- Ask before writing `<state_root>/videos/{id}.md` or exports that persist.
- Delete temp subtitle files when the turn ends unless the user asked to keep them.
- On "show saved" / "delete video X", operate only under the resolved `<state_root>`.

## 8. Batch / rate limits

For playlists or channel loops, add polite delays:

```bash
yt-dlp --sleep-interval 2 --max-sleep-interval 5 ...
```

Do not hammer subtitle endpoints; surface failures per-id rather than aborting the whole batch silently.
