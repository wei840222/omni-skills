# Working File Templates — Writing

Read this file only when writing durable state. `config.yaml` is what the user
**declared**; `memory.md` and everything it indexes is what you **observed** or
produced. An observation yields to a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences | `<state_root>/config.yaml` | Key by key, read-modify-write |
| Voice traits, format habits, never-list, corrections, pieces in flight, audiences, box index, due dates | `<state_root>/memory.md` | Rewritten in place; stays small |
| Their own writing kept as voice evidence | `<state_root>/samples/<kebab-name>.md` | One file per sample |
| House style for a publication, client, employer, or project | `<state_root>/style-sheets/<context>.md` | One file per context |
| Reusable templates, standing bios/sign-offs, editorial letters, briefs, surviving outlines | `<state_root>/artifacts/<kebab-name>.md` | Born as its own file |
| Finished and published pieces | `<state_root>/pieces/<year>.md` | Append-only, cut by year |
| People they write to or for | `<contacts_root>/contacts.md` (**shared**) | One row per person |
| Writing projects with a life beyond one piece | `<projects_root>/<project>.md` (**shared**) | One file per project; style stays in `style-sheets/` |
| Anything durable this table does not name | `<state_root>/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if read whole | Name the file after what it holds; add its `## Boxes` line in the same turn |
| Credentials of any kind | Nowhere under skill state | Pointer only — see Secrets |

## When to write

No permission needed for ordinary durable notes; every write is announced in one
line that names the file. Writes and deletions stay inside the resolved roots.
In a shared box, only rows this skill itself wrote are updated or removed.

| It happened | Write |
|---|---|
| A voice trait was confirmed, corrected, or contradicted twice | `## Voice` |
| The user rejected a word, phrase, construction, or move | `## Never` |
| They shared representative writing of their own | `samples/<kebab-name>.md` |
| They stated how they handle a format or channel | `## Formats` |
| They edited your draft | `## Corrections` — what you wrote → what they changed it to |
| A style decision was made for a publication, client, or project | `style-sheets/<context>.md` |
| A piece was finished, sent, or published | `pieces/<year>.md`, and its row leaves `## Pieces` |
| A piece was commissioned or started, with a deadline | `## Pieces` |
| A template, bio, sign-off, outline, or editorial letter will be reused | `artifacts/<kebab-name>.md` |
| A named person's register or channel preference was learned | Their row in `contacts.md` |
| A recurring deadline or review cycle was agreed | `## Due` |
| The user declared a preference | Its key in `config.yaml` |

## Start flat, split only when it hurts

Everything except samples, style sheets, artifacts, the pieces log, and the
shared boxes begins inside `memory.md`. Splitting is a procedure:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content**,
   then in the same turn: create the new file under `<state_root>/`, move the
   whole section into it, delete the section from `memory.md`, add its line to
   `## Boxes`, and append the new entry to the new file.
3. Keep headings identical on both sides of the move.
4. Leave no duplicate behind. If the same data appears in both places, the
   extracted file wins and the `memory.md` copy is deleted.

Samples, style sheets, and artifacts are born as their own files whatever their
size, because each is read whole and only when its subject comes up.

## Secrets

Nothing under `<state_root>/`, `<contacts_root>/`, or `<projects_root>/` holds a
secret value. Store the pointer in the shape `<kind>:<locator>`:

`env:GHOST_ADMIN_KEY` · `keychain:substack` · `1password:Work/Newsletter/api` ·
`bitwarden:Personal/Medium` · `file:~/.config/newsletter/token`

When the user pastes something to save, replace each secret value before writing
and leave the pointer visible: `api_key: <env:GHOST_ADMIN_KEY>`. Say in one line
that you did it.

**Keep:** publication names, editor/client names, bylines, public URLs of
published work, word counts and deadlines, subscriber counts, style rules,
document titles, and the user's own prose.

