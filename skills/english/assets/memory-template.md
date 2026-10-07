# English memory templates

Copy shapes only after State location resolution and required consent. Replace angle-bracket placeholders.

## `<state_root>/memory.md`

```markdown
# English memory

## Boxes
<!-- relative-path | read when condition -->

## Due
<!-- YYYY-MM-DD | item | cadence | status -->

## Recurring Errors
<!-- YYYY-MM-DD | class | rule (one line) | example | count -->

## Vocabulary
<!-- chunk | variety/register | note | added -->
```

## `<state_root>/config.yaml`

```yaml
variety: en-US
spelling_system: american
register_default: neutral
first_language: null
oxford_comma: true
correction_mode: silent
max_sentence_words: 25
banned_words: []
voice_file: null
review_cadence: off
```

## `<state_root>/sessions/YYYY.md`

```markdown
# English practice YYYY

## YYYY-MM-DD
- focus:
- prompts:
- outcome:
- next:
```

## `<state_root>/styles/<name>.md`

```markdown
# Style: <name>
- variety:
- register:
- notes:
- sample:
```

## Shared contacts row (English Context only)

`Name | Key | Role | Preferred channel | Context | Last contact | File`

Update `Context` with register notes this skill owns; leave foreign columns unchanged when the row already exists.
