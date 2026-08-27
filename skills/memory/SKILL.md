---
name: memory
description: Manage a durable markdown fact store at <state_root>/ for long-term memory. Trigger this skill when the user explicitly asks to remember, update, or forget a fact, or when retrieving historical context outside of the current session. Do not use for session-scoped context.
metadata:
  related-skills: '{"notes": "Note-taking into apps like Obsidian, Notion, or Apple Notes; use it when the destination is an app, not a durable fact store", "journal": "Journaling practice, prompts, and reflection; use it for the entry the user writes, not the fact you extract from it", "learn": "Spaced repetition and study tracking; use it when the goal is knowing something by heart, not looking it up", "spaced-repetition": "Scheduling review at expanding intervals for retention; use it when the goal is remembering by spaced practice, not looking a fact up", "decide": "Decision-making patterns on top of the decisions/ category this store builds"}'
  openclaw: '{"emoji":"🧠","requires":{"config":["<state_root>/"]}}'
---

All data lives in `<state_root>/` on the user's machine — plain markdown, no external services, no network requests. Configuration in `<state_root>/config.yaml` (`references/setup.md` on first use, `references/memory-template.md` for file formats). If you have data at an old location (like `~/memory/` or `~/clawic/memory/`), move it to `<state_root>/`, and say in one line that you moved it and from where.

## When To Use

- User says "remember this", "save this", "don't forget" about anything with lasting value
- Recall: "what did I tell you about X", "when did we decide Y", "who is Z" — search `<state_root>/` before answering "I don't know"
- A stored fact changed, turned out wrong, or contradicts what the user just said
- The user wants something forgotten, or asks what is stored about a subject
- Consolidating scattered notes, importing an existing vault, or sharing the store across devices and agents
- Recall degrades: misses, duplicates, stale answers, slow lookups as the store grows
- Direct session-scoped context to built-in memory, decline secrets (Rule 9), and use dedicated skills for note-taking (`notes`), journaling (`journal`), or studying (`learn`, `spaced-repetition`)
- Store domain facts in their respective skill's data folder (Rule 5): route pet facts to `dog`/`cat`, household to `family`, plants to `garden`, code style to `coding`

## Quick Reference

| Situation | Play | When to load |
|-----------|------|--------------|
| No `<state_root>/` yet | Run the setup conversation — `references/setup.md` | When `<state_root>/` does not exist |
| User shares something durable | Write the entry + update the category INDEX **before** replying (Rule 3); what qualifies → `references/capture.md` | When user explicitly wants to save a durable fact |
| User asks about the past | Search ladder: root INDEX → category INDEX → one file (→ Finding Things); it missed → `references/recall.md` | When answering questions about past decisions or facts |
| "Actually it's X now" | Supersede: new dated line, old line moved to History with its own date (Rule 8) → `references/conflicts.md` | When updating or correcting an existing fact |
| Stored fact was never true | Delete it — archiving a wrong fact resurfaces it as true (Rule 8) | When fixing an incorrect entry |
| Two files about the same person or project | Merge into the older file, leave a one-line pointer behind → `references/entities.md` |
| Two people share a name | Disambiguate the filename with a stable token (company, role), never `-2` → `references/entities.md` |
| "Forget that" / delete request | Purge file + index rows + inbound links, then report exactly what was removed → `references/privacy.md` |
| User offers a password, key, or token | Decline and store a pointer to where it lives (Rule 9) → `references/privacy.md` |
| Existing vault or another agent's memory to import | Category-by-category with a dedupe pass, never a bulk copy → `references/migration.md` |
| Store lives in Dropbox/iCloud/git, or two agents write to it | `references/sync.md` |
| Category INDEX past `index_split_at` (default 100) | Split along the axis you retrieve by (Rule 6) → `references/layouts.md` |
| Over 500 files and recall is degrading | `references/scaling.md` |
| Deciding how much memory to read this session | Root INDEX only at start; open one file after the index names it → `references/sessions.md` |
| Fact fits two categories | One canonical home, links from the rest (Rule 5) |
| Fact belongs to a domain that has its own Clawic skill and store | Write it in that skill's `<state_root>/`, keep only a pointer line here (Rule 5) |
| Anything else | Closest existing category beats a new one; if nothing fits, `inbox/` and sort it at maintenance |

