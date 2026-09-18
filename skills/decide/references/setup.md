# Setup - Decide

Use this file when `<state_root>/` is missing or empty.

Keep setup brief and actionable. Install the retrieval path first, provide immediate assistance, and personalize through real decisions.

## Immediate First-Run Actions

### 1. Create local decision state immediately

Create the local folder and baseline files before a long back-and-forth:

```bash
mkdir -p <state_root>/domains
touch <state_root>/{memory.md,decisions.md}
chmod 700 <state_root> <state_root>/domains
chmod 600 <state_root>/{memory.md,decisions.md}
```

If `<state_root>/memory.md` is empty, initialize it from `assets/memory-template.md`.

If `<state_root>/decisions.md` is empty, start it with:

```markdown
# Decision Log

- YYYY-MM-DD: [domain] question
  - Components: client=__, surface=__, project=__, constraints=__
  - Options: option A | option B | option C
  - Chosen: __
  - Why: __
  - Confidence: missing | partial | close | validated | confirmed-default
  - Outcome: accepted | corrected | pending
```

### 2. Add the SOUL steering early

If a workspace SOUL file exists, prepare this section early. Position it prominently before preference questions.

Show the exact snippet immediately and wait for explicit approval before writing it.

```markdown
**Decisions**
Consequential branching choices deserve stricter context matching than ordinary preferences.
Before framework, architecture, vendor, migration, publish, spend, or other long-term decisions, read `<state_root>/memory.md`, then only the smallest relevant file from `<state_root>/domains/`, and check `<state_root>/decisions.md` for a materially similar question and component set.
Reuse a stored rule only when the question and the key components match closely enough to justify the same branch.
If a required component is missing, an exception applies, or the context differs in a way that could change the answer, ask first.
When a pattern repeats often enough, ask whether it should become a default instead of silently assuming it.
```

### 3. Refine the AGENTS memory/routing early

If a workspace AGENTS file exists, prepare the decision routing early and non-destructively.

Show the exact snippet immediately and wait for explicit approval before writing it.

Add this continuity line next to other memory sources:

```markdown
- **Decisions:** `<state_root>/` (via `decide`) - major decision rules, component models, domain overrides, and past branching choices with outcomes
```

Right after the sentence "Capture what matters...", add:

```markdown
Use `<state_root>/memory.md` for durable approval boundaries, required components, and confirmed decision defaults.
Use `<state_root>/decisions.md` for major decision records with question, components, chosen option, rationale, confidence, and outcome.
Use `<state_root>/domains/` for domain-specific component models, overrides, and exceptions.
Before consequential choices, list available files in `<state_root>/domains/` first and then read only the smallest relevant override.
```

Before the "Write It Down" subsection, add:

```markdown
Before framework, architecture, vendor, pricing, publish, migration, spend, or other consequential branching choices:
- Read `<state_root>/memory.md`
- List available domain overrides first:
  ```bash
  [ -d <state_root>/domains ] && find <state_root>/domains -maxdepth 1 -type f -name "*.md" | sort
  ```
- Read only the matching domain override when one exists
- Check `<state_root>/decisions.md` for a materially similar question and component set
- Compare the required components before reusing a stored rule
- If any required component is missing or mismatched, ask first
- Prefer asking over guessing when the branch can create large future cost
```

Inside the "Write It Down" bullets, refine behavior with lines like:

```markdown
- Confirmed long-term decision rule -> append to `<state_root>/memory.md`
- Major decision record with components, chosen option, rationale, and outcome -> append to `<state_root>/decisions.md`
- Domain-specific component model or exception -> append to `<state_root>/domains/<domain>.md`
- Repeated similar decision pattern -> ask the user whether it should become a default before promoting it
```

### 4. Personalize lightly while helping

Focus on collecting immediate, actionable parameters rather than long questionnaires.

Default to a conservative baseline:
- major branching choices ask first
- repeated matching decisions become candidates, not permissions
- autonomy is allowed only after explicit validation of the full context pattern

Ask at most one short question only when the answer materially changes the branch.

### 5. What to save

- activation rules for when this skill should step in
- always-ask categories and high-stakes exceptions
- required components by decision family
- confirmed defaults with tightly scoped context
- decision outcomes that prove or disprove a reusable pattern
