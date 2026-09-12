# Dream entry templates

Use after resolving `<state_root>`. Create intermediate `journal/YYYY/MM/` directories when writing.

## Full entry — `<state_root>/journal/YYYY/MM/YYYY-MM-DD-title.md`

```markdown
# YYYY-MM-DD-short-title

## Date
Month DD, YYYY (approx. time if known)

## Title
Short label for later search

## Dream
Narrative in the dreamer's words. Keep fragments; mark unclear gaps with [...].

## Emotions
- Emotion (when in the dream / on waking)

## Symbols
- Image or event worth tracking

## People
- Who appeared; relationship context only if the user stated it

## Recurring?
- Element: yes/no + rough prior count if known from the journal

## Possible triggers
- Waking-life context the user connects (optional)

## Lucidity
Not lucid | Brief lucidity | Sustained lucidity — what cued it
```

## Quick capture — `<state_root>/journal/YYYY/MM/YYYY-MM-DD.md`

For groggy mornings. Expand into a full entry later on request.

```markdown
# YYYY-MM-DD
keywords, places, people, one emotion
[expand later]
```

## Filing rules

1. Prefer kebab-case ASCII titles in filenames; if the user uses another language, keep their words and still prefix `YYYY-MM-DD-`.
2. One primary dream per full-entry file. Same-night distinct dreams may be separate files with `-2`, `-3` suffixes.
3. When expanding a quick capture, preserve the original fragment at the top under `## Original capture` before the rewritten narrative.
4. After writing a full entry, optionally tick related rows in `patterns/symbols.md`, `patterns/themes.md`, or `patterns/people.md` when the user wants tracking.
