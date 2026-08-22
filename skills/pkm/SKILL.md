---
name: pkm
description: Capture, organize, retrieve, and connect personal knowledge in a Markdown-based knowledge base. Use when the user shares notes, links, ideas, quotes, questions, research, or asks to find and develop existing knowledge.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🧠"}'
---

# Personal Knowledge Base

Use this skill to turn incoming material into retrievable, connected notes without losing the original input. Keep the knowledge base portable: plain Markdown, stable filenames, and a workspace-specific state directory.

## State location

Store persistent notes outside the skill package:

1. Use the runtime-provided `<state_root>` when available.
2. Otherwise, ask the user for a knowledge-base directory before creating files; if they choose not to specify one, use a `workspace` or `state` directory relative to the current execution path.
3. Create the selected state directory before writing. Preserve existing notes and conventions rather than replacing them.

## Default workflow

1. **Capture first.** Save every incoming link, idea, quote, question, reminder, or long thought before organizing it. Use `inbox.md` when its destination is not yet clear.
2. **Classify the input.** A link keeps its source URL and capture date; a quote keeps attribution and source when available; a question is marked for future research; a long thought is separated into independent ideas.
3. **Create or update notes.** Give each durable idea a descriptive lowercase-hyphenated filename, an H1 title, concise tags, source information when applicable, and relevant links.
4. **Connect deliberately.** Add links only where a useful conceptual relationship exists. Keep a standalone note standalone when no clear connection is present.
5. **Retrieve before duplicating.** Search the knowledge base by full text, tag, and recent notes before creating an overlapping note. Offer retrieval when a user asks a question that may already be answered locally.
6. **Process the inbox.** During a separate processing pass, turn inbox material into atomic notes, add tags and links, then remove only the entries that were successfully incorporated.

## Note conventions

- Prefer descriptive names such as `how-to-negotiate-salary.md`; date prefixes are useful for journals such as `2024-01-15-weekly-review.md`.
- Keep one main concept per note, while retaining enough context to understand it later.
- Use broad, searchable tags first (roughly 5–10); consolidate synonyms that fragment retrieval.
- Use wiki-style links when the host supports them, otherwise use relative Markdown links.
- Keep a flat structure while the archive is small. Add a consistent tagging system around 20 notes, an index or Map of Content (MOC) around 50, and domain folders only after recurring navigation patterns emerge.

## Safe operation and recovery

- Preserve the original text in `inbox.md` when classification, fetching, or summarization is uncertain; mark the item for follow-up instead of discarding it.
- Treat a reminder as captured context, not as a scheduled task. Ask before creating reminders or changing external calendars.
- Keep private material in the user-selected local state directory. Ask before syncing, sharing, or publishing notes.
- Before reorganizing a mature archive, inspect existing naming, tags, and links; make additive changes and explain any proposed migration.

## References to load

- Read `references/pkm-methodology.md` when designing note workflows, explaining Zettelkasten principles, processing an inbox, or restructuring an archive.

## Common requests

- **“Save this idea.”** Capture it immediately, then create an atomic note when the idea is sufficiently clear.
- **“Organize these notes.”** Preserve each source item, split unrelated ideas, search for existing related notes, and show the resulting paths.
- **“What do I know about X?”** Search first, synthesize from matching notes, and identify any uncertainty or missing evidence.
- **“Set up a knowledge base.”** Establish the state directory and inbox first; introduce tags, MOCs, or folders only when the archive needs them.
