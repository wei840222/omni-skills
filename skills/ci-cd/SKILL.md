---
name: ci-cd
description: >
  Automate builds, tests, and deployments for web, mobile, and backend apps.
  Use when setting up continuous integration, fixing failing pipelines, choosing
  GitHub Actions / GitLab CI / platform deploys, caching builds, signing mobile
  apps, or debugging environment drift in CI. Prefer `devops` for release
  strategy and on-call ops, `github-actions` for Actions-only workflow dialect,
  and `k8s` / `server` / `monitoring` for orchestration, host config, and
  observability.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🔄"}'
  related-skills: '{"devops":"Release strategy, environments, rollback, and on-call after pipeline mechanics are set.","github-actions":"Actions-only workflow dialect and marketplace actions when the stack is GitHub-centric.","k8s":"Container orchestration after CI produces deployable artifacts.","monitoring":"Observability and alerting once pipelines and deploys are running.","server":"Host and runtime configuration outside the pipeline definition."}'
---

## When to Use

Trigger on: automated deployment, continuous integration, pipeline setup, GitHub Actions, GitLab CI, build failing, deploy automatically, CI configuration, release automation, Fastlane Match, Next.js cache in CI.

## Routing

- For copy-paste CI/CD workflows and configurations: load `references/templates.md`
- For platform selection, common pipeline pitfalls, and debugging failed builds: load `references/core-concepts.md`
- For mobile CI/CD patterns (iOS Fastlane Match, Android signing, Flutter): load `references/mobile.md`
- For web CI/CD patterns (Next.js/Nuxt build caching, preview deploys): load `references/web.md`

## Out of Scope

- Delivery platform strategy, DORA, and on-call policy → see `devops`
- GitHub Actions marketplace/workflow dialect deep-dive → see `github-actions`
- Container orchestration (Kubernetes) → see `k8s`
- Server configuration → see `server`
- Monitoring and observability → see `monitoring`
