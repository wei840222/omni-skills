---
name: image-edit
description: >
  Edit and enhance existing images with AI tools for inpainting, outpainting,
  background removal, upscaling, restoration, and style transfer. Trigger when
  a user asks to modify, fix, upscale, relight, or alter an existing image.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"✂️","os":["linux","darwin","win32"],"displayName":"Image Editing"}'
  related-skills: '{"image-generation":"Use when creating new images from prompts rather than editing an existing image.","photography":"Use for camera technique, composition, and capture guidance outside post-edit workflows.","video-edit":"Use when the asset is video rather than a still image.","screenshot":"Use for capture and annotation of screen images before deeper edit pipelines."}'
---
# AI Image Editing

Help users edit and enhance images with AI tools.

Load `references/sources.md` when you need current tool docs, model limits, or research-backed edit guidance.

**Rules:**
- Ask what edit they need: remove objects, extend canvas, upscale, fix faces, change background
- Load `references/inpainting.md` when tasked with removing objects.
- Load `references/outpainting.md` when asked to extend image borders.
- Load `references/background-removal.md` when asked to remove backgrounds.
- Load `references/upscaling.md` when asked to increase resolution.
- Load `references/restoration.md` when asked to fix blurry faces.
- Load `references/style-transfer.md` when asked to change style.
- Load `references/tools.md` to configure provider-specific tools.
- Preserve the original file before editing; write results as new files

---

## Edit Type Selection

| Task | Technique | Best Tools |
|------|-----------|------------|
| Remove objects/people | Inpainting | DALL-E, SD Inpaint, IOPaint, Flux.1 Fill |
| Extend image borders | Outpainting | DALL-E, SD Outpaint, Photoshop AI, Flux.1 Fill |
| Remove background | Segmentation | remove.bg, ClipDrop, Photoroom |
| Increase resolution | Upscaling | Real-ESRGAN, Topaz, Magnific |
| Fix blurry faces | Restoration | GFPGAN, CodeFormer |
| Change style | Style Transfer | SD img2img, ControlNet |
| Relight scene | Relighting | ClipDrop, IC-Light |

---

## Workflow Principles

- **Non-destructive editing** — keep originals, save edits as new files
- **Work in layers** — combine multiple edits sequentially
- **Match resolution** — edit at original resolution, upscale last
- **Mask precision matters** — better masks = better results
- **Iterate on masks** — refine edges for seamless blends

---

## Masking Basics

Masks define edit regions:
- **White** = edit this area
- **Black** = preserve this area
- **Gray** = partial blend (feathering)

**Mask creation methods:**
- Manual brush in editor
- SAM (Segment Anything) for auto-selection
- Color/luminance keying
- Edge detection

---

## Common Workflows

### Object Removal
1. Create mask over unwanted object
2. Run inpainting with context prompt (optional)
3. Blend edges if needed
4. Touch up artifacts

### Background Replacement
1. Remove background (get transparent PNG)
2. Place on new background
3. Match lighting/color
4. Add shadows for realism

### Enhancement Pipeline
1. Restore faces (if present)
2. Remove artifacts/noise
3. Color correct
4. Upscale to final resolution

---

## Quality Tips

- **Feather masks** — hard edges look artificial
- **Context prompts help** — describe what should fill the area
- **Multiple passes** — large edits may need iterative refinement
- **Check edges** — zoom in to verify blend quality
- **Match grain/noise** — add film grain to match original

---

### Current Setup
<!-- Tool: status -->

### Projects
<!-- What they're editing -->

### Preferences
<!-- Preferred tools, quality settings -->

---
*Check technique files for detailed workflows.*


## State location

- `<state_root>/image-edit/` - Used for storing original and edited images.
