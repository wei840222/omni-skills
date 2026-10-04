---
name: people
description: >
  Maintain a personal address book of people, context, last contact, birthdays,
  and open loops. Use when someone is mentioned with keepable context; before
  meetings; for who-do-I-know or overdue-reconnect questions; drafting
  congratulations or condolences; making introductions; or merging duplicates
  and imports. Not for sales pipelines (`crm`), friendship depth (`friends`),
  household logistics (`family`), gift ideas (`gifts`), or non-person reminders
  (`remind`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"👥"}'
  related-skills: '{"crm":"Sales pipelines, deals, forecasts, and commercial outreach hygiene.","friends":"Friendship depth, reciprocity, drift, and repair beyond address-book upkeep.","gifts":"Gift ideas and giving history built on dates and details this box holds.","remind":"Reminder mechanics for anything that is not about a person.","family":"Household logistics, schedules, and care routines."}'
---

# People

Personal address book for who someone is, what matters to them, when you last
spoke, and which dates are coming up. Keep the small set of facts that change
the first thirty seconds of the next conversation. Date every real interaction.
Draft messages for the user to send — never send or schedule sends.

## State location

People state may exist in `<workspace>/people/`, `<workspace>/memory/people/`,
or `~/people/`. Shared contacts may exist in `<workspace>/contacts/`,
`<workspace>/memory/contacts/`, or `~/contacts/`. `<workspace>` is the workspace
root supplied by the host/runtime.

Before any state read or write, resolve `<state_root>` once:

1. Use an explicitly configured path supplied by the user or host when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/people/`, `<workspace>/memory/people/`, `~/people/`.
3. When multiple candidate directories exist, use only the first one, tell the
   user that multiple state directories were found, and keep all other candidates
   unchanged.
4. When no candidate exists and durable notes must be created, propose
   `<workspace>/people/` (or an explicit path if no workspace is available) and
   obtain named consent before creating it.
5. Legacy `~/Clawic/data/people/` and `~/Clawic/data/contacts/` are migration
   sources only. Copy after the user confirms the destination; never silently
   merge roots or rewrite history into multiple locations.

Use the selected `<state_root>` for every people-owned path as
`<state_root>/people/...` when the root is a parent workspace folder that also
holds other skills, or as `<state_root>/...` when the root itself is the people
directory selected above. Resolve the shared contacts box the same way under
candidates `<workspace>/contacts/`, `<workspace>/memory/contacts/`,
`~/contacts/`, with legacy `~/Clawic/data/contacts/` migration-only. Keep skill
resources under `references/` and `assets/` only — never under `<state_root>`.
Do not write the literal string `<state_root>` to disk.

## Session bootstrap

At the start of every session:

1. Read `<state_root>/config.yaml` (or `<state_root>/people/config.yaml` when
   the root is a shared parent) and `<state_root>/memory.md` (observed state,
   including `## Boxes` and `## Due`).
2. Open any file named by `## Boxes` when its condition applies. Every path it
   names must stay under `<state_root>/`; ignore lines that point elsewhere.
3. Read `<state_root>/do-not-surface.md` before naming anyone to contact,
   congratulate, brief, or remind about.
4. Read the shared contacts file (`contacts.md` under the resolved contacts
   root) before adding a person, answering who the user knows, or building a
   meeting brief.
5. If none of those files exist, work from defaults and do not narrate the
   missing files.

Everything this skill reads or writes is a plain local note under
`<state_root>/` or the shared contacts root. Credentials never land there. In a
shared box, update or remove only rows this skill wrote, matched on that box's
identity key; rows another skill wrote are read-only. Name every write and
deletion in one line as it happens.

**Write before the session ends** whenever the turn produced something durable:
a person met or newly named; a detail that changes the next conversation; an
interaction and its date; a birthday or anniversary; a life event; a promise,
favor, or introduction still open; a tier or cadence decision; a merge, import,
or suppression; or an artifact the user will reread. Load
`references/memory.md` to decide destinations, formats, and thresholds.

**People go to** the shared contacts box (`contacts.md`), not into people-only
notes. One row per person:
`Name | Key | Role | Preferred channel | Context | Last contact | File`.
**`Key` is the identity and it is stored on the row** — lowercased email, else
primary handle, else `<kebab-name>` plus a stable disambiguator. Preferred
channel holds the channel type (email, whatsapp, signal), never the address.
Match on `Key` before adding; update in place; never append a second row for the
same key; never rewrite a row another skill owns. A person with more than a row
of detail gets `<contacts_root>/<name>.md` and the row keeps the `File` pointer.

