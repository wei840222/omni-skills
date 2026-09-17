---
name: udio
description: Generate AI music via Udio community API wrappers or browser automation.
  Trigger when asked to create, extend, or prompt engineer music using Udio.
metadata:
  openclaw: '{"emoji": "🎵", "requires": {"bins": ["python3"], "env": ["UDIO_AUTH_TOKEN"]},
    "primaryEnv": "UDIO_AUTH_TOKEN"}'
---

## Initialization

Upon loading for the first time, immediately read `references/setup.md` to establish the user's preferred integration approach (API vs Browser) and configure authentication.

## When to load

Load this skill when the user explicitly requests music generation, extension, or prompt crafting using Udio. Maintain focus exclusively on Udio interactions; route general music playback or Suno requests to appropriate alternative skills.

## Architecture

Memory at `<state_root>/udio/`. See `references/memory-template.md` for structure.

```
<state_root>/udio/
├── [memory.md]       # Created on first use: preferences, auth token location
├── [projects/]       # Per-project song tracking
└── [songs/]          # Downloaded audio files
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup | `references/setup.md` |
| Memory | `references/memory-template.md` |
| API usage | `references/api.md` |
| Browser automation | `references/browser.md` |
| Prompt crafting | `references/prompts.md` |
| Style tags | `references/styles.md` |
| Lyrics guide | `references/lyrics.md` |

## Core Rules

### 1. Choose the Right Approach
| Situation | Method |
|-----------|--------|
| Programmatic generation, batch jobs | API wrapper |
| User wants to browse and listen | Browser automation |
| Just need prompt help | Prompt engineering only |

### 2. API Requires Auth Token
Udio has no official public API. Community wrappers use the internal API:
- Token: `sb-api-auth-token` cookie from udio.com
- Token expires: refresh if 401 errors occur
- See `references/api.md` for setup instructions

### 3. Structure Prompts in Layers
```
[genre] [subgenre] [mood] [instruments] [voice] [era/influence]
```
Example: "indie folk melancholic acoustic guitar female vocals 90s"

### 4. Extend Songs Strategically
Udio generates ~30 second clips. Build full songs:
1. Create initial clip with strong hook
2. Extend 2-3 times with consistent style
3. Add outro with ending indicators
4. Target 2-4 minutes total

### 5. Save Successful Seeds
Same prompt + different seed = different result. When close to desired output:
- Note the seed number
- Try adjacent seeds (seed +/- 1)
- Document working combinations

## API Integration

### Python Wrapper (Recommended)
```bash
pip install udio_wrapper
```

```python
from udio_wrapper import UdioWrapper

# Initialize with auth token
udio = UdioWrapper("your-sb-api-auth-token")

# Create a song
song = udio.create_song(
    prompt="electronic ambient downtempo dreamy synth pads",
    seed=-1,  # -1 for random
    custom_lyrics="Optional lyrics here"
)

# Extend the song
extended = udio.extend(
    prompt="add drums and bass, building energy",
    audio_conditioning_path=song['song_path'],
    audio_conditioning_song_id=song['id']
)

# Add outro
outro = udio.add_outro(
    prompt="gentle fade out, conclusion",
    audio_conditioning_path=extended['song_path'],
    audio_conditioning_song_id=extended['id']
)
```

### TypeScript/Node Wrapper
```bash
npm install udio-wrapper
```

```typescript
import { createUdioWrapper } from 'udio-wrapper';

const client = await createUdioWrapper('your-auth-token');

const song = await client.createSong({
    prompt: 'indie rock upbeat energetic guitar',
    seed: 12345,
    customLyrics: 'Optional lyrics'
});

