---
name: screenshot
description: Capture screenshots of desktop apps, browser pages, simulators, and CI
  environments. Load when you need to capture screenshots for debugging, QA, visual
  reviews, or before/after visual comparisons.
metadata:
  openclaw: '{"emoji": "📸"}'
  related-skills:
  - playwright
  - image
  - image-edit
  - documentation
  - video
---

## When to load

Load when the task requires capturing screenshots of a desktop app, browser page, simulator, region, or full screen for debugging, QA, or visual review.

## Tool Choice

| Context | Best default | Why |
|---------|--------------|-----|
| macOS desktop or window | `screencapture` | Built-in, reliable, supports silent, interactive, region, and window capture |
| iOS Simulator | `xcrun simctl io booted screenshot` | More reliable than generic desktop capture for simulator output |
| Linux Wayland | `grim` + `slurp` | X11 tools often fail or behave oddly on Wayland |
| Linux X11 / headless CI | `scrot` or browser-native capture | Works in minimal or virtual-display environments |
| Windows desktop capture | `nircmd savescreenshot` or Pillow `ImageGrab` | Easier than verbose PowerShell screen APIs |
| Web page or web app | Playwright | Best for stable viewport, element, full-page, masked, and regression screenshots |
| Visual diff / screenshot tests | Playwright with fixed viewport | Better control over animations, caret, masks, and reproducibility |

Default to the most native capture path first. Move to browser-native tooling when determinism, masking, element capture, or visual regression matters more than convenience.

## Core Rules

### 1. Pick the capture path by artifact, not by habit

- Desktop UI screenshots usually want OS-native tools.
- Web pages and web apps usually want browser-native capture, not a desktop screenshot of the browser window.
- Simulator screenshots should come from the simulator tooling when possible.
- Use region, window, or element capture when the point is local; use full screen or full page only when the full context matters.

### 2. Stabilize the target before capturing

- Dynamic pages should settle before capture: wait for network idle or the specific element that matters, then give fonts and transitions a brief moment to finish.
- Wait for the real rendered state to exist before taking the screenshot.
- For browser capture, prefer explicit readiness over blind sleeps when possible.
- If the page remains continuously active, wait for the specific UI state required rather than seeking perfect stillness.

### 3. Freeze viewport, scale, zoom, and theme for reproducibility

- Screenshot comparisons are meaningless if viewport, zoom level, theme, or device scale changed.
- For browser captures, fix the viewport before taking baselines or before/after images.
- Retina and HiDPI displays can produce more pixels than expected; decide whether you want physical pixels or CSS-scale output and keep that choice consistent.
- If dark/light mode matters, capture both intentionally instead of mixing them accidentally.

### 4. Capture the smallest useful scope

- Element, region, or window screenshots are usually better than noisy full-screen captures.
- Full-page screenshots are useful for audits and archives, but long pages become hard to read and compare.
- For browser work, element screenshots or clipped regions usually produce cleaner diffs than full-page output.
- If the screenshot is evidence, keep enough surrounding context that the user can understand what they are looking at.

### 5. Remove noise before you capture

- Exclude unstable UI elements when they are not the subject: cursors, carets, toasts, chat widgets, notifications, loading spinners, timestamps, and randomized content.
- Mask out secrets, personal data, tokens, and internal URLs prior to capture.
- For Playwright-style browser capture, features like disabled animations, hidden carets, and masking are worth using when visual stability matters.
- If the noise is the bug, keep it; otherwise remove it.

### 6. Use the right output format

- PNG is the default for screenshots, UI, code, terminals, and text-heavy captures.
- JPEG is for photographic content, not normal screenshots.
- WebP is fine for sharing or storage when compatibility is acceptable, but default to PNG if the consumer expects plain PNG files.
- Preserve screenshot quality by keeping formats uncompressed or losslessly compressed unless the user explicitly wants smaller lossy output.

### 7. Make automation and CI captures debuggable

- On failures, save a screenshot immediately before retrying or moving on.
- Use stable filenames for baselines and timestamps for ad hoc or batch captures.
- In CI, identical viewport and deterministic state matter more than raw screenshot volume.
- Headless runs should prefer browser-native screenshots over trying to screen-grab the host display.

### 8. Validate that the screenshot is actually useful

- Check that the important detail is visible, legible, and not cropped away.
- Verify that secrets are not still visible in tabs, sidebars, URLs, notifications, or test data.
- Before/after comparisons should use the same viewport, zoom, theme, and state.
- A screenshot is bad if it is technically correct but useless for the human who needs it.

## High-Value Patterns

- macOS: `screencapture -x out.png` for silent capture, `-i` for interactive selection, `-R x,y,w,h` for a fixed region.
- iOS Simulator: `xcrun simctl io booted screenshot out.png`
- Linux Wayland: `grim -g "$(slurp)" out.png`
- Playwright page capture: wait for the target state, then use page, element, clipped, or full-page screenshots deliberately.
- Playwright stability features worth remembering: fixed viewport, disabled animations, hidden caret, masks for sensitive regions, and stable theme/media settings.

## Common Traps

- Taking a browser-window screenshot when an element or page screenshot was the real need.
- Capturing before fonts, data, or layout transitions finish.
- Comparing screenshots with different viewport sizes or zoom levels and treating the diff as meaningful.
- Using JPEG for screenshots and blurring text, edges, and code.
- Letting timestamps, cursor blinks, notifications, or random data ruin visual diffs.
- Forgetting that Wayland breaks familiar X11 screenshot tools.
- Sharing screenshots with secrets still visible in tabs, sidebars, URLs, or test accounts.
- Taking full-page captures of huge pages and ending up with unreadable evidence.
