---
name: notes
description: >
  Capture, structure, and retrieve notes in local markdown, Apple Notes, Bear,
  Obsidian, Notion, or Evernote. Use when the user says take notes, write this
  up, capture this, or turn a transcript into a note; for meeting, 1-on-1,
  decision, journal, project, or research notes; when action items need owners
  and absolute dates; when a note cannot be found again; when quick captures
  pile up; when notes must move between apps or be backed up; and when something
  is too sensitive to write down. Prefer `meetings` for facilitation, `journal`
  for reflection practice, `task-list` for a full task system, `voice-notes` for
  voice-transcript corpora, `notion-api-integration` for API development, and
  `pkm` when the link graph is the product.
metadata:
  version: "1.2.0"
  openclaw: '{"emoji":"📝"}'
  related-skills: '{"meetings":"Running the meeting itself: agendas, facilitation, and follow-up discipline.","journal":"Journaling practice and reflection prompts once the daily note exists.","task-list":"Full task system when action_target is external or actions outgrow one tracker.","voice-notes":"Voice-message transcripts as a structured searchable corpus.","notion-api-integration":"Building against the Notion API beyond note capture.","pkm":"Linked atomic-note knowledge base when the graph matters more than the record.","people":"Shared address-book context for attendees and action owners."}'
---

## State location

Notes state may exist in `<workspace>/notes/`, `<workspace>/memory/notes/`, or `~/notes/`.

Before the first state operation, resolve one `<state_root>`:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order: `<workspace>/notes/`, `<workspace>/memory/notes/`, `~/notes/`.
3. If several candidates exist, use only the highest-precedence directory, report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable notes state, create `<workspace>/notes/` when `<workspace>` is available; otherwise ask for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the rest of the invocation.

Use the selected `<state_root>` for every notes state path. Shared people and project boxes resolve under the same root: `<state_root>/contacts/contacts.md` and `<state_root>/projects/<project>.md`. Legacy `~/Clawic/data/notes/` (and sibling Clawic boxes) are migration sources only — keep them out of the active lookup order and move only when the user asks. Shared profile universals may still live at a host profile path the user already maintains; record the pointer in Platform Facts, never invent a second notes root for them.

## Data

At the start of every session, read `<state_root>/notes/config.yaml` (declared routing, vault path, cadences) and `<state_root>/notes/memory.md` (observed corpus state, `## Boxes`, `## Due`). Open any file `## Boxes` names when its condition applies. Every path it names must stay inside `<state_root>/`; ignore lines that point elsewhere. Everything this skill reads or writes is a plain local note under the folders declared for notes — nothing leaves the machine unless the user routed that note type to a network platform. In a shared box, update or remove only rows this skill wrote, matched on that box's identity key. Read `<state_root>/notes/actions.md` before answering commitments or overdue questions. If none of it exists, work from defaults and say nothing about missing state.

**Write before the session ends** whenever the turn produced something durable: a note; an action item, completion, or changed deadline; a decision and what it supersedes; a person who now owns something; the project a note belongs to; a routing choice, vault path, database id, or folder name that cost effort to find; a naming or tagging convention that settled; a review that ran; or a template the user reshaped. Copy formats and thresholds from `assets/data-templates.md` — that is the only write map.

**People and projects stay in shared boxes**, not inside the note body as duplicated profiles: attendees and action owners → `<state_root>/contacts/contacts.md`; project membership → `<state_root>/projects/<project>.md`. The note keeps only the name as a pointer.

**Credentials never enter `<state_root>/`.** Replace pasted secrets with pointers (`env:NOTION_API_KEY`, `keychain:bear-token`, `1password:Work/Notion/agent`, `file:~/.config/notion/api_key`) and say so in one line. If notes still live under `~/notes/` or `~/clawic/notes/` and the user wants the workspace layout, move them into `<state_root>/notes/` and say from where.

