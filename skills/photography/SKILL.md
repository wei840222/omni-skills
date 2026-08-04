---
name: photography
description: Advise on camera settings, exposure, focus, composition, lighting, flash, RAW editing, and genre-specific workflows (portrait, landscape, action, street, smartphone). Use when the user asks how to photograph something, what settings to use, how to fix a photo problem, or how to improve their photos — including phone photography.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📷"}'
---

## Diagnostic Workflow

When the user describes a photo problem, follow this sequence:

1. **Identify the symptom**: blurry, dark, bright, noisy, wrong color, bad composition
2. **Ask clarifying questions if needed**: camera model, lens, lighting conditions, shooting mode
3. **🔴 CHECKPOINT**: Before recommending settings, confirm you understand the user's goal (sharp action shot vs. artistic motion blur, bright and airy vs. moody and dark)
4. **Diagnose the root cause**: use the Troubleshooting section to match symptom → cause
5. **Provide specific settings**: give exact aperture, shutter speed, ISO values
6. **Suggest post-processing fix if applicable**: AI denoise, WB correction, exposure adjustment
7. **Prevent recurrence**: explain the principle so the user can self-diagnose next time

If the user asks "how to photograph X" (not a problem), skip to step 5 and provide genre-specific settings from the Settings by Genre section.

**🛑 STOP if**: The user's question is ambiguous between multiple genres (e.g., "photograph my kid" could be indoor portraits or outdoor action). Ask which scenario applies before giving settings.

## Exposure Triangle

- ISO: double ISO = double brightness + double noise. Stay at base ISO when possible. Dual native ISO cameras (Sony, Panasonic) have a second clean base — use it in low light instead of pushing the first ISO.
- Aperture: f/2.8 = shallow DOF, f/8–11 = sharp across frame. Most lenses peak 2 stops down from wide open. Diffraction softens past f/11 (APS-C) or f/16 (full frame).
- Shutter: 1/focal-length minimum handheld without stabilization. With IBIS, expect 3–5 stops of compensation — a 50mm lens can shoot 1/15s or slower.
- Expose for highlights — blown highlights are unrecoverable. ETTR (Expose To The Right) maximizes SNR; pull exposure down in post.

## Focus

- Focus on the nearest eye for portraits. Enable real-time eye-AF on mirrorless bodies — it tracks humans, animals, and vehicles.
- Use AF-ON (back-button focus) to separate focus from shutter. Single-point AF for precision, wide-area tracking for movement.
- Modern phase-detect AF covers 90%+ of the frame. Trust it; stop manually repositioning focus points for static subjects.
- Hyperfocal for landscapes: focus 1/3 into scene at f/8–11. Use focus peaking + magnification to confirm.
- Diffraction is real — don't stop past f/11 (APS-C) or f/16 (FF) just for more DOF.

## Troubleshooting

**Problem: Blurry photos**
- If motion blur (subject moving) → increase shutter speed to 1/500s+ for action, 1/250s for people moving
- If camera shake (entire image soft) → use 1/focal-length rule minimum, enable IBIS, or use tripod
- If out of focus → check focus point placement, switch to single-point AF for precision, use back-button focus

**Problem: Too dark or too bright**
- If underexposed → check histogram (not LCD), increase ISO or open aperture, use ETTR technique
- If overexposed → expose for highlights, use -1 to -2 EV compensation for bright scenes, bracket exposures
- If high contrast scene → use graduated ND filter, bracket for HDR, or expose for highlights and lift shadows in post

**Problem: Harsh shadows or flat lighting**
- If harsh midday sun → move subject to open shade, use as backlight, or add fill flash at -2 EV
- If flat/overcast → add directional light with flash, or use reflector to add dimension
- If backlighting face → use fill flash or reflector to illuminate subject

**Problem: Noisy/grainy images**
- If shot at high ISO → use AI denoise (Topaz, DxO PureRAW, Lightroom Denoise)
- If underexposed and lifted → expose brighter next time (ETTR), noise is worse in shadows
- If old camera with poor high-ISO performance → stay at base ISO, use tripod or flash

**Problem: Colors look wrong**
- If wrong white balance → set custom WB or shoot RAW and adjust in post
- If mixed lighting → set WB to dominant source, correct rest in post with local adjustments
- If colors look different on different screens → calibrate monitor, export with correct color space (sRGB for web)

## Composition Gotchas

- Level the horizon — it's the first thing viewers notice is wrong. Enable grid overlay.
- Leading lines, frame-within-frame, and negative space work. Odd subject counts (3, 5) read better than even.
- Color/tonal contrast draws the eye without any compositional rule — warm subject on cool background.
- Take one step left or right to clear busy backgrounds before recomposing.

## Natural Light

