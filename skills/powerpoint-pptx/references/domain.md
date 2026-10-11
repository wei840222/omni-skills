# Domain Knowledge — PowerPoint PPTX

Core rules and traps for offline `.pptx` work. Code and layout patterns live in
sibling references; official anchors live in `sources.md`.

## 1. Choose the workflow before touching the deck

- Reading text, editing an existing deck, rebuilding from a template, and
  creating from scratch are different jobs with different failure modes.
- For text extraction or inspection, read the deck before editing it.
- Text extraction plus thumbnail-style visual inspection is safer than editing
  from shape assumptions alone.
- For template-driven work, inventory the deck before replacing content.
- For deep edits, remember a `.pptx` file is OOXML (PresentationML) with
  separate parts for slides, layouts, masters, media, notes, and comments.
- If a template exists, template fidelity beats generic slide-design instincts.
- Reusing or duplicating a good existing slide is often safer than rebuilding it
  and hoping the theme still matches.
- Live window / presenter / slideshow control is out of scope — route to the
  `powerpoint` skill.

## 2. Inventory the deck before replacing content

- Count the reusable layouts, real placeholders, notes, comments, media, and
  recurring typography or color patterns first.
- Placeholder indexes and layout indexes are template-specific assumptions.
- Inspect the actual slide or template before targeting title, body, chart, or
  image shapes.
- Speaker notes, comments, and linked assets can live outside the visible slide
  surface.
- A missing or wrong placeholder target can silently land content in the wrong
  box or wrong layer.
- Master and layout settings can override local slide edits, so the visible
  problem often originates from the master template.

### Inventory checklist

1. `prs.slide_width` / `prs.slide_height` (aspect ratio)
2. Layout names and placeholder counts (`prs.slide_layouts`)
3. Per-slide shape list (title, body, pictures, charts, tables, free boxes)
4. Notes slides present?
5. Comments / linked media?
6. Theme fonts and dominant colors in use

## 3. Match content to the actual placeholders

- Count the actual content pieces before choosing a layout.
- Pick layouts based on the real number of ideas, columns, images, or charts the
  slide needs.
- Match the number of ideas exactly to the layout columns and provide ample
  whitespace around charts.
- Category counts and data series lengths must match or charts will break in
  ugly ways.
- Explicit sizing beats wishful thinking: text boxes, images, and charts need
  calculated, verifiable space.
- Select layouts with the exact number of placeholders your content will fill.
- Quote layouts are for real quotes, and image-led layouts are for slides that
  actually have images.
- For chart-, table-, or image-heavy slides, full-slide or two-column layouts are
  usually safer than stacking dense text above the visual.

## 4. Preserve the deck's visual language

- Theme, master, and layout files usually decide fonts, colors, and hierarchy
  more than any one slide does.
- Start from the deck's actual theme, fonts, spacing, and aspect ratio instead
  of improvising a new style.
- Reuse the deck's own alignment and spacing system instead of inventing a
  second visual language.
- Use common fonts for portability and strong contrast for readability.
- Preserve the template's visual logic first; prioritize adherence to the deck's
  existing visual language over originality.
- Combining slides from multiple sources requires normalizing themes, masters,
  and alignment afterward.

## 5. Run content QA and visual QA separately

- Text overflow, bad alignment, clipped shapes, weak contrast, and placeholder
  leftovers are normal first-pass failures.
- Run both content QA and visual QA; missing text and broken layout are
  different failure classes.
- Render or inspect the actual deck output before delivery when layout matters.
- Search for leftover template junk, sample labels, and placeholder text before
  calling the deck finished.
- Check notes, comments, labels, legends, and chart/table semantics separately
  from the visual pass.
- A deck can pass text extraction and still fail on overlap, clipping, wrong
  theme inheritance, or broken notes.
- Thumbnail grids and rendered slides usually reveal layout bugs faster than
  code or text inspection.
- Assume the first render is wrong and do at least one fix-and-verify cycle
  before calling the deck finished.
- Re-check affected slides after each fix because one spacing change often
  creates another issue.

### Content QA

- [ ] All intended titles/bodies present and free of sample/lorem text
- [ ] Notes and comments reviewed when in scope
- [ ] Chart categories align with series lengths; legends/labels correct
- [ ] Table headers and units correct

### Visual QA

- [ ] No overflow, clipping, or near-collisions
- [ ] Margins and alignment consistent with the deck system
- [ ] Contrast readable on expected background
- [ ] Aspect ratio matches the delivery target (16:9 vs 4:3)

## 6. Keep decks portable and review-safe

- Template masters can override direct edits in surprising ways.
- Complex effects may degrade across PowerPoint, LibreOffice, and conversion
  pipelines, so keep important content robust without them.
- Image sizing, font substitution, and placeholder mismatch are common reasons a
  deck looks good in code and bad on screen.
- Notes, comments, linked media, and merged decks can stay broken even when the
  visible slide looks fine.

## python-pptx orientation (verify against sources.md)

Typical create/edit path:

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()                 # or Presentation("template.pptx")
# discover layouts — do not hard-code indexes across templates
for i, layout in enumerate(prs.slide_layouts):
    print(i, layout.name)

slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Title"
prs.save("out.pptx")
```

Charts use `CategoryChartData` and `XL_CHART_TYPE` (see `charts.md`). Geometry
uses `Inches` / `Emu` / `Pt`. Always re-check the installed `python-pptx` docs
when API names matter.

## Common traps

- Placeholder text and sample charts often survive template reuse unless
  explicitly replaced.
- Directly editing one slide can fail if the real issue lives in the master or
  layout.
- Charts, icons, and text boxes need enough space; near-collisions are usually
  visible only after rendering.
- Layout indexes vary by template, so built-in assumptions from one deck often
  break in another.
- A missing placeholder or wrong shape target can silently put content in the
  wrong place.
- Counting the text ideas after choosing the layout usually leads to empty
  placeholders, weak hierarchy, or leftover template junk.
- Font substitution can move line breaks and wreck careful spacing.
- Speaker notes, comments, and linked media can stay broken even when the
  visible slide looks fine.
- A deck can pass text inspection and still fail visually because of overlap,
  contrast, or edge clipping.
- Editing from one slide alone can miss the real source of truth in the theme,
  master, or layout definitions.
- Choosing a quote, comparison, or multi-column layout without matching content
  usually makes the deck look templated rather than intentional.
- Combining or duplicating slides without checking masters and themes can create
  subtle inconsistency slide by slide.
- Aspect-ratio mismatches like `16:9` versus `4:3` can shift every placement
  decision even when each slide looks locally reasonable.
- Treating a live PowerPoint window as a static file — use `powerpoint` instead.

## Load order

1. This file for workflow and traps
2. `slides.md` / `charts.md` / `design.md` for patterns
3. `sources.md` before restating API or OOXML facts
