---
name: voice-notes
description: Organize voice message transcripts into a structured, searchable knowledge base. Use when the user sends voice messages and wants to process transcripts into notes, tags, and links.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🎤"}'
---

## State location

Voice Notes state may exist in `<workspace>/voice-notes/`, `<workspace>/memory/voice-notes/`, or `~/voice-notes/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/voice-notes/`, `<workspace>/memory/voice-notes/`, `~/voice-notes/`.
3. If none exists and state must be created, default to `<workspace>/voice-notes/`.

Use the selected `<state_root>` for every state operation in this skill.

## When to Use

User sends voice messages. The agent platform handles transcription (via its configured STT). This skill organizes the resulting transcripts into structured notes, links related content, and maintains a scalable tag-based system.

## Transcription is Platform-Handled

This skill delegates transcription to the platform. It expects the agent platform to:
1. Receive audio from the user
2. Transcribe it using the platform's configured STT (local or cloud)
3. Pass the transcript text to this skill for organization

The skill only organizes and stores text transcripts locally in `<state_root>/`. Audio files are never accessed or stored by this skill.

## Architecture

All data stored in `<state_root>/`. See `assets/memory-template.md` for setup.

```
<state_root>/
+-- memory.md           # HOT: tag registry + recent activity
+-- index.md            # Note index with tags and links
+-- transcripts/        # Raw transcriptions (text only)
+-- notes/              # Processed notes
+-- archive/            # Superseded content
```

## Quick Reference

- Read `assets/memory-template.md` for memory setup.
- Read `references/processing.md` for note processing.
- Read `references/linking.md` for linking system.
- Read `references/tags.md` for tag management.

## Data Storage

All data stored in `<state_root>/`. Create on first use:
```bash
# Example (replace with your actual state directory)
STATE_ROOT="$HOME/.openclaw/state/voice-notes"
mkdir -p "$STATE_ROOT"/{transcripts,notes,archive}
```

## Scope

This skill ONLY:
- Receives transcript text from the agent platform
- Stores transcripts and notes in `<state_root>/`
- Links related notes based on content
- Manages user-defined tags

This skill is restricted to:
- Relying on the platform for audio transcription
- Ignoring audio files
- Deleting content only with explicit user confirmation
- Accessing files only within `<state_root>/`
- Operating entirely locally without external requests
- Operating without API keys or credentials

## Self-Modification

This skill preserves its own SKILL.md without modification.
All data stored in `<state_root>/` files.

## Core Rules

### 1. Always Preserve Information
| Event | Action |
|-------|--------|
| New transcript | Save immediately to `transcripts/` |
| Edit note | Preserve original in transcript reference |
| Strategy change | Archive old version, link to new |
| User deletes | Confirm first, then move to `archive/` |

### 2. Tag System Over Folders
- Tags defined in `<state_root>/memory.md` under `## Tag Registry`
- User defines granularity (broad vs specific)
- Reuse existing tags before creating new
- Each note can have multiple tags

### 3. Detect Related Content
Before creating new note:
1. Search existing notes for topic overlap
2. If related -> append or link (not duplicate)
3. If continuation -> extend existing note
4. If contradicts -> link as evolution, preserve both

### 4. Document Scaling
When note exceeds ~100 lines:
1. Identify natural sections
2. Split into linked child notes
3. Parent becomes overview with links
4. Like Notion: notes contain notes

### 5. Progressive Disclosure
| Tier | When Loaded |
|------|-------------|
| `<state_root>/memory.md` | Always (tags, recent) |
| `<state_root>/index.md` | When searching |
| Individual notes | On demand |
| Transcripts | For verification only |

### 6. Reorganize Chaotic Input
User may speak stream-of-consciousness:
- Extract clear meaning
- Structure logically
- Preserve nuance (not over-condense)
- Group related points

### 7. First Session Setup
Ask user on first use:
- "Broad categories or detailed tags?"
- "Any existing topics to seed?"

## Common Traps

- Creating new note when should append -> always search first
- Losing tag consistency -> check registry before creating tags
- Over-condensing -> preserve user's intent and nuance
- Deleting "outdated" content -> archive instead of deleting
