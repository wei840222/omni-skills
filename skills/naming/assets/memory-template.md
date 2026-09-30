# Memory Template — Naming

After `<state_root>` is resolved to a real directory and the user approves persistence, create these files on first durable use.

Example commands (replace the path with the resolved root):

```bash
RESOLVED_ROOT="/path/to/resolved/naming"
mkdir -p "$RESOLVED_ROOT/archive"
touch "$RESOLVED_ROOT/memory.md" "$RESOLVED_ROOT/briefs.md" "$RESOLVED_ROOT/winners.md" "$RESOLVED_ROOT/collisions.md"
```

## `memory.md`

```markdown
# Naming Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Context
- Durable notes about what the user names most often
- Audience vocabulary that repeatedly matters
- System-wide language constraints worth remembering

## Preferences
- Naming style they prefer: plain, branded, technical, or hybrid
- Words, tones, suffixes, or cliches to exclude
- Preferred output style: one winner first, shortlist first, or exploratory families

## Constraints
- Namespace limits, localization concerns, legal caution, UI length limits, or API consistency rules

## Repeating Patterns
- Families or structures that have worked repeatedly
- Failure modes that keep killing candidates

---
Updated: YYYY-MM-DD
```

## `briefs.md`

```markdown
# Naming Briefs

## YYYY-MM-DD — [asset]
- Role: what this thing is
- Audience: who must understand or use the name
- Limits: character, tone, namespace, or rollout constraints
- Lexicon: words to include, echo, or exclude
- Yardstick: what makes a winner in this context
```

## `winners.md`

```markdown
# Naming Winners

## YYYY-MM-DD — [asset]
- Winner: [name]
- Backups: [name], [name]
- Lane: product | feature | api | file | codename | taxonomy
- Why it won: [short rationale]
- Open checks: [domain, trademark, docs update, migration, none]
```

## `collisions.md`

```markdown
# Naming Collisions

## YYYY-MM-DD — [asset]
- Rejected: [name]
- Reason: ambiguity | pronunciation | namespace clash | legal risk | negative connotation | too generic
- Notes: [short explanation]
```

## Principles

- Save reusable naming taste and constraints, not every brainstorm
- Promote a preference only after repeated evidence
- If the user declines persistence, work normally without local writes
- Keep memory compact enough to scan fast on activation
- Write only under the resolved path; never persist the placeholder string `<state_root>`
