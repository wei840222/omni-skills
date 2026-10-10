# Tools — Video Generation APIs & CLIs

Routing below is a **heuristic starting point**. Product names, max duration, resolution, and pricing change often—re-open the URLs in `references/sources.md` before stating hard limits or recommending a paid tier.

## Video generation families (verify before locking)

| Family (examples) | Typical strength | Notes |
|-------|----------|-------|
| Motion-forward generators (e.g. Seedance-class) | Action, dance, camera energy | Confirm current SKU on vendor site |
| Narrative / physics-oriented (e.g. Sora-class) | Longer beats, scene logic | Use OpenAI video-generation docs for current API behavior |
| Dialogue / lip-sync oriented (e.g. Kling-class) | Talking heads, longer takes | Confirm live product page |
| Cinematic broadcast-oriented (e.g. Veo-class) | Look, lighting aesthetics | Use Google DeepMind / Gemini video docs |
| Controllable style / motion-brush (e.g. Runway Gen-4 class) | Style transfer, guided motion | Use Runway help center |
| Budget / local open weights | Cheap iteration, privacy | Expect shorter clips and more manual continuity work |

## Tool selection rules

- **Action/motion sequences** → motion-forward family first, then verify availability
- **Dialogue scenes** → lip-sync capable family; attach matching character stills
- **Establishing shots** → narrative or cinematic family; lock lighting keywords from style bible
- **Style-heavy artistic** → controllable style family (Runway-class or equivalent)
- **Quick throwaway animatics** → cheapest available path; do not polish yet
- **Privacy/offline** → local/open weights when the host can run them; document the trade-off

When the task collapses to a single API call with no production tree, hand off to `video-generation`.

## FFmpeg essentials

Prefer the dedicated `ffmpeg` skill for non-trivial filter graphs. Common production snippets:

```bash
# Concatenate clips (create list.txt first)
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4

# Extract frame for reference
ffmpeg -i clip.mp4 -ss 00:00:02 -vframes 1 ref.jpg

# Match duration exactly
ffmpeg -i input.mp4 -t 00:00:05 -c copy output.mp4

# Aspect ratio for social
ffmpeg -i input.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" vertical.mp4

# Color grade with LUT
ffmpeg -i input.mp4 -vf lut3d="style.cube" graded.mp4

# Add audio track
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -map 0:v -map 1:a final.mp4
```

Official CLI reference: https://ffmpeg.org/ffmpeg.html

## Image generation (storyboards)

Use `image-generation` for still frames. Keep character sheets under `<state_root>/<project>/characters/`.

## Audio

Music/voice tools are project-dependent. Prefer user-approved providers; for dialogue captions alone use `video-captions` / Whisper-class transcription rather than inventing timings.

## Frame analysis

For continuity checking, extract frames:

```bash
ffmpeg -i scene.mp4 -vf "fps=1" frames/frame_%04d.jpg
```

Then analyze each frame for:

- Character appearance consistency
- Lighting direction
- Color palette adherence
- Prop/costume continuity
