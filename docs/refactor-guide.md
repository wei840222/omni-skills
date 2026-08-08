# Skill Refactor Guide

This document defines the canonical quality gates and workflow standards for the `clawic-skills` refactor process. It is an incrementally extensible quality contract: automation may mark a skill as "refactor complete" and open a pull request only after every defined gate passes.

The currently defined gates are Gate 1: Agent Skills format compatibility, Gate 2: official resource directories and reference paths, Gate 3: persistent state location, Gate 4: related-skill metadata integrity, Gate 5: removal of Clawic feedback and promotional content, Gate 6: knowledge research and domain accuracy, Gate 7: best-practices and description optimization, Gate 8: Darwin Skill evaluation and test coverage, and Gate 9: Freud cognitive load and white bear effect audit. All gates use `skills/garden` as the primary example.

## Core principles

- "Complete" means reproducible check results, not merely rewritten prose.
- Record automated checks separately from human or model judgment; subjective commentary must not replace specification validation.
- Every refactor must preserve the pre-change issue inventory, post-change validation results, and the specification sources used.
- Do not open a pull request while any required gate is failing.
- Every research source used to update skill knowledge must be recorded with its full URL, grouped by topic (e.g., retention benchmarks, CAC benchmarks, experimentation frameworks), and included in the pull request description. Source links must be verifiable and point to the actual page where the data or guidance was found.

## Refactor Workflow Lifecycle & Commit Sequence

Every skill refactor must proceed through the following phases **in strict sequential order**. Each of phases 1–5 must conclude with exactly one focused commit, and phase 6 publishes those commits as a Gitea pull request:

```text
Phase 0 (Baseline) → Phase 1 (Commit: refactor) → Phase 2 (Commit: research) → Phase 3 (Commit: optimize) → Phase 4 (Commit: darwin) → Phase 5 (Commit: freud) → Phase 6 (Gitea PR)
```

### Phase Breakdown

1. **Phase 0: Baseline Establishment**
   - Create a dedicated refactor branch from `local` (`refactor/<slug>`).
   - Check working-tree status and record the target package's complete file inventory (including hidden files/symlinks).
   - Classify all observed baseline nonconformities as `SPEC`, `VALIDATOR`, `PROJECT`, or `RECOMMENDATION`.

2. **Phase 1: Specification Compliance Refactor (Gates 1–5)**
   - Fix format compatibility, file locations (`references/`, `assets/`, `scripts/`), relative paths, persistent state `<state_root>`, `metadata.related-skills` JSON map, and remove all `clawic.com` references.
   - Commit: `refactor(<slug>): specification compliance (Gates 1-5)`

3. **Phase 2: Knowledge Research & Fact Verification (Gate 6)**
   - Execute sub-steps 2.1 (claim inventory & freshness classification) → 2.2 (deep research via `/research` or primary sources) → 2.3 (update knowledge & record full citation URLs).
   - Commit: `research(<slug>): update domain knowledge and sources (Gate 6)`

4. **Phase 3: Best-Practices & Description Optimization (Gate 7)**
   - Streamline `SKILL.md` for progressive disclosure; optimize frontmatter `description` for imperative, trigger-focused accuracy.
   - Commit: `optimize(<slug>): progressive disclosure and description (Gate 7)`

5. **Phase 4: Darwin Skill Evaluation & Test Prompts (Gate 8)**
   - Create `test-prompts.json` in English with happy-path and complex scenarios.
   - Execute prompts and record real output in `actual`.
   - Iterate with `/darwin-skill` until the score is at least 80/100 without regressing safety or spec compliance.
   - Commit: `darwin(<slug>): iterate evaluation to score >= 80 (Gate 8)`

6. **Phase 5: Freud White Bear & Cognitive Load Audit (Gate 9)**
   - Scan with `/freud-skill` Mode 2 across Lenses 2, 3, 4, and 6. Reframe prohibitions into positive definitions and manage cognitive load (<= 25 concepts).
   - Commit: `freud(<slug>): eliminate white bear effects and cognitive load (Gate 9)`

7. **Phase 6: Gitea Pull Request Creation**
   - Push branch to Gitea remote, create PR targeting `local`, and assign `ani6439walc` as reviewer.
   - Populate the PR description with the template at `docs/pull-request-template.md`.
   - After Gitea assigns the PR number, add the skill name, PR number, date, and final Darwin score to the root `CHANGELOG.md` table on the same branch; commit and push the update so it lands with the merged PR.

### Pre-Commit Verification Checklist

Before committing any phase:
- Run official validator: `uvx --from skills-ref agentskills validate skills/<slug>`.
- Verify all relative references resolve correctly.
- Perform syntax checks on scripts and safe smoke tests.
- Scan package for credentials, private keys, or sensitive user data.
- Run `git diff --check` to ensure no whitespace or formatting errors.
- Confirm working-tree contains only authorized changes for the target skill.

## Gate 1: Agent Skills specification compatibility

### Specification sources

1. Read the document index first: <https://agentskills.io/llms.txt>
2. Then read the normative specification: <https://agentskills.io/specification>
3. Use the reference validator named by the specification: <https://github.com/agentskills/agentskills/tree/main/skills-ref>

If the specification and validator differ, report the findings separately:

- **SPEC**: directly required by specification text.
- **VALIDATOR**: additionally enforced by, or an actual execution constraint of, the reference validator.
- **RECOMMENDATION**: officially recommended, but not a hard format requirement.

Do not misreport recommendations as hard errors, and do not ignore a specification requirement merely because the validator does not check it.

### Check procedure

For each candidate skill, perform these steps in order:

1. Read `skills/<slug>/SKILL.md` and inspect its actual frontmatter, body, and referenced files.
2. Read the latest Agent Skills document index and specification at execution time. Do not rely on model memory or a previously cached specification summary.
3. Compare the directory structure, frontmatter, name, description, progressive disclosure, and file-reference rules item by item.
4. Run the reference validator and retain the complete command, version, exit code, and error messages.
5. Classify every finding as `SPEC`, `VALIDATOR`, or `RECOMMENDATION`.
6. After making corrections, rerun the same checks. Gate 1 is complete only when every required item passes.