Depth on demand: `references/capture.md` what to write and how to phrase it · `references/recall.md` search ladder, query expansion, proactive lookup · `references/conflicts.md` changed vs wrong facts, temporal validity · `references/entities.md` people, projects, aliases, merges · `references/privacy.md` secrets, sensitive subjects, deletion requests · `references/migration.md` importing and exporting · `references/sync.md` multi-device, git, multi-agent · `references/scaling.md` growth thresholds and when plain files stop being enough · `references/sessions.md` read/write protocol per session · `references/maintenance.md` cadences and integrity repair · `references/layouts.md` folder structures and split axes · `references/commands.md` operator toolkit · `references/troubleshooting.md` symptom→cause · `references/memory-template.md` file formats · `references/setup.md` first run.

## Core Rules

1. **Built-in memory is read-only territory, and sync runs one way.** Never modify the runtime's MEMORY.md or workspace `memory/` — the runtime owns them and may rewrite them, so your edits are lost or conflict. This skill reads them and copies into `<state_root>/sync/`, reformatted, with the sync date recorded in `sync/INDEX.md`. Never the reverse, never automatic.

2. **The user defines the structure.** Create categories from their words, not a preset taxonomy. A category created before its first item rots empty and teaches the user the system is dead weight.

   | They say... | Create |
   |-------------|--------|
   | "I have many projects" | `<state_root>/projects/` |
   | "I meet lots of people" | `<state_root>/people/` |
   | "I want to track decisions" | `<state_root>/decisions/` |
   | "I'm learning [topic]" | `<state_root>/knowledge/[topic]/` |
   | "I collect [things]" | `<state_root>/collections/[things]/` |

3. **Write before you reply.** Sequence: write the entry → update the category INDEX.md → then respond. The reply is disposable; the write is the durable part. A session that dies mid-reply then loses nothing.

4. **Every entry carries a date and a source.** `YYYY-MM-DD` plus one of `stated` (the user said it), `observed` (seen in a file or output), `inferred` (the agent concluded it). Undated facts can't be judged stale — "Alice works at Acme" means different things written last week and two years ago. Unsourced facts can't be trusted: an inference stored as a statement is the main way a memory store poisons itself, because Rule 8 lets a stated fact overrule an inferred one only if you can tell them apart.

5. **One fact, one home — including homes outside this store.** Store each fact in the file it is most *about*; everywhere else links to it (`→ people/alice.md`). Duplicated facts diverge silently — the copy you update is never the copy you find later. This applies across skills: when the fact's domain has its own Clawic store (`<state_root>/dog/`, `cat/`, `family/`, `couple/`, `garden/`, `kanban/`, `coding/`, `employee/`), that store is the home and this one keeps at most a pointer line — "dog's diet → `<state_root>/dog/`". Writing "the dog is allergic to chicken" in both places is the silent fork this rule exists to prevent.

6. **Every folder has an INDEX.md, capped at `index_split_at` (default 100).** Past the cap, split into subcategories. Capacity = cap^depth: at the default, two levels hold 10,000 items, three hold 1,000,000, and every lookup stays two or three small reads instead of one giant scan. Every number below written as 100 is that default — read `config.yaml` before judging any index size. Archive indices are exempt (rarely read, off the hot path).

7. **Keep entry files lean.** An entry is loaded whole to answer one question, so its size is a tax on every question. Past `entry_max_lines` (default ~200), move the `## History` bulk to `{name}-history.md` and keep the dossier short; the history file is opened only when someone asks about the past.

8. **Changed facts supersede; wrong facts get deleted.** A fact that *became* false (Alice left Acme) keeps its old line, dated, under History, with the new line on top — the timeline is itself information. A fact that was *never* true (she never worked there) is deleted outright: archived wrong facts resurface later as truth. Test: "was this true on the day it was written?" Yes → supersede. No → delete.

9. **Never store secrets.** These files are plaintext with no encryption. Decline passwords, API keys, tokens, and full card or account numbers; store a pointer instead — "API key lives in [their vault], rotated 2026-07".

## Built-In Memory vs This Store

Built-in memory holds current context and works automatically. This store holds everything that grows. Parallel and complementary — never a replacement.

| | Built-in memory | This skill (`<state_root>/`) |
|---|---|---|
| Size | Small, summaries | Unlimited |
| Written by | The runtime, automatically | This skill, by explicit rules |
| Holds | Current status, quick facts, recent decisions | Full histories, dossiers, decision logs, collections, domain knowledge |
| Touched here | Read-only (sync source) | Fully managed |
| Survives | The runtime's own compaction rules | Until deleted on purpose |