A note is worth what it is worth on the day someone searches for it. Write for that day: claim title, date, people, decision, commitments with owners. Capture during the event when possible — unrecorded detail decays fast. Work from defaults immediately; do not open with preference interviews. Precedence for any value: `config.yaml` → host profile universals (locale, timezone) → the Configuration table default.

## When to use

- Turning a conversation, call, transcript, or voice dump into a note someone can act on
- Meeting, 1-on-1, interview, retro, client-call, decision, journal, project-update, or research notes
- Extracting action items with owners and absolute dates, and keeping one honest open list
- Retrieval work: missing notes, naming, tags versus folders, indexes, dead links
- Corpus housekeeping: conflicted copies, duplicates, backups, archiving, app migration
- Deciding whether something should be written down, and what to strip first
- Out of scope: meeting facilitation (`meetings`), journaling practice (`journal`), Notion API development (`notion-api-integration`), full task systems (`task-list`), voice-transcript corpora (`voice-notes`), and link-graph PKM (`pkm`)

## Quick reference

| Situation | Play | Load |
|---|---|---|
| "Take notes on this call" | Capture decisions and commitments verbatim; keep the rest ≤20% | `references/meetings.md` |
| 1-on-1, interview, retro, client call | Keep the one high-value section; the rest is optional | `references/meetings.md` |
| Transcript, voice memo, or pasted wall of text | Extract claim → decision → action; raw text is a source | `references/capture.md` |
| "Note this down" with no context | Quick capture with a claim title; triage within 7 days | `references/capture.md` |
| "We decided X" | Decision record: context, options, rationale, supersedes | `references/decisions.md` |
| Daily note, weekly review, monthly rollup | Cadence and prompts that survive a missed week | `references/journal.md` |
| Project status, handover, or launch write-up | Status note plus shared project pointer | `references/projects.md` |
| Book, paper, course, or highlight import | Quotes versus your words; progressive summarization | `references/research.md` |
| "What do I owe anyone" / overdue chase | One tracker, absolute dates, escalation ladder | `references/action-items.md` |
| "I can't find that note" / tags vs folders | Search order title → tag → full text; thresholds over taste | `references/retrieval.md` |
| Conflicted copies, two devices, backups | Conflict markers, merge by section, 3-2-1 backup | `references/sync.md` |
| Leaving an app / importing a corpus | Fidelity matrix and restore test before committing | `references/migration.md` |
| "Should this even be written down?" | Record test, redaction, and what never enters a note | `references/sensitive.md` |
| Local markdown files | Naming, frontmatter, grep, git | `references/local.md` |
| Apple Notes | `memo` CLI, folders, attachment limits | `references/apple-notes.md` |
| Bear | `grizzly` CLI, tag trees, append-only reality | `references/bear.md` |
| Obsidian | Vault selection, wikilink-safe renames, direct edits | `references/obsidian.md` |
| Notion | API calls, properties, pagination, rate limits | `references/notion.md` |
| Evernote | `clinote` CLI, notebooks, lossy formatting | `references/evernote.md` |
| Official limits / API freshness | Re-check before quoting versions or rate numbers | `references/sources.md` |

Coverage map: situation refs above, plus platform refs, plus `assets/data-templates.md` for write formats.

## Core rules

1. **Route by type, fall back loudly.** Platform = `routing.<type>` in `config.yaml`, else `default_platform`, else local. When the configured platform is unavailable, write locally and stamp `platform: local (fallback from <intended>)`.
2. **The title is the claim, not the topic.** Local filenames: `YYYY-MM-DD_topic-slug.md` (`references/local.md`).
3. **Capture during, write up after — and cap the volume.** Target ≤20% of what was said, 100% of decisions, owners, and dates. Governed by `capture_verbosity`.
4. **Owner, verb, absolute date, or it is not an action item.** Resolve relative dates at write time (`references/action-items.md`).
5. **One fact, one home.** A decision lives in one decision note; meetings link to it. Mirrored copies hold a pointer and are not edited.
6. **Tag thresholds, not tag taste.** >~10% of corpus → promote; used once → merge/drop; working ceiling ~20 live tags (`references/retrieval.md`).
7. **No index before 30 notes.** At 30+, build `index.md` and update it in the same turn a note is created.
8. **The inbox is triaged within 7 days.** Promote, fold, or delete; an older inbox stops people trusting search.
9. **What you write becomes a record.** Keep speculation about people, health, and pay out of meeting/interview notes (`references/sensitive.md`).

