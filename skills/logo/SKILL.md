---
name: logo
description: Create, refine, validate, and deliver brand logos or App Store icons with AI-assisted prompts, vector cleanup, and export guidance. Use when a user needs logo concepts, a design brief, logo-format deliverables, or review of a logo workflow.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎨"}'
---

## Quick Start: AI Logo Generation

**Best model for most logos: Google Imagen** (Google Imagen)

### Basic Prompt Formula
```
Create a [STYLE] logo featuring [ELEMENT] on [BACKGROUND].
[DESCRIPTION]. The logo should look good at 32px with recognizable shapes.
```

### Example
```
Create a minimalist logo featuring a geometric mountain peak on white background.
Clean lines, navy blue (#1E3A5A), modern and professional style.
The logo should look good at 32px with recognizable shapes.
```

For the full 7-step prompt framework and model comparison, load `references/ai-generation.md`.

---

## Decision Tree

| Situation | Load |
|-----------|------|
| AI generation (Nano Banana, GPT Image, prompts, iOS icons) | `references/ai-generation.md` |
| Logo types (wordmark, symbol, combo, emblem) | `references/types.md` |
| Design process with a human designer | `references/process.md` |
| File formats and export requirements | `references/formats.md` |
| DIY without AI (templates, Canva) | `references/diy.md` |
| Hiring designers or agencies | `references/hiring.md` |

---

## Model Quick Reference

| Model | Best For |
|-------|----------|
| **Google Imagen** | Overall best, text + icons, App Store icons |
| **GPT Image** | Conversational iteration, natural language |
| **Ideogram** | Perfect text rendering |
| **Midjourney** | Artistic icons only (no text) |

---

## iOS App Icons (Liquid Glass)

For Apple-platform app icons, confirm the current Human Interface Guidelines before applying Liquid Glass guidance. Use this prompt structure:

```
Create a polished iOS app icon featuring [ELEMENT].
Rounded square with [COLOR] gradient, minimalist white symbol centered.
Soft shadows, glassy depth effect, works at 60px.
The icon represents [APP PURPOSE].
```

See `references/ai-generation.md` for the complete app-icon prompt template.

---

## Validation Loop (MANDATORY)

**Always perform visual review before delivery.** Inspect every AI output before sharing.

1. Generate → 2. Look at the actual image → 3. Check for issues → 4. Fix or regenerate → 5. Repeat (max 5-7 attempts)

**Common fixes:**
- Unwanted padding → Crop
- Elements cut off → Regenerate with "centered composition"
- Text garbled → Use Nano Banana/Ideogram or add manually
- Too complex → Simplify prompt

If 5-7 attempts fail, change model or strategy entirely.

---

## Universal Truths

**AI output is a starting point.** Every AI logo needs vectorization, cleanup, and manual text refinement. Always vectorize, clean up, and manually refine raw output before final delivery.

**Test at small sizes early.** If it doesn't work at 32px, simplify. Most real-world usage is small.

**Text handling varies.** Only Nano Banana and Ideogram reliably render text. For Midjourney, generate icon-only.

**Simple logos last.** Nike, Apple, McDonald's. Complexity dates quickly and fails at small sizes.

---

## Before Finalizing

- [ ] Works in black and white
- [ ] Readable at 32px (favicon test)
- [ ] Vectorized (SVG), not just PNG
- [ ] All variants created (horizontal, stacked, icon-only)
- [ ] Text manually refined, not AI-generated
- [ ] Tested on dark and light backgrounds

---

## When to Load More

| Situation | Reference |
|-----------|-----------|
| Full prompt frameworks, model comparison, iOS icons | `references/ai-generation.md` |
| Wordmark vs symbol vs emblem decisions | `references/types.md` |
| Working with designers, brief templates | `references/process.md` |
| SVG, PNG, favicon, size requirements | `references/formats.md` |
| Track what works, learn from iterations | `references/feedback.md` |
