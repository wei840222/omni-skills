# Capture

Use when the input is a transcript, voice dump, pasted wall of text, or a vague "note this down".

## Goal

Produce a findable note with a claim title, not a second copy of the raw input.

## Procedure

1. Identify the note type from trigger phrases (meeting/decision/journal/project/research/quick).
2. Extract **claim → decision → action**. Keep raw text as a linked source, not the body.
3. Cap volume with `capture_verbosity` (default: ≤20% of what was said; 100% of decisions/owners/dates).
4. Route by `config.yaml`; on fallback, stamp `platform: local (fallback from <intended>)`.
5. Write action items only with owner + verb + absolute date; otherwise park them under Open Questions.
6. For no-context captures, create a quick note with one claim line and a tag; triage within 7 days.

## Quick template

```markdown
# <Claim title>
date: YYYY-MM-DD
source: <transcript|voice|paste|conversation>

## Claim
...

## Decisions
- ...

## Actions
- @owner: verb — YYYY-MM-DD

## Open questions
- ...
```

## Failure modes

- Pasting the whole transcript → decision becomes undiscoverable and secrets may ride along.
- Topic titles ("Pricing") → search returns noise.
- Relative dates left unresolved → chase fails months later.
