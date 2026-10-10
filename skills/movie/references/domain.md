## Core Workflow

Every film follows: Script → Breakdown → Generation → Assembly → Polish.

Before generating ANY video, establish:

1. **Style bible** — Visual language, color palette, lighting, grain
2. **Character sheets** — Reference images from multiple angles
3. **Shot list** — Scene-by-scene with framing, duration, transitions

Store these under the resolved project tree:

```text
<state_root>/<project>/
```

## Generation Checklist

Before each shot generation:

- [ ] Character reference images attached
- [ ] Style keywords locked (from style-bible)
- [ ] Previous shot reviewed for continuity
- [ ] Tool selected based on shot type (see `references/tools.md`)
- [ ] Time-sensitive vendor limits re-checked via `references/sources.md` when claiming duration/resolution

After generation:

- [ ] Check character consistency vs reference
- [ ] Check lighting/color matches scene
- [ ] Log prompt + result in shots folder
- [ ] Flag continuity issues for re-generation

## Critical Rules

1. **Consistency over speed** — Better to re-generate than break character continuity
2. **Log everything** — Every prompt, every iteration, what worked/failed
3. **Tool routing matters** — Prefer motion-strong tools for action, dialogue-oriented tools for lip work, style-control tools for look development; verify current product names in sources before locking a vendor
4. **Start rough** — Animatics first, polish approved shots only
5. **Project scope** — Feature length implies hundreds of shots. Plan iterations and batch reviews.
