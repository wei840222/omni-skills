# Locales, scripts, bidi, and locale data

Load when choosing locale codes, register, encoding/bidi repair, or number/date/name formatting.

## Locale codes (BCP 47)

Name a locale with language + script/region as needed (`es-419`, `zh-Hant-TW`). Bare `es` or `zh` is incomplete for product work.

Primary references:

- https://www.rfc-editor.org/rfc/rfc5646
- https://www.w3.org/International/articles/language-tags/
- https://www.w3.org/TR/ltli/
- https://unicode.org/reports/tr35/

## Register defaults

Decide formality once per locale and reuse it:

- T-V languages: tu/vous, tú/usted, du/Sie
- Japanese: politeness / keigo level
- Korean: speech level
- Arabic: MSA vs dialect

`variant_policy=regional` keeps es-ES / es-419 and pt-BR / pt-PT separate. Neutral variants exist for some legal/technical text and often read foreign in marketing.

## Encoding vs font vs bidi

| Symptom | Layer | Fix posture |
|---|---|---|
| `Ã©`, `â€™` | Encoding | Repair the decode hop; avoid retyping "fixes" |
| `?????` | Lossy charset | Fix DB/export charset, re-export |
| Tofu / fallback face | Font coverage | Choose a font that covers the script |
| Punctuation/numbers on the wrong side in Arabic/Hebrew | Bidi | Wrap embedded LTR in isolates; do not reverse storage order |

Primary bidi references:

- https://www.w3.org/International/articles/inline-bidi-markup/
- https://www.w3.org/International/questions/qa-bidi-unicode-controls
- https://www.w3.org/TR/string-meta/

## Numbers, dates, names

Format from locale data at render time. Keep numeric **values** unless conversion was requested. Personal name order and surname handling vary by culture — ask or follow the cited W3C personal-names guidance before inventing a rule.

- https://tc39.es/ecma402/
- https://www.w3.org/International/questions/qa-personal-names
- https://www.w3.org/TR/i18n-glossary/
