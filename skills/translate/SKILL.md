---
name: translate
description: >
  Translate and localize text, software strings, documents, subtitles, and
  marketing copy across language pairs. Use when translating anything, fixing
  machine-sounding output, localizing UI catalogs (JSON, XLIFF, .po, .strings,
  ARB, RESX, YAML), choosing locale/register (es-ES vs es-419, zh-Hans vs
  zh-Hant, tu/vous, keigo), handling ICU plurals, placeholders, RTL/bidi, CJK
  typography, expansion budgets, TM/fuzzy matches, MT post-editing, or
  regulated/certified work. Prefer `spanish`/`french`/`german`/`japanese`/
  `chinese` for native monolingual writing, `video-captions` for captions from
  audio, and `seo` for ranking multilingual pages after localization.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"chinese":"Write original Chinese copy natively when the task is no longer source-to-target translation.","copywriting":"Craft source marketing copy that later localization or transcreation must carry.","french":"Write original French copy natively when nothing is being translated.","german":"Write original German copy natively when nothing is being translated.","japanese":"Write original Japanese copy natively when nothing is being translated.","seo":"Handle multilingual SEO and hreflang ranking after pages are localized.","spanish":"Write original Spanish copy natively when nothing is being translated.","speech-to-text-transcription":"Produce transcripts before caption localization begins.","video-captions":"Generate and time-code captions from audio before translating the caption file."}'
---

## State location

Translate state may exist in
`<workspace>/translate/`, `<workspace>/memory/translate/`, or `~/translate/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/translate/`, `<workspace>/memory/translate/`, `~/translate/`.
3. If none exists and durable translation state must be created, default to
   `<workspace>/translate/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/translate/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

Legacy locations `~/Clawic/data/translate/`, `~/clawic/translate/`, and bare
`~/translate/` leftovers outside the resolver are migration sources only. Copy,
validate, and cut over only after the user chooses migration; do not write there
by default.

Host-shared memory such as workspace `MEMORY.md` is outside `<state_root>` and
needs separate consent. Shared contact, project, or subscription rows belong to
their owning skills and are listed separately below. Store only term/locale/job metadata under translate state by default. Keep MT/CAT API secrets, NDA source dumps, and third-party private data out unless the user explicitly asks to retain a named reference text.

```text
<state_root>/
├── config.yaml      # Declared defaults (source_lang, target_locales, formality, …)
├── memory.md        # Observed decisions, ## Boxes index, ## Due table
├── glossaries/      # Per-locale term bases
├── style/           # Per-locale register / voice notes
└── artifacts/       # Briefs, LQA reports, approved references (user-requested)
```

Shared boxes (separate consent / owning skills; formats in
`assets/memory-template.md`):

- Contacts / vendors → owning contacts skill box when installed
- Active localization projects → owning projects skill box when installed
- Tool subscriptions → owning finances skill box when installed

## When to Use

- Translating sentences, documents, UI catalogs, subtitle files, decks, or contracts
- Reviewing or repairing translations (machine register, term drift, reviewer complaints)
- Localizing a product: extraction, plurals/gender, placeholder safety, expansion, RTL, locale codes
- Choosing locale/register: es-ES vs es-419, zh-Hans vs zh-Hant, formal vs informal address
- Running jobs: scoping, briefing, glossary/TM, MT post-editing, quality scoring
- Regulated output where a mistranslation has consequences (legal, clinical, financial, certified)
- Not for monolingual native writing (`spanish`, `french`, `german`, `japanese`, `chinese`) or caption generation from audio (`video-captions`, `speech-to-text-transcription`)

## Core path

1. Resolve `<state_root>` before any state read/write.
2. Read `<state_root>/config.yaml` and `<state_root>/memory.md` when present; open only the boxes that `## Boxes` names for the current locale.
3. Name a target **locale** (script + region), not just a language, before the first target word.
4. Load only the `references/` leaf needed for the current job type.
5. Open `references/research-sources.md` before asserting CLDR plural categories, BCP 47 shape, bidi controls, expansion guidance, or ISO 17100 process claims as current fact.
6. Deliver through the Output Gates; write durable decisions back under `<state_root>/` in the same turn.

