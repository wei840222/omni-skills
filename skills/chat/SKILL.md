---
name: chat
description: Learn and apply communication preferences for tone, format, and style. Use when a user explicitly corrects your style, states a preference, or asks you to adapt communication.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💬"}'
---

## State location

Chat state may exist in `<workspace>/chat/`, `<workspace>/memory/chat/`, or `~/chat/`. Before a state read or write, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured state path when one exists.
2. Otherwise, use the first existing directory in this order: `<workspace>/chat/`, `<workspace>/memory/chat/`, then `~/chat/`.
3. When multiple candidates exist, use only the highest-precedence directory and tell the user that separate copies were found.
4. When none exists and the user asks to save a preference, create `<workspace>/chat/`.
5. When the host cannot provide `<workspace>`, use an existing `~/chat/`; otherwise ask for a state path before creating data.

Use the selected `<state_root>` for every state operation in this skill.

## Data storage

```text
<state_root>/
├── memory.md       # Confirmed preferences (≤50 lines)
├── experiments.md  # Testing patterns (not yet confirmed)
└── rejected.md     # User said no; do not re-propose
```

Create `<state_root>` only when persistence is needed and permitted.

## Scope

This skill:
- Learns preferences from explicit user corrections or statements.
- Stores confirmed patterns in `<state_root>/memory.md`.
- Adapts communication style from stored preferences.
- Modifies only external preference memory, not `SKILL.md`.
- Treats silence and observation as non-signals.
- Excludes sensitive personal information from preference storage.

## Reference routing

| Topic | File | When to load |
|-------|------|--------------|
| Preference dimensions | `references/dimensions.md` | When you need to categorize a user's explicit style or tone preference. |
| Confirmation criteria | `references/criteria.md` | When deciding whether to retain an experiment, promote a preference, or resolve a conflict. |

## Core rules

### 1. Learn from explicit feedback

- Accept an explicit correction or preference statement as a signal.
- Treat silence or a lack of complaint as no signal.
- Record only the actionable communication preference, without unrelated personal details.

### 2. Three-strike confirmation

| Stage | Location | Action |
|-------|----------|--------|
| Testing | `<state_root>/experiments.md` | Record one or two consistent explicit signals. |
| Confirming | Ask the user | After three consistent signals, ask whether to promote it. |
| Confirmed | `<state_root>/memory.md` | Store the preference after user approval. |
| Rejected | `<state_root>/rejected.md` | Record a declined pattern so it is not re-proposed. |

### 3. Compact storage format

Store one actionable preference per line in `<state_root>/memory.md`:

```text
- Concise responses, no fluff
- Uses 🚀 for launches, ✅ for done
- Prefers bullets over paragraphs
- Technical jargon OK
- Omits “Great question!” openers
```

### 4. Conflict resolution

- Give the most recent explicit statement precedence.
- Ask the user when the conflict is ambiguous.
- Change a confirmed preference only when the user explicitly instructs you to do so.

### 5. Transparency

- When applying a stored preference, cite its source: "Using bullets (from `<state_root>/memory.md`)".
- On request, show the selected `<state_root>/memory.md`.
- A request to forget a preference removes it from all preference-state files.
