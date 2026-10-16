# For Print Production: Technical Precision

- Confirm the printer's written spec before locking files. Common planning heuristics (not substitutes for the printer): ~3 mm bleed for many small jobs; ~5 mm or more for large format; keep critical content inside a safe zone inset from trim.
- Use CMYK (or the printer's required profile) for process color; convert RGB images intentionally; specify spot/Pantone only when the job and budget call for it.
- Target ~300 dpi at final size for continuous-tone print imagery unless the printer states otherwise; keep high-res links rather than embedding low-res previews.
- Embed or assign the agreed ICC profile; note coated vs uncoated stock; soft-proof with the correct profile when available.
- Outline fonts or embed them per the printer's RIP rules; check special characters and non-Latin scripts.
- Review transparency, overprints, and knockouts; flatten when the printer/RIP requires it.
- Specify stock weight, coating (matte/gloss/satin), binding, and finishing (die-cut, foil, emboss) in the quote package.
- Run preflight for missing links, RGB leftovers in CMYK jobs, insufficient bleed, and low-resolution images.
- Prefer PDF/X family delivery when the printer requests an ISO 15930 PDF/X workflow; ask which PDF/X flavor they accept rather than guessing.
