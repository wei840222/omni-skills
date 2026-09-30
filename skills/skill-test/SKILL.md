---
name: skill-test
description: >
  Trial, compare, and evaluate agent skills in isolated sandboxes before install
  or publish. Use when the user wants to try a skill without loading it into the
  main session, A/B two candidates on the same task, or run multi-lens quality
  review before publishing. Prefer `skill-audit` for security/supply-chain
  scanning, `skill-finder` for discovery/install, `skill-publish` for registry
  publish, and `skill-builder` for authoring new skills from scratch.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧪"}'
  related-skills: '{"skill-audit":"Security and supply-chain scan before trusting a candidate.","skill-builder":"Author or restructure a skill after evaluation findings.","skill-finder":"Discover and install candidates to compare.","skill-manager":"Lifecycle tracking after a trial graduates to install.","skill-publish":"Registry publish path after evaluation passes.","skill-update":"Safe update/diff/rollback when re-testing an installed skill."}'
---

## When to load

Load this skill for **pre-install trials**, **A/B comparisons**, and **pre-publish multi-lens evaluations** of agent skills.

Do **not** load as the primary skill for security/supply-chain audits (`skill-audit`), catalog discovery (`skill-finder`), authoring a new package (`skill-builder`), or registry publish (`skill-publish`).

## State location

Optional trial notes (candidate slugs, side-by-side results, user preferences) may live under `<workspace>/skill-test/`, `<workspace>/memory/skill-test/`, or `~/skill-test/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/skill-test/`, `<workspace>/memory/skill-test/`, `~/skill-test/`.
3. If none exists and persistent state must be created, default to `<workspace>/skill-test/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path, report the conflict, and leave other copies unchanged.

Use only the selected `<state_root>` for every state operation in this skill. Never invent `<workspace>` from the shell cwd. Keep credentials, private eval corpora, and production secrets **out of the skill package and out of git**.

```text
<state_root>/
|-- trials.md          # Dated trial notes and keep/pass decisions
|-- comparisons.md     # A/B outcomes and user preference
`-- eval-log.md        # Pre-publish multi-lens summaries
```

One-off trials may stay conversational. Before creating or changing files under `<state_root>/`, explain the planned write and ask for confirmation.

## Routing

| Need | Load |
|------|------|
| Isolated single-skill trial setup | `references/sandbox.md` |
| Same-task A/B comparison | `references/compare.md` |
| Multi-lens pre-publish review | `references/evaluate.md` |
| Spec + source map for checks | `references/sources.md` |

## Core rules

1. **Isolate every trial.** Run candidates in a sub-agent or disposable directory so the main session skill set stays unchanged until the user explicitly approves install.
2. **Use the same task for comparisons.** A/B only when both skills receive identical inputs and success criteria.
3. **Separate usefulness from safety.** A clear, helpful skill can still fail a safety lens; surface both verdicts.
4. **Prefer primary specs and validators** listed in `references/sources.md` over memorized format rules.
5. **Graduate only with consent.** Install, publish, or write under `<state_root>/` only after an explicit user decision.

## Modes

### Trial (before install)

1. Confirm the candidate path or package the user named.
2. Load `references/sandbox.md` and spawn an isolated runner with **only** that skill.
3. Execute 2–3 representative tasks the user would actually ask.
4. Report activation, instruction clarity, output quality, rough token cost, and a keep / pass / try-another recommendation.

### Compare (A/B)

1. Load `references/compare.md`.
2. Define one shared task and success criteria with the user.
3. Run each candidate in a separate isolated runner.
4. Present side-by-side outputs and ask which feels better and why.
5. Optionally record the preference under `<state_root>/comparisons.md` after consent.

### Evaluate (before publish)

1. Load `references/evaluate.md`.
2. Spawn structure, safety, usefulness, and (when domain-specific) domain reviewers.
3. Synthesize a table of verdicts and a single recommend / revise / reject decision.
4. Route security blockers to `skill-audit` and authoring fixes to `skill-builder`.

## Completion check

Before finishing: isolation held for the main session; comparison used one shared task when A/B; safety and usefulness were not collapsed into one score; mutable format claims were checked against `references/sources.md` or marked unverified; no secrets were written into the skill tree.
