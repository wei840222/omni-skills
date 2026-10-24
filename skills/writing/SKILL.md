---
name: writing
description: >
  Draft, edit, and rewrite prose in the user's own voice across emails, posts,
  essays, memos, proposals, and social copy. Use when a draft feels flat, wordy,
  robotic, or "not like me"; when a piece will not start or the ending trails
  off; when an email must deliver bad news, say no, chase a reply, or make an
  ask that lands; when a post needs a hook, headline, or hard cut; when order,
  transitions, or paragraph structure are the real problem; or when matching a
  house style, spelling variant, second language, or word count. Prefer
  `grammar` for mechanics-only fixes, `copywriting` for conversion copy,
  `book-writing` for manuscripts, `storytelling` for narrative craft, `write`
  for versioned draft-and-audit pipelines, and `email-management` for inbox
  triage and follow-ups.
metadata:
  version: "1.2.0"
  openclaw: '{"emoji":"✍️","requires":{"config":["<state_root>/"]},"os":["linux","darwin","win32"],"displayName":"Writing"}'
  related-skills: '{"book-writing": "Chapter architecture and voice consistency across a manuscript.", "copywriting": "Conversion-focused persuasion, offers, benefits, and calls to action.", "documentation": "Technical docs, READMEs, and API reference shaped by the doc type.", "email-management": "Inbox triage, routing, and follow-up chase after the words are written.", "grammar": "Mechanical spelling, agreement, and punctuation fixes without style changes.", "storytelling": "Narrative arc, scene, and tension when the deliverable is a story.", "text": "Encoding, CSV/regex transforms, and locale utilities outside voice-matched prose.", "write": "Versioned draft-and-audit pipelines with numbered revisions and sign-off gates."}'
---

## State location

Writing state may exist in `<workspace>/writing/`, `<workspace>/memory/writing/`,
or `~/writing/`. Shared contacts may exist in `<workspace>/contacts/`,
`<workspace>/memory/contacts/`, or `~/contacts/`. Shared projects may exist in
`<workspace>/projects/`, `<workspace>/memory/projects/`, or `~/projects/`.
Shared profile may exist as `<workspace>/profile.yaml`,
`<workspace>/memory/profile.yaml`, or `~/profile.yaml`. `<workspace>` is the
host/runtime workspace root, never the shell cwd.

Resolve `<state_root>` once per invocation before any writing-owned read or write:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/writing/`, `<workspace>/memory/writing/`, `~/writing/`.
3. If multiple candidates exist, keep only the highest-precedence directory,
   report the duplicates and preserve every other copy untouched.
4. If none exists and durable notes must be created, describe the write, obtain
   consent, then default to `<workspace>/writing/`. If `<workspace>` is
   unavailable, ask for a state root instead of guessing from the current
   directory.
5. Keep the resolved `<state_root>` fixed for the invocation. Write only real
   filesystem paths; the literal token `<state_root>` is documentation-only.

Resolve shared boxes the same way under their own candidate lists above. Legacy
`~/Clawic/data/writing/`, `~/Clawic/data/contacts/`, `~/Clawic/data/projects/`,
and `~/Clawic/profile.yaml` are migration sources only — copy after the user
confirms the destination; do not silently merge roots.

```text
<state_root>/
├── config.yaml          # Declared preferences
├── memory.md            # Observed voice, never-list, boxes, due dates
├── samples/             # Representative samples of their own writing
├── style-sheets/        # House style per publication/client/project
├── artifacts/           # Reusable templates, bios, briefs, outlines
└── pieces/              # Finished/published log by year
```

Shared contacts live at `<contacts_root>/contacts.md`. Shared projects live at
`<projects_root>/<project>.md`. Shared profile lives at the resolved profile
path. Seed new memory from `references/memory-template.md`. Domain research
anchors live in `references/sources.md`.

## Session bootstrap

At the start of every session:

1. Read `<state_root>/config.yaml` (declared) and `<state_root>/memory.md`
   (observed, including `## Boxes` and `## Due`).
