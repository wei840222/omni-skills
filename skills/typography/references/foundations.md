# Typography Foundations and Deep Dive

Use this reference when the question needs screen-rendering, print, or contested-camp detail beyond the hot-path rules in `SKILL.md`.

## Screen rendering and fallbacks

- System font stack renders instantly, web font renders identity. The tradeoff is the FOIT/FOUT flash: `font-display: swap` shows fallback then swaps (FOUT, shift risk), `block` hides text up to 3s then shows fallback (FOIT, no shift but invisible), `optional` loads if cached else stays fallback (no shift, no flash, first visit sees the fallback).
- Layout shift on swap is the descender jump: fallback and web font have different x-heights and metrics, so lines reflow when the swap fires. Match the fallback's x-height and advance width to the web font, or use `size-adjust` on the fallback, to kill the shift.
- Subpixel rendering is dead on macOS (Retina forces grayscale AA) and fading on Windows (HiDPI). Hinting matters below 16px on non-HiDPI: a hinted font (Verdana, Tahoma, Inter) stays crisp at 12px; an unhinted face turns to fuzz. Pick hinted faces for dense UI.
- Variable font as the only file: one woff2 with the axes you need replaces 4-6 static weights. Below ~3 weights the static set is smaller; above it, variable wins on bytes and on the optical range.
- `font-feature-settings` is the power tool: `tnum` (tabular figures) for any number that aligns in a column or changes, `lnum` vs `onum` (lining vs old-style figures) for data vs prose, `ss01`-`ss20` for stylistic sets the designer built in. Set on body, not per element, to avoid cascade cost.

## Print: where the rules invert

- Leading is physical in print: the space between baselines in points, not a multiplier. 10pt type on 13pt leading = 3pt of space. The ratio is the same concept, the unit is absolute.
- Print body sits at 9-11pt with 11-13pt leading (120-130%); screen body sits at 16-18px. Same ratio, different absolute sizes, because print is read at ~30cm and screen at ~50cm.
- Justify works in print, breaks on screen. Print has a hyphenation engine (InDesign, TeX) that breaks words to keep word spacing even; CSS `hyphens: auto` is spotty and the engine is weak, so justified web text gets rivers (word spaces stacking vertically) and loose lines. Ragged right is the web default for a reason.
- Tracking and kerning survive print exactly as set; what you see in the proof is what prints. Screen rendering rounds stem edges, so tracking reads ~5-10% tighter on screen than it will in print. Proof in the target medium, not on screen.
- Widows (last line of a paragraph alone at the top of the next column) and orphans (first line alone at the bottom) are print sins; CSS `widows` and `orphans` properties control them but support is uneven. Manual fix: tighten or loosen the paragraph by a word.
- Rivers form in justified text when word spaces stack vertically; the fix is hyphenation, looser tracking, or a narrower measure. A river is visible as a white diagonal stripe through a block of text.
- Print measure is wider: two-column work tolerates 50-60 chars per column, single-column can go to 75-90. Screen single-column stays at 45-60 because the eye tires faster on self-illuminated text.

## Where camps disagree

- **Serif vs sans for body**: serif wins in print (serifs guide the eye along the line, long-form reading-speed studies favor serif). Sans wins on low-DPI screen (serifs fuzz below 16px without hinting). On HiDPI screen the gap closes; pick by identity, not legibility. The competent picks sans for screen by reflex, the elite checks the DPI and the measure first.
- **Justified vs ragged**: justify for formal, print, multi-column work where hyphenation is available; ragged for screen, narrow measure, and any context without a hyphenation engine. Justify without hyphenation is worse than ragged in every case.
- **System fonts vs web fonts**: system wins on perf and zero flash; web font wins on identity and the optical range a system stack cannot give. Variable fonts narrow the gap (one file, full optical range) but cannot beat zero-cost. The frontier is first-visit perceived performance vs brand consistency; `font-display: optional` is the compromise for content below the fold.
- **Modular scale vs pragmatic sizing**: scale gives rhythm and a defensible type system; pragmatic sizing (pick the size that fits the content) gives flexibility and handles edge cases a scale cannot predict. Scale for systems and design tokens; pragmatic for editorial one-offs.
- **Hyphenation on web**: `hyphens: auto` with a `lang` attribute works in modern engines but break quality varies by language and browser. The elite hyphenates long-measure justified text in print, leaves web ragged unless the CMS has a server-side hyphenation engine.