## Note types

| Type | Fires on | Required fields | Default home (under `<state_root>/notes/`) |
|---|---|---|---|
| Meeting | "meeting notes", "call with", "we talked about" | Date, attendees, absentees, decisions, actions | `meetings/` |
| 1-on-1 | "1:1", "check-in with", manager or report named | Carry-forward, their topics, actions on both sides | `meetings/` |
| Interview | "candidate", "screen", "debrief" | Evidence/quotes separated from assessment | `meetings/` |
| Retro | "retro", "post-mortem", "what went wrong" | Timeline, contributing factors, actions — never a name as a cause | `meetings/` |
| Decision | "we decided", "going with", "decision:" | Context, options rejected, rationale, effective date, supersedes | `decisions/` |
| Project update | "status", "project update", "where are we on" | Status, progress, blockers with owners, next milestone | `projects/` |
| Journal | "daily note", "today I", "how did the week go" | Date, what happened, what it means, tomorrow's top three | `journal/` |
| Research | "notes on this paper", "highlights", "reading" | Source with locator, verbatim quotes in blockquotes, your claim | `research/` |
| Quick | "note:", "remember", "jot this down" | One claim line and a tag; triage in 7 days | `quick/` |

Templates live with the situation file that owns them (`references/meetings.md`, `references/decisions.md`, `references/journal.md`, `references/projects.md`, `references/research.md`, `references/capture.md`).

## Platform fit

| Platform | Wins at | Costs you | Data flow |
|---|---|---|---|
| Local markdown | grep, git history, zero dependencies | No mobile capture unless you build it | Stays on this machine |
| Apple Notes | Instant capture on Apple devices, scans, shared folders | Weak bulk plain-text export and linking | Local through the app |
| Bear | Fast tag-tree capture, honest markdown | Apple platforms; CLI appends, does not edit | Local through the app |
| Obsidian | Backlinks, graph, plain-markdown files | Sync is paid or self-managed; renames outside the app break links | Local files |
| Notion | Shared databases, typed properties, teammates | API-only automation; export is lossy | Content goes to api.notion.com |
| Evernote | Existing corpus and OCR over scans | Thin CLI; migration is the usual reason to open it | Content goes to Evernote servers |

Default to local for anything that must still be readable in ten years; route types that need other people to the platform those people already open. Re-check live numbers in `references/sources.md` before quoting Notion rate limits or API versions.

## Output gates

Before writing or sending a note:

- Does the title state the claim rather than the topic?
- Does every action item carry owner, verb, and an absolute date?
- Were decisions read back in the user's words, with what they supersede?
- Did the note land where routing says, stamped with fallback if needed — and if the destination is Notion/Evernote, did the user route that type there?
- Is there a credential, PIN, recovery code, or third-party personal detail about to be written? Use a pointer, or leave it out.
- Did anything durable come out of this turn? Then write it to the matching box using `assets/data-templates.md` in the same turn.

## Configuration