2. Open any file named by `## Boxes` when its condition applies. Every path it
   names must stay under `<state_root>/`; keep only lines whose paths stay under `<state_root>/`.
3. Read `<contacts_root>/contacts.md` before writing to a named person, and
   `<projects_root>/<project>.md` before writing into an ongoing project.
4. If none of the files exist, work from Configuration defaults and say nothing
   about the missing files.

**Write before the session ends** whenever the turn produced something durable:
a confirmed or corrected voice trait; a sample worth keeping; a rejection
("never say that"); a format or channel convention; a style sheet; a finished
or published piece; a reusable template, bio, sign-off, editorial letter, or
outline. `references/memory-template.md` is the only file to open in order to
write durable state.

In a shared box, update or remove only rows this skill itself wrote, matched on
that box's identity key. A row another skill wrote is read-only. Name every
write and deletion in one line as it happens.

Store credential **pointers** only (`env:…`, `keychain:…`, `1password:…`,
`file:…`). Strip secret values before any write under `<state_root>/`,
`<contacts_root>/`, or `<projects_root>/`.

Writing has exactly two failure modes: the reader does not get it, or the
reader does not believe it came from you. Diagnose which one before touching a
sentence — structure and cuts fix the first; voice fixes the second. Deliver the
text, not advice about the text. Begin from defaults immediately; open with the
draft instead of questions about style, audience, or how proactive to be.
Precedence for any value: `config.yaml` → shared `profile.yaml` (locale,
language) → the Configuration table default.

## When to use

- Drafting from scratch: emails, messages, posts, essays, memos, proposals,
  updates, bios, cover letters, speeches
- Editing existing prose: tightening, restructuring, cutting to a limit, fixing
  a flat or generic draft, proofing before send
- Voice work: learning how a person writes, reproducing it, checking a draft
  against it, writing under a brand or another person's byline
- Diagnosing a draft that is "wrong" without a clear reason — order, rhythm,
  register, or a buried ask
- Standing consistency: house style sheets, spelling variants, terminology,
  recurring formats
- Writing in a second language, where the errors are register and idiom rather
  than grammar
- Out of scope: grammar/spelling alone (`grammar`); conversion sales copy
  (`copywriting`); narrative craft (`storytelling`); book-length projects
  (`book-writing`); versioned draft-and-audit pipelines (`write`); inbox triage
  and follow-up chase (`email-management`)

## Quick reference

| Situation | Play | Depth |
|-----------|------|-------|
| "Make this better", no other instruction | Structure pass, then the cut to `cut_target_pct`, then voice — in that order (Rule 2) | Core Rules + Output Gates |
| "That doesn't sound like me" | Re-derive the fingerprint from stored samples, then offer two variants and let the pick be the signal | Session bootstrap + `memory.md` |
| Draft reads flat, generic, or machine-written | Structural tells first: uniform sentence length, abstractions in the subject slot, stacked hedges, tricolons | Sentence Diagnostics |
| Blank page, or the draft will not start | Three-move outline, then a timeboxed zero draft written from the middle | Core Rules 1–2 |
| All the parts are there and it still reads wrong | Order and transitions, not sentences — pick the shape the purpose demands | Format Specs |
| Clear in your head, mush on the page | Character in the subject slot, action in the verb, nominalization deleted | Sentence Diagnostics |
| Too long for the slot | Cut arithmetic: whole sections, then clauses, then adjectives last (Rule 3) | Core Rules |
| Email that has to land: bad news, a no, a chase, a cold ask, an apology | One ask, in the first screen, with a deadline and an owner | Format Specs |
| Blog post, essay, op-ed — hook, headline, or a pitch | Lead types, headline patterns, scannability, the outlet's own word limit | Format Specs |
| X, LinkedIn, a thread, a bio, a comment | Payload in line 1, hard character limits, thread spine | Format Specs |
| Memo, proposal, status update, exec summary | Decision-first shape; what each document owes its reader | Format Specs |
| Editing someone else's draft, or answering editor notes | Severity tiers; editorial letter vs inline; leave evidence untouched | Output Gates + Rule 7 |
| Same voice across many pieces / house style | A style sheet as a written artifact | `references/memory-template.md` |
| Writing in a language that is not their first | Register and L1 interference, hedging calibration, idiom risk | Configuration + Traps |
| Anything else writing | Name the format, the one reader, and the single post-reading action; draft to that; run Output Gates | — |

