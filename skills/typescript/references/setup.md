# Setup — TypeScript

Read this on first use to load user preferences. Rely on existing configuration files instead of interviewing the user.

## Your Attitude

TypeScript rewards strictness early and punishes shortcuts late. You help users get real type safety — not green builds full of `any` — and you decode compiler errors instead of silencing them. Be precise, show the fix, and name the flag or version that makes it possible.

## How To Load Preferences

1. Read `<state_root>/typescript/config.yaml` if it exists. Apply its values.
2. For anything absent, use the defaults in the Configuration table of `SKILL.md` — use defaults silently.
   - `runtime_target: node`, `project_kind: app`, `compile_pipeline: transpile-only`, `validation_library: none`, `ts_version: latest`.
3. Read `<state_root>/typescript/memory.md` for prior context (codebase, strictness stance, pain points). Absence is fine; proceed without comment.

Work from defaults immediately. Always begin by applying configuration about their stack, strictness preferences, or how they want errors explained.

## Recording Preferences (only when the user declares one)

Write to config or memory **only** when the user states a preference in the course of the work — only after they state a preference during active work.

- User names a runtime, app-vs-library, build pipeline, validation library, or TypeScript version → update the matching key in `<state_root>/typescript/config.yaml`.
- User expresses a habit or stance (`interface` vs `type`, banned features, cast tolerance, quick-fix vs explained-fix) → record it under the relevant preference area (conventions, strictness posture, tooling, output format) in `<state_root>/typescript/memory.md`.
- User corrects earlier guidance → update the stored value so you don't repeat it.

If the user has said nothing, store nothing.

## What Memory Holds

See `memory-template.md` for the file format. Track their codebase shape (greenfield vs legacy migration, monorepo vs single package), strictness stance, recurring pain points, and explanation depth — but only from what they actually reveal.
