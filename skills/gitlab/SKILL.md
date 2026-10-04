---
name: gitlab
description: >
  Diagnose, troubleshoot, and write GitLab CI/CD pipelines. Use when fixing
  GitLab pipeline errors, rules evaluation, YAML inheritance traps, Docker-in-Docker
  failures, artifacts/cache surprises, protected/masked variables, or MR vs branch
  pipeline triggers. Not for generic CI product selection (`ci-cd`), GitHub Actions
  semantics (`github-actions`), plain Docker host ops (`docker`), or YAML parser
  issues alone (`yaml`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🦊"}'
  related-skills: '{"ci-cd":"Cross-platform CI product choice and generic pipeline pitfalls.","github-actions":"GitHub Actions workflow semantics instead of GitLab CI.","docker":"Host Docker/daemon issues outside GitLab runner DinD.","yaml":"Parser-level YAML quoting and indentation without CI keywords.","git":"Git branching and merge mechanics outside pipeline YAML."}'
---

## State location

This skill is stateless and does not store local configuration or persistent user state. Keep pipeline drafts, incident notes, and project-specific runner inventories in ordinary user files outside the skill package.

## When to Use

- Job never runs, always runs, or runs on the wrong branch/tag/MR
- `extends` / `include` / `!reference` produced unexpected scripts or variables
- Job pending forever, empty secrets, or DinD cannot reach the daemon
- Artifacts missing across jobs, or cache treated as a hard dependency
- Choosing between branch pipelines, MR pipelines, and `CI_PIPELINE_SOURCE` values

Redirect product-level “which CI vendor” questions to `ci-cd`. Redirect GitHub Actions YAML to `github-actions`.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Rules and triggers | `references/rules.md` | Job selection, tags, MR vs branch, fallthrough |
| Inheritance and reuse | `references/inheritance.md` | `extends`, `!reference`, `include`, anchors |
| Execution environment | `references/environment.md` | DinD, runner tags, artifacts vs cache |
| Silent failures | `references/silent-failures.md` | Pending jobs, empty protected vars, mask leaks |
| Domain knowledge and sources | `references/domain-knowledge.md` | Before asserting GitLab CI semantics or citing docs |

## Operating Rules

1. Prefer `rules:` over legacy `only:`/`except:`; never mix them on the same job.
2. Treat the first matching `rules` entry as decisive; end catch-alls with `when: never` when fallthrough must not create the job.
3. Assume `extends` reverse-deep-merges keys but **replaces** keyword values (including arrays) — use `!reference` to compose scripts.
4. Treat cache as best-effort optimization; require artifacts (or explicit `needs`) for required outputs.
5. For DinD, verify privileged runner capability, `DOCKER_HOST`, and TLS (`DOCKER_TLS_CERTDIR`) together — partial setup fails cryptically.
6. Name the failure layer before editing YAML: rules selection, variable scope, runner/executor, inheritance merge, or artifact graph.

## Safety

- Never commit real CI/CD variable values, tokens, or `.gitlab-ci.yml` secrets; use placeholders such as `$PROJECT_TOKEN` or `glpat-***`.
- Do not advise disabling masking or protection solely to “make the job work”; fix branch protection and variable scope instead.
- Prefer non-privileged Docker build alternatives when the runner cannot enable privileged mode.