const completed = await client.waitForCompletion(song.id);
console.log('Download URL:', completed.url);
```

### Complete Song Sequence
```python
# Generate intro + extensions + outro in one call
complete = udio.create_complete_song(
    short_prompt="peaceful acoustic guitar melody",
    extend_prompts=[
        "add piano and soft strings",
        "introduce light percussion, building"
    ],
    outro_prompt="gentle resolution, fading",
    num_extensions=2,
    custom_lyrics_short="Opening verse...",
    custom_lyrics_extend=["Middle section...", "Bridge..."],
    custom_lyrics_outro="Final words..."
)
```

## Browser Automation

When API isn't available or user prefers visual interaction:

### Navigate to Udio
```
browser action=open targetUrl="https://www.udio.com" profile=openclaw
```

### Get Auth Token (for API use)
1. Open DevTools: `Cmd+Option+I` (Mac) or `F12` (Windows)
2. Go to Application tab > Cookies > udio.com
3. Find `sb-api-auth-token`
4. Copy the value

### Generate Music via UI
1. Navigate to create page
2. Enter prompt in text field
3. Adjust settings (instrumental, duration)
4. Click generate
5. Wait for completion (~30-60 seconds)
6. Download or extend

## Prompt Patterns

### By Genre
| Genre | Prompt Pattern |
|-------|---------------|
| Electronic | `electronic [subgenre] [mood] synth [texture] [era]` |
| Rock | `[sub]rock [energy] [guitars] [drums] [vocals] [decade]` |
| Hip Hop | `hip hop [subgenre] [beat style] [sample type] [era]` |
| Jazz | `jazz [subgenre] [instruments] [setting] [mood]` |
| Classical | `classical [period] [ensemble] [mood] [dynamics]` |

### Mood Combinations
| Energy | Mood Stack |
|--------|------------|
| High + Positive | euphoric energetic uplifting triumphant |
| Low + Positive | peaceful calm serene contemplative |
| High + Negative | aggressive chaotic intense dark |
| Low + Negative | melancholic somber mournful introspective |
| Complex | bittersweet nostalgic hopeful yearning |

### Voice Control
```
# Female vocals
female vocals ethereal soprano breathy

# Male vocals  
male vocals deep baritone raspy emotional

# Choir
choir harmonies gospel powerful anthemic

# No vocals
instrumental only no singing no vocals
```

## Common Traps

| Trap | Problem | Solution |
|------|---------|----------|
| Vague prompts | "good music" = random | Be specific: genre, mood, instruments |
| Contradictions | "upbeat sad" confuses model | Pick consistent descriptors |
| Token expiry | 401 errors | Re-extract from browser cookies |
| Too many keywords | 20+ terms dilute focus | Use 5-10 key descriptors |
| No seed tracking | Can't reproduce good results | Log seeds for successful generations |
| Abrupt extensions | Jarring transitions | Match style/key in extend prompts |

## Extension Strategy

### Building Full Tracks
| Phase | Duration | Prompt Additions |
|-------|----------|------------------|
| Intro | 0-30s | "intro, building, atmospheric" |
| Verse/Main | 30s-2m | Original prompt |
| Bridge | 2m-2:30 | "variation, bridge, key change" |
| Outro | Final 30s | "outro, ending, fade, resolution" |

### Ending Indicators
Add to final extend/outro:
- "fade out" / "fading"
- "song ending" / "conclusion"
- "final chorus" / "last verse"
- "resolution" / "outro"

## Data Storage

This skill creates `<state_root>/udio/` on first use:
- **memory file** — Preferences, successful prompts, token location reference
- **projects folder** — Per-project tracking with seeds and URLs
- **songs folder** — Downloaded audio files (optional)

All data stays local. Auth tokens should be stored in system keychain, not plain text.

## Scope

**This skill does:**
- Generate music via community API wrappers (requires auth token)
- Navigate udio.com with browser automation (user must be logged in)
- Craft optimized prompts for Udio's model (no token needed)
- Track projects, seeds, and successful patterns locally
- Download generated audio files to `<state_root>/udio/songs/`

**This skill does NOT:**
- Store auth tokens in plain text (must use keychain/credential manager)
- Bypass Udio's rate limits or terms of service
- Access files outside `<state_root>/udio/`
- Auto-extract tokens without user guidance

## Security Notes

**Auth Token:** The `sb-api-auth-token` cookie grants API access to your Udio account. Handle it like a password:
- Securely store in the system keychain rather than plain text
- Token expires after ~7 days of inactivity
- Re-extract if you get 401 errors

**Community Wrappers:** The Python and Node wrappers are community-maintained (not official Udio software). Review their source code before installing:
- Python: github.com/flowese/UdioWrapper
- Node: github.com/josephgodwinkimani/udio-wrapper

**Prompt-Only Mode:** If you prefer not to use API or share tokens, this skill works in prompt-only mode — just help with crafting effective prompts without any API calls.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| api.udio.com | Prompts, lyrics | Music generation (via wrappers) |
| udio.com | Browser session | Direct platform access |

Auth token is sent with API requests. No other data leaves the machine.

## Trust

By using this skill with API wrappers, prompts and lyrics are sent to Udio's servers for music generation. Only use if you trust Udio with your creative content. Review Udio's terms of service at udio.com/terms.

## Related Skills
- `suno` — Alternate AI music generation platform and lyrics workflows
- `audio` — Audio processing and editing
- `video` — Combine music with video content
- `ffmpeg` — Audio format conversion, cropping, cross-fades