The current PyPI `skills-ref` 0.1.1 package exposes the executable as `agentskills`, so the reproducible command is:

```bash
uvx --from skills-ref agentskills validate skills/<slug>
```

The official specification page currently shows `skills-ref validate ./my-skill`. Automation must use the executable actually provided by the installed package and record this documentation/package-interface difference in its report.

## `skills/garden` baseline audit

Audit target: `skills/garden/SKILL.md`, currently declaring version `1.1.6`.

### Nonconformities

#### 1. `name` violates the naming rules (SPEC)

Current value:

```yaml
name: Garden
```

Problems:

- It contains an uppercase letter; the specification requires lowercase.
- `Garden` does not exactly match the parent directory name `garden`.

After the preceding YAML parsing problem is removed, the reference validator reports both errors:

```text
Skill name 'Garden' must be lowercase
Directory name 'garden' must match skill name 'Garden'
```

#### 2. Frontmatter contains unsupported top-level fields (VALIDATOR)

Current additional fields:

```yaml
slug: garden
version: 1.1.6
homepage: https://clawic.com/skills/garden
changelog: Natural setup flow, explicit consent, no technical jargon
```

`skills-ref` 0.1.1 accepts only the following top-level fields:

```text
allowed-tools, compatibility, description, license, metadata, name
```

The validator therefore rejects `slug`, `version`, `homepage`, and `changelog`. This project applies one consistent treatment: remove `slug`, `homepage`, and `changelog`; move `version` to `metadata.version` and retain it as a string. Daily refactor tasks must not invent alternative locations or compatibility fields for individual skills.

#### 3. YAML cannot be parsed by the reference validator (VALIDATOR)

The original file contains:

```yaml
requires:
  bins: []
```

This causes the StrictYAML parser in `skills-ref` 0.1.1 to fail immediately:

```text
Invalid YAML in frontmatter
Found ugly disallowed JSONesque flow mapping
```

This is an actual constraint of the reference validator. Even if a general YAML parser accepts a flow-style empty array, completion still requires an exit code of 0 from the official reference-validation command.

#### 4. `metadata` is not a string-to-string mapping (SPEC)

The specification defines `metadata` as an arbitrary string-to-string mapping. Garden uses a nested structure containing mappings, lists, and empty arrays:

```yaml
metadata:
  clawdbot:
    emoji: 🌱
    requires:
      bins: []
    os:
    - linux
    - darwin
    - win32
    displayName: Garden
```

This does not conform to the required data shape. OpenClaw still accepts the legacy `metadata.clawdbot` alias, but its official guidance recommends `metadata.openclaw` for new skills. To satisfy both the Agent Skills string-to-string mapping and OpenClaw's JSON5 parsing, `metadata.openclaw` must be stored as a JSON string rather than a nested YAML object.

Handle Garden's fields as follows:

- Move `metadata.clawdbot.emoji` to `emoji` in the `metadata.openclaw` JSON string.
- Remove the empty `requires.bins`; it has no gating effect.
- Remove `os` when it lists `linux`, `darwin`, and `win32` together; covering every platform is equivalent to no restriction.
- Remove `displayName`, which is not an officially supported OpenClaw field.

Currently documented `metadata.openclaw` fields include `emoji`, `homepage`, `os`, `always`, `skillKey`, `primaryEnv`, `envVars`, `requires`, `install`, `nix`, and `config`. Within `requires`, OpenClaw supports `bins`, `anyBins`, `env`, and `config`. A refactor may preserve only fields that the skill actually uses and OpenClaw officially supports; empty arrays, all-platform filters, and unsupported display fields must not remain.

#### 5. `description` does not clearly state when to trigger the skill (RECOMMENDATION)

The current description explains the capability, but readers must infer most of the "when to use" behavior:

```yaml
description: Track your entire garden with structured memory for plants, zones, tasks, harvests, and climate-aware planning that compounds over seasons.
```

The specification recommends that a description explain both what the skill does and when to use it, with keywords that help an agent recognize appropriate trigger conditions. The refactor should explicitly cover user intents such as garden planning, plant tracking, watering tasks, harvest logging, crop rotation, and plant problem diagnosis. Final wording must still avoid over-triggering adjacent skills.

### Target frontmatter for Garden

After Gate 1, Garden should use the following frontmatter shape:

```yaml
---
name: garden
description: Track plants, garden zones, care tasks, harvests, health issues, crop rotations, and climate-aware seasonal plans across growing seasons. Use when the user wants to manage, diagnose, plan, or review a garden.
metadata:
  version: "1.1.6"
  openclaw: '{"emoji":"🌱"}'
  related-skills: '{"daily-planner":"Places garden work into daily priorities and time blocks.","habits":"Turns recurring garden care into trackable routines.","journal":"Captures free-form garden observations outside structured records.","plants":"Extends Garden with plant-specific care and identification.","remind":"Schedules watering and seasonal task reminders."}'
---
```

Repository-metadata single-source rules:

- Remove top-level `slug`; derive the slug from the directory name and `name`.
- Delete each skill's `_meta.json`; do not maintain a second copy of version or display-name data.
- Keep `version` only in `metadata.version`, and require a string value.
- Do not add `license`; this project does not override licensing per skill.
- Remove `homepage` from both top-level and OpenClaw metadata.
- Remove `changelog`; Git history and pull requests preserve release notes.
- Store all OpenClaw-specific metadata in the `metadata.openclaw` JSON string.
- Garden currently needs only OpenClaw's `emoji`; omit every other field because it has no practical effect.

### Already conforming items

Garden already satisfies these baseline requirements:

- The directory contains the required `SKILL.md`.
- `SKILL.md` consists of YAML frontmatter followed by a Markdown body.
- `description` is nonempty and shorter than 1,024 characters.
- The main file is 123 lines, below the recommended 500-line limit.
- Detailed content is already split into multiple files loaded on demand, providing the basis for progressive disclosure.
- `setup.md`, `tracking.md`, `climate-setup.md`, `diagnostics.md`, `planning.md`, and `memory-template.md` are all one-level relative paths from the skill root.
- Additional files remain inside the skill directory; the specification permits `scripts/`, `references/`, `assets/`, and other additional files.

