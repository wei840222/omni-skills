---
name: english
description: >
  Edit and correct English for native cadence, register, and regional variety
  (US, UK, AU, CA, IE, IN, NZ). Use when text sounds stiff, translated, robotic,
  or AI-generated; when grammar is fine but tone is wrong; when spelling,
  vocabulary, punctuation, or dates mix varieties; when L1 interference
  (articles, prepositions, tense, collocations) shows; when email or meeting
  register must match the reader; or for pronunciation, small talk, and
  deliberate practice. Not for grammar-only passes (`grammar`), translation
  (`translate`), IELTS/TOEFL tactics (`ielts`, `toefl`), or drafting in the
  user's own long-form voice (`writing`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇬🇧"}'
  related-skills: '{"grammar":"Pure correctness passes where meaning and style must not move.","writing":"Long-form drafting and editing in the users own voice.","translate":"Moving text between languages, glossaries, and localization.","ielts":"Band scoring, task types, and exam tactics for IELTS.","toefl":"TOEFL iBT structure, scoring, and admissions prep.","speak":"Turning text into speech-ready output for a TTS engine."}'
---
# English

Target is *this variety, at this register, to this person, with no seams* — not abstract "correctness". Name which of variety / register / person / seam is off before rewriting, and change only that. Infer variety, first language, and register from the text; state assumptions in one clause; start the edit without a questionnaire.

## State location

English state may exist in `<workspace>/english/`, `<workspace>/memory/english/`, or `~/english/`. Shared contacts may exist in `<workspace>/contacts/`, `<workspace>/memory/contacts/`, or `~/contacts/`. Shared projects may exist in `<workspace>/projects/`, `<workspace>/memory/projects/`, or `~/projects/`. Shared profile may exist as `<workspace>/profile.yaml`, `<workspace>/memory/profile.yaml`, or `~/profile.yaml`. `<workspace>` is the host/runtime workspace root (resolve from host/runtime config, not from the shell cwd alone).

Before any state read or write, resolve `<state_root>` once:

1. Use an explicitly configured path from the user or host when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/english/`, `<workspace>/memory/english/`, `~/english/`.
3. When multiple candidates exist, use only the highest-precedence one, tell the user duplicates were found, and leave the others unchanged.
4. When none exists and durable notes must be saved, propose `<workspace>/english/` (or an explicit path if no workspace is available) and obtain named consent before creating it.
5. Legacy paths `~/Clawic/data/english/`, `~/clawic/english/`, and bare `~/english/` copies outside the selected root are migration sources only. Copy into the selected layout only after the user names the destination; leave legacy trees untouched unless the user asks to remove them.

Resolve shared contacts, projects, and profile the same way under their candidate lists above. Legacy `~/Clawic/data/contacts/`, `~/Clawic/data/projects/`, and `~/Clawic/profile.yaml` are migration sources only.

Use the selected `<state_root>` for every english-owned path. Keep skill resources under `references/` and `assets/` only. Write only resolved concrete paths to disk; keep `<state_root>` as a documentation placeholder.

### State tree (after resolution)

```text
<state_root>/
├── config.yaml          # declared preferences (optional until first save)
├── memory.md            # observed state, ## Boxes index, ## Due, ## Recurring Errors, ## Vocabulary
├── sessions/            # optional practice logs by year
│   └── YYYY.md
└── styles/              # optional reusable style sheets / voice samples
    └── <name>.md
```

Shared (outside english root, independently resolved):

- `<contacts_root>/contacts.md` — one row per person; this skill owns only the English `Context` cells it wrote
- `<projects_root>/<project>.md` — one line of English decisions for a tracked project
- `<profile_path>` — shared locale/country defaults

Create optional children only when needed. Credentials stay outside state roots; store pointers only (`env:…`, `keychain:…`, `1password:…`, `file:…`).

## Session bootstrap

1. Resolve `<state_root>` (and contacts/projects/profile roots when those boxes are needed).
2. Read `<state_root>/config.yaml` and `<state_root>/memory.md` when they exist. Open any path listed under `## Boxes` when its condition applies; ignore paths outside `<state_root>/`.
3. Before writing to a named person, read `<contacts_root>/contacts.md`.
4. Preference precedence: `config.yaml` → shared profile → Configuration table defaults. An observation overwrites a declaration only after the user confirms it.
5. If none of the files exist, work from defaults without narrating the gap.

**Write before the session ends** when the turn produced something durable: a correction needed twice; a word, collocation, or pronunciation they asked about; an approved reusable phrasing; a variety/spelling/punctuation decision; a domain term and agreed English rendering; the register that worked with a person; a practice session or level note; a style sheet, voice sample, speech, or template set. Load `references/memory.md` for destinations, formats, and thresholds; use `assets/memory-template.md` only as the blank shapes to copy.

In a shared box, update or remove only rows this skill wrote (match the box identity key). Rows another skill wrote stay read-only: extend the English `Context` cell when appropriate, leave every other column untouched. Name each write and deletion in one line as it happens.

## When to use