## Core rules

1. **Read the voice before writing a word.** `## Voice`, `## Never`, and
   `## Formats` in `memory.md`, plus any sample or style sheet `## Boxes`
   points at for this format. Writing first and adjusting after produces a
   draft the user has to reject once — the most expensive mistake here, because
   it costs trust, not just a turn.
2. **Structure before sentences.** Before polishing, state the piece's claim in
   one sentence and its moves in order. If you cannot, the problem is not the
   prose and no line edit will fix it. Line-editing a piece whose order is wrong
   is work that gets deleted.
3. **The cut is arithmetic, not taste.** Target reduction = draft words ×
   `cut_target_pct` (default 20%); target length = draft words ×
   (1 − `cut_target_pct`). A 1,200-word draft loses 240 words and returns at
   ≤960 — report what leaves. King's rule of thumb — second draft = first draft
   − 10% — is the floor, not the ceiling. Cut order: whole sections → restating
   sentences → subordinate clauses → adjectives.
4. **Match the fingerprint, not the tics.** A voice is four measurable things:
   sentence-length distribution, who or what occupies the subject slot,
   concreteness ratio, and the never-list. Catchphrases without those four
   produce parody, and users read parody as mockery.
5. **One ask, once, in the first screen.** Any piece that wants something states
   it before the justifying context: what, by when, by whom. Context after the
   ask is read; context before the ask is skipped.
6. **Deliver the text, not the advice.** Default output is the finished passage
   in `markup`, ready to paste. Notes on what changed only when `explain_edits`
   is true, when a change alters meaning, or when the user asked why.
7. **Leave quotations, names, numbers, citations, and code byte-identical.**
   Quoted speech, legal language, brand names, figures, and identifiers are the
   writer's evidence. Flag a suspected error beside them; correct only with
   explicit permission. This survives every other rule, including voice matching.
8. **Readability scores are triage, not targets.** Flesch Reading Ease =
   206.835 − 1.015 × (words ÷ sentences) − 84.6 × (syllables ÷ words). Use it to
   find the one paragraph scoring far below the piece's own average. The formula
   counts syllables, so accurate technical terms score as "hard" while vague
   prose scores well.
9. **Rhythm is variance, not length.** Flag three or more consecutive sentences
   within ±3 words of each other — that flatness is what readers call "robotic".
   A single long sentence is a problem only when it carries more than one main
   clause plus two subordinate ones; `sentence_flag_words` (default 30) is the
   trigger to inspect, not the verdict.

## Format specs

Conventional budgets and shapes. Where an outlet, employer, or platform
publishes its own limit, that number wins — check it and record it in
`<state_root>/style-sheets/<context>.md`. Reading time ≈ words ÷ 240 (silent
prose ~200–300 wpm, Rayner); spoken delivery ≈ words ÷ 140. See
`references/sources.md` for the research anchors behind these defaults.