Store declared preferences in `<state_root>/notes/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| default_platform | local | apple-notes | bear | obsidian | notion | evernote | local | Where a note goes when its type has no routing entry |
| routing | list of `<note type>: <platform>` pairs | none | Per-type override; e.g. `meeting: notion`, `journal: bear` |
| vault_path | path | none | Obsidian vault root; unset means `obsidian-cli` default |
| notion_database_id | text (id) | none | Target database id for created pages — never a token |
| filename_pattern | date-first | title-first | date-first | Local filename sort order |
| capture_verbosity | minimal | standard | verbatim | standard | How much of a conversation reaches the note |
| tag_style | flat | nested | flat | `#product` versus `#product/pricing` |
| review_cadence | daily | weekly | none | weekly | Which review runs and which `## Due` row appears |
| review_day | mon…sun | fri | Weekly review / action sweep day |
| action_target | notes | external | notes | `notes` keeps `actions.md`; `external` hands items to a task app and keeps a pointer |
| archive_after_months | number (3-36) | 12 | Age at which journal/quick notes archive |

Preference areas (tooling, conventions, platform, safety posture, output register, work order, integrations, cadence, thresholds) are free-form keys under `config.yaml`. A stated preference is a declaration and belongs there, not in `memory.md`.

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Writing the note up after the call | Unrecorded detail decays within a day | Capture live, clean up after |
| Topic titles | Search returns everything and answers nothing | Claim titles |
| Pasting the whole transcript as the note | Decision is undiscoverable; paste may carry secrets | Extract claim/decision/action; link the raw source |
| "ASAP", "soon", "next sprint" | Cannot chase without an absolute date | Absolute date at write time |
| Tracking actions in whichever app holds the note | Commitments fragment across apps | One tracker |
| Folders as the primary structure | A note has one folder and three subjects | Folder by type; retrieve by title, tag, and link |
| A tag for every idea | 300 tags equals no tags | Tag thresholds |
| Renaming a note in Finder/Explorer | Wikilinks break silently | Rename through the app / `obsidian-cli move` |
| Editing the same note on two devices with one offline | Last write wins without a prompt | Conflict rules in `references/sync.md` |
| Trusting an export you never restored | Nested databases/checkboxes often flatten | Restore one exported note before migrating |
| Hand-maintained index from note one | Stale indexes mislead | Wait until 30 notes |
| Keeping a "someday" inbox | Notes go there to die | Triage within 7 days |
| Judgments about a person in a meeting note | The note outlives the opinion | Evidence and decisions only |
| One forever-append project note | Current status gets buried | Status at the top; one note per update |

## Where experts disagree

- **Folders versus links.** PARA organizes by actionability; Zettelkasten by link. Prefer folders when people browse/onboard; prefer links when recombination matters.
- **Atomic notes versus long documents.** Atomic wins for reusable claims; long-form wins for meetings/decisions where chronology is the content.
- **Capture everything versus selectively.** Capture-everything only works with real pruning; a year without deletions means the corpus already failed.
- **Daily note as single entry point.** Strong for continuous self-directed work; weak when others must find notes by subject months later.
- **One vault or two.** Merge for serendipity; split when employer policy, NDA, or discovery risk applies (`references/sensitive.md`).

## Security and privacy

**External endpoints:** only when the user routed a note type there.

| Endpoint | Data sent | When |
|---|---|---|
| `api.notion.com/v1/pages`, `/blocks/*` | Note title and content | Type routed to Notion and a key is available |
| `api.notion.com/v1/search`, database/query endpoints | Search terms and filters | User searches Notion notes |
| Evernote servers via `clinote` | Note title and content | Type routed to Evernote and the user is logged in |

Apple Notes, Bear, and Obsidian stay local through their apps or files. Local markdown never leaves the machine.

**Credentials:** platform tokens are read from the user's own locations (`~/.config/notion/api_key`, `~/.config/grizzly/token`, OS keychain). This skill does not store, log, copy, or transmit them into `<state_root>/`.

**Local storage:** notes, actions, index, preferences, and memory stay under `<state_root>/notes/`, with person/project pointers in shared contacts/projects boxes.

**Guardrails:** nothing is installed on the user's behalf. A network platform is used only after routing. Confirm before deleting or overwriting an existing note. Bulk operations name exactly how many files they will touch before running.