- Rewrite stiff, cold, translated, or AI-cadence English into native rhythm
- Enforce one variety across spelling, vocabulary, punctuation, quotes, dates, numbers
- Address systematic L1 interference (articles, prepositions, tense, false friends)
- Calibrate register for email, chat, meeting, client, boss, stranger, friend
- Settle mechanics house rules (commas, hyphens, quotes, titles, numbers)
- Speaking: stress, intonation, small talk, polite interruption
- Act-as by default; add the rule in one line when the same correction has appeared before
- Route pure grammar-only fixes to `grammar`, translation to `translate`, exam tactics to `ielts`/`toefl`, long-form voice drafting to `writing`, TTS prep to `speak`

## Progressive disclosure

| Situation | Load |
|---|---|
| Formality ladder, plain English, sentence-length bands | `references/register.md` |
| AI cadence tells and repairs | `references/ai-tells.md` |
| US/UK/AU/CA/IE/IN/NZ spelling and lexis splits | `references/varieties.md` |
| L1 interference procedures (articles, prepositions, tense) | `references/learners.md` |
| Punctuation, titles, dates, numbers house rules | `references/mechanics.md` |
| Confusables, jargon, nominalizations, hedging | `references/word-choice.md` |
| Idioms, phrasal verbs, collocations, slang freshness | `references/idioms.md` |
| Email shapes, chase cadence, understatement | `references/business.md` |
| Meetings, small talk, discourse markers | `references/conversation.md` |
| Stress, sounds, intelligibility-first practice | `references/pronunciation.md` |
| Level, error journal, collocation drills, review cadence | `references/practice.md` |
| Core editing rules 1–9 | `references/core-rules.md` |
| Grammar → collocation → register → cadence diagnosis | `references/the-four-layers.md` |
| High-leverage native signal swaps | `references/native-signals.md` |
| Pre-delivery checklist | `references/output-gates.md` |
| Config variables and preference areas | `references/configuration.md` |
| Common failure modes | `references/traps.md` |
| Contested style points with defaults | `references/where-experts-disagree.md` |
| State destinations and write thresholds | `references/memory.md` |
| Blank templates for memory/config boxes | `assets/memory-template.md` |
| Claim sources and freshness notes | `references/sources.md` |

## Quick reference

| Situation | Play | Depth |
|---|---|---|
| "Sounds AI-written" | Cut closing summary, break sentence-length uniformity, add one concrete specific | `references/ai-tells.md` |
| Correct but stiff | Contractions, one fragment, lighter connector | `references/register.md` |
| Too casual | Move up one notch only; hedge the ask, not the whole message | `references/register.md` |
| Mixed variety | Pick `variety`, sweep spelling axes in one pass | `references/varieties.md` |
| *gotten/got*, *at/on the weekend* | Variety-split table — both right, only one is yours | `references/varieties.md` |
| Article / preposition / "I am knowing" | Fix the class, not the sentence | `references/learners.md` |
| Comma splice, quotes, titles, 07/08 dates | House rules with variety split | `references/mechanics.md` |
| affect/effect, fewer/less, jargon | Confusables, then cut nominalizations | `references/word-choice.md` |
| Idiom or slang freshness | Register + freshness tags; prefer plain word when unsure | `references/idioms.md` |
| Ask, decline, chase, apologize | One shape per job | `references/business.md` |
| Interrupt, disagree, small talk | Phrase banks that stay polite in US/UK | `references/conversation.md` |
| Mispronounced word / "people don't understand me" | Stress and rhythm before individual sounds | `references/pronunciation.md` |
| "How do I get better?" | Level, error journal, collocation drilling | `references/practice.md` |

## Core rules (summary)

Full text: `references/core-rules.md`.

1. Match register to the relationship, not the maximum politeness.
2. In casual/neutral English, keep contraction density natural (about one every 2–3 sentences), with full forms for emphasis, legal/formal register, and sentence-final copulas.
3. Prefer sentence-length variance over uniform brevity; neutral default mean about 14–20 words with real spread.
4. Vary openers and endings; rewrite runs of identical openings.
5. One variety end-to-end (spelling, lexis, punctuation, dates, agreement).
6. Prefer verbs to nominalizations; more than about one *-tion/-ment/-ance/-ity* noun per 30 words reads bureaucratic.
7. One hedge per claim.
8. On the **second** occurrence of the same correction, name the class, give the rule once, and record it under `## Recurring Errors` in `<state_root>/memory.md`.
9. State assumptions; deliver the edit with a one-clause assumption instead of a setup questionnaire.

## Output gates

Before delivering edited English, run `references/output-gates.md`: read-aloud test; one variety; register fit; contraction and length variance; AI-tell scan; load-bearing hedges plus one concrete specific; meaning preserved; durable writes filed the same turn.

## Configuration

Defaults live in `references/configuration.md` and, once consented, in `<state_root>/config.yaml`. Key variables: `variety`, `spelling_system`, `register_default`, `first_language`, `oxford_comma` (default true), `correction_mode`, `max_sentence_words`, `banned_words`, `voice_file`, `review_cadence`.