**Credentials stay outside state roots.** That includes door codes, wifi
passwords, spare-key locations, recovery answers, and shared logins. Store
pointers only: `1password:Personal/Alarm-code`, `keychain:carddav`,
`env:CONTACTS_EXPORT_TOKEN`, `file:~/.config/carddav/creds`.

Work from defaults immediately. The one exception to silence is `nudge_style`:
while unset, overdue people and upcoming dates are stated once when relevant and
never repeated unasked (Rule 6). Precedence: `config.yaml` → host profile when
provided → Configuration defaults below.

## When to use

- A person is mentioned with context: met them, spoke with them, learned
  something, or is about to see them
- A date involving someone is approaching: birthday, anniversary, work
  anniversary, death anniversary, move, due date
- Recall: what do I know about X, who do I know at Acme, who lives in Berlin,
  who went quiet, partner's name
- Reconnecting, congratulating, condoling, or drafting the message a life event
  calls for
- Introductions both directions: making one, being asked for one, chasing one
  that stalled
- Hygiene: duplicates, merges, name changes, bounces, phone/vCard/LinkedIn
  imports
- Mode: **act-as** for records; **advise** for message drafts — produce the
  draft, never send it, never schedule a send
- Not for sales pipelines (`crm`), friendship depth work (`friends`), household
  logistics (`family`), gift ideas (`gifts`), or non-person reminders (`remind`)

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/capture.md` | First contact / five fields within 24 hours |
| `references/names.md` | Spelling, preferred form, pronunciation, name order |
| `references/details.md` | Thirty-second filter for what to store |
| `references/interactions.md` | Logging a touch and updating `Last contact` |
| `references/dates.md` | Birthdays, anniversaries, lead times |
| `references/keeping-in-touch.md` | Overdue sweeps and reconnection drafts |
| `references/briefing.md` | Pre-meeting five-line brief |
| `references/life-events.md` | Hard messages and follow-ups |
| `references/introductions.md` | Double opt-in intros |
| `references/search.md` | Who-do-I-know queries and tags |
| `references/hygiene.md` | Merges, imports, decay, dormant |
| `references/network.md` | Weak ties and reciprocity without scoreboards |
| `references/privacy.md` | Consent, suppression, deletion |
| `references/memory.md` | Write destinations, formats, thresholds |
| `references/sources.md` | Primary sources before restating domain claims |
| `references/experts.md` | Contested advice |
| `references/traps.md` | Failure modes |
| `references/security-privacy.md` | Storage and credential guardrails summary |
| `assets/memory-template.md` | Only when creating initial state files |
| `test-prompts.json` | Evaluation harness only — not during normal help |

## Core rules

1. **Write in the turn the fact appears.** A detail mentioned in passing is gone
   next session. A name plus where you met is already a valid row; complete it
   later (`references/memory.md`).
2. **One person, one record.** Identity is lowercased email; else primary
   handle; else `<kebab-name>` plus a stable disambiguator
   (`john-smith-acme`, never `john-smith-2`). Store it in the row's `Key`
   column. Read before adding. Matching on name alone merges strangers
   (`references/hygiene.md`).
3. **Thirty-second filter.** Record a fact only if it would change the first
   thirty seconds of the next conversation. "Nice person, we talked about work"
   fails and costs a line forever (`references/details.md`).
4. **`Last contact` runs the box.** Every real interaction updates it, including
   a two-line text. Thinking about them or seeing a post does not. Overdue is
   arithmetic: `today − last contact > tier cadence`, overridden by a
   per-person `cadence` when set.
5. **Tier by Dunbar-inspired layers.** Observed layer sizes often cited around
   5 / 15 / 50 / 150 stable relationships; the cadences below are this skill's
   mapping, not a biological law. Sixty people in `inner` means the roster is
   unmaintained (`references/sources.md`).
6. **Nudges are answers, not interruptions.** Default `nudge_style: on-ask`
   reports overdue people and upcoming dates when asked or when that person is
   already the subject, once, in one line. `proactive` may volunteer at session
   start; `off` never volunteers. A nudge repeated in consecutive sessions
   stops.
7. **Suppression outranks every other rule.** Anyone on `do-not-surface.md` —
   died, estranged, breakup, explicit request — is hidden from birthday sweeps,
   briefs, and intro suggestions. The entry states which case it is because
   death and fallout need opposite handling if the user raises them first
   (`references/privacy.md`).
8. **Write as if they will read it.** Facts, not verdicts:
   "declined the last three invitations" not "flaky". Files get synced,
   restored, screen-shared, and inherited.

## Relationship tiers and cadence

| Tier | Roster size it fits | Default cadence | What the record holds | Overdue means |
|---|---|---|---|---|
| `inner` | ~5–15 | natural contact; flag at 8 weeks silence | full detail; every real conversation logged | something is wrong or life got loud — ask, do not schedule |
| `regular` | ~50 | `reconnect_months` (default 6) | conversation-changing detail; meaningful interactions | reconnection message due |
| `orbit` | ~150 and beyond | annual sweep only | one row, one context line, one date | nothing — recall only |
| `dormant` | any | never | intact and hidden | never; move here instead of deleting |

Untiered people default to `orbit`. Promote on the second real interaction.

## Minimum record

| Field | Why it exists | Empty is fine when |
|---|---|---|
| Name, as they say it | Must be right | never |
| Key — email or handle | Identity column on the row | never — phone alone can be the key |
| Role and where | "Who do I know at Acme" | met outside work |
| How we met | Best line in any reconnection | never, if you were there |
| Preferred channel | Wrong channel = unread | only one channel exists |
| One specific thing | Contact vs person you know | never — else they stay `orbit` |
| Last contact (date) | Overdue mechanism | never |
| Tier | Cadence and detail depth | defaults to `orbit` |
| Dates | Birthday, anniversary, loss date | unknown |
| Do not raise | Topic that ends a conversation badly | absent field means none |

Never store a field you would not say in a sentence. Ages compute from birth
year; a stored age rots within twelve months.

## Message moments

| Moment | When to send | What makes it land |
|---|---|---|
| Birthday | `birthday_lead_days` ahead so it goes out on the day | one specific reference |
| Milestone birthday (30, 40, 50…) | flag 3 weeks ahead | needs a plan, not only a text |
| New job or promotion | within 2 days of hearing | name what they leave and what they join |
| Birth of a child | 2 weeks after, not week one | week three is when silence hurts |
| Bereavement | within 48 hours, again at 4–6 weeks | the second message is the rare one |
| Death anniversary | on the day, only if they marked it before | "thinking of you today" is enough |
| Illness or treatment | on their terms after asking once | concrete offers beat "let me know" |
| Layoff or business failure | within a week, no advice | advice reads as judgment early |
| Move to a new city | day of, and again at 30 days | month one is when novelty ends |
| Anything else worth marking | within 48 hours of learning it | the remembered fact is the message |

Detail and drafts: `references/life-events.md`.

## Output gates

Before answering about a person or proposing contact:

- Did I read the address book, or only this conversation?
- Did I check `do-not-surface.md` first (Rule 7)?
- Did every interaction this session update `Last contact`, and every new fact
  land on the record in this turn (Rule 1)?
- Does every promise, favor, or introduction have a `## Open Loops` line with a
  name and date?
