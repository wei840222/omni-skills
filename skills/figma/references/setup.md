# Setup — Figma

Read this on first use to load user preferences. Proceed directly to work.

## Your Attitude

Figma files fail quietly: the layout looks right and the tree is wrong, the palette passes in Light and fails in Dark, the library edit breaks ten files at once. Be concrete, name panels and shortcuts precisely, and surface the structural defect rather than the cosmetic one.

## How To Load Preferences

1. Read `<state_root>/config.yaml` if it exists. Apply its values.
2. For anything absent, use the defaults in the Configuration table in `references/best-practices.md`.
   - `figma_plan: professional`, `spacing_base: 8`, `target_platforms: [web]`, `token_pipeline: native`, `component_naming: slash`, `icon_grid: 24`, `library_model: federated`.
3. Read `<state_root>/memory.md` for prior context (their file structure, recurring pain points, who consumes the handoff). Absence is fine; proceed without comment.

Work from defaults immediately. Apply defaults for plan, design-system maturity, and answer depth unless the user states otherwise.

## Delivery Mode

Figma has no CLI. Canvas work is delivered as instructions the user executes: name the panel, the field, and the shortcut, in the order they click them. Anything scriptable — bulk edits, audits, token exports, asset pipelines — is delivered as plugin code or REST calls the user can run.

Before proposing a mechanism that is plan-gated (modes, branching, Dev Mode, library analytics, the Variables API), resolve it against `figma_plan` and offer the fallback if it is unavailable.

## Recording Preferences (only when the user declares one)

Write to config or memory **only** when the user states a preference in the course of the work, rather than running a preflight questionnaire.

- User names their plan, spacing base, target platforms, token route, naming convention, icon grid, or library model → update the matching key in `<state_root>/config.yaml`.
- User expresses a habit or stance (how much to annotate, whether to confirm before destructive actions, tokens-first vs screens-first, which integrations the handoff must feed) → record it under the relevant preference area in `<state_root>/memory.md`.
- User corrects earlier guidance → update the stored value so it does not recur.

If the user has said nothing, store nothing.

## What Memory Holds

The memory file format is the template named alongside this file in SKILL.md's opening paragraph. Track their file and library structure, who consumes the handoff, the pain points they raise, and the depth of explanation they want — but only from what they actually reveal.
