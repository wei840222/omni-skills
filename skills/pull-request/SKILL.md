---
name: pull-request
description: Create and review pull requests with repository-specific validation, focused scope, and maintainer-ready descriptions. Use when preparing, submitting, or reviewing a pull request for any repository.
metadata:
  openclaw: '{"emoji":"🔀"}'
  related-skills: '{"git":"Manage source code versioning locally before creating a pull request.","github-actions":"Inspect and understand CI workflows that a pull request must satisfy."}'
---

## When to Use

Use this skill before creating, submitting, or reviewing a pull request. It provides a quality gate that protects maintainer time and makes the contributor accountable for the change.

## Workflow

1. Read `CONTRIBUTING.md`, the pull-request template, and repository context before changing code. Load `references/repo-context.md` when entering an unfamiliar repository.
2. Check the project issue policy, active duplicate work, target branch, contribution activity, and AI-contribution policy. Load `references/checklist.md` before committing or opening the pull request.
3. Keep the proposed change focused, validate it with the repository's documented checks, and report any check that could not run.
4. Write a specific title and description using `references/templates.md`; disclose AI assistance when it materially contributed.
5. During review, load `references/red-flags.md` to check for scope creep, unsafe changes, fabricated APIs, and abandonment risks. Address review feedback within 48 hours, or leave a clear handoff/closure message.

## Quick Reference

| Domain | File | When to load |
|--------|------|--------------|
| Repository context | `references/repo-context.md` | Before working in an unfamiliar repository. |
| Pre-submission checklist | `references/checklist.md` | Before committing or opening a pull request. |
| Red flags | `references/red-flags.md` | While reviewing or checking a proposed pull request. |
| Description templates | `references/templates.md` | When drafting the pull-request description. |
| Pull-request practices | `references/best-practices.md` | When policy or workflow needs supporting guidance. |

## Scope Decision

Check `CONTRIBUTING.md` first, then apply the repository's policy:

| Change type | Default action |
|-------------|----------------|
| Typo or small bug fix | Open a pull request directly when repository policy allows it. |
| New feature | Open a discussion or issue and obtain approval first. |
| Architecture change | Start an RFC or discussion. |
| Uncertain fit | Ask in an issue before writing the change. |

Escalate for a human decision before opening a pull request that changes more than five files or 200 lines, modifies public APIs, involves security/authentication/cryptography, changes governance, or conflicts with maintainer direction.

## Safety and Quality Rules

- Read repository contribution guidance and match its branch, commit, formatting, and test conventions.
- Use `<PLACEHOLDER>` for secrets and exclude credentials, private keys, and environment files from the pull request.
- Use a single logical change per pull request and remove unrelated formatting or drive-by refactoring.
- Run documented tests, lint, and build checks where available; state the exact checks that did not run.
- Confirm the target branch and check existing pull requests before submitting.
- If two consecutive pull requests are rejected, pause and escalate to the accountable human.
- Keep at most one open pull request per repository unless maintainers explicitly allow otherwise, and check repository velocity before contributing.
