# Memory Template — State Storage Reference

This file defines the ONLY file the skill opens to write state. All other files are read-only inputs. State lives under `<state_root>/`.

---

## File Layout

```
<state_root>/
├── memory.md         ← the single writable file
├── boxes/
│   ├── <box_id>.md   ← individual box content
│   └── ...
└── logs/
    └── <date>.md     ← optional daily log
```

## memory.md Structure

```markdown
# State

## Boxes index

| box_id | recipient | topic | created | last_touched |
|--------|-----------|-------|---------|--------------|
| b001   | @alice    | 周报  | 2025-01-15 | 2025-01-17 |
| b002   | @group:dev | 技术方案 | 2025-01-16 | 2025-01-16 |

## Due table

| box_id | due_date | priority | note |
|--------|----------|----------|------|
| b001   | 2025-01-20 | high   | 周五前交 |
| b002   | 2025-01-23 | normal | 等评审 |

## Recipients

| key | display_name | relationship | notes |
|-----|-------------|--------------|-------|
| @alice | 李婷 | 同事-同组 | 喜欢简洁风格 |
| @group:dev | 开发群 | 工作群 | 12人 |
```

---

## Boxes Index Format

- `box_id`: `b` + 3-digit zero-padded counter, auto-incremented.
- `recipient`: identity key (see below).
- `topic`: ≤15 characters, human-readable label.
- `created` / `last_touched`: ISO date `YYYY-MM-DD`.
- Sorted by `last_touched` descending (most recent first).

## Due Table Format

- Only boxes with a deadline appear here. Remove row when due date passes or task completes.
- `priority`: `high` | `normal` | `low`.
- `note`: optional, ≤20 characters.
- Sorted by `due_date` ascending.

## Recipients Format

- One row per unique recipient or group.
- `key`: identity key — see below.
- `display_name`: how they appear in output (Chinese name or group label).
- `relationship`: e.g. 同事-同组, 客户, 上级, 朋友, 家人.
- `notes`: style preferences, sensitivities, inside jokes — anything that affects tone.

---

## Identity Keys

| Pattern | Meaning | Example |
|---------|---------|---------|
| `@<name>` | Individual person | `@alice`, `@王总` |
| `@group:<label>` | Group chat | `@group:dev`, `@group:家人` |
| `@self` | The user themselves | — |

Keys are case-insensitive for Latin names. Chinese names use the characters as given.

---

## File Creation Thresholds

| Condition | Action |
|-----------|--------|
| New recipient encountered | Add row to Recipients table |
| New topic/task for existing recipient | Create `<state_root>/boxes/<box_id>.md`, add index row |
| Deadline assigned | Add row to Due table |
| Box completed | Remove from Due table; keep in index with `last_touched` updated |
| Box older than 90 days, no activity | Archive: move file to `<state_root>/boxes/archive/`, remove from index |

---

## The Single-Write Rule

> **`<state_root>/memory.md` is the ONLY file opened for writing.**
>
> - Box content files (`boxes/*.md`) are created but never rewritten — append-only if needed.
> - Log files are append-only.
> - All other reference files (this skill's own references/) are strictly read-only.
> - If state needs correction, edit `memory.md` only.

This prevents drift between the index and actual box files.

---

## Box File Template

```markdown
# <topic>

- Recipient: <display_name>
- Created: <date>
- Status: active | done | archived

## Content

<written drafts, notes, versions>
```
