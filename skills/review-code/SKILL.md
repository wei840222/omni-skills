---
name: review-code
description: Review code and pull requests with risk-first analysis, evidence-backed
  findings, severity-confidence triage, and patch-ready fixes for correctness, security,
  performance, and maintainability. Use when the user asks for a code review, PR review,
  merge-readiness check, or bug-risk audit. Route implementation work to `code`, branch
  or commit hygiene to `git`, and release gates to `ci-cd` or `devops`.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🔎"}'
  related-skills: '{"ci-cd":"Release-gate and deployment safeguard checks after review fixes land.","code":"Implementation workflow that turns review findings into concrete code changes.","devops":"Production risk, monitoring, and rollback planning around reviewed changes.","git":"Safer branch, diff, and commit handling while remediating review findings.","typescript":"Stricter typing and runtime-safety review when the diff is TypeScript-heavy."}'
---

## When to load

Load this skill when the user asks for a code review, PR review, merge-readiness check, or bug-risk audit before shipping.

Do not load as the primary skill for greenfield implementation (`code`), routine git mechanics without a review ask (`git`), or CI pipeline authoring without a review target (`ci-cd` / `devops`).

## State location

Review preferences and optional finding logs may live under `<workspace>/review-code/`, `<workspace>/memory/review-code/`, or `~/review-code/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use a host- or user-configured review-code state path when one is explicitly supplied.
2. Otherwise use the first existing directory in this order: `<workspace>/review-code/`, `<workspace>/memory/review-code/`, then `~/review-code/`.
3. If none exists and the user asks to persist review data, create `<workspace>/review-code/` after confirmation.

Use only the selected `<state_root>` for this invocation. Do not hardcode absolute paths or write the literal string `<state_root>` to disk. If more than one candidate exists, use the highest-precedence directory, report the conflict, and keep the directories separate rather than merging.

```text
<state_root>/
├── memory.md      # Review preferences, stack context, accepted risk baselines
├── findings/      # Optional per-review finding logs
├── baselines/     # Team conventions and accepted risk baselines
└── sessions/      # Session summaries for ongoing audits
```

One-off reviews may stay conversational. Before creating or changing files under `<state_root>/`, explain the planned write and ask for confirmation.

## Core behavior

This is an instruction-only code review skill. Deliver a risk-ranked review with explicit evidence, impact, confidence, and concrete fix direction.

1. **Define the review contract first.** Confirm target scope: branch, files, risk tolerance, and release context. If scope is unclear, state assumptions and keep findings tied to them.
2. **Start with risk mapping.** Locate high-risk zones first (auth, money, data integrity, concurrency, migrations), then deep-dive with `references/review-workflow.md`.
3. **Evidence-backed findings only.** Each finding needs trigger location, failure mode, user/business impact, and a reproduction clue. Weak evidence → low confidence or a targeted question.
4. **Separate blocking vs advisory.** Use `references/severity-and-confidence.md`. Blockers must be reproducible or highly probable with strong impact.
5. **Pair every blocker with a fix path.** Use `references/patch-strategy.md` for minimal, rollback-safe edits and verification steps.
6. **Tie quality to test impact.** Map changes with `references/test-impact-playbook.md`. Missing critical tests become explicit gaps with exact scenarios.
7. **Optimize for signal.** Prefer high-impact defects over style noise. If no blockers exist, say so and list residual risks, test gaps, and monitoring advice.

Load supporting files only when needed:

| Need | Load |
|------|------|
| First activation / empty state | `references/setup.md` |
| End-to-end review execution flow | `references/review-workflow.md` |
| Severity and confidence calibration | `references/severity-and-confidence.md` |
| Language and architecture risk checks | `references/language-risk-checklists.md` |
| Test impact by change type | `references/test-impact-playbook.md` |
| Comment and report templates | `assets/comment-templates.md` |
| Patch strategy for actionable fixes | `references/patch-strategy.md` |
| Durable memory file shapes | `assets/memory-template.md` |
| Gate 6 research sources | `references/sources.md` |

## Common traps

- Reporting opinions as facts — credibility drops and teams ignore real blockers.
- Mixing blocker and nit feedback without labels — delayed merges and mis-prioritized fixes.
- Calling something safe without tests — silent regressions in production.
- Suggesting large rewrites for local defects — good fixes are postponed indefinitely.
- Ignoring release context (hotfix vs refactor) — wrong trade-offs for urgency.
- Missing migration and backward-compatibility checks — runtime failures after deploy.

## Safety and trust

- Instruction-only by default: no credentials required and no third-party network calls unless the user explicitly exports artifacts.
- Do not auto-approve code or merge pull requests from this skill alone.
- Do not store credentials, tokens, or sensitive payloads in `<state_root>/`.
- Do not modify this skill package during a normal review run.

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| None by default | None | Instruction-only review |
