---
name: bookmarks
description: "Build a unified bookmark system that imports saves from X, YouTube, Reddit, Pinterest, Instagram, TikTok, and manual links into one tagged, searchable collection under portable state. Use when the user wants to consolidate bookmarks or read-later queues, auto-tag saves, search old saves, run digests of saved themes, clean stale links, or keep a silent background bookmark workspace; not for inbox triage (`inbox`) or generic knowledge vaults."
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔖","requires":{"config":["<state_root>/"]},"displayName":"Bookmarks"}'
  related-skills: '{"inbox":"Triage unread streams across email/chat/tools rather than long-lived bookmark collections.","archive":"Long-term archival of completed material after bookmark usefulness fades.","productivity":"Prioritize which saved items deserve action beyond passive organization.","brief":"Turn bookmark themes into concise status briefs when the user wants a digest.","journal":"Capture free-form notes about why a save mattered outside structured bookmark tags."}'
---

## State location

Bookmark workspace may exist in `<workspace>/bookmarks/`, `<workspace>/memory/bookmarks/`, or `~/bookmarks/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/bookmarks/`, `<workspace>/memory/bookmarks/`, `~/bookmarks/`.
3. If none exists and state must be created, ask for permission and default to `<workspace>/bookmarks/`.

Use the selected `<state_root>` for every state operation in this skill.

Directory structure after resolution:

```text
<state_root>/
├── saves.md          # All saves, tagged
├── sources.md        # Connected platforms and import policy
├── preferences.md    # Passive / digest / active / cleanup style
└── reports/          # Generated summaries (create only when needed)
```

If data still sits at a legacy path such as `~/Clawic/data/bookmarks/`, treat it as a migration source only: copy after consent, validate, then cut over. Do not keep the legacy path in active lookup order.

## When to Use

- Consolidate bookmarks / likes / watch-later / pins into one searchable collection
- Auto-tag new saves and keep source provenance
- Search by tag, source, or fuzzy title text
- Optional weekly/monthly digests, project resurfacing, or stale-save cleanup
- Keep the system silent until the user asks or opts into digests

Out of scope:

- Live inbox triage across email/chat (`inbox`)
- Sending messages or mutating remote social accounts without explicit grant
- Replacing a full knowledge wiki / Obsidian vault

## Quick Reference

Load only the file needed for the current step; keep `SKILL.md` as the control plane.

| Topic | File | When to load |
|---|---|---|
| Domain knowledge and retention research | `references/domain_knowledge.md` | Explaining bookmark vs social-bookmarking concepts, or justifying silent-default / tag-first design |
| Save / source / preference schemas | `references/workspace-schemas.md` | Creating or editing `<state_root>` files |
| Import, search, digest, and cleanup workflows | `references/workflows.md` | Running setup, search, digest, or stale-link cleanup |

## Core Behavior

- Import explicit saves silently from connected platforms
- Auto-tag and organize without forcing folder hierarchies
- Surface results only when useful, asked, or configured
- Preserve original source context on every save
- Persist everything under the resolved `<state_root>/`

## Philosophy

User saves things and forgets — that is fine. The system:

- Works silently in the background
- Avoids interrupting unless configured to
- Is available when the user searches or asks
- Optionally produces periodic summaries when requested

## Saves Format

Prefer tags over folders:

```markdown
# saves.md
## 2024-02-11
- [Thread on AI agents](https://example.com/ai-agents)
  source: X | tags: #tech #ai

- [Kitchen inspiration](https://example.com/kitchen)
  source: Pinterest | tags: #home #design

- [Article user shared](https://example.com/article)
  source: manual | tags: #productivity
```

## Setup

### Minimal Start

1. Connect sources (X, YouTube, Reddit, Pinterest, Instagram, TikTok, manual).
2. Import explicit saves — silently, no questionnaire.
3. Auto-tag based on title/content signals.
4. Leave the workspace running in the background.

### Ask Later (After They Have Saves)

Only after meaningful volume exists, offer optional modes:

- Send a weekly summary of themes?
- Alert when something relates to a current project?
- Periodically ask whether old saves are still relevant?
- Stay silent until search?

## Per-Person Preferences

```markdown
# preferences.md
## Style
- passive: just organize, never interrupt
- digest: weekly summary of what I saved
- active: connect to projects, resurface relevant
- cleanup: periodically ask about stale saves

## Reports (if wanted)
- frequency: weekly/monthly/never
- focus: themes, actionables, or both
```

## Sources

```markdown
# sources.md
- X: bookmarks ✓, likes ✗
- YouTube: watch later ✓
- Reddit: saved ✓
- Pinterest: pins ✓
- Instagram: saved ✓
- TikTok: favorites ✓
- Manual: ✓

Note: Default to explicit saves only.
Ask before importing likes (too noisy).
```

## Reports (Optional)

```markdown
# reports/2024-02-week-6.md
## What You Saved This Week
- 8 saves total
- Themes: AI (4), recipes (2), travel (2)

## Patterns
- You're saving a lot about AI agents lately

## Actionables
- That tutorial from 3 weeks ago — tried it?

## Stale
- 12 saves from 6+ months ago, unvisited
```

## What To Surface

Only when configured or asked:

- "Your saves this week: mostly AI and design"
- "Old save relates to what you're working on"
- "15 dead links cleaned up"

## Searching

When the user asks:

- "What did I save about X?" → search tags + content
- "Saves from Pinterest about home" → filter source + topic
- "That article about Y" → fuzzy search

## Operating Guidelines

- Keep setup simple and silent; limit questions during initial configuration
- Rely on tags instead of folder hierarchies for organization
- Default to a silent approach; notify only when explicitly requested
- Respect individual preferences for workflows (passive, active, digest, cleanup)
- Always retain and record the original source of the save
- Request platform access only for sources the user explicitly connects
- Treat remote mutations (unlike, unpin, delete cloud save) as ask-first actions
