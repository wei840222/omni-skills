# Translation workflows by content type

Load the section that matches the job. Keep claims tied to `references/research-sources.md`.

## Documents and structured files

Extract structure (headings, tables, footnotes, alt text) before translating segments. Reassemble, then check layout overflow and cross-references.

## Web, CMS, and hreflang

Translate human-visible attributes (`title`, `alt`, `aria-label`) and decide URL policy per locale. Hreflang entries must be reciprocal and self-referencing; invalid region codes (for example `en-UK`) break discovery.

## Subtitles and dubbing scripts

Honor reading-speed ceilings (`subtitle_cps`, default 17 chars/sec unless configured). Condense to the budget instead of packing every syllable. Progressive drift usually means frame-rate conversion — ratio-scale timestamps rather than applying a constant offset.

## Transcreation and brand voice

When the job is effect (slogan, humor, campaign), brief the intended effect, deliver options, and attach back-translations so non-speakers can judge meaning.

## Games

Keep variable-safe grammar, respect on-screen limits, and run a culturalization pass for imagery, humor, and rating-sensitive content.

## Legal, medical, and certified work

Identify the receiving authority's certification regime first (sworn translator, notarization, apostille). Route risk-bearing segments through second-person revision or back-translation. Machine translation is out for these regimes unless counsel explicitly authorizes a controlled tool.

ISO 17100 defines a translation service as translation plus revision by a second person: https://www.iso.org/standard/59149.html

## Translation memory and XLIFF

Fuzzy leverage depends on segmentation. In-context (101%) matches may reuse silently; plain 100% matches still get a read because surrounding product context may have changed.

## Machine translation and post-editing

Before reading MT for style, check in order:

1. Dropped or inverted negation
2. Gender/number agreement
3. Glossary terminology
4. Politeness / register
5. Numbers and units copied unchanged

When edit distance grows roughly past 30%, delete the segment and translate fresh. `mt_policy` never overrides regulated-content bans.

DeepL and similar vendor docs are integration references only; they are not permission to send confidential source text: https://www.deepl.com/docs-api

## Jobs and vendor briefs

A brief includes audience, register, glossary/DNT, reference materials, file format, and deadline. Scope with word counts and realistic throughput before promising dates.
