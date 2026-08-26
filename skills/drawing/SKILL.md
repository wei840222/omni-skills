---
name: drawing
description: Generate children's drawings and coloring pages with modular prompts, style packs, and print-ready constraints across image models.
metadata:
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"art":"Broader art direction, critique, and technique guidance beyond image prompting","logo":"Prompt patterns for icons, marks, and other cleaner graphic outputs","design":"Clarify visual taste and creative direction before locking a drawing style","graphic-design":"Improve layout, print choices, and supporting visual materials around the drawing"}'
---

## When to Use

User needs original AI drawings, coloring pages, or simple educational illustrations, especially for children. Agent turns vague requests into model-portable prompts, age-appropriate style choices, and print-ready constraints that work in OpenClaw or any image model the user already has.

Use this when the real problem is not "pick the best model" but "get a clean result fast": full color vs coloring page, preschool vs older kids, one-off scene vs consistent series, or first prompt vs refinement loop.

## State location

Memory lives in `<state_root>/drawing/` by default. Use workspace-first resolution:
1. `$CLAWIC_STATE_ROOT/drawing/` if defined
2. `~/.clawic/drawing/` if `~/.clawic` exists
3. `<state_root>/drawing/`

If the directory does not exist, run `references/setup.md`. See `references/memory-template.md` for structure and status fields.

## Quick Reference

Load only the smallest file needed for the current bottleneck using explicit commands like `cat references/prompt-system.md` when the user asks for a specific step or when the current workflow matches the trigger condition in the table.

| Topic | File | When to load |
|-------|------|--------------|
| Setup and activation behavior | `references/setup.md` | When `<state_root>/drawing/` is empty |
| Memory structure and status model | `references/memory-template.md` | When updating preferences |
| Universal prompt scaffold and iteration loop | `references/prompt-system.md` | When writing a new prompt |
| Coloring-page rules by age and print target | `references/coloring-pages.md` | When the mode is `coloring-page` |
| Ready-to-use visual directions | `references/style-packs.md` | When selecting visual style |
| OpenClaw integration and model adapters | `references/model-portability.md` | When dealing with model specifics |
| Source-backed prompt notes | `references/source-notes.md` | When needing evidence for prompt guidelines |

## D.R.A.W. Protocol

Use this four-step protocol before writing a prompt.

### Decide the output mode

Pick one mode first and make it explicit:

| Mode | Best for | Default constraints |
|------|----------|---------------------|
| `color-scene` | Storybook art, posters, reward images | Full color, clear focal point, simple background |
| `coloring-page` | Printable black-and-white pages | Thick clean outlines, white background, no shading |
| `learning-card` | Flashcards, classroom visuals, themed worksheets | One concept per image, didactic clarity, minimal decoration |

### Reduce the scene

Keep 1-3 focal elements. If the user wants a coloring page, simplify harder than feels natural. A "cute but detailed" prompt usually fails for children because the model fills the page with tiny shapes and noisy backgrounds.

### Anchor the style

Pick one style pack and one composition. Select a single, consistent style instead of combining conflicting modifiers like "watercolor + kawaii + paper cut + cinematic". The style must support the use case:
- soft color illustration for story or gift
- bold cartoon for fast recognizability
- black outline sheet for coloring
- classroom visual for learning

### Wrap with constraints

End with non-negotiables:
- age appropriateness
- original characters only unless the user explicitly asks otherwise
- ensure friendly mood, calm scenes, text-free images, uncropped subjects, and clean unmarked graphics
- print target if relevant: A4 or US Letter, portrait or landscape

For full templates and slot order, load `references/prompt-system.md`.

## Fast Prompt Starters

### Full-color drawing

```text
Create an original children's illustration for ages [age range].
Subject: [main subject].
Scene: [simple setting with 1-2 supporting elements].
Style: [style pack].
Composition: [portrait or landscape], centered focal point, generous breathing room.
Color: [palette or mood].
Keep it friendly, clear, and easy to recognize. Ensure images are text-free, unmarked, and friendly.
```

