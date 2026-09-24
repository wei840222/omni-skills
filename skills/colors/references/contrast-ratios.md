# Contrast Ratios (WCAG 2.2)

Measure contrast with relative luminance. Do not round a failing ratio up to a pass.

| Level | Normal text | Large text (18pt, or 14pt bold) | UI and meaningful graphics |
| --- | --- | --- | --- |
| AA | ≥ 4.5:1 (SC 1.4.3) | ≥ 3:1 (SC 1.4.3) | ≥ 3:1 (SC 1.4.11) |
| AAA | ≥ 7:1 (SC 1.4.6) | ≥ 4.5:1 (SC 1.4.6) | no AAA non-text criterion |

Inactive controls, pure decoration, and logotypes have no contrast requirement under these criteria.

## Thresholds on white

| Foreground | Ratio | Use |
| --- | --- | --- |
| `#767676` | 4.54:1 | Bare AA for normal text |
| `#777777` | 4.48:1 | Fails normal-text AA |
| `#757575` | 4.61:1 | Safer gray floor for normal text |
| `#FF0000` | 4.00:1 | Large text or UI, not normal text |
| `#00FF00` | 1.37:1 | Backgrounds only |
| `#0000FF` | 8.59:1 | AAA normal text |
| `#3B82F6` | 3.68:1 | Large text or UI; not normal text |
| `#9CA3AF` | 2.54:1 | Fails normal-text AA |

`#3B82F6` with `#9CA3AF` text is about 1.45:1. Replace that pair with `#FFFFFF` text on a darker blue such as `#1D4ED8` (about 6.7:1) when the label is normal text.

## Color is not the only signal

About 1 in 12 men (8%) have color-vision deficiency (NIH National Eye Institute; Colour Blind Awareness). Add an icon or text label beside the hue, then check the screen in grayscale.

```html
<!-- Hue alone cannot carry the state -->
<span class="text-green-500">Active</span>

<!-- Icon + text + hue -->
<span class="text-green-500">✓ Active</span>
<span class="text-red-500">✗ Inactive</span>
```
