# Patterns — YouTube Video Transcript

## Research and citation

```markdown
"{Exact quote}"
— {Speaker or channel}, "{Video Title}", {timestamp},
accessed {date}. https://youtube.com/watch?v={id}&t={seconds}
```

For multi-video literature passes, with consent create `<state_root>/research/{topic}/` and an index of key quotes per id.

### Timestamp link forms

- Standard: `https://youtube.com/watch?v=ID&t=323`
- Short: `https://youtu.be/ID?t=323`
- Embed start: `https://youtube.com/embed/ID?start=323`

Prefer integer seconds in `&t=` / `start=`.

## Content reuse

From a timestamped transcript you may derive (still faithful to source speech):

- chapter blog outline
- short social quotes (<280 chars) with timestamp
- newsletter or show-note bullets
- competitor topic coverage lists

Do not invent claims absent from the transcript.

## Language workflows

```bash
yt-dlp --list-subs "VIDEO_URL"
yt-dlp --skip-download --write-subs --sub-langs en,es,fr "VIDEO_URL"
```

When comparing languages, label each track and avoid mixing lines without attribution.

## Summarization patterns

### Chapter-based

```markdown
### {Chapter Title} [{timestamp}]
**Key points:**
- Point 1
- Point 2
**Notable quote:** "{quote}" [{timestamp}]
```

### Executive

```markdown
## TL;DR
{2-3 sentences}

## Key takeaways
1. {takeaway} [{timestamp}]
2. ...
```

Summaries still need source timestamps on non-trivial claims so the user can verify.

## Search patterns

User: "Where do they talk about pricing?"

1. Keyword + near-synonym scan (`price`, `cost`, `subscription`, `monetization`)
2. Return each hit with ±10–15s context
3. Deep link every hit
4. If only auto-captions exist, warn about ASR errors near the match

## Quote mining

Prefer definitive statements, spoken lists, contrasts ("not X, but Y"), and unusual memorable phrases. Return:

```markdown
**[12:34] Quote**
> "{exact words}"

**Context:** {before/after}
**Link:** https://youtube.com/watch?v=ID&t=754
```

## Export formats

| Format | Use | Notes |
|--------|-----|-------|
| Markdown | Reading / notes | Default; keep timestamps |
| SRT / VTT | Editors / players | `--sub-format srt` or convert |
| Plain text | grep | Only strip timestamps when asked |
| JSON | Programmatic | From `--write-info-json` + cues |

## Error recovery

| Failure | Action |
|---------|--------|
| No subs in requested language | List alternatives; offer another lang or auto |
| No subs at all | Stop; suggest creator-provided description chapters only if present — still not a transcript |
| Geo-restricted | Report restriction; no built-in proxy |
| Age-restricted / login wall | User-supplied `--cookies` or `--cookies-from-browser` only |
| Empty or garbage auto text | Warn; offer retry other lang or manual track |
| yt-dlp too old / unknown flag | Upgrade guidance via `references/setup.md` |

## Batch archive (consent + delays)

```bash
yt-dlp --flat-playlist -j "CHANNEL_OR_PLAYLIST_URL" | jq -r '.id'
# per id: metadata, list-subs, extract with --sleep-interval
```
