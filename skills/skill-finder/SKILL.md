---
name: skill-finder
description: >
  Find, compare, and install agent skills across Clawic and Skills.sh when the
  user needs a new capability, a better workflow, a safer alternative, or an
  installable replacement for a weak manual approach. Use when they ask how to
  do something, what to install, whether a skill exists, or which option fits
  best. Prefer `skill-manager` for lifecycle of already-known installs,
  `skill-update` for preview/backup/rollback of one upgrade, `skill-builder`
  for authoring from scratch, and `skill-audit` before trusting a new package.
metadata:
  version: "1.2.0"
  openclaw: '{"emoji":"🔍","requires":{"bins":["npx"]}}'
  related-skills: '{"skill-audit": "Security and supply-chain scan before install or after updates.", "skill-builder": "Author a new skill when catalog search finds nothing strong enough.", "skill-manager": "Lifecycle for installed skills: inventory, contextual suggest, update/remove with consent.", "skill-test": "Isolated trial before a candidate graduates to tracked install.", "skill-update": "Safe single-skill upgrade with diff preview, backup, and rollback."}'
---

## State location

Optional skill-finder continuity may live under `<workspace>/skill-finder/`,
`<workspace>/memory/skill-finder/`, or `~/skill-finder/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/skill-finder/`, `<workspace>/memory/skill-finder/`,
   `~/skill-finder/`.
3. If none exists and durable state must be created, default to
   `<workspace>/skill-finder/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell
   cwd. An existing `~/skill-finder/` may be read; otherwise ask before
   creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.
Never write the literal string `<state_root>` to disk.

**Legacy paths.** Historical notes may exist under
`~/Clawic/data/skill-finder/` or `~/clawic/skill-finder/`. They are **not** in
the active lookup order and must **not** be moved, merged, or deleted during
ordinary sessions. Migration is a separate user decision (see
`references/migration.md`).

**Data.** Durable notes live in `<state_root>/memory.md` when the user wants
continuity (see `references/memory-template.md` and `references/setup.md`).
Optional recent-query continuity may use `<state_root>/searches.md`. This
skill can answer one-off discovery questions without state.

```text
<state_root>/
├── memory.md     # Source mode + preferences + liked/passed skills
└── searches.md   # Recent search history (optional)
```

## When to Use

User asks how to do something, wonders whether a skill exists, wants a new
capability, or asks for the best skill for a job. Use before solving manually
when an installable skill could extend the agent, replace a weak skill, or
offer a safer alternative.

Do **not** use as the primary skill for lifecycle of already-installed skills
(`skill-manager`), safe single-skill upgrade (`skill-update`), authoring
(`skill-builder`), security scanning (`skill-audit`), or isolated trial
(`skill-test`).

## Progressive disclosure

Keep this file as the always-on contract. Load **at most one** reference for
the current ask; do not preload every deep dive.

| Need | Load |
|------|------|
| First-time setup / no `<state_root>` yet | `references/setup.md` |
| Memory file shape | `references/memory-template.md` |
| Dual-source search tactics | `references/search.md` |
| Candidate quality rubric | `references/evaluate.md` |
| Category / domain brainstorming | `references/categories.md` |
| Edge cases and scanner warnings | `references/troubleshooting.md` |
| Legacy Clawic path migration | `references/migration.md` |
| Gate 6 source ledger | `references/sources.md` |

## Activation Signals

Activate when the user says things like:

- "How do I do X?"
- "Is there a skill for this?"
- "Can you do this better?"
- "Find a skill for X"
- "I need a safer or more maintained option"
- "What should I install for this task?"

Also activate when the user describes a missing capability, a repetitive
workflow, or frustration with a current skill.

## Search Sources

This skill can search two ecosystems:

| Source | Search | Install | Best for |
|--------|--------|---------|----------|
| `Clawic` | `npx clawic search "query"` | `npx clawic add <slug>` | Curated catalog search with built-in inspection |
| `Skills.sh` | `npx skills find [query]` | `npx skills add <owner/repo@skill>` | Broad open ecosystem from the `skills` CLI |

Default mode: search **both** sources, then compare results together.

Configurable modes:

- `both` — recommended default
- `clawic` — only search Clawic
- `skills.sh` — only search the Skills.sh ecosystem

Store the current mode in `<state_root>/memory.md`. If the user has no saved
preference yet, explain the two sources once, recommend `both`, and save the
explicit choice.

Verified CLI surfaces (re-check before quoting mutable flags):

- `clawic` npm package — registry https://registry.npmjs.org/clawic ;
  upstream https://github.com/clawic/skills
- `skills` npm package (Skills.sh ecosystem) — homepage
  https://skills.sh/ ; registry https://registry.npmjs.org/skills ;
  upstream https://github.com/vercel-labs/skills

## Security Note

This skill uses `npx clawic` and `npx skills` to discover and install skills
from two different ecosystems. Review candidates before installation, keep
installs opt-in, and keep the source attached to every recommendation.

## Core Rules

### 1. Search Both Sources by Default

Unless the user has explicitly chosen otherwise, search `Clawic` and
`Skills.sh` for the same need, then compare the strongest results together.

Verify the package manager explicitly; a `Skills.sh` result requires
`npx skills add`, while a Clawic result requires `npx clawic add`. Keep the
source and install command attached to every recommendation.

### 2. Trigger on Capability Gaps, Not Just Explicit Search Requests

Do not wait only for "find a skill." Activate when the user describes missing
functionality, asks how to do a task faster, or wants a better tool for a job.

### 3. Search by Need, Not Name

User says "help with PDFs" — think about what they actually need:

- Edit? → `npx clawic search "pdf edit"` and `npx skills find pdf edit`
- Create? → `npx clawic search "pdf generate"` and `npx skills find pdf generate`
- Extract? → `npx clawic search "pdf parse"` and `npx skills find pdf parse`

### 4. Evaluate Before Recommending

Inspect strong candidates before recommending and check
`references/evaluate.md` criteria:

- Description clarity
- Download / install count (popularity ≈ maintenance signal)
- Last update (recent ≈ active)
- Author or repository reputation
- Install scope and friction

For `Skills.sh` candidates, pay attention to the package source and install
string the CLI returns (often `owner/repo@skill` with a skills.sh page).

### 5. Present a Decision, Not a Dump

Present a curated recommendation by explaining why each fits, who it is best
for, and why the winner wins:

> "Best fit: `pdf-generator` from Clawic — Markdown/HTML → PDF reports and
> invoices. Matches contract-generation better than adjacent extract-only
> options."

When there are multiple good fits, rank the top 1–3 and call out tradeoffs.

### 6. Learn Preferences and Source Mode

When the user explicitly states what they value, confirm and update
`<state_root>/memory.md`:

- "Search both by default" → set source mode to `both`
- "Only use Skills.sh for this workspace" → set source mode to `skills.sh`
- "Only check Clawic" → set source mode to `clawic`
- "I prefer minimal skills" → add to Preferences
- "This one is great" → add to Liked with reason
- "Too verbose" → add to Passed with reason

Do not infer hidden preferences from behavior-only signals.

### 7. Check Memory First

Before recommending, read `<state_root>/memory.md` when it exists:

- Respect saved source mode unless the user overrides it
- Skip skills similar to Passed ones
- Favor qualities from Liked ones
- Apply stated Preferences

### 8. Respect Installation and Security Boundaries

If a candidate skill is marked risky by scanner output, or the install path is
unclear:

- Explain the warning or ambiguity first
- Prefer a safer alternative
- Do not run force-install flags for the user
- Do not auto-accept install prompts with `-y`
- Do not choose global install scope unless the user explicitly wants it
- Install only with explicit user consent
- Prefer `skill-audit` before trusting a new or unfamiliar package

### 9. Fallback Gracefully

If nothing is strong enough:

- Say what was searched
- Say which source mode was used
- Explain why the matches are weak
- Help directly or hand off to `skill-builder` for a purpose-built skill

## Search Commands

```bash
# Clawic search and inspect
npx clawic search "query"
npx clawic show <slug>
npx clawic add <slug>
npx clawic list
```

Every Clawic result maps to a repository entry in `https://github.com/clawic/skills`
or package details via `npx clawic show <slug>` — use it to double-check a candidate or
share it with the user before installing.