**Strip:** publishing-platform API keys and admin tokens, SMTP/app passwords,
share/preview links carrying an access token, CMS logins, and anything inside a
pasted `.env` or credentials block.

Third-party personal data that arrives inside a pasted draft — identity numbers,
card numbers, medical details, home addresses — stays in the draft you hand
back and stays out of skill state.

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested
under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only
the key just declared, keep every other key byte for byte. Create
`<state_root>/` only after consent when it does not exist.

```yaml
spelling: uk
edit_depth: heavy
cut_target_pct: 25
feedback_mode: rewrite
explain_edits: true
markup: markdown
voice_file: voice-guide.md
```

## memory.md

```markdown
# Writing memory

## Voice
- Short sentences mixed with one longer turn; concrete subjects; low hedge density

## Never
- "delve", "tapestry", "in today's fast-paced world"

## Formats
- Internal email: ask first, deadline as a date, owner named

## Corrections
- Was: "I wanted to reach out to..." → Now: "I'm writing because..."

## Pieces
- Q3 report announcement — due 2026-10-31 — draft

## Boxes
- samples/launch-announcement.md — when matching newsletter voice
- style-sheets/acme.md — before any Acme byline draft

## Due
- 2026-11-07 — refresh Acme style sheet after legal review
```

## samples/

One file per sample of the user's own writing, at
`<state_root>/samples/<kebab-name>.md`.

```markdown
# Sample — launch announcement, own newsletter
Source: 2026-07 issue
Metrics: 412 words · sentences 6-24 words · 3 paragraphs of 2 sentences
Notes: opens on the change, not the product name; ends with one ask

<body of the sample>
```

## style-sheets/

One file per context at `<state_root>/style-sheets/<context>.md`.

```markdown
# Style sheet — Acme blog
Audience: existing users
Spelling: us
Voice notes: conversational, no "revolutionary" / "seamless"
Open questions: whether case-study numbers need legal sign-off — asked 2026-07
```

If the context is also a project, this file holds the style and
`<projects_root>/<project>.md` holds the work; each names the other.

## artifacts/

One file per reusable artifact at `<state_root>/artifacts/<kebab-name>.md`.

```markdown
# Cold intro email — the version that gets replies
When to read: cold ask to a named person already in contacts
Body:

...
```

## pieces/

Append-only yearly logs at `<state_root>/pieces/<year>.md`.

## Shared contacts box

Lives at `<contacts_root>/contacts.md` and is shared with every skill that deals
with people.

```markdown
# Contacts
| Key | Name | Context |
|---|---|---|
| marta@acme.example | Marta Ruiz | Prefers short asks; ignores soft closes |
```

- Read the file before adding. If the key is already there, update the row in
  place.
- Rows written by another skill are read-only; add missing context only.
- Retirement: delete the row and note the date in `memory.md`.
- Scale cut: one row per person while ≤15; past that, a file per person at
  `<contacts_root>/<name>.md` with `contacts.md` as the index.
- Foreign columns win. Match an existing header; add missing notes as trailing
  text.
- Credentials stay as pointers only.

## Shared projects box

Lives at `<projects_root>/<project>.md`.

```markdown
# Acme blog — ghostwritten series
status: active
owner: Marta Ruiz (see contacts)
goal: 2 posts a month under the Acme byline, through 2026-12
style: <state_root>/style-sheets/acme.md
milestones:
- 2026-06-30 — first three posts published
decisions:
- Keep product names lowercase in body copy
```

- Identity is the project name (kebab file name).
- Style stays in `style-sheets/`; work stays here.
- Client/editor goes in contacts and is referenced by name only.
- Finished projects keep `status: done — <date>`; archive past ~20 closed
  projects under `<projects_root>/archive/`.
- Foreign structure wins: add new lines; leave existing fields alone.

## Split-out files

When a `memory.md` section is extracted, keep the same headings, delete the
section from `memory.md`, and add the `## Boxes` pointer in the same turn.
