---
name: netlify-deploy
description: Deploy, host, publish, or relink a web project on Netlify. Use for first deploys, preview deploys, production releases, monorepo deployment paths, or netlify.toml configuration.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"NET","requires":{"bins":["npx","git"]}}'
  related-skills: '{"ci-cd":"Provides delivery-pipeline design and release automation practices.","deploy":"Provides provider-neutral deployment planning across environments.","devops":"Provides infrastructure and operational guardrails for deployment work.","git":"Provides branch hygiene and release-safe commit workflow."}'
---

## State location

Netlify deployment preferences may exist in `<workspace>/netlify-deploy/`, `<workspace>/memory/netlify-deploy/`, or `~/netlify-deploy/`.
Before reading or writing preferences, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/netlify-deploy/`, `<workspace>/memory/netlify-deploy/`, `~/netlify-deploy/`.
3. If none exists and preferences must be saved, default to `<workspace>/netlify-deploy/`.

Use the selected `<state_root>` for every preference operation in this skill. When multiple candidate directories exist, use only the highest-precedence one and report the conflict; do not merge them automatically.

## Setup

On first use, read `references/setup.md` for integration and environment checks.

## When to Use

Use this skill when the user asks to deploy, host, publish, or relink a terminal-based Netlify project, including a first deploy, preview, production release, monorepo configuration, or `netlify.toml` correction.

## Architecture

Deployment preferences live in `<state_root>/memory.md`; use them only for operational defaults that help future deployment requests start safely. Read `references/memory-template.md` when creating or updating these preferences.

## Quick Reference

Load only the resource that matches the active task.

| Topic | File | When to load |
|---|---|---|
| Setup and integration flow | `references/setup.md` | First use, or when project and authentication context are unknown. |
| Preference template | `references/memory-template.md` | Creating or updating saved deployment preferences. |
| CLI command map | `references/cli-commands.md` | Checking Netlify CLI syntax. |
| Deployment scenarios | `references/deployment-patterns.md` | Diagnosing a deploy failure, linking a site, or deploying a monorepo. |
| Configuration examples | `references/netlify-toml.md` | Editing `netlify.toml` for builds, redirects, or environment-specific settings. |

## Core workflow

1. Verify authentication and the current site link with `npx netlify status` before deploying.
2. When the project is unlinked, obtain its Git remote with `git remote get-url origin`, attempt `npx netlify link --git-remote-url <remote-url>`, and use `npx netlify init` only when no matching site is available.
3. Build with the project's declared build command and verify the resulting publish directory. Use framework defaults only as an initial hypothesis.
4. Use `npx netlify deploy` for a requested preview. Use `npx netlify deploy --prod` only after the user explicitly requests a production release or confirms readiness after validation.
5. For a monorepo, establish the target app directory or `build.base` in `netlify.toml` before linking or deploying.
6. Report the deploy URL, environment, and one concrete next step after each deploy.

## Common traps

| Situation | Recovery |
|---|---|
| Authentication error | Run `npx netlify login`, then re-check with `npx netlify status`. |
| Site is not linked | Use the link-first flow; initialize a new site only when no matching site exists. |
| Publish directory is absent or stale | Run the declared local build and verify the actual output directory before redeploying. |
| Wrong monorepo app selected | Confirm the working directory and `build.base`, then link and deploy from that target. |
| Production release is unreviewed | Keep the release as a preview until an explicit production request or readiness confirmation. |

## Security and data handling

Deploy commands send project artifacts, deploy metadata, and site identifiers to Netlify. Authentication exchanges session data with Netlify. Local source files remain local until a deploy command is run; keep secrets out of skill files and inspect project configuration before a deploy that could include them.
