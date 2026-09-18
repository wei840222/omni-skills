---
name: vibe-design
description: Create visual designs with AI tools. Covers prompting for UI/graphics,
  Midjourney techniques, Figma AI workflow, and iteration patterns.
metadata:
  openclaw: '{"emoji": "🎨"}'
---

## What is Vibe Design

Design where you describe what you want and let AI generate visuals, layouts, and assets. You iterate based on results rather than pixel-pushing from scratch. Same philosophy as vibe coding applied to visual design.

**Core principle:** AI handles exploration and generation. You handle curation and refinement.

## Quick Reference

| Topic | File |
|-------|------|
| Prompting for visuals | `references/prompting.md` |
| UI/UX design with AI | `references/ui-design.md` |
| Image generation tips | `references/image-gen.md` |
| Figma AI workflow | `references/figma.md` |
| Tools by use case | `references/tools.md` |

## Core Rules

### 1. Use Design Vocabulary, Not Art Vocabulary
AI responds differently to design vs art terms.

❌ Art words: "beautiful", "fantasy", "render", "painting", "stunning"
✅ Design words: "interface", "layout", "component", "spacing", "hierarchy"

Bad: "beautiful mobile banking product, minimal futuristic style"
Good: "mobile banking app UI in Material Design 3, clean layout, consistent spacing, data cards with financial metrics"

### 2. Anchor with Design Systems
Adding a design system name drastically improves structure:
- "Material Design 3" → balanced spacing, cards, shadows
- "Apple HIG" → soft radii, clear typography, native feel
- "IBM Carbon" → enterprise dashboard layouts
- "Atlassian" → B2B tone, crisp typography

### 3. Layer Your Prompts
Build prompts with structure:
```
[Project type] UI design for [product/audience],
[style keywords],
[layout type],
[color palette],
[design system reference],
[rendering style]
```

### 4. Aspect Ratios Matter
- Web: --ar 16:9
- Mobile: --ar 4:5 or --ar 9:16
- Square/icons: --ar 1:1
- Always specify for consistent output

### 5. Iterate Rapidly Instead of Perfecting First Try
Vibe design = rapid exploration.
1. Generate 4-8 variants
2. Identify elements that work
3. Remix: "Like image 2, but with the color palette from image 3"
4. Refine winner in production tool (Figma, etc.)

### 6. AI for Exploration, Tools for Production
- **AI generates**: Mood, direction, concepts, rough layouts
- **Production tools refine**: Pixel-perfect spacing, real content, responsive behavior

Aim for 80% completion with AI, and manually refine the remaining 20% for production.

### 7. Reference Over Description
When possible, show instead of tell:
- Attach reference images
- Link to existing designs you like
- Use "in the style of [specific designer/brand]"

### 8. Design System Consistency
For production work:
- Export AI concepts as references, not finals
- Rebuild in your design system
- Maintain your spacing, typography, and color tokens
- AI inspiration → human implementation

### 9. Know the Tool Strengths

| Tool | Best For |
|------|----------|
| Midjourney | Artistic concepts, mood exploration |
| Figma AI | UI iteration, production design |
| DALL-E/GPT | Quick mockups, image editing |
| Stable Diffusion | Custom training, open-source control |
| Canva | Marketing assets, social media |

See `references/tools.md` for detailed comparison.