"Already conforming" means only that this gate does not require changing the item. It does not establish content quality or actual behavior under later gates.

## Gate 1 pass criteria

A skill passes only when every item below is satisfied:

- [ ] `SKILL.md` exists, and both its frontmatter and Markdown body are parseable.
- [ ] `name` is 1–64 characters using lowercase letters, digits, and hyphens; it has no leading, trailing, or consecutive hyphens and exactly matches its parent directory name.
- [ ] `description` is 1–1,024 characters and clearly describes the skill's capability and trigger conditions.
- [ ] Frontmatter uses only top-level fields allowed by the specification.
- [ ] If present, `metadata` is a string-to-string mapping.
- [ ] `version` exists only as `metadata.version` with a string value; no top-level `version` remains.
- [ ] OpenClaw-specific metadata uses a `metadata.openclaw` JSON string and includes only officially supported fields with a practical effect.
- [ ] No top-level `slug`, `license`, `homepage`, or `changelog` remains.
- [ ] The skill directory contains no `_meta.json`.
- [ ] If present, `compatibility` is a string of 1–500 characters.
- [ ] If present, `allowed-tools` is a space-delimited string, not a YAML list.
- [ ] The main `SKILL.md` does not exceed 500 lines; detailed or branching content is split out for on-demand loading.
- [ ] Every file reference is relative to the skill root and avoids unnecessary deep reference chains.
- [ ] `uvx --from skills-ref agentskills validate skills/<slug>` exits with code 0.
- [ ] The pull-request report includes the specification URL, validator version, execution command, and before/after results.

## Gate 2: Official resource directories and reference paths

### Specification sources and project requirements

