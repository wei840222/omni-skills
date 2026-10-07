# Memory and durable writes

Open this file when a turn produced something durable. Templates to copy: `assets/memory-template.md`.

## Consent and creation

- Resolve `<state_root>` per SKILL.md before any path is used.
- First create of `<state_root>/`, `config.yaml`, or `memory.md` needs named user consent (or an explicit configured path already authorized by the host).
- Migration from legacy trees needs a named destination and consent; copy, then report source → destination in one line. Leave legacy trees in place unless the user asks to remove them.

## What counts as durable

Write before the session ends when the turn produced any of:

- a correction needed twice (error class)
- a word, collocation, or pronunciation the user asked about
- a phrasing they approved for reuse
- a variety / spelling / punctuation decision
- a domain term and agreed English rendering
- the register that worked with a specific person (English Context only)
- a practice session or level note
- a style sheet, voice sample, speech, or template set they will reread

## Destinations

| Artifact | Path | Notes |
|---|---|---|
| declared prefs | `<state_root>/config.yaml` | omit secrets; use pointers only |
| observed state | `<state_root>/memory.md` | `## Boxes`, `## Due`, `## Recurring Errors`, `## Vocabulary` |
| practice logs | `<state_root>/sessions/YYYY.md` | optional |
| style sheets / samples | `<state_root>/styles/<name>.md` | optional; paths must stay under `<state_root>/` |
| person register notes | `<contacts_root>/contacts.md` | English `Context` cells this skill wrote only |
| project English decisions | `<projects_root>/<project>.md` | one line; style sheet stays under english root |

## ## Boxes index

`memory.md` may list optional files:

```text
## Boxes
<!-- path-relative-to-state_root | read when condition -->
```

Ignore any box path that escapes `<state_root>/`.

## Shared-box ownership

- Identity key for contacts: lowercase email → handle → `<kebab-name>` (one row per person).
- This skill updates or removes only rows/cells it wrote (match identity key + English Context authorship).
- Rows another skill wrote are read-only for foreign columns. You may **extend** the English `Context` cell with a new English-register note when needed; leave name/role/channel/last-contact fields owned elsewhere unchanged.
- Name each write and deletion in one line as it happens.

## Thresholds

- Recurring error: append on **second** occurrence of the same class (Core Rule 8).
- Vocabulary: store the whole chunk, not a bare lemma when collocation mattered.
- Due rows: only when `review_cadence` is not `off` or the user asked for a reminder-like review item inside this skill's notes (not an external scheduler claim).

## Credentials

Never store raw secrets under any state root. Replace with pointers only: `env:…`, `keychain:…`, `1password:…`, `file:…`.