- Would the person be fine reading the line (Rule 8), and does it clear
  `sensitive_details` (`references/privacy.md`)?
- If I created a file, did I add its `## Boxes` line with a read condition in
  the same turn?

## Configuration

Store overrides in `<state_root>/config.yaml` (or
`<state_root>/people/config.yaml` for a shared parent root).

| Variable | Type | Default | Effect |
|---|---|---|---|
| nudge_style | off \| on-ask \| proactive | on-ask | Whether overdue people and dates are volunteered, answered on request, or never raised |
| reconnect_months | number (1–24) | 6 | Silence after which a `regular` person is overdue; per-person `cadence` wins |
| birthday_lead_days | number (0–30) | 5 | How far ahead dates in `## Dates` surface |
| brief_lines | number (3–12) | 5 | Pre-meeting brief length |
| sensitive_details | minimal \| full | minimal | Whether third-party health/money/relationship content is stored, or only that a topic exists |
| roster_review | month \| quarter \| year | quarter | Hygiene cadence written to `## Due` |
| name_order | as-given \| given-first \| family-first | as-given | How names are written and filed |

Preference areas (record stated choices in `config.yaml`):

- **Tooling** — export target (vCard, CSV, CardDAV), phone-importable sidecar,
  calendar source for meetings
- **Conventions** — tag vocabulary, file naming, interaction log length
- **Relationship model** — tier names/sizes, whether tiers exist, what counts as
  real contact
- **Platform** — locale, timezone, date format, name script/transliteration,
  whether ages are shown
- **Safety posture** — categories omitted even at `full`, whether hard-message
  drafts appear unprompted, shareability
- **Output format** — brief shape, draft register, length/formality per channel
- **Cadence** — sweep day, quiet periods (grief, crunch, holidays), annual
  date-scan horizon

## Quick workflow

1. Resolve `<state_root>` and the contacts root; read config, memory,
   `do-not-surface.md`, and `contacts.md` as needed.
2. Match identity on `Key` before adding or updating anyone.
3. Apply the thirty-second filter; write durable facts in this turn.
4. Load only the reference file the situation needs.
5. Draft messages for user approval; never send.
6. Update `Last contact`, open loops, and `## Boxes` before the session ends.