### Coloring page

```text
Create a printable black-and-white coloring page for ages [age range].
Subject: [main subject].
Use thick clean outlines, large closed shapes, minimal background, white page, and no shading.
Keep only the essential elements needed to recognize the scene.
Ensure images are text-free, use solid shapes over gray fill, omit tiny decorations, keep objects fully visible, and remain unmarked.
```

### Educational drawing

```text
Create a simple educational illustration for children learning [topic].
Show [concept] clearly using one main scene and only the supporting objects that help explain it.
Use [style pack]. Keep labels out of the image unless the user specifically needs them.
Make it accurate, friendly, uncluttered, and easy to print.
```

## Core Rules

### 1. Start with the child, not the model
- Ask or infer the age band, use case, and whether the result is for coloring, printing, or screen viewing.
- Preschool output should be radically simpler than "pretty" output for older kids.
- If the user does not care about the model, optimize for prompt quality and let OpenClaw use the configured image model.

### 2. Separate subject, style, and constraints
- Prompts work better when the main subject, scene, style, and restrictions are stated in distinct blocks.
- Translate vague adjectives like "nice", "professional", or "beautiful" into concrete visual traits.
- Reusable prompts should keep variables obvious: subject, age, style, color mode, page format.

### 3. Match detail level to coloring difficulty
- Coloring pages for ages 3-5 need big shapes, thick outlines, and almost no background clutter.
- Ages 5-7 can handle one or two supporting objects and mild patterning.
- Older kids can tolerate moderate detail, but the subject must still read instantly.
- If the user says "for kids" and gives no age, default to the safer 5-7 profile.

### 4. Lock invariants for any series
- For multiple pages, repeat the same character traits, line style, camera distance, palette family, and page framing.
- Preserve one prompt block called "always keep" and reuse it unchanged across generations.
- Change one variable at a time between attempts so the cause of improvement stays visible.

### 5. Design for print when print matters
- Explicitly request white background, clean margins, uncropped subject, and portrait or landscape orientation.
- Coloring pages should be ink-friendly: use solid black lines and pure white spaces instead of halftones, gray textures, or faux paper grain.
- If the result will be printed at home, prefer centered compositions and avoid edge-to-edge details.

### 6. Run a tight validation loop
- Generate a small batch, inspect the actual result, then change only one thing: style, detail, composition, or negative constraints.
- If hands, faces, or proportions fail, simplify the pose before adding more detail.
- If the background is noisy, remove it rather than trying to "clean it up" with more adjectives.

### 7. Keep the output kid-safe and IP-safe by default
- Default to friendly expressions, calm scenes, and original characters.
- Use original characters by default, and include brand characters only if the user explicitly accepts the IP risk.
- Use generic descriptions instead of real child photos, requesting photos only if the user explicitly requires that workflow and trusts the provider.

## Common Traps

- Asking for "cute and detailed" coloring pages -> the model adds clutter that frustrates children.
- Mixing too many styles in one prompt -> inconsistent output and lower controllability.
- Forgetting the age band -> detail level drifts and the result misses the user.
- Leaving text inside the image -> most image models still mangle labels in children's material.
- Changing five things at once -> you cannot tell which edit improved the result.
- Using the same prompt for color and coloring-page modes -> line quality and composition drift immediately.

## Security & Privacy

**Data that leaves your machine:**
- Prompt text and any reference images sent to the selected image provider through OpenClaw or another image client.

**Data that stays local:**
- Style preferences, winning prompts, and recurring constraints under `<state_root>/drawing/`.

**This skill does NOT:**
- Force a specific model purchase or provider.
- Upload files unless the active image workflow already does so.
- Store real child photos by default.
- Modify its own skill file.

## Trust

By using image generation, prompt text and optional reference images may be sent to third-party model providers. Only use providers you trust, and avoid sending unnecessary personal details or identifiable child photos when a generic description would work.