The same item can live in both — summary there, detail here, and the summary points here. When in doubt: does it grow over time, or does it need to be findable in a year? Then it belongs here.

## Entry Anatomy

Every entry file, whatever the category, carries the same four things (full templates: `references/memory-template.md`):

```markdown
# Alice Smith                                    <- display name, human-readable
**Keywords:** Ali, PM, product manager, Acme, alpha project    <- retrieval aliases
**Updated:** 2026-07-25                          <- freshness at a glance

## Facts
- 2026-07-25 · stated · Moved to Northwind as Head of Product
- 2026-03-02 · stated · Prefers async updates, no calls before 10:00

## History
- 2024-11-08 · stated · Joined Acme as PM   (superseded 2026-07-25)
```

- **Filename is a stable slug** (`alice-smith.md`), never the display name — renames break every inbound link (`references/entities.md`).
- **One fact per line, dated and sourced** (Rule 4). Lines, not paragraphs: a paragraph can't be superseded or deleted surgically.
- **Keywords is the retrieval index**, not decoration — see Finding Things.

## Finding Things

| Store size | Strategy |
|-------------|----------|
| <50 files | `grep -ri "keyword" <state_root>/` — a full scan is cheap |
| 50–500 files | Indices first: `grep -i "keyword" <state_root>/*/INDEX.md`, then open the one matching file |
| >500 files | Hierarchical: root INDEX → category INDEX → file; semantic search if `search_backend` says the runtime has it |

```bash
cat <state_root>/INDEX.md                 # which categories exist
grep -i "alpha" <state_root>/*/INDEX.md   # which category holds it
cat <state_root>/projects/alpha.md        # the answer
```

Vocabulary asymmetry is the reason recall misses: grep matches the words used at *write* time, recall arrives in *today's* words. Try at least 3 variants — the user's word, the formal name, the entity's canonical slug — before concluding absence, and when a miss is later resolved, add the missed term to that file's `Keywords:` line so the same search never misses twice (`references/recall.md`).

## When Facts Change

| The user says | Do |
|---|---|
| "It's X now" | Supersede: new dated line on top, old line to History with its original date (Rule 8) |
| "That was never right" | Delete the line; if the whole entry was wrong, delete the file and its index row |
| "I'm not sure any more" | Keep the fact, mark it `stale YYYY-MM-DD`; a doubted fact recalled with its doubt beats a silent gap |
| Two stored facts disagree | The one with the later date and the stronger source wins; `stated` beats `observed` beats `inferred` on the same date |
| Nothing — the fact just aged | Class-based expiry: identity facts never expire, role and address facts get re-checked yearly, project-state facts within weeks (`references/conflicts.md`) |

## Maintenance

**Every session:** anything durable said this session is written (Rule 3); anything unclear is in `inbox/`.

**Weekly** (or per `maintenance_cadence`): sort `inbox/` into categories; update any INDEX touched during the week; archive items with terminal status (completed, cancelled, inactive).

**Monthly:** audit index sizes (`wc -l <state_root>/*/INDEX.md`); split any category past `index_split_at`; sweep for stale facts by class; delete entries that are wrong. Repair procedures and the integrity checks: `references/maintenance.md`.

## Output Gates

Before replying when the user shared something durable:
- Is it written to `<state_root>/` already? (Rule 3 — the write precedes the reply)
- Is the category INDEX.md row added or updated?
- Does the entry carry a date and a source marker? (Rule 4)

Before answering "I don't remember": did the full search ladder run with ≥3 keyword variants, including `inbox/`, `sync/`, and built-in memory?

Before storing: does it contain a credential (Rule 9) or fall under `excluded_topics`? → decline and say so once.

Before deleting: is this a wrong fact rather than an outdated one (Rule 8), and does `delete_policy` require confirmation first?

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| index_split_at | number (25-250) | 100 | Entry count at which a category INDEX splits into subcategories (Rule 6; split axes in `references/layouts.md`) |
| entry_max_lines | number (100-500) | 200 | Line count at which an entry's History moves to `{name}-history.md` (Rule 7) |
| delete_policy | confirm \| direct | confirm | Whether removing a file or fact needs an explicit go-ahead first (Output Gates, `references/privacy.md`) |
| recall_citations | bool | true | Whether a recalled fact is answered with its file path and date, or as a bare answer (`references/recall.md`) |
| sync_from_builtin | bool | false | Enables the one-way built-in → `sync/` copy during maintenance (Rule 1) |
| excluded_topics | list | empty | Subjects never written to the store even when mentioned; the agent says so once instead of storing (`references/privacy.md`) |
| inbox_enabled | bool | true | Whether unclear items land in `inbox/` or force a category decision at capture time (`references/capture.md`) |
| maintenance_cadence | weekly \| monthly \| on-demand | weekly | Frequency of the inbox sort, index audit, and staleness sweep (Maintenance) |
| search_backend | grep \| semantic | grep | Which retrieval path the >500-file rung of the search ladder uses (Finding Things) |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:

