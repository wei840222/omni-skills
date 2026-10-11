---
name: text
description: >
  Process, clean, and format text for encoding/line-ending hygiene, CSV/regex
  transforms, localization, academic citations, creative-writing craft, and
  marketing copy patterns. Use when the user needs string transforms, style
  enforcement, citation formatting, or locale-aware copy rules. Prefer
  `writing` for voice-matched long prose, `copywriting` for campaign copy,
  `markdown` for Markdown syntax, `csv`/`regex` for dedicated parsers, and
  `grammar` for grammar-only fixes.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"📝"}'
  related-skills: '{"writing":"Voice-matched long-form drafting and rewrite.","copywriting":"Campaign and direct-response marketing copy.","markdown":"Markdown syntax, fences, and parser targets.","csv":"Dedicated CSV/TSV parsing and transforms.","regex":"Regex pattern design beyond quick text recipes.","grammar":"Grammar-only correction without style systems.","storytelling":"Narrative craft beyond general text hygiene.","book-writing":"Book-length manuscript structure.","latex":"LaTeX when Markdown or plain citation patterns are not enough."}'
---

# Text

**Knowledge-only** patterns for everyday text hygiene and style systems. Does not
store local runtime state. Does not invent citation facts or locale rules from
memory when a standard must be verified.

## When to use

- Detect encoding, BOM, line endings, and invisible Unicode before transforms
- Clean whitespace, normalize quotes/dashes, count unique lines, extract emails/URLs
- Format citations in APA / MLA / Chicago when the user names a style
- Apply creative-writing craft (voice, dialogue, show-vs-tell) from references
- Draft short marketing patterns (headline, CTA, email skeleton) without owning campaigns
- Localize register, false friends, and date/number/currency shape with context

Prefer sibling skills when the job is primarily voice drafting (`writing`), paid
or funnel copy (`copywriting`), Markdown syntax (`markdown`), heavy CSV pipelines
(`csv`), deep regex design (`regex`), or grammar-only polish (`grammar`).

## Progressive disclosure

| Need | Load |
|------|------|
| Encoding, CSV/regex, shell transforms | `references/data.md` |
| APA / MLA / Chicago citation patterns | `references/academic.md` |
| Voice, dialogue, pacing, show-vs-tell | `references/writing.md` |
| Headlines, CTA, email copy skeletons | `references/copy.md` |
| False friends, register, locale formats | `references/localization.md` |
| Official anchors for fact checks | `references/sources.md` |

## Core rules

1. **Detect before transform.** Run encoding and line-ending checks before bulk edits.
2. **Parse structured text.** CSV/TSV uses a real parser (`csv`, `csvkit`, `pandas`); bare `split(',')` is out of scope for production data.
3. **One style per document.** Citation style, dialogue attribution pattern, and tú/usted register stay consistent once chosen.
4. **Load the matching reference** before inventing domain detail; verify mutable style facts against `references/sources.md`.
5. **Route out of scope work** to related skills instead of stretching this package.

## Quick transforms

| Task | Command pattern |
|------|-----------------|
| Detect encoding | `file -I document.txt` / `file -bi document.txt` |
| Strip CR (CRLF→LF view) | `tr -d '\r'` |
| Collapse runs of whitespace | `sed 's/[[:space:]]\+/ /g'` |
| Lowercase | `tr '[:upper:]' '[:lower:]'` |
| Word count | `wc -w` |
| Unique lines | `sort -u \| wc -l` |
| Duplicate lines | `sort \| uniq -d` |
| Emails | `grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'` |

## Common traps

- Smart quotes and em/en dashes break naive ASCII parsers — normalize when the target is plain ASCII tooling
- UTF-8 length is character count, not byte length (`café` → 4 chars, 5+ bytes)
- Zero-width and BOM characters pass visual review and fail equality checks
- Delimiter sniffing on one header line is a hint, not a schema

## Before-processing checklist

- [ ] Encoding verified
- [ ] Line endings known (LF vs CRLF)
- [ ] Delimiter identified for tabular text
- [ ] Target style or locale named
- [ ] Empty input, Unicode, and special-character edges considered

## Failure recovery

| Symptom | Next step |
|---------|-----------|
| Mojibake / odd symbols | Re-detect encoding; re-read with explicit codec; avoid double-decoding |
| CSV columns shift | Switch to a CSV library; inspect quotes and embedded delimiters |
| Mixed citation styles | Ask once for the required style; reload `references/academic.md` |
| Locale register clash | Lock one register; reload `references/localization.md` |
| Task is long-form voice or campaign copy | Hand off to `writing` or `copywriting` |
