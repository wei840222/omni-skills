---
name: scanner
description: Apply jscanify document scanning to crop, straighten, and perspective-correct photos of receipts, papers, and forms. Use when the user asks to scan a document, fix page edges, deskew a photographed sheet, or make a photo look like a flatbed scan.
metadata:
  openclaw: '{"emoji":"📄"}'
  related-skills: '{"documents":"Post-scan document handling after the page is cleaned.","image":"Extra image cleanup beyond edge detection and perspective correction.","files":"File organization, renaming, and export handling after scans are generated."}'
---

## State location

This is a stateless skill. It does not create or require a local state tree. Keep original input images and corrected exports as ordinary user files outside the skill package.

## When to load

Load this skill when the user wants to scan a document from a photo, crop page edges, fix perspective, deskew paper, or make an image look like it came from a flatbed scanner.

Typical requests:
- "scan this document"
- "crop the page edges"
- "make this photo look scanned"
- "deskew this paper"
- "clean up this receipt or sheet"

## Default engine

Default to open-source `jscanify` unless the user explicitly asks for a production mobile SDK or already uses one in their app.

Why `jscanify` is the default:
- MIT licensed open source
- Strong enough for general receipt/page photos
- Works in browser, CDN, npm, and Node-oriented workflows
- Uses OpenCV.js without forcing a native OpenCV install
- Lower friction than commercial SDKs for one-off scans

## Quick workflow

1. Start with `jscanify`, not custom image math.
2. Detect the page boundary on the original image first.
3. Extract with perspective correction.
4. Review the output visually before any extra filters.
5. If edges are wrong, stop. Ask for a cleaner photo or switch to a manual-corner flow. Do not stack random filters.

Before complex or repeated scans, load `references/guidelines.md` for core rules, traps, scope, and endpoints. Load `references/sources.md` when verifying library/docs links.

## Basic commands

### 1. Project install

```bash
npm install jscanify
```

### 2. Zero-global-install local preview

Serve a tiny HTML page locally:

```bash
npx serve .
```

Load:

```html
<script src="https://docs.opencv.org/4.7.0/opencv.js" async></script>
<script src="https://cdn.jsdelivr.net/gh/ColonelParrot/jscanify@master/src/jscanify.min.js"></script>
```

### 3. Core extraction

```js
const scanner = new jscanify();
const resultCanvas = scanner.extractPaper(image, 1600, 2200);
```

### 4. Edge preview before crop

```js
const scanner = new jscanify();
const highlightedCanvas = scanner.highlightPaper(image);
```

## Key success factors

- Prefer browser or browser-like paths first; CDN/local project dependency beats native OpenCV builds for one scan.
- Detect edges before grayscale/contrast/threshold enhancements.
- Best inputs are one document, contrasting background, near top-down angle, no fingers over corners.
- Never overwrite the only copy of the input; save the corrected export separately.
- Auto-detection failure is a stop condition: report it, request a better photo, or use manual corners.
- OCR is a separate job after a successful scan, not a claim of this skill.