- **Taxonomy**: which categories exist and what belongs in each — affects Rule 2 and every capture routing decision
- **Capture threshold**: write everything said, or only explicit "remember this" — affects the durability test in `references/capture.md`
- **Naming conventions**: filename style, entity slug format, index columns — affects `references/entities.md` and `references/memory-template.md`
- **Retrieval style**: how much surrounding context comes back with an answer, and whether the agent volunteers related facts unasked — affects `references/recall.md` and `references/sessions.md`
- **Privacy posture**: which subjects need an explicit go-ahead, whether third-party personal details are stored at all — affects `references/privacy.md`
- **Sync and versioning**: cloud folder, git history, which agents share the store — affects `references/sync.md`
- **Language**: which language entries are written in when it differs from the conversation — affects every write

## Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| Modifying built-in memory | The runtime owns it; edits are overwritten or conflict | Read-only, parallel system (Rule 1) |
| Batching writes for later | The session can end between hearing and writing | Write before replying (Rule 3) |
| Same fact in two files | Copies diverge; you update one and retrieve the other | One home + links (Rule 5) |
| Storing the conversation instead of the fact | "User mentioned maybe Postgres" answers nothing a year later | Store the resolved fact with its date and source (`references/capture.md`) |
| An inference written as a statement | Later contradicts the user and gets defended as if they had said it | Source marker on every line (Rule 4) |
| Archiving a wrong fact | Archive preserves it; it resurfaces as true | Wrong → delete; old-but-true → supersede (Rule 8) |
| Undated entries | A current fact and a two-year-old one look identical | Date-stamp everything (Rule 4) |
| No indices | Every lookup degrades to a full-folder grep; misses rise with size | INDEX.md in every folder (Rule 6) |
| One giant category | 500 unsplit items = slow scans and noisy grep hits | Split at `index_split_at` (Rule 6) |
| Renaming files by hand | Dead links — recall says "not found" while the data sits there | Rename = `mv` + fix every index and inbound link (`references/entities.md`) |
| Bulk-copying an old vault in | Mass duplicates with no dates or sources, and the store loses trust on day one | Category slices with a dedupe pass (`references/migration.md`) |
| Syncing everything from built-in | Duplication of things built-in already answers | Sync only what needs deep structure (Rule 1) |
| Loading the whole store at session start | Burns context on facts nobody asked about | Root INDEX first, one file after (`references/sessions.md`) |
| Storing a fact a domain skill already owns | Two stores answer the same question and neither knows about the other | Domain store is the home; keep a pointer here (Rule 5) |

## Where Experts Disagree

- **Capture everything vs curate.** Capture-everything survives only with real maintenance; curated stores stay fast but lose the fact nobody thought was important. Default: capture durable facts, inbox the ambiguous ones, and let the weekly sort be the curation step — the split lives in the `capture threshold` preference area.
- **Folders vs flat plus tags.** Flat + `Keywords:` scales fine for retrieval and badly for browsing; folders make a human able to read the store like a book. Default: folders, because the human decides whether the system is worth keeping. Escape hatch: one flat category with heavy keywords for domains with no natural taxonomy.
- **Plain files vs a database.** Grep over markdown stays honest, portable, and inspectable; an index or embedding store answers fuzzy questions plain grep can't. Default: files until >500 entries AND recall still misses after the Keywords fix (`references/scaling.md`) — the migration is one-way in practice.

## Security & Privacy

**Data location:**
- All data in `<state_root>/` on the user's machine
- No external services, no network requests

**Skill Boundaries:**
- Treat built-in agent memory as read-only (for one-way sync)
- Keep data strictly on the local machine
- Decline secrets and keep storage plaintext (Rule 9)
- Skip subjects listed in `excluded_topics`

**Guardrails:** deletion requests are honored in full and reported back (`references/privacy.md`); anything stored about third parties is limited to what the user needs recalled.
