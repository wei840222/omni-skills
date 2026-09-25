---
name: gifts
description: Track gift ideas, occasions, and giving history for people the user cares about. Use when the user mentions a present, a birthday, a wishlist item, or asks what to give someone.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🎁"}'
---

## State location

Gift notes may exist in `<workspace>/gifts/`, `<workspace>/memory/gifts/`, or `~/gifts/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/gifts/`, `<workspace>/memory/gifts/`, `~/gifts/`.
3. If none exists and state must be created, default to `<workspace>/gifts/`.
4. If more than one candidate exists, use the highest-precedence one and tell the user that other copies were left untouched.
5. If `<workspace>` cannot be resolved and `~/gifts/` does not exist, ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Do not write the literal string `<state_root>` to disk.

## Core Behavior

- User mentions a gift idea → save it to that person's file
- User asks what to gift → check saved ideas first
- User gives or receives a gift → log it for future reference

## File Structure

```
<state_root>/
├── people/
│   ├── mom.md
│   └── sarah.md
├── occasions/
│   └── birthdays.md
├── given/
│   └── 2024.md
├── ideas/
│   └── generic.md
└── my-wishlist.md
```

## State Templates

Load `references/state-templates.md` before creating or updating any file under `<state_root>/`.

## Capturing Ideas

When the user mentions that someone wants something:

- Save it immediately, with the context of the mention
- Note the source, such as "mentioned while cooking" or "saw her eyeing it"
- Treat casual mentions as the best later gift leads

## What To Surface

- "Sarah's birthday is in 2 weeks"
- "You saved an idea for her last month"
- "Last year you gave her X, and it went well"

## Progressive Enhancement

- Start by adding the closest people and their birthdays
- Keep capturing ideas when they are mentioned
- After a gift is given, log the reaction

## Critical Requirements

- Check the person's file before suggesting a generic gift
- Log gifts that were given so later suggestions do not repeat them
- Capture "I want that" moments when the user expresses them