```bash
# Skills.sh ecosystem
npx skills find [query]
npx skills add <owner/repo@skill>
npx skills list
npx skills update

# Example install string returned by `npx skills find`
npx skills add vercel-labs/agent-skills@vercel-react-best-practices
```

Note: `npx skills find` may open an interactive TUI when run in a TTY; in
automation or non-interactive shells it still prints ranked matches with
skills.sh URLs. Do not invent install strings that the CLI did not return.

## Workflow

1. **Detect** — Is the user describing a capability gap or installable need?
2. **Load memory** — Read `<state_root>/memory.md` for source mode and preferences
3. **Understand** — What does the user actually need?
4. **Search** — Use `both` by default, or the saved single-source mode
5. **Evaluate** — Check quality signals (see `references/evaluate.md`)
6. **Compare** — Rank results across both sources by fit + quality
7. **Recommend** — Top 1–3 with clear reasoning and a winner
8. **Install or fallback** — Install only with consent, otherwise help directly
9. **Learn** — Store explicit feedback in memory

## Recommendation Format

When presenting results, prefer this structure:

```text
Best fit: <slug or owner/repo@skill>
Source: <Clawic or Skills.sh>
Why it wins: <1-2 lines>
Install: <exact command>
Tradeoffs: <what it does not cover or where alternative is stronger>
Alternatives: <slug>, <slug>
Next step: Install now or continue without installing
```

## Common Traps

- Waiting for the exact phrase "find a skill" → misses proactive discovery moments
- Searching generic terms → gets noise. Be specific: "react testing" not "testing"
- Searching only one ecosystem when the saved mode is `both`
- Recommending by name match only → misses better alternatives with different names
- Mixing install commands between `Clawic` and `Skills.sh`
- Ignoring download / install counts → low counts often means abandoned
- Not checking last update → outdated skills cause problems
- Treating empty Clawic results as proof the other ecosystem is empty

## Security & Privacy

**Data that leaves your machine:**

- Search queries sent to the Clawic catalog (public search)
- Search queries sent through the `skills` CLI / Skills.sh ecosystem

**Data that stays local:**

- All preferences in `<state_root>/memory.md`
- Search history (if enabled)

**This skill does NOT:**

- Install skills without user consent
- Use force-install flags to skip scanner warnings
- Auto-confirm `npx skills add` with `-y`
- Switch to global install scope silently
- Collect hidden behavior data
- Access files outside `<state_root>/`