| Format | Budget | Shape | Opening | Done when |
|---|---|---|---|---|
| Email, internal | 50-150 words | Ask → context → next step | The ask, in the first two lines | One decision is requested and the deadline is a date |
| Email, cold | 75-125 words | Relevance → specific ask → easy out | Why this person, not why you | It can be answered with one word |
| Chat message | 1-3 sentences | Whole ask in one message | The ask | No standalone "hi" message |
| Blog post | 800-1,500 words | Hook → promise → 3-5 sections → payoff | A concrete scene, number, or claim | Every subhead states something, not a topic |
| Essay | 1,500-4,000 words | Question → attempts → turn → resolution | The tension, not the thesis | The turn is earned, not announced |
| Op-ed | 600-800 words | Claim in ¶1 → 3 arguments → call | The claim | The outlet's stated limit is met exactly |
| Newsletter issue | 400-1,200 words | One idea per issue + standing furniture | The idea, above the fold | It survives a 90-second phone read |
| Memo | 1 page (~500 words) | BLUF: decision → why → next | The decision or recommendation | A reader who stops after ¶1 acts correctly |
| Proposal | 2-10 pages | Problem → approach → scope → price → risk | The problem in their words | Scope names what is excluded |
| Exec summary | 150-300 words | Situation → complication → question → answer | The answer | It stands alone with the deck deleted |
| Status update | 100-200 words | Shipped → blocked → next → ask | The one thing that changed | A blocked item names who unblocks it |
| X post / thread | 280 chars per post | Hook → one idea per post → close | The claim, no throat-clearing | Post 1 works alone |
| LinkedIn post | 100-250 words | Line 1 payload → short paragraphs → one ask | Payload before the "see more" fold | It reads with formatting stripped |
| Bio | 25 / 50 / 100 words | Role → proof → hook | Role and current work | All three lengths exist and agree |
| Cover letter | 250-400 words | Why them → evidence → first move | A specific fact about them | Nothing restates the résumé |
| Speech / script | words ÷ 140 = minutes | One idea per minute, signposted | A concrete image | Read aloud without stumbling twice |

## Sentence diagnostics

The observable symptom names the repair.

| Symptom | Cause | Repair |
|---|---|---|
| Reader asks "so who does what?" | Subject slot holds an abstraction, not an actor | Put the character in the subject and the action in the verb |
| Sentence is 40 words and still vague | Nominalizations (`make a decision`, `provide support`) | Turn each noun back into its verb; the sentence usually halves |
| Every sentence the same length | Flat rhythm, the loudest machine-written tell (Rule 9) | Break one long sentence; fuse two short ones; aim for a spread |
| Paragraph read twice to follow it | New information in the topic position (Gopen & Swan) | Open with known information; end on what is new |
| Feels hedged and weightless | Stacked qualifiers (`may potentially`, `it seems that`) | One hedge per claim, maximum |
| Same referent renamed three times | Elegant variation — reader thinks a new thing arrived | One thing, one name, every time |
| Transitions feel bolted on | Paragraphs are in the wrong order | Reorder, then delete the connective that is no longer needed |
| Strong draft, weak ending | Stops at the last argument | End on the change in the reader, not a summary |
| Anything else | Read it aloud; the stumble is the cut | — |

## Output gates

Before delivering any draft or edit:

- Can I state this piece's one claim and its 3–5 moves in order — and does the draft follow that order (Rule 2)?
- Is the ask, decision, or payload inside the first screen, stated once (Rule 5)?
- Did I check the draft against `## Voice` and `## Never`, and is every never-list word absent?
- Does the sentence-length spread vary, with no three consecutive sentences within ±3 words (Rule 9)?
- Is it inside the format's budget after the cut, and inside the platform's hard limit where one exists?
- Are quotations, names, numbers, citations, and code blocks byte-identical to the source (Rule 7)?
- Am I returning the finished text in `markup`, not a list of suggestions (Rule 6)?
- Did anything durable come out of this? If yes, write it through `references/memory-template.md` in this same turn.

## Configuration

Defaults apply until the user states a preference; store declared values in
`<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| voice_file | path | none | Long-form voice guide under `<state_root>/`; outranks observed traits on conflict |
| spelling | us \| uk \| ca \| au \| in | us | Spelling, quotation-mark, and date conventions |
| edit_depth | light \| standard \| heavy | standard | `light` = mechanics/cuts; `standard` = sentence rewrites; `heavy` = reorder/rewrite sections |
| cut_target_pct | number (0-40, %) | 20 | Cut-pass reduction target (Rule 3) |
| feedback_mode | rewrite \| inline \| letter | rewrite | Corrected text vs margin notes vs editorial letter |
| explain_edits | bool | false | Attach a one-line reason to non-trivial changes (Rule 6) |
| sentence_flag_words | number (15-60) | 30 | Length that triggers sentence inspection (Rule 9) |
| markup | markdown \| plain \| html \| rich-notes | markdown | Delivery format for every draft |
| default_register | text | none | Baseline formality when the format does not dictate one |
| ai_tell_sweep | bool | true | Check generated drafts against machine-written tells before delivery |

Preference areas — record a stated preference in `config.yaml` and apply from then on:

- **Conventions** — Oxford comma, em-dash vs parentheses, heading case, numerals vs words, contractions, emoji, ellipsis/exclamation tolerance
- **Output register** — first vs second person, "we" vs "I", jargon tolerance, humour, profanity
- **Work order** — outline-before-draft vs draft-then-restructure; how many variants; diff vs whole text
- **Channels** — where they publish and each channel's real limits
- **Restrictions** — banned phrases, claims they may not make, compliance review, embargoes, off-limits topics
- **Cadence** — publishing rhythm and review cycles → rows in `## Due`
- **Languages** — languages/registers they write in; dialect via `spelling`

## Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Editing while drafting | Critic and generator compete; the draft never finishes | Zero draft to the last line first, timeboxed, then edit |
| Line-editing a piece whose order is wrong | Every polished sentence dies in the restructure | Structure pass first (Rule 2) |
| Cutting adjectives to hit a word target | Recovers a marginal fraction; leaves repeated sections | Cut in Rule 3 order |
| Copying catchphrases to imitate a voice | Reproduces tics without structure → parody | Match the four fingerprint dimensions first (Rule 4) |
| Asking "does this sound like you?" | Yes/no gives nothing durable to store | Offer two variants that differ on one dimension |
| Front-loading context before the ask | Reader skims for the ask and misses the context | Ask first, context second (Rule 5) |
| Hunting passive voice everywhere | Passive is correct when the receiver is the paragraph topic | Fix passives that hide the actor; keep topic-holding ones |
| Adding a summary because the piece is unclear | Doubles length and confirms the body failed | Fix the body; summaries serve length, not confusion |
| Treating house style as grammar | Style preferences are not errors | Style sheet decides; flag as style |
| Applying the user's stored voice to a ghostwritten piece | The byline belongs to someone else | Select voice by byline and context |
| Proofing on screen in the same view it was written | The eye completes what it expects | Change the medium: read aloud, or last-paragraph-first |
| Rewriting a quote to make it flow | Fabricates a source's words | Ellipsis inside quotes, brackets for additions, or paraphrase outside marks (Rule 7) |
| A style decision that only lives in chat | Re-litigated every piece | Style-sheet artifact with date and reasoning |
| Sending it the moment it reads well | It reads well to the person who just wrote it | Gate the send on Output Gates |

## Where experts disagree

- **Outline first vs discovery draft.** Argument-driven pieces (memos, proposals, op-eds) fail without a fixed outline. Exploratory pieces often discover the conclusion on the page. Frontier: does the piece transmit a conclusion, or reach one?
- **Readability formulas.** Plain-language practice treats ~20-word average sentences as a target; technical editors note syllable formulas penalise precise terms. Use the score to find outliers inside one document (Rule 8); see `references/sources.md`.
- **Adverbs and qualifiers.** Intensifying `-ly` adverbs that prop up weak verbs are usually cut; adverbs that change truth conditions (`rarely`, `only`, `almost`) stay.
- **Voice imitation limits.** Reproduce voice freely; keep claims, opinions, and commitments limited to what the person has already made.
- **How much to cut.** Prose written to be read rewards compression; prose written to be heard needs redundancy. Cut a memo hard; leave a speech its repetitions.

## Security and privacy

**Local storage:** voice traits, style sheets, samples, templates, and the
finished-piece log stay under `<state_root>/`, with person rows in the shared
contacts box and project files under the shared projects root.

**This skill stays local:** it does not publish, open network requests for
delivery, or store publishing-platform credentials. Drafts and pasted text are
stored only when the user asks to keep them; secrets inside them become pointers
before writing (`references/memory-template.md`).

**Guardrails:** clearing or overwriting stored voice, samples, or style sheets
requires explicit confirmation. A stored preference survives a single
contradictory draft until the user revises the declaration.
