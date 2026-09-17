# Scanner Guidelines

## Core rules

### 1. Browser-first wins

- Prefer the browser or browser-like path first because `jscanify` is strongest there.
- Prefer CDN or local project dependency over native OpenCV builds.
- If the user only needs one scan, choose the lowest-friction path.

### 2. Detect before you enhance

- First run boundary detection on the original image.
- Only add grayscale, contrast, or thresholding after edge detection fails.
- Keep focus on the default extraction path before applying image enhancement.

### 3. Expect flat, visible borders

- Best results come from one document on a contrasting background.
- Top-down or near-top-down photos are safer than steep angles.
- Hard shadows, fingers over corners, or white paper on white tables reduce reliability.

### 4. Preserve the original

- Keep the original input image untouched.
- Save the corrected export separately.
- If the scan is for legal, accounting, or archive use, keep the original photo too.

### 5. Manual correction beats fake certainty

- If auto-detection is clearly wrong, report the failure accurately.
- Ask for a better photo or switch to a manual-corner workflow.
- Wrong corners produce worse output than no crop.

## Common traps

- Busy backgrounds can confuse edge detection.
- Low-contrast document-on-table shots fail more often than users expect.
- Glare can hide one full edge and collapse the crop.
- Very curved paper is not a normal document-scan case.
- Receipts with torn edges or shadows often need one retry with a better photo.
- OCR and document scanning are different jobs; scan first, OCR second.

## Scope

This skill ONLY:
- Chooses and applies a document-scanning workflow
- Prioritizes `jscanify` by default
- Produces cropped, perspective-corrected scan-style images

This skill NEVER:
- Claims OCR accuracy improvements by itself
- Recommends paid SDKs by default
- Reimplements document detection from scratch unless the user explicitly wants that

## External endpoints

| Endpoint | Purpose |
|----------|---------|
| `https://docs.opencv.org/` | Load OpenCV.js in browser-first workflows |
| `https://cdn.jsdelivr.net/` | Load `jscanify` without global install |
