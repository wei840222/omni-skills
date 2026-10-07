# GIF Creation and Optimization

Load this file when converting video to GIF, repairing washed-out colors, or shrinking an existing GIF.

## Requirements

**Required for creating GIFs:**

- `ffmpeg` — video to GIF conversion

**Optional:**

- `ffprobe` — inspect source before encode
- `gifsicle` — post-optimization (often reduces size 30–50%)

## Inspect first

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,avg_frame_rate,duration \
  -of default=noprint_wrappers=1 input.mp4
```

Confirm duration and resolution before choosing `-t`, fps, and scale. If `ffprobe` is missing, ask for duration/resolution or probe with a short `ffmpeg -i` read.

## Creating GIFs with FFmpeg

**Always use palettegen (without it, colors look washed out).** One-pass filter_complex:

```bash
ffmpeg -ss 0 -t 5 -i input.mp4 \
  -filter_complex "fps=10,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" \
  -loop 0 \
  output.gif
```

Two-pass (useful for harder palettes):

```bash
ffmpeg -ss 0 -t 5 -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -ss 0 -t 5 -i input.mp4 -i palette.png \
  -filter_complex "fps=10,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" \
  -loop 0 output.gif
```

| Setting | Value | Why |
|---------|-------|-----|
| fps | 8–12 | Higher fps grows file size fast with little perceived gain |
| scale width | 320–480 | 1080p GIFs are massive for chat/web |
| lanczos | always for downscale | Better scaling quality than default |
| duration (`-t`) | keep short | GIF size scales roughly with frame count |
| `-ss` placement | before `-i` for speed; after `-i` for frame accuracy | See `ffmpeg` skill for seek trade-offs |

### Seek notes

- Fast approximate cut: `-ss` before `-i`
- Frame-accurate cut: `-ss` after `-i` (slower)
- Combine when needed: fast pre-seek then accurate trim (document the exact flags used)

### Transparent / screen content

- UI screenshots and flat graphics may need fewer fps but sharper edges; start at scale 480 and fps 8–10.
- Do not upscale tiny sources; native resolution with palettegen is usually cleaner.

## Post-optimization with gifsicle

If `gifsicle` is available:

```bash
gifsicle -O3 --lossy=80 --colors 128 input.gif -o output.gif
```

Typical effect: 30–50% smaller with acceptable quality loss for chat GIFs. Re-check quality after lossy passes; drop `--lossy` or raise colors if banding is visible.

If `gifsicle` is missing, keep the FFmpeg output and report that the optional optimizer was skipped.

## Video alternative (preferred for web)

For web pages, muted looping video is usually 80–90% smaller than a large GIF:

```html
<video autoplay muted loop playsinline>
  <source src="animation.webm" type="video/webm">
  <source src="animation.mp4" type="video/mp4">
</video>
```

Example encode handoff (then use the `video` skill for platform limits):

```bash
ffmpeg -ss 0 -t 5 -i input.mp4 -an -c:v libx264 -pix_fmt yuv420p -movflags +faststart loop.mp4
ffmpeg -ss 0 -t 5 -i input.mp4 -an -c:v libvpx-vp9 -b:v 0 -crf 32 loop.webm
```

## Verify before delivery

```bash
# size
ls -lh output.gif
# basic decode smoke (exit 0 means readable)
ffmpeg -v error -i output.gif -f null -
```

Report path, approximate size, duration/fps intent, and whether gifsicle ran.

## Common mistakes

- No `palettegen` / `paletteuse` — colors look terrible
- FPS >15 for chat GIFs — file size explodes for little benefit
- Shipping 1080p GIF to messaging apps — timeouts and failed uploads
- No lazy loading on web pages that still use GIF — blocks page load
- Using a huge GIF where muted MP4/WebM would work — often ~10× larger
- Claiming success without checking the output file exists and decodes