This gate is based on Agent Skills [Optional directories](https://agentskills.io/specification#optional-directories), [Progressive disclosure](https://agentskills.io/specification#progressive-disclosure), and [File references](https://agentskills.io/specification#file-references).

The Agent Skills specification allows other additional files at the skill root, so a root-level supporting document is not itself a format error. To make daily refactors consistent, predictable, and progressively loadable, this project applies a stricter completion standard: every supporting file other than `SKILL.md` must be classified by official purpose under `references/`, `assets/`, or `scripts/`. Supporting files must not remain flattened at the skill root, and empty directories must not be created merely to imitate the format.

### Directory classification rules

#### `references/`

Store supplemental documents that an agent reads only in specific situations, such as operating procedures, domain rules, diagnostic knowledge, data semantics, and detailed references. Each reference file should focus on one topic, and `SKILL.md` must explicitly explain when to read it.

#### `assets/`

Store static resources that an agent uses, copies, or emits, such as document templates, configuration templates, images, schemas, lookup tables, and sample data. Assets must not contain the primary decision process. If an original file mixes operating rules with templates, split it by role into one reference and one asset, each with a single source of truth.

#### `scripts/`

Store only programs an agent can actually execute. Every script must be self-contained or clearly document its dependencies, provide useful errors, and handle reasonable edge cases. A skill with no executable logic must not create `scripts/`; Markdown instructions or documents containing example commands must not be misclassified as scripts because of their extension or presentation.

### Reference-path rules

- Resolve every internal skill-file reference from the skill root containing `SKILL.md`.
- `SKILL.md` uses one-level relative paths such as `references/setup.md`, `assets/garden-data-templates.md`, or `scripts/validate.py`.
- Do not use absolute filesystem paths, repository-root paths, legacy root-level filenames, or ambiguous paths that depend on the current working directory.
- When moving or splitting files, update references in the `SKILL.md` body, tables, examples, and every supporting file at the same time.
- `SKILL.md` should directly list resources available for on-demand loading and when to read them. Avoid deep reference chains where one reference must be read merely to discover another resource.
- Every referenced target must exist. Every moved file must be reachable through routing in `SKILL.md`; stale references and orphaned resources are forbidden.
- This rule governs resource references in skill source code only. User-data paths created at runtime, such as `<state_root>/memory.md`, must instead be reviewed under Gate 3's state-location resolver and safety rules; they must not be moved into skill resources.

### Target directory for Garden

```text
skills/garden/
├── SKILL.md
├── references/
│   ├── setup.md
│   ├── memory.md
│   ├── tracking.md
│   ├── climate.md
│   ├── diagnostics.md
│   └── planning.md
└── assets/
    └── garden-data-templates.md
```

Garden currently has no executable program, so it does not create `scripts/`.

### Garden file migration

| Current file | Target | Treatment |
| --- | --- | --- |
| `SKILL.md` | `SKILL.md` | Keep at the root; update routing and every resource path. |
| `_meta.json` | Delete | Gate 1 already requires removing duplicate repository metadata. |
| `setup.md` | `references/setup.md` | Move first-use, consent, and integration procedures. |
| `climate-setup.md` | `references/climate.md` | Move climate decision rules; extract template portions into the asset. |
| `diagnostics.md` | `references/diagnostics.md` | Move symptom-diagnosis knowledge and procedures. |
| `planning.md` | `references/planning.md` | Move crop-rotation and seasonal-planning rules. |
| `tracking.md` | `references/tracking.md` | Preserve tracking triggers and update rules; extract template portions into the asset. |
| `memory-template.md` | `references/memory.md` | Preserve storage lifecycle, state values, and data semantics; extract template portions into the asset. |
| Data templates in multiple files | `assets/garden-data-templates.md` | Centralize templates for `memory.md`, `climate.md`, `harvests.md`, plants, zones, and monthly logs to avoid duplicate definitions. |

Garden's `SKILL.md` must update at least these legacy references:

```text
setup.md            -> references/setup.md
memory-template.md  -> references/memory.md + assets/garden-data-templates.md
tracking.md         -> references/tracking.md + assets/garden-data-templates.md
climate-setup.md    -> references/climate.md + assets/garden-data-templates.md
diagnostics.md      -> references/diagnostics.md
planning.md         -> references/planning.md
```

### Gate 2 pass criteria

- [ ] The skill root retains only `SKILL.md` and the actually used `references/`, `assets/`, and `scripts/` directories.
- [ ] Every supporting file is classified by official purpose; files mixing operating rules with static templates are split by role.
- [ ] `references/` contains only on-demand instructions, procedures, and domain knowledge, with each file remaining focused.
- [ ] `assets/` contains only templates and other static resources and does not duplicate rules defined in references.
- [ ] If present, `scripts/` contains only executable programs; dependencies, errors, and edge cases are handled.
- [ ] No empty optional directory exists, and no useless script was added merely for form.
- [ ] `SKILL.md` clearly explains the purpose of every reference, asset, or script and when to load or execute it.
- [ ] Every internal skill reference is relative to the skill root containing `SKILL.md` and uses a one-level relative path.
- [ ] Every legacy path was updated after moving, renaming, or splitting files; no stale reference remains.
- [ ] Every referenced target exists, and every resource is directly discoverable from `SKILL.md`; no orphaned resource remains.
- [ ] Templates and operating rules each have one source of truth, with no duplication or contradiction introduced by splitting.
- [ ] `SKILL.md` remains under 500 lines, resources load only when needed, and there are no unnecessary deep reference chains.
- [ ] The pull-request report includes before/after directory trees, a complete migration table, and reference-path audit results.

## Gate 3: Workspace-relative persistent state location

### Specification status

Agent Skills does not define a runtime-state location. First-party source research and recommendations for this project are collected in `docs/research/skill-state-storage.md`. This gate is a `clawic-skills` project specification and must not be presented as the official Agent Skills or OpenClaw state layout.

This project adopts a workspace-first state convention. Every stateful skill must define candidate locations, lookup order, creation behavior, and a single placeholder near the beginning of `SKILL.md`, so every file in the same skill uses consistent semantics.

### Terms

- `<workspace>`: the current agent workspace root supplied by the host/runtime. Do not substitute the shell's current working directory or guess when it cannot be resolved.
- `<skill>`: the skill's specification name, which must equal both the `name` in `SKILL.md` and the parent directory name.
- `<state_root>`: the one active state directory selected by this gate's resolution procedure. It is a placeholder in skill documentation, not a literal directory name, and must never be written unchanged to the filesystem.

This project consistently uses `<state_root>`, not synonyms such as `<status_folder>`, `<data_dir>`, or `<memory_path>`, which could make different files appear to refer to different locations.

### Candidate locations and precedence

For Garden, permitted state roots are, in order:

```text
<workspace>/garden/
<workspace>/memory/garden/
~/garden/
```

Generalized order:

```text
<workspace>/<skill>/
<workspace>/memory/<skill>/
~/<skill>/
```

If the user or host configuration explicitly defines a state root, that explicit path takes precedence over all candidates above. Resolve the explicit path to an actual location and record it as `<state_root>`; do not mix candidate directories afterward.

### State-root resolution procedure

Before the first state read, query, create, update, or delete in each skill invocation:

1. If the user or host explicitly defines a state root, use it.
2. Otherwise, check `<workspace>/<skill>/`, `<workspace>/memory/<skill>/`, and `~/<skill>/` in that order.
3. The first existing candidate directory becomes the only `<state_root>` for this invocation.
4. If multiple candidate directories exist, still use the highest-precedence one. Do not automatically merge, synchronize, or cross-read/write lower-precedence directories, and tell the user that multiple copies of state were detected.
5. If no candidate exists and the user wants to begin saving state, create `<workspace>/<skill>/` by default.
6. If the host cannot supply `<workspace>`, do not impersonate it with the current working directory. An existing `~/<skill>/` may be read; if it also does not exist, ask the user or host to specify a state root before creating data.
7. Once selected, `<state_root>` remains fixed for the invocation. Do not silently switch because another candidate appears later.

Search for existing locations before performing default creation. Creating `<workspace>/<skill>/` first is forbidden because a new empty directory could shadow existing user data at a lower-precedence location. The state resolver chooses a location; it does not grant permission to write. Creating or modifying persistent state must still comply with the skill's declared consent rules and host policy.

### Required section near the beginning of `SKILL.md`

Every stateful skill must provide a State location section immediately after frontmatter and before other operating instructions. Garden's target semantics are:

```markdown
## State location

Garden state may exist in `<workspace>/garden/`, `<workspace>/memory/garden/`, or `~/garden/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/garden/`, `<workspace>/memory/garden/`, `~/garden/`.
3. If none exists and state must be created, default to `<workspace>/garden/`.

Use the selected `<state_root>` for every state operation in this skill.
```

The actual rewrite may match the skill's voice, but it must not omit:

- all three candidate locations;
- the explicit override;
- first-existing lookup order;
- the default creation location when none exists; and
- consistent use of `<state_root>` afterward.

### State-path notation in skill content

Outside the State location section, every skill-state path in `SKILL.md`, `references/`, `assets/`, and `scripts/` uses `<state_root>`:

```text
<state_root>/memory.md
<state_root>/climate.md
<state_root>/harvests.md
<state_root>/plants/{name}.md
<state_root>/zones/{name}.md
<state_root>/log/YYYY-MM.md
```

Rules:

- Do not repeatedly hard-code `<workspace>/<skill>/`, `<workspace>/memory/<skill>/`, or `~/<skill>/` in later sections.
- Do not use bare `plants/`, `zones/`, `log/`, or `memory.md` for runtime state. Prefix them with `<state_root>/` so they cannot be mistaken for paths relative to the skill package or current working directory.
- Do not use `<state_root>` for skill resources. Resource paths continue to use `references/...`, `assets/...`, or `scripts/...` under Gate 2.
- If an asset demonstrates the locations of files that will be created, it also uses `<state_root>`; the template itself remains a read-only skill resource.
- Scripts must receive or resolve the actual state root before reading or writing child paths. They must not treat the literal string `<state_root>` as a filesystem path.
- Host-owned shared memory such as workspace `MEMORY.md` is outside `<state_root>`. If a skill needs to write there, it must separately list the external write, actual host-provided path, content scope, and consent.

### Garden state inventory

After selecting `<state_root>`, Garden uses this state tree:

```text
<state_root>/
├── memory.md          # Required once persistent state is enabled
├── climate.md         # Optional
├── harvests.md        # Optional
├── plants/            # Optional
│   └── {name}.md
├── zones/             # Optional
│   └── {name}.md
└── log/               # Optional
    └── YYYY-MM.md
```

| Path | Role | Creation condition |
| --- | --- | --- |
| `<state_root>/memory.md` | Current context, status, and integration preferences | Create the first time data must persist across sessions. |
| `<state_root>/climate.md` | Climate zone, frost dates, and microclimate settings | Create when the user needs climate-aware planning. |
| `<state_root>/harvests.md` | Harvest records and cross-season comparisons | Create when the user requests harvest tracking. |
| `<state_root>/plants/{name}.md` | Per-plant tracking | Create when the user requests detailed plant tracking. |
| `<state_root>/zones/{name}.md` | Zone and rotation tracking | Create when the user requests zone tracking. |
| `<state_root>/log/YYYY-MM.md` | Monthly activity record | Create when garden activity is first recorded. |
| Workspace `MEMORY.md` | Optional external integration pointer | Write only after the host supplies the actual path and the user explicitly consents. |

Create optional state only when the corresponding feature is actually needed. Do not pre-expand every template into empty files or directories.

### Garden decisions and results for this rewrite

1. `~/Clawic/data/garden/` was removed from Garden's active instructions; skill content now uses the State location resolver and `<state_root>`.
2. `memory-template.md` no longer creates `~/garden/` unconditionally or writes to `~/Clawic/data/garden/memory.md`; it now creates only the resolved `<state_root>` and required child paths.
3. A State Location section was added near the beginning of `SKILL.md`, requiring `<state_root>` resolution before the first state operation.
4. State paths in `SKILL.md`, `setup.md`, `memory-template.md`, `tracking.md`, `climate-setup.md`, `diagnostics.md`, and `planning.md` were normalized to `<state_root>/...`.
5. `log/YYYY-MM.md` was added to the Architecture tree and normalized as `<state_root>/log/YYYY-MM.md`.
6. Existing user data under `~/Clawic/data/garden/` must not be automatically moved or deleted during content refactoring. It is not in the new active lookup order. Migration requires a separate user decision and must provide copy, validation, cutover, and rollback steps.

### Gate 3 pass criteria

- [ ] A stateful skill lists `<workspace>/<skill>/`, `<workspace>/memory/<skill>/`, and `~/<skill>/` near the beginning of `SKILL.md`.
- [ ] The documentation explicitly defines the override and first-existing lookup order.
- [ ] Reads, queries, updates, and deletes use the first existing directory found by precedence.
- [ ] If multiple candidate directories exist, only the highest-precedence directory is used; no automatic merge, synchronization, or cross-write occurs, and the state conflict is reported.
- [ ] Existing-directory lookup completes before creation; `<workspace>/<skill>/` is created by default only when no candidate exists.
- [ ] `<workspace>` comes from the host/runtime and is not guessed from the shell's current working directory.
- [ ] `<state_root>` is resolved once per invocation, and every subsequent state operation uses the same location.
- [ ] Outside the State location section, every state path uses `<state_root>/...`; candidate roots are not hard-coded.
- [ ] There are no ambiguous bare runtime-state paths such as `memory.md`, `plants/`, `zones/`, or `log/`.
- [ ] Skill resources continue to use Gate 2 relative paths; `<state_root>` is not mixed with `references/`, `assets/`, or `scripts/`.
- [ ] If scripts exist, they accept or resolve the actual state root and do not treat the `<state_root>` literal as a filesystem name.
- [ ] Every state child is marked required or optional and documents its creation condition and data role.
- [ ] Optional state is created only when needed; no useless empty file or directory is pre-created.
- [ ] Shared or external writes are listed separately from `<state_root>`, use a host-provided path, and have explicit consent and minimum write scope.
- [ ] Runtime state is not written into the skill package, repository, or an unmanaged path dependent on the current working directory.
- [ ] A legacy non-candidate path appears only as a migration source, never in active lookup order, and is not silently moved or deleted during refactoring.
- [ ] `SKILL.md`, every supporting file, template, and script uses fully consistent `<state_root>` semantics.
- [ ] The pull-request report includes before/after state inventories, resolver order, removed hard-coded paths, conflict behavior, and external-write inventory.

## Gate 4: Related-skill metadata integrity

### Specification status

`metadata.related-skills` is a project-level `clawic-skills` extension that turns cross-skill relationships inside a skill package into one machine-readable index. The Agent Skills specification supplies only the string-to-string `metadata` container. This gate defines the JSON schema for the `related-skills` string value and must not present this field as a built-in Agent Skills or OpenClaw relationship mechanism.

After `metadata.related-skills` is added, it becomes the canonical relationship list. A dedicated `Related Skill`, `Related Skills`, or equivalent section in `SKILL.md` that enumerates other skills must be removed so metadata and prose do not maintain two lists.

### Trigger conditions and scan scope

Before deleting any section during refactoring, scan the complete skill package, not only `SKILL.md`:

- dedicated sections in `SKILL.md` that enumerate other skills;
- inline handoffs, alternatives, dependencies, install instructions, or statements such as "for this case, see/use `<skill>`";
- `references/`, `assets/`, `scripts/`, and other supporting files;
- Markdown links, code spans, CLI examples, comments, template text, and explicit skill names.

Create a relationship only when the text genuinely identifies another skill. General domain vocabulary does not count. For example, the ordinary noun "plants" in Garden does not become a relationship merely because the repository contains a `plants` skill; there must be an explicit skill mention, handoff, installation suggestion, or capability boundary.

### Repository existence gate

Every related skill must actually exist in the current repository:

```text
skills/<canonical-name>/SKILL.md
```

Validation rules:

- The key is the directory name in `skills/<canonical-name>/`. After Gate 1, the target `SKILL.md` name must also exactly match that directory.
- Do not assume a skill exists solely because a website, registry, old slug, or natural-language text mentions its name.
- If the target does not exist, do not add it to `related-skills`. Record an unresolved reference and correct or remove the original mention; Gate 4 remains failing.
- Do not create an empty placeholder skill to make validation pass.
- The current skill must not include itself in the relation map.

### `metadata.related-skills` format

The field must be under `metadata` in `SKILL.md`, and its YAML value must be a single string containing a valid JSON object:

```yaml
metadata:
  related-skills: '{"daily-planner":"Places garden work into daily priorities and time blocks.","plants":"Extends Garden with plant-specific care and identification."}'
```

The decoded JSON contract is:

```text
object<string, string>
key   = canonical name of the related skill
value = one concise reason the skill relates to the current skill
```

Required rules:

- The JSON root must be an object, not an array, nested object, boolean, or null.
- Every key must be a canonical skill name that actually exists in the repository; display names, URLs, `<slug>` placeholders, and speculative nonexistent names are forbidden.
- Every value must be a nonempty string explaining the specific relationship to the **current skill**, not merely repeating the target name or saying "related."
- Sort keys lexicographically to produce deterministic diffs.
- When no related skill exists, omit `related-skills`; do not write `'{}'`, `'[]'`, or an empty string.
- `related-skills` describes relationships only. It does not replace dependencies, runtime requirements, installation procedures, or user authorization.

### Prose deduplication and inline-reference rules

After metadata is created and validated, normalize content as follows:

- Delete dedicated `Related Skill`, `Related Skills`, or equivalent sections in `SKILL.md`, including installation introductions and catalog links within them.
- Do not recreate the same complete list, table, or expanded JSON elsewhere in `SKILL.md`.
- A contextual handoff such as "for general plant identification, see the `plants` skill" may remain because it is an in-context operational decision rather than a duplicate list.
- Every retained inline skill reference must appear in `metadata.related-skills`; its reason should summarize that handoff, alternative, or capability boundary.
- Contextual references in supporting files may remain when required for agent behavior, but metadata must index them as well.
- Do not add a useless recommendation to prose merely to make a metadata entry "traceable." If the source was a removed dedicated section, the pre-change inventory and pull-request report provide provenance; metadata is the sole post-change list.
- If one related skill appears in multiple places, metadata keeps one key whose value summarizes the primary relationship to the current skill.
- If a mention represents a required dependency, declare it through the runtime's formal dependency or requirement mechanism in addition to `related-skills`. The agent must not infer and install dependencies from this field.

### Link and installation safety

- The `related-skills` JSON stores canonical names and reasons only, not catalog URLs.
- When deleting a dedicated Related Skills section, also remove generic catalog links and `<slug>` placeholder links in that section.
- If a retained inline reference includes a link, verify the actual target. Remove or correct dead and 404 URLs.
- Installing, downloading, or enabling a related skill still requires user authorization; the presence of a metadata key is not installation consent.

### Garden decisions and results for this rewrite

Garden's original `Related Skills` section listed five skills. Before creating metadata, the following targets were individually verified to contain `SKILL.md` in the repository:

```text
skills/daily-planner/SKILL.md
skills/habits/SKILL.md
skills/journal/SKILL.md
skills/plants/SKILL.md
skills/remind/SKILL.md
```

Garden now keeps this canonical relation map:

```yaml
metadata:
  related-skills: '{"daily-planner":"Places garden work into daily priorities and time blocks.","habits":"Turns recurring garden care into trackable routines.","journal":"Captures free-form garden observations outside structured records.","plants":"Extends Garden with plant-specific care and identification.","remind":"Schedules watering and seasonal task reminders."}'
```

The dedicated `Related Skills` section was removed from `SKILL.md`; Garden currently has no other inline related-skill reference that needs to remain. The original section's `https://clawic.com/skills/<slug>` placeholder was removed with it.

### Gate 4 pass criteria

- [ ] Before deleting a relationship section, `SKILL.md`, `references/`, `assets/`, `scripts/`, and every other package file were scanned.
- [ ] Every candidate mention was classified as a genuine skill identity or ordinary domain vocabulary.
- [ ] Every relationship key passes the `skills/<canonical-name>/SKILL.md` existence check.
- [ ] Nonexistent targets were not added to metadata; unresolved references were fixed or explicitly block Gate 4.
- [ ] `metadata.related-skills` exists when relationships exist and is omitted entirely when none exist.
- [ ] The YAML value is a string that decodes successfully into a JSON object.
- [ ] Every key and value in the decoded object is a nonempty string; no nested values exist.
- [ ] Keys are lexicographically sorted, with no self-relationship or duplicate relationship.
- [ ] Every reason explains a concrete relationship to the current skill rather than using a generic label.
- [ ] Dedicated `Related Skill` or `Related Skills` list sections were removed from `SKILL.md`.
- [ ] Prose does not recreate the complete relationship list or a copy of metadata elsewhere.
- [ ] Every retained inline or situational skill reference appears in metadata.
- [ ] Every explicit skill reference retained in supporting files appears in metadata.
- [ ] Required dependencies still use the formal dependency/requirement mechanism; `related-skills` does not imply automatic installation.
- [ ] No unresolved `<slug>`, dead catalog URL, or URL stored in a JSON value remains.
- [ ] The pull-request report includes the pre-change relationship inventory, mention sources, resolved canonical names, existence checks, JSON parse result, removed dedicated sections, and unresolved references.

## Gate 5: Removal of Clawic feedback and promotional content

### Specification status

A skill package should contain only instructions, resources, and compatible metadata needed to execute the skill. It should not include requests to rate or star it, check the latest version, browse a catalog, or follow traffic to `clawic.com`. This gate is a project-level `clawic-skills` content-cleanup rule.

### Scan scope

Scan every file under `skills/<name>/`, including:

- `SKILL.md` frontmatter and body;
- `references/`, `assets/`, and `scripts/`;
- other Markdown, JSON, YAML, templates, examples, comments, and text resources;
- Markdown inline links, reference-style links, bare URLs, HTML links, and text inside code blocks.

At minimum, perform a case-insensitive search for:

```text
clawic.com
www.clawic.com
http://clawic.com
https://clawic.com
```

A human or model must also inspect sections named `Feedback`, `Support`, `More Skills`, `Discover`, `Explore`, `Star`, `Latest version`, and similar headings that may contain promotional calls to action, so removing a URL cannot leave empty advertising copy behind.

### Removal rules

- No occurrence of the `clawic.com` domain may remain in a skill package. This applies to frontmatter, prose, references, assets, scripts, comments, and examples.
- If a dedicated feedback, advertising, catalog, rating, starring, latest-version, or referral section contains `clawic.com`, delete the **entire dedicated section**, including its heading, introduction, list, and whitespace remnants—not only the URL.
- If promotional content is mixed with operationally useful content, remove the promotional sentence and retain the necessary operation in an appropriate nonpromotional section. The package must still reach zero `clawic.com` matches.
- Remove promotional or homepage `clawic.com` URLs from frontmatter and metadata. Do not relocate them to another metadata key, comment, asset, or encoded JSON string to evade scanning.
- Do not recreate the same advertising call to action without a URL using wording such as "visit our site," "find more Clawic skills," or "star this skill."
- Do not replace a removed URL with a `<slug>` placeholder, short URL, redirect, or plain-text domain.
- This gate does not require removing genuine third-party official documentation needed by the skill. There is no exception for `clawic.com` inside this project's skill packages.
- Repository- or registry-level publication information should be managed by an external index, Git history, or pull requests and must not be copied back into individual skill content.

### Relationship to other gates

- Gate 1 already requires removing top-level `homepage`; this gate additionally ensures supporting files and prose contain no `clawic.com` promotion.
- Gate 4 already requires removing dedicated Related Skills lists; catalog URLs within those lists are also subject to this gate's zero-match rule.
- This gate is not based solely on whether a URL is dead. Feedback and advertising calls to action must be removed even when their links still work.

### Garden decisions and results for this rewrite

Garden originally contained three `clawic.com` occurrences:

```text
SKILL.md frontmatter: homepage: https://clawic.com/skills/garden
SKILL.md Feedback: If useful, star it: https://clawic.com/skills/garden
SKILL.md Feedback: Latest version: https://clawic.com/skills/garden
```

Treatment:

- Removed top-level `homepage`.
- Removed the complete `## Feedback` section rather than leaving an empty heading or an unlinked call to action.
- The other Garden supporting files and `_meta.json` contained no `clawic.com` occurrence. Gate 1 remains responsible for deleting `_meta.json`; this gate does not expand its scope.

### Gate 5 pass criteria

- [ ] Every file in the skill directory was scanned, not only `SKILL.md`.
- [ ] A case-insensitive search for `clawic.com` returns zero matches.
- [ ] Frontmatter and encoded metadata strings contain no `clawic.com`.
- [ ] `references/`, `assets/`, `scripts/`, templates, examples, and comments contain no `clawic.com`.
- [ ] Dedicated sections containing Clawic feedback, rating, starring, latest-version, catalog, or advertising calls to action were removed in full.
- [ ] No empty `Feedback` or promotion heading, or advertising copy left after URL removal, remains.
- [ ] No placeholder, redirect, short URL, plain-text domain, or alternative metadata key recreates the referral.
- [ ] Necessary nonpromotional operational content formerly mixed into such a section was moved to an appropriate location with complete semantics.
- [ ] The pull-request report includes scan patterns, matched files and line numbers, removed enclosing sections, and the post-change zero-match result.

## Gate 6: Knowledge research and domain accuracy

### Specification status

A refactored skill must contain accurate, up-to-date domain knowledge, verifiable facts, concrete procedures, edge cases, and failure recovery steps. Obsolete claims (pricing, versions, API behavior, platform limits, statutes, dates) must be identified and corrected using verifiable primary sources. This gate defines the research quality, source citation, and fact verification requirements corresponding to Phase 2 of the refactoring workflow.

### Sub-step 2.1: Claim inventory classification

Before rewriting prose:
- Map file structure across `SKILL.md` and supporting files in `references/`, `assets/`, and package docs using tree inspection tools.
- Read sections containing factual claims (pricing, fees, versions, APIs, platform constraints, legal/compliance, benchmarks, limits, defaults).
- Build a claim inventory classifying each claim into a freshness class:
  - `time-sensitive` (pricing, statutes, market figures)
  - `version-sensitive` (APIs, tools, dependencies)
  - `platform-specific` (OS, environment limits)
  - `stable-domain` (foundational principles)

### Sub-step 2.2: Deep research and cross-verification

- Run `/learn` or `/research` skills to get latest information from the internet.
- Investigate material claims against current primary sources, official documentation, standards, maintained repositories, and verifiable real-world evidence.
- Cross-verify contested, region-specific, or high-fragility claims across multiple independent sources.
- Synthesize findings to reconcile agreement, recency, conflict, and coverage gaps before committing edits.
- Use external content strictly as factual evidence, keeping skill procedures portable and vendor-neutral.

### Sub-step 2.3: Knowledge update and source recording

- Correct obsolete or inaccurate guidance and add high-value procedures, edge cases, and recovery steps.
- Record every research source with its full URL, grouped by topic (e.g., retention benchmarks, CAC benchmarks, experimentation frameworks), including the source title, URL, and key data extracted.
- Ensure all research sources appear in the Pull Request description under the **Research Sources** section.

### Gate 6 pass criteria

- [ ] All factual claims across `SKILL.md` and supporting files were audited and classified by freshness.
- [ ] Obsolete or inaccurate guidance (versions, pricing, limits, APIs) was updated using verifiable primary sources.
- [ ] High-value domain procedures, edge cases, and failure recovery were added where beneficial.
- [ ] Every research source used is recorded with full URL, title, topic grouping, and key takeaways.
- [ ] Research source citations are included in the Pull Request description.

## Gate 7: Best-practices, structure, and description optimization

### Specification status

Refactored skills must conform to official Agent Skills best practices: concise `SKILL.md` entry points, progressive disclosure for detailed or conditional material, explicit reference loading instructions, clear execution order, and a tuned, trigger-optimized `description`. This gate corresponds to Phase 3 of the refactoring workflow.

### Structure and instruction optimization

- Maintain `SKILL.md` as a concise entry point; offload detailed schemas, extended guides, or conditional workflows to `references/`.
- Ensure explicit instructions state *when* and *how* the agent should load each reference file.
- Calibrate instruction prescriptiveness to task fragility, eliminating redundant or generic knowledge the agent already possesses.

### Description optimization

- Follow official guidelines for optimizing skill descriptions.
- Make the `description` concise, imperative, intent-focused, and precise about triggering scope.
- Define both what the skill *does* and when it *should or should not trigger*.
- Test trigger behavior against realistic positive prompts and near-miss negative prompts without overfitting to explicit keywords.

### Gate 7 pass criteria

- [ ] `SKILL.md` remains concise, utilizing progressive disclosure with explicit loading instructions for `references/`.
- [ ] Instructions are intent-focused, calibrated for fragility, and free of generic background fluff.
- [ ] The `description` is concise, imperative, and precisely defines trigger conditions.
- [ ] Trigger scope has been evaluated against positive and near-miss negative prompts.

## Gate 8: Darwin Skill evaluation and test coverage

### Specification status

To ensure quantitative quality and empirical validation, every refactored skill must be evaluated using `/darwin-skill` until it achieves a score of at least 80 without sacrificing correctness, safety, portability, or source fidelity. This gate corresponds to Phase 4 of the refactoring workflow.

### Test prompt inventory (`test-prompts.json`)

Before evaluation, create a `test-prompts.json` file in the skill package root containing 2–3 test prompts written in English:

```json
[
  {"id": 1, "prompt": "typical user request in English", "expected": "expected behavior", "actual": "actual output after running", "pass": true},
  {"id": 2, "prompt": "complex or ambiguous scenario in English", "expected": "expected behavior", "actual": "actual output after running", "pass": true}
]
```

Requirements:
- Prompts must cover the standard happy path and at least one complex/edge-case scenario.
- Prompts must be executed against the skill, and real execution outputs must be recorded in the `actual` field (no placeholders).
- The `pass` boolean field must accurately reflect whether the actual output met expected behavior.

### Darwin evaluation iteration

- Run `/darwin-skill` against the package and review dimension feedback.
- Iterate on instructions based on valid feedback while preserving compliance gates and domain accuracy.
- Achieve a final evaluation score of at least 80/100.

### Gate 8 pass criteria

- [ ] `test-prompts.json` exists in the skill directory containing 2-3 English test prompts (happy path + complex scenario).
- [ ] All test prompts were executed, with real outputs recorded in `actual` and accurate `pass` status.
- [ ] `/darwin-skill` evaluation was executed and achieved a score of at least 80/100.
- [ ] No regression occurred in specification compliance, safety, portability, or source fidelity to boost scores.

## Gate 9: Freud cognitive load and white bear effect audit

### Specification status

Evaluation mechanisms (like Darwin) may encourage intrusive stop markers (`🔴 STOP`, `🛑 CHECKPOINT`) that trigger white bear effects—occupying the agent's working memory with prohibition checks ("should I stop?") rather than execution ("how do I proceed?"). This gate applies `/freud-skill` Diagnostic Optimization (Mode 2) to eliminate white bear effects and manage cognitive load, corresponding to Phase 5 of the refactoring workflow.

### Applicable Freud lenses

Scan the skill using the 4 skill-appropriate lenses:
- **Lens 2: Positive vs Negative**: Rephrase prohibitions ("don't", "never", "avoid") into positive definitions ("do Y instead", "verify X before proceeding").
- **Lens 3: Consistency**: Resolve conflicting or ambiguous instructions.
- **Lens 4: Anchoring precision**: Replace vague advice with concrete decision heuristics and mental models.
- **Lens 6: Working space hygiene**: Ensure critical instructions are clearly positioned and total working memory concepts remain within limits (<= 25 concepts).

*(Lenses 1 and 5 are skipped as they apply to personas, not skill packages).*

### Gate 9 pass criteria

- [ ] `/freud-skill` Mode 2 diagnostic optimization was performed across Lenses 2, 3, 4, and 6.
- [ ] Prohibition statements ("don't", "never") were converted into positive execution definitions.
- [ ] Visual stop markers (`🔴 STOP`, `🛑 CHECKPOINT`) causing white bear effects were removed or rephrased positively.
- [ ] Critical instructions are prominently structured and concept load stays under cognitive thresholds (<= 25 concepts).
- [ ] Re-ran reference validator to ensure Freud corrections did not break any Gate 1-5 compliance rules.

## Common pitfalls

### `age` encryption passphrase mode

`age -p` requires a TTY for interactive passphrase input. In non-interactive contexts (subprocess, kanban worker, cron script), use `age -r <pubkey>` with a keyfile instead:

```bash
# Encrypt
age -r <pubkey> -o output.age < input

# Decrypt
age -d -i keyfile -o - output.age
```

### `metadata.openclaw` format

`metadata.openclaw` must be a JSON **string** in YAML, not a nested YAML object. Example:

```yaml
metadata:
  openclaw: '{"emoji":"🔐"}'
```

Do not write:

```yaml
metadata:
  openclaw:
    emoji: 🔐
```

### Gitea reviewer assignment

`tea pulls edit --add-reviewers` silently fails even when the command appears successful. Use the REST API or `@mention` comment as fallback:

```bash
# REST API method
TOKEN=$(grep -A5 '<login-name>' ~/.config/tea/config.yml | grep token | awk '{print $3}')
curl -s -X POST "https://<host>/api/v1/repos/<owner>/<repo>/pulls/<number>/requested_reviewers" \
  -H "Authorization: token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"reviewers":["<username>"]}'

# Or @mention comment
tea comments add <PR-number> --repo <owner/repo> --login <account> -d "@<reviewer> please review, thank you!"
```

**CRITICAL**: The reviewer must NOT be the PR author. Gitea returns HTTP 422 if you try to assign the PR author as their own reviewer. The default reviewer is `ani6439walc` (not `wei840222`, who is the PR author).

## Current scope of this document

"Refactor complete" defines full multi-phase quality compliance across Gates 1 through 9: format compatibility (Gate 1), resource classification (Gate 2), persistent state location (Gate 3), related-skill metadata (Gate 4), removal of promotional content (Gate 5), knowledge research and accuracy (Gate 6), best-practices and description optimization (Gate 7), Darwin evaluation and test coverage (Gate 8), and Freud cognitive load audit (Gate 9). A skill refactor is complete and ready for pull request merge only when every applicable gate passes.