- Golden hour (1h after sunrise / before sunset): warm, soft, directional.
- Blue hour (20–30min after sunset): even, moody.
- Overcast = giant softbox — ideal for portraits.
- Midday sun: backlight or open shade, never direct overhead.
- Window light: subject faces the window, not the camera.
- Mixed lighting: set WB to dominant source, correct the rest in post.

## Flash

- Bounce off ceiling/wall — direct flash is harsh and flat.
- Flash exposure compensation: start at -1 to -2 stops to blend with ambient.
- HSS (high-speed sync) allows wide aperture in daylight beyond the camera's sync speed (typically 1/200–1/250s).
- Off-camera flash: 45° from subject, elevated — creates dimension.
- TTL works for most situations; switch to manual power when background exposure must stay constant across recompositions.

## Settings by Genre

**Portraits:** f/1.8–2.8 (f/4 for groups), eye-AF, +1/3 EV for skin.

**Landscapes:** f/8–11, tripod + 2s timer (mirror lock only for DSLRs), bracket for HDR or use graduated ND.

**Sports/Action:** 1/500s minimum (1/1000s+ for motorsport), continuous AF + subject recognition, burst at max fps.

**Street:** f/5.6–8, zone focus at 2–3m, silent/electronic shutter for discretion.

## RAW Editing Workflow

1. Import with keywords, ratings, color labels — not later when context is gone.
2. Cull: reject blur, blink, miss immediately.
3. Global: exposure, WB, contrast, highlight/shadow recovery.
4. Local: dodge/burn, graduated/radial filters, subject/sky masks.
5. Color grade: consistent look across set.
6. Export: sRGB for web, AdobeRGB for print. Sharpen per output size.

- Calibrated monitor + hardware calibrator (X-Rite, Datacolor) quarterly. Laptop screens lie.
- AI denoise (Topaz, DxO PureRAW, Lightroom Denoise) recovers previously unusable high-ISO shots.
- Sharpen last, after resize. If you notice the edit, you went too far.

## Gear

- Lenses > bodies. A great lens on an older body beats a kit lens on the latest body.
- 50mm f/1.8: cheap, sharp, teaches DOF and composition. Best first prime.
- Carbon fiber tripod saves weight; flimsy tripod is worse than none.
- One good light > three bad ones. Start with a single speedlight or LED.

## Backup: 3-2-1-1-0

3 copies, 2 media types, 1 offsite (cloud), 1 offline/air-gapped, 0 errors (verify checksums).

- Folder: `YYYY/YYYY-MM-DD_EventName`
- Rename on import: `YYYYMMDD_ProjectName_0001.ext`
- Archive RAW forever, even rejects — storage is cheap, moments aren't.
- Test-restore a random sample periodically to confirm integrity.

## Smartphone Photography

- Default camera app handles most scenes via computational photography (multi-frame HDR, Night mode). Use it.
- For manual control: ProCam (iOS), ProShot (Android) — set ISO, shutter, focus manually.
- Phone RAW = DNG. Edit in Lightroom Mobile, Snapseed, or Darkroom.
- Portrait mode simulates bokeh computationally — struggles with fine hair, glasses, complex edges.
- Third-party clip-on lenses (Moment, Sandmarc) add wide-angle, macro, or anamorphic.

## Don't Do This

**Don't chimp constantly** — checking the LCD after every shot means you miss the next moment. Review histograms periodically, not every frame.

**Don't shoot wide open for groups** — f/1.8 gives shallow DOF that will leave some faces out of focus. Use f/4 or narrower for groups of 3+ people.

**Don't stop down past diffraction limit** — f/16 on APS-C or f/22 on full frame softens the entire image. If you need more DOF, use focus stacking instead.

**Don't trust the LCD for exposure** — LCD brightness deceives, especially in bright sunlight. Always check the histogram for highlight clipping on the right side.

**Don't use direct flash** — bouncing off ceiling/wall at -1 to -2 EV blends with ambient. Direct flash is harsh, flat, and creates red-eye.

**Don't crop at joints** — cutting at ankles, wrists, or knees looks awkward. Crop mid-limb or show the full body.

**Don't ignore lens distortion** — wide-angle lenses bend straight lines at edges. Correct in post or keep critical lines away from frame edges.

**Don't assume phone portrait mode is real bokeh** — computational bokeh fails on fine hair, glasses, and complex edges. Use it for simple subjects against clean backgrounds.

## Validation Checklist

After recommending settings, verify:

- [ ] Shutter speed is fast enough for the subject motion (1/500s+ for action, 1/250s for people moving)
- [ ] Aperture gives sufficient DOF for the subject (f/4+ for groups, f/1.8–2.8 for single portraits)
- [ ] ISO is as low as possible while maintaining shutter speed (base ISO or dual native ISO)
- [ ] Exposure is set for highlights (check histogram, not LCD)
- [ ] Focus mode matches subject behavior (single-point for static, tracking for moving)
- [ ] White balance matches dominant light source
- [ ] Backup strategy is in place before shooting (3-2-1-1-0 rule)
