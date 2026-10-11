---
name: multi-engine-web-search
description: >
  Search across global, regional, privacy-focused, and specialist engines to
  cross-check current facts, investigate conflicting claims, or find site-specific,
  time-filtered, academic, and developer sources. Use when one search index is
  insufficient or a decision needs independent evidence.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔎"}'
  related-skills: '{"analysis":"Turn search findings into clear conclusions.","compare":"Compare options and trade-offs side by side.","web":"Inspect a selected page after discovery.","in-depth-research":"Expand discovery into a structured investigation.","elasticsearch":"Design or operate a custom search backend."}'
---

## State location

multi-engine-web-search preference state may exist in
`<workspace>/multi-engine-web-search/`,
`<workspace>/memory/multi-engine-web-search/`, or
`~/multi-engine-web-search/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/multi-engine-web-search/`,
   `<workspace>/memory/multi-engine-web-search/`,
   `~/multi-engine-web-search/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and state must be created, default to `<workspace>/multi-engine-web-search/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/multi-engine-web-search/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Do not treat the literal string `<state_root>` as a filesystem path. Store only non-sensitive preference fields (activation mode, engine order, blocked engines, search style). Never write credentials, personal identifiers, private query history, or secrets into state files or package files.

Default preference file (create on first authorized write):

| File | Purpose |
| --- | --- |
| `<state_root>/memory.md` | Activation mode, engine priority, blocked engines, search style |

## Setup

For a repeatable search profile, read `references/setup.md` on first use. Store only the selected activation mode, engine order, blocked engines, and output style in `<state_root>/memory.md`. Read `references/memory-template.md` when creating or updating that file.

## Workflow

Read `references/domain.md` for search engines, query patterns, and evidence quality rules. Read `references/sources.md` when validating operators, date filters, or evidence-quality claims.

1. Read saved preferences when they exist; otherwise use a balanced three-engine pass (one mainstream, one privacy/alternate, one domain specialist).
2. Form the primary query, URL-encode user text, and keep credentials / personal data out of query strings.
3. For material claims, run a contradiction query that seeks corrections, limitations, or disagreement.
4. Open the strongest primary or first-party sources, verify publication and event dates, and separate confirmed facts from unresolved differences.
5. Return a concise answer with the recommendation, direct evidence links, date context, and confidence.

If an engine blocks automation, returns a challenge page, or has no useful result, record the limitation and substitute another engine from the same category. If results conflict, prioritize original documentation, direct announcements, primary datasets, or peer-reviewed work; explain the remaining conflict rather than treating repeated rewrites as independent confirmation.

## Examples

```javascript
// Compare independent indexes for a current topic.
web_fetch({"url": "https://www.google.com/search?q=llm+agent+framework"})
web_fetch({"url": "https://duckduckgo.com/html/?q=llm+agent+framework"})
web_fetch({"url": "https://search.brave.com/search?q=llm+agent+framework"})

// Verify a technical claim from its primary documentation.
web_fetch({"url": "https://www.bing.com/search?q=site%3Agithub.com+fastapi+auth"})
```
