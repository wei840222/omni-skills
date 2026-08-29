# Core Rules and Common Traps

## Core Rules

### 1. Resolve aliases to official model IDs first

Community names shift quickly. Before calling an API, map the nickname to the provider model ID.

| Community label | Official model ID to try first | Notes |
|-----------------|--------------------------------|-------|
| Nano Banana | `gemini-2.5-flash-image-preview` | Common nickname, not an official Google model ID |
| Nano Banana 2 / Pro | Verify provider docs | Usually a provider preset over Gemini image models |
| GPT Image 1.5 | `gpt-image-1.5` | Current OpenAI high-tier image model |
| GPT Image mini / iMini | `gpt-image-1-mini` | Budget/faster OpenAI variant |
| FLUX 2 Pro / Max | `flux-pro` / `flux-ultra` | Many platforms rename these SKUs |

### 2. Pick models by task, not by hype

| Task | First choice | Backup |
|------|--------------|--------|
| Exact text in image | `gpt-image-1.5` | Ideogram |
| Multi-turn edits | `gemini-2.5-flash-image-preview` | `flux-kontext-pro` |
| Photoreal hero shots | `imagen-4.0-ultra-generate-001` | `flux-ultra` |
| Fast low-cost drafts | `gpt-image-1-mini` | `imagen-4.0-fast-generate-001` |
| Character/product consistency | `flux-kontext-max` | `gpt-image-1.5` with references |
| Local no-API workflows | `flux-schnell` | SDXL |

### 3. Use benchmark tables as dated snapshots

Benchmarks drift weekly. Use `references/benchmarks-2026.md` as a starting point, then recheck current rankings when quality is critical.

### 4. Draft cheap, finish expensive

Start with 1-4 low-cost drafts, pick one, then upscale or rerender only the winner.

### 5. Keep a fallback chain

If the preferred model is unavailable, fallback by tier:
1) same provider lower tier, 2) cross-provider equivalent, 3) local/open model.

### 6. Treat DALL-E as legacy

OpenAI lists DALL-E 2/3 as legacy. Use modern alternatives like GPT-image-1.5 or Gemini for new projects.

## Common Traps

- Using vendor nicknames as model IDs -> API errors and wasted retries
- Assuming "Nano Banana Pro" or "FLUX 2" are universal IDs -> provider mismatch
- Copying old DALL-E prompt habits -> weaker output vs modern GPT/Gemini image models
- Comparing text-to-image and image-editing scores as if they were the same benchmark
- Optimizing every draft at max quality -> cost spikes without quality gain
