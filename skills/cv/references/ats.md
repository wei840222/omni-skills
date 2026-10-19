# ATS — Parseability and Keyword Fit

Load for layout, export format, section headers, and keyword integration questions.

## Safe defaults

Prefer:

- Single-column layout
- Standard fonts: Arial, Calibri, Times New Roman, Georgia (≈10pt+)
- Simple bullets (`-` or `•`)
- Standard headers: Experience / Work Experience, Education, Skills, Summary
- Text-layer PDF **or** DOCX (not a scanned image)
- Filename like `FirstName_LastName_Resume.pdf`

Prefer alternatives when these appear:

- Tables, multi-column layouts, text boxes used for structure
- Headers/footers holding critical contact or dates
- Images, logos, icons used as text
- Creative headers ("My Journey") instead of "Experience"
- Fancy symbols (✓, ➤, ★) as the only bullet markers
- Keyword stuffing lists disconnected from real experience

## Keyword strategy

1. Extract must-have terms from the job description.
2. Integrate exact phrasing where the user's experience supports it.
3. Include acronym **and** spelled-out forms when both appear in the market (for example `AWS (Amazon Web Services)`).
4. Place critical terms inside achievement bullets first; skills section second.
5. Prefer natural repetition of critical terms over stuffing.

Modern ATS increasingly uses context; fake density still risks human rejection even when parsers accept the file.

## Heuristics vs facts

Industry materials often cite high ATS filter rates and very short first-pass scan times. Treat precise percentages and "N-second" claims as heuristics unless a live primary in `sources.md` still supports the number. Prefer actionable guidance: parseable layout, quantified impact, and JD keyword fit.

## Pre-export checks

- Selectable text (copy/paste works)
- Single column, consistent date format
- Standard section headers
- No critical content only in images/headers/footers
- Keywords mirrored from the JD only where truthful
