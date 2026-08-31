# Numbers That Decide

Every one of these is a threshold, not a preference. Sources are named so they can be re-verified.

| Thing | Number | Where it comes from |
|---|---|---|
| Body text floor | 16px web (`min_body_px`); 17pt iOS, 16sp Android default | Platform defaults; below 16px mobile browsers zoom on focus |
| Measure (line length) | 45-75 characters, ~65ch target | Bringhurst; wider needs more leading, narrower breaks rhythm |
| Line height | Body 1.4-1.6; display 1.05-1.25 | Leading ratio falls as size rises |
| Contrast, body text | 4.5:1 | WCAG 1.4.3 AA (7:1 at AAA) |
| Contrast, large text (≥24px / ≥18.66px bold) | 3:1 | WCAG 1.4.3 AA (4.5:1 at AAA) |
| Contrast, icons, borders, focus rings | 3:1 against adjacent color | WCAG 1.4.11 |
| Target size | 24×24 CSS px floor, 44×44 default | WCAG 2.5.8 AA / 2.5.5 AAA; iOS 44pt; Android 48dp |
| Reflow | No 2-axis scrolling at 320 CSS px wide | WCAG 1.4.10 (equals 400% zoom at 1280px) |
| Text-spacing survival | line-height 1.5, paragraph 2em, letter 0.12em, word 0.16em | WCAG 1.4.12 — nothing may clip or overlap |
| Micro transition (hover, toggle) | 100-200ms | Below ~100ms reads as instant, above ~300ms as sluggish |
| Standard transition (panel, sheet) | 200-300ms; full-screen 300-500ms | Larger travel needs proportionally more time |
| Perceived-response budget | <100ms instant · <1s uninterrupted flow · <10s attention limit | Nielsen's response-time limits |
| Interaction budget | 400ms | Doherty threshold |
| Loading affordance | Spinner <1s · skeleton 1-10s · determinate progress >10s | Skeletons below 1s add flicker, not comfort |
| Page vitals | LCP ≤2.5s · INP ≤200ms · CLS ≤0.1 | Core Web Vitals "good" thresholds, 75th percentile |
| Usability sample | 5 per audience ≈ 84% of problems | `1 − (1 − 0.31)ⁿ` (Rule 9) |
| SUS benchmark | 68 = average; ~80+ = top quartile | Sauro's benchmark database |
| Print | 3mm bleed · 300 ppi at final size · ≤300% total ink | the print-production guidance |
| Favicon | Must resolve at 16px | the brand guidance |
