---
name: archive
description: Preserve user-provided URLs, text, and files as semantic snapshots, then retrieve them by topic, project, time, author, or content type. Use when the user asks to archive material or find a previously archived item.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📦"}'
  related-skills: '{"bookmarks":"Bookmarks stores just URLs, whereas Archive captures full content for permanence.","memory":"Memory manages agent context, whereas Archive preserves external content as snapshots.","pkm":"PKM manages evolving notes, whereas Archive handles immutable snapshots."}'
---


## State Location

Archive state may exist in `<workspace>/archive/`, `<workspace>/memory/archive/`, or `~/archive/`. `<workspace>` is the workspace root supplied by the host/runtime.

Before any state read, search, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path supplied by the user or host when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/archive/`, `<workspace>/memory/archive/`, `~/archive/`.
3. If multiple candidates exist, use only the first, tell the user that multiple archive locations were found, and leave other candidates unchanged.
4. If none exists and the host supplied `<workspace>`, ask for consent to create `<workspace>/archive/`; without a host workspace, ask for an explicit state path.

Use the selected `<state_root>` for every state operation in this invocation. Create the resolved path, not a literal directory named `<state_root>`.

## Architecture

Archive storage lives in the resolved `<state_root>/` with tiered structure. Read `assets/memory-template.md` when creating the initial archive files after consent.

```
<state_root>/
├── memory.md          # HOT: recent items, ≤100 lines
├── index.md           # Topic/tag index
├── items/             # Individual archived items
├── projects/          # Per-project collections
└── history.md         # Search/access history
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| What to capture | `references/capture.md` | When the user asks to save or archive new content. |
| Search patterns | `references/search.md` | When the user queries past archives or looks for saved info. |
| Resurfacing rules | `references/resurface.md` | When providing contextual information for a new task. |

## Core Rules

### 1. Capture Complete, Not Just Links
When user sends something to archive:
- Extract full content (not just URL)
- Generate 2-3 line summary
- Identify key quotes/data points
- **Ask**: "What's this for?" — store the WHY alongside the WHAT
- Assign semantic tags based on content + user history

### 2. Content Types
| Type | What to extract |
|------|-----------------|
| Article/webpage | Full text, author, date, key quotes |
| Video (YouTube) | Title, creator, duration, timestamps mentioned |
| Tweet/thread | Full text, author, context, media |
| PDF/paper | Title, authors, abstract, cited references |
| Image | Description, source, context given |
| Idea/note | Raw text + timestamp + related items |

### 3. Storage Structure
Each archived item stored as:
```
items/{date}_{slug}.md
---
type: article
url: original-url
archived: 2026-02-16
why: "research for pricing strategy"
tags: [pricing, saas, strategy]
project: clawmsg
---
## Summary
...
## Key Points
...
## Full Content
...
```

### 4. Semantic Search
User can ask naturally:
- "What did I save about X?" → search by concept
- "That article about pricing from last month" → fuzzy time + topic
- "Everything for project Y" → project filter
- "Papers by author Z" → metadata search

Always use conceptual matching over exact keywords.

### 5. Proactive Resurfacing
When user works on a topic:
- Check if archived items relate
- Surface ONLY if genuinely relevant (max 1-2 per session)
- Include context: "You saved this 3 months ago when researching X"

### 6. Preserve Before Deletion
- Mark old items as "possibly outdated" and retain them.
- Merge duplicates while retaining both URLs.
- Move closed projects to cold storage and retain their records.
- Obtain explicit confirmation before deleting any archived item.

## Scope

Use Archive only to store content the user explicitly sends, search archived content, or surface contextually relevant items.

Required protections:
- Start monitoring or observation only after an explicit request.
- Obtain confirmation before deleting content.
- Preserve original archived content unmodified.
- Access external services only after user action.

## Data Storage

After resolving `<state_root>` and receiving consent to create state, create only the needed directories:
```bash
mkdir -p <state_root>/items <state_root>/projects
```