Precedence for any configured value:
`<state_root>/config.yaml` → host profile universals when separately authorized → Configuration defaults below.

## Progressive disclosure

Keep `SKILL.md` as the always-on control plane. Load exactly one `references/`
leaf for the active job type, plus `references/research-sources.md` when a
standard or policy claim must be asserted. Open `assets/memory-template.md`
only when writing durable state.

## Quick Reference

| Situation | Play | Load |
|---|---|---|
| Plain text / document | Locale + register + sentence-level translation + Output Gates | — |
| UI strings / catalogs / `%s` | Placeholders are payload; plurals from CLDR for the **target** | `references/software-strings.md` |
| Button/label overflow | Expansion budget by source length before design freeze | `references/software-strings.md` |
| Mojibake / tofu / RTL breakage | Encoding or bidi isolation, not "translation fixes" | `references/locales-and-scripts.md` |
| Locale / register / variant choice | BCP 47 shape + per-locale formality | `references/locales-and-scripts.md` |
| Web / hreflang / CMS | Translatable attributes, reciprocal hreflang, URL policy | `references/workflows.md` |
| Subtitles / dubbing scripts | Reading-speed and line budget first | `references/workflows.md` |
| Marketing / humor / brand voice | Transcreation brief → options + back-translations | `references/workflows.md` |
| Legal / medical / certified | Regime routing + second-person or back-translation on risk segments | `references/workflows.md` |
| Glossary / DNT / term drift | One term, one rendering, written down | `references/terminology-and-quality.md` |
| TM / XLIFF / fuzzy grid | Leverage math + segmentation rules | `references/workflows.md` |
| MT post-editing | Five-failure checklist before style reading | `references/workflows.md` |
| Numbers / dates / names | Format from locale data; keep values unless conversion requested | `references/locales-and-scripts.md` |
| Job scoping / vendor brief | Word counts, throughput, brief contents | `references/workflows.md` |
| Primary citations | Live official pages before policy claims | `references/research-sources.md` |
| State write formats | Destinations, identity keys, thresholds | `assets/memory-template.md` |

## Core Rules

1. **Translate the sentence, with the paragraph as context.** Split/merge/reorder when the target needs it; changing a claim, number, or hedge is a defect. A bilingual reader should point at the source clause for every target claim.
2. **No string without context.** Record missing `msgctxt` / screenshot / developer comment as an assumption in the delivery note instead of guessing silently.
3. **One message equals one string with named placeholders and ICU plural/select forms.** Avoid concatenating fragments that freeze English word order.
4. **Plural categories come from CLDR for the target locale.** English `one/other` is not Russian, Arabic, or Japanese. Confirm categories before filling a catalog (`references/software-strings.md`).
5. **Budget expansion from source length before layout freezes.** Short English strings expand most; CJK often contracts but needs larger line height. Re-check live W3C/i18n size guidance when quoting percentages (`references/research-sources.md`).
6. **One term, one rendering, written down the first time.** Accepted and rejected renderings become glossary rows with part of speech and reason (`references/terminology-and-quality.md`).
7. **Register is a per-locale decision reused across the product.** T-V, keigo, Korean speech levels, and MSA vs dialect switch mid-product only when the brief changes.
8. **Treat machine output as a draft.** Before style reading, check dropped/inverted negation, agreement, glossary terms, politeness, and unchanged numbers/units. Regulated content stays human-governed regardless of `mt_policy`.
9. **Risk-bearing segments get a second pass.** Prefer second-person revision (ISO 17100 shape). When unavailable, use delayed self-review plus back-translation on numbers, dosages, negations, obligations, deadlines, and names.

## Output Gates

Before delivery:

- Target is a locale (script + region) with consistent register applied
- Placeholder parity: same set/count/names; positional markers when order changes
- Glossary and do-not-translate list honored
- Numbers/dates/currencies/units: values unchanged unless conversion requested; formats adapted
- Negations, quantities, dosages, obligations, and names re-read against source in isolation
- Every source clause has a home; no invented target claims
- Delivery states audience + register assumptions and any missing-context segments
- Durable decisions written under `<state_root>/` using `assets/memory-template.md`

## Configuration

Store declared defaults in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| source_lang | BCP 47 text | en | Assumed source when a job omits one; anchors expansion planning |
| target_locales | BCP 47 list | none | Default locales; each gets glossary/style boxes |
| formality | formal / informal / per-locale | per-locale | T-V / keigo / speech-level default |
| variant_policy | regional / neutral | regional | Separate regional variants vs one neutral form |
| mt_policy | never / draft-only / mtpe / free-rein | draft-only | Machine-output allowance; `never` for regulated content |
| review_stage | none / self-review / second-person / back-translation | self-review | Pre-delivery gate |
| placeholder_style | icu / printf / mustache / i18next | icu | Generated message syntax |
| catalog_format | json / xliff / po / strings / xcstrings / arb / resx / yaml / properties | json | Catalog shape |
| subtitle_cps | number (8-25) | 17 | Subtitle reading-speed ceiling |
| deliverable_shape | target-only / bilingual-table / inline-comments | target-only | Output shape |
| cat_tool | none / trados / memoq / phrase / crowdin / lokalise / weblate / poedit | none | Export/import conventions |

Preference areas recorded into config when stated: tooling, key/comment conventions, platform (iOS/Android/web/print), brand voice per locale, risk posture, review cadence, and how much reasoning to show.

## Failure decoding

| Symptom | Likely cause | First move |
|---|---|---|
| `Ã©` / `â€™` mojibake | UTF-8 read as Latin-1 | Find the legacy decode hop |
| `?????` gaps | Lossy single-byte conversion | Fix charset at DB/export boundary |
| Tofu boxes | Missing font coverage | Check script coverage, not the file bytes |
| String stays English | Never extracted / wrong runtime locale | Grep literal; confirm resolved locale |
| `%!s(MISSING)` / crash | Placeholder parity break | Positional forms; parity check per segment |
| Wrong grammar at 2/21/101 | Missing CLDR categories | Add target categories at file level |
| Arabic period on the wrong side | Missing bidi isolation | Isolate embedded LTR; avoid string reversal |
| Button scrollbar / truncation | Expansion | Re-measure; shorten source before over-condensing target |
| Progressive subtitle drift | Frame-rate conversion | Ratio-scale timestamps |
| Wrong page ranks | Non-reciprocal / invalid hreflang | Reciprocity + self-reference audit |
| Same term, three renderings | No glossary / polluted TM | Consolidate, then enforce at delivery |

## Security & Privacy

- Record MT/CAT credential **pointers** only (`env:DEEPL_AUTH_KEY`, `keychain:…`, `1password:…`); values stay in the environment or password manager.
- Before proposing MT, state which content would leave the machine. For legal, medical, personal, or confidential material, prefer an on-machine workflow.
- Keep preferences, glossaries, style decisions, and delivery records under `<state_root>/`. Terms, locale codes, and word counts only by default.

## Do Not Translate (default)

Code and identifiers · placeholders in every syntax · HTML/XML tag and attribute names · URLs/paths/extensions · emails/phones · API endpoints/params/headers/error codes · brand names without a registered local form · unit symbols · license IDs · English-kept key names · legal-entity suffixes · citations/DOIs/ISBNs · quoted UI that the reader will still see in the source language.

Quoted error messages are translated only when the running product UI is localized. CJK brand naming is a trademark/marketing decision, not a translator default.
