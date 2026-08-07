# Skill Review Guide

This document defines the canonical **Skill Review** procedure for open Gitea pull requests in `clawic-skills`. It is the review counterpart to `docs/refactor-guide.md`: refactor authors prove Gates 1–9; reviewers verify those gates **and** apply three quality lenses before approving or requesting changes.

## Core principles

- Review against evidence: PR branch, full diff, commit history, validator output, and skill package contents. Do not approve from the PR description alone.
- Required findings block merge. Optional findings do not.
- Request changes by leaving a concrete review on the PR. Do not only summarize in chat.
- Approve only when required gates and required findings are clean; then merge when the task authorizes merge.
- Prefer actionable fixes over style preferences. Approve when the change clearly improves overall skill health, even if optional nits remain.

## Required review skills

Always load and apply these three skills before issuing a verdict:

| Skill | Role in this review |
|---|---|
| `code-review-and-quality` | Correctness, readability, architecture fit, security, and performance axes. Prefer required vs optional severity. |
| `writing-great-skills` | Skill craft: description triggers, progressive disclosure, failure modes, anti-patterns, concrete commands, and information hierarchy. |
| `darwin-skill` | Structural / dry-run evaluation of workflow clarity, checkpoints, failure recovery, specificity, and blacklist quality. Use absolute score only as secondary signal; do not keep/revert solely on a claimed score. |

Also load operational helpers as needed:

| Skill | When |
|---|---|
| `gitea` | Checkout, comment, approve, reject, merge on Gitea. |
| `git-master` | Local branch inspection, atomic history checks, safe push/merge hygiene. |

## Sources of truth during review

Use this precedence order:

1. Current user instructions for the review task (for example: request changes must comment; approve must merge).
2. Official Agent Skills specification + reference validator behavior.
3. `docs/refactor-guide.md` Gates 1–9 and commit-phase contract.
4. This guide’s three-lens review and comment templates.
5. Target skill package files and verified runtime/tool evidence.
6. Existing repository conventions, only when they do not conflict with the sources above.

---

## Review Workflow Lifecycle

```text
Step 0 Identity → Step 1 Fetch PR → Step 2 History/Diff → Step 3 Automated checks
→ Step 4 Gates 1–9 → Step 5 Three-lens quality review → Step 6 Verdict & Gitea action
→ (if updated) Step 7 Re-review
```

### Step 0: Reviewer identity

```bash
tea whoami
# Expected for Ani reviews: ani6439walc
```

If the active Gitea login is not the reviewer account, switch before any approve/reject/merge action.

### Step 1: Locate and fetch the PR

Default repository: `wei840222/clawic-skills` on Gitea.

```bash
tea pulls <n> --repo wei840222/clawic-skills
tea pulls checkout <n> --repo wei840222/clawic-skills
# or clean clone + fetch head branch when the working tree is dirty
```

Capture:

- PR number, title, author, base (`local`), head branch
- mergeability / conflicts
- current review state (`OPEN`, `APPROVED`, `REQUEST_CHANGES`)
- linked skill slug(s) from paths under `skills/<slug>/`

### Step 2: Commit history and diff audit

```bash
git fetch origin local <head-branch>
git log --oneline origin/local..<head>
git diff --stat origin/local...<head>
git diff origin/local...<head>
```

Check:

1. **Phase commits present and ordered** for a full refactor PR:
   `refactor` → `research` → `optimize` → `darwin` → `freud`
2. Follow-up fix commits after review are allowed (`fix(<slug>): ...`) and expected during re-review.
3. Diff scope is limited to the intended skill package plus authorized docs. Flag unrelated files.
4. Deleted files (`_meta.json`, clawic homepage refs, etc.) match Gate 5 / project policy, not accidental removal of needed resources.

### Step 3: Automated validation

From the checked-out PR head:

```bash
uvx --from skills-ref agentskills validate skills/<slug>
git diff --check origin/local...<head>
```

Also verify manually:

- Relative paths in `SKILL.md` resolve inside the package
- No secrets, private keys, tokens, or live credentials
- No remaining `clawic.com` promotional/feedback references when Gate 5 applies
- `metadata.related-skills` JSON (if present) parses and target slugs exist
- State guidance uses portable `<state_root>` resolution when the skill persists state

Gate 1 fails if the validator does not exit 0.

### Step 4: Gates 1–9 verification

Cross-check the PR description and package against `docs/refactor-guide.md`.

| Gate | Reviewer checks |
|---|---|
| 1 Spec compatibility | Validator clean; `name` lowercase and matches directory; only allowed top-level frontmatter fields; `metadata` string-to-string compatible project pattern |
| 2 Resource dirs | Supporting files live under `references/`, `scripts/`, `assets/` as appropriate; links are relative and real |
| 3 State location | Knowledge-only skills state non-persistence; stateful skills document `<state_root>` resolution outside the package |
| 4 Related skills | `metadata.related-skills` valid JSON map; targets exist; no fabricated relationships |
| 5 Clawic removal | No `clawic.com` homepage/feedback promo; `_meta.json` removed when that is project policy |
| 6 Research | PR lists verifiable full URLs grouped by topic; claims in the skill match cited guidance |
| 7 Best practices | Progressive disclosure; description is imperative and trigger-rich; always-needed content stays in `SKILL.md` |
| 8 Darwin + tests | `test-prompts.json` present when claimed; prefer real `actual` + `pass: true` for completed Darwin work; claimed score is not a substitute for structural quality |
| 9 Freud | Prohibitions reframed positively where required; no disruptive stop-only markers that increase cognitive load without a recovery path |

Record each failed gate with severity:

- **Required**: blocks approve/merge
- **Optional / Consider**: non-blocking guidance
- **Nit**: tiny cleanup, never blocking alone

### Step 5: Three-lens quality review

Apply the three required skills as independent lenses. A finding may appear in more than one lens; report it once under the strongest severity.

#### Lens A — `code-review-and-quality`

Review the skill as an executable instruction surface:

1. **Correctness**
   - Commands, APIs, flags, and recovery steps must be real.
   - Invented syntax is an automatic Required finding (example: non-existent `ALTER TABLE ... CANCEL`).
   - Platform claims need version/context when behavior differs.
2. **Readability**
   - Sections are scannable; critical path is obvious.
   - Examples are minimal and copy-pasteable.
3. **Architecture / fit**
   - Matches refactor patterns used by recently merged skills.
   - Overlap with sibling skills is handled via `related-skills` or clear scope boundaries.
4. **Security**
   - No secret leakage; OIDC/permissions/supply-chain guidance must not mix unrelated controls.
   - Dangerous operations require explicit confirmation language when appropriate.
5. **Performance**
   - Avoid instructions that force unnecessary full-context loads or unbounded scans when progressive disclosure is available.

Severity rule of thumb from this lens:

- Wrong command / unsafe default / broken path → **Required**
- Missing related-skill pointer / mild sprawl → **Optional**
- Wording polish → **Nit**

#### Lens B — `writing-great-skills`

Review the package as a model-facing skill:

1. **Description quality**
   - Starts with what the skill does.
   - Includes trigger terms and “use when” situations.
   - Avoids vague filler and pure capability lists.
2. **Information hierarchy**
   - Default workflow and checkpoints appear before deep reference material.
   - Rare platform detail can move to `references/`.
3. **Failure modes**
   - Prefer if-then recovery branches over “be careful” advice.
4. **Anti-patterns**
   - Gotchas / Common Mistakes / explicit don’t-do-this lists are present when the domain has footguns.
5. **Specificity**
   - Concrete tools, thresholds, and commands beat abstract slogans.
6. **Sprawl control**
   - Large always-loaded `SKILL.md` without progressive disclosure is a Consider finding, not always Required.

#### Lens C — `darwin-skill` (structural / dry-run)

Do **not** invent a floating total score as the merge decision. Evaluate structure:

| Darwin focus | Pass signal |
|---|---|
| Workflow clarity | Ordered path or unmistakable decision tree for the main job |
| Failure encoding | Explicit recovery branches for common breakages |
| Checkpoints | Visual or imperative stop/verify points before irreversible actions |
| Actionable specificity | Real commands/examples an agent can execute |
| Blacklist / anti-patterns | Concrete mistakes called out |
| Resource integration | `references/`, scripts, or self-contained guidance that loads on demand |

Use claimed Darwin scores in the PR only as author evidence. Reviewer judgment comes from the package itself.

### Step 6: Verdict and Gitea action

Choose exactly one primary outcome:

| Outcome | Condition | Gitea action |
|---|---|---|
| **Approve** | Validator clean, required gates pass, no Required findings | `tea pulls approve <n> "<body>"` then merge if authorized |
| **Request changes** | Any Required finding, missing phase evidence when required, or broken validator | `tea pulls reject <n> "<body>"` |
| **Comment only** | Need clarification without blocking, or partial note while waiting on author | `tea comments add <n> --description "<body>"` |

Default authorization for this repository’s review tasks:

- Request changes → post the reject review immediately.
- Approve → approve and merge immediately unless the user says review-only.
- Prefer squash merge for refactor PRs unless the user specifies otherwise:

```bash
tea pulls approve <n> "$(cat /tmp/pr-review-approve.md)" --repo wei840222/clawic-skills
tea pulls merge <n> --style squash --repo wei840222/clawic-skills
```

```bash
tea pulls reject <n> "$(cat /tmp/pr-review-request-changes.md)" --repo wei840222/clawic-skills
```

### Step 7: Re-review after author updates

When the author says the review findings are fixed:

1. Fetch the updated head commit.
2. Inspect only the delta since the previous review commit first, then spot-check full package integrity.
3. Re-run validator.
4. Confirm each previous Required item is actually fixed (not merely mentioned).
5. Approve + merge if clean; otherwise reject again with a short delta-focused review.

---

## Decision rubric

### Approve when all are true

- `agentskills validate` exits 0
- No Required findings from Gates 1–9 or the three lenses
- Diff scope is intentional
- For full refactor PRs: phase history is acceptable (exact five-phase set, or clearly equivalent with explained deviation plus fixup commits)
- Skill is net safer/clearer than base

### Request changes when any are true

- Validator fails
- Factual/instructional error that would make an agent run a wrong or unsafe command
- Gate 5 leftovers (`clawic.com` promo) on a compliance refactor
- Claimed state/path contracts are inconsistent or package-writable by default
- Security guidance mixes unrelated controls in a way that teaches the wrong fix
- Missing critical recovery path for a dangerous operation the skill encourages

### Do not block only for

- Optional `related-skills` suggestions
- Progressive-disclosure tidy-ups under a still-readable size
- Darwin score numerology without structural failure
- Pure prose style preferences
- Empty `actual` / `pass: false` harness residue when house style still treats Darwin as in-progress **and** the skill body itself is structurally sound — prefer Optional unless the PR claims Gate 8 complete

---

## PR review comment templates

Copy a template, replace placeholders, and submit through `tea`. Keep the review in English unless the PR discussion is already localized and the user asks otherwise.

### Template A — Request changes

```markdown
## Review: <short title> — request changes

Reviewed with **code-review-and-quality** + **writing-great-skills** + **darwin-skill** (structural / dry-run).

### Context
- Target: `skills/<slug>`
- Head: `<branch>` @ `<short-sha>`
- Diff focus: <1-3 bullets>
- Gate 1: `uvx --from skills-ref agentskills validate skills/<slug>` → **<Valid / FAIL>**

### Verdict
**Request changes** — <N> required fix(es) before merge.

### Required
1. **<title>** (`<section or file>`)
   - Current: <what is wrong>
   - Evidence: <command, docs, or observed behavior>
   - Fix: <concrete replacement or acceptance criteria>

2. **<title>** (`<section or file>`)
   - ...

### Optional / Consider
3. **Consider: <title>**
   - <non-blocking guidance>

### Nit
- <tiny cleanup>

### What looks solid
- <keep momentum; list real strengths>

### Axis snapshot
| Axis | Notes |
|---|---|
| Correctness | <pass / blocked by ...> |
| writing-great-skills | <notes> |
| darwin (structural) | <notes; no fake precision score required> |
| Gates 1–9 | <pass list / fail list> |

After the Required items are fixed, this should be a straightforward approve.
```

### Template B — Approve

```markdown
## Review: <short title> — approve

Reviewed with **code-review-and-quality** + **writing-great-skills** + **darwin-skill** (structural / dry-run).

### Context
- Target: `skills/<slug>`
- Head: `<branch>` @ `<short-sha>`
- Gate 1: `uvx --from skills-ref agentskills validate skills/<slug>` → **Valid**

### Verdict
**Approve** — no Required findings.

### Verified
- [ ] Commit/diff scope intentional
- [ ] Validator clean
- [ ] Gates 1–5 compliance signals present
- [ ] Gate 6 sources adequate or N/A with reason
- [ ] Gate 7 description / disclosure acceptable
- [ ] Gate 8 structural quality acceptable (tests noted if present)
- [ ] Gate 9 no blocking white-bear / load issues
- [ ] Three-lens review: no wrong commands, unsafe defaults, or broken recoveries

### Notes (non-blocking)
- <optional follow-ups, if any>

Merging as authorized.
```

### Template C — Re-review approve after fixes

```markdown
## Re-review: <short title> — approve

Delta reviewed at `<short-sha>` (`<fix-commit subject>`).

### Previous Required items
1. <item> → **Fixed** — <one-line evidence>
2. <item> → **Fixed** — <one-line evidence>

### Recheck
- Gate 1: `uvx --from skills-ref agentskills validate skills/<slug>` → **Valid**
- No new Required findings in the delta

**Approve** and merge.
```

### Template D — Re-review still blocked

```markdown
## Re-review: <short title> — request changes

Delta reviewed at `<short-sha>`.

### Previous Required items
1. <item> → **Fixed** — <evidence>
2. <item> → **Still open** — <what remains wrong>
3. <new item if introduced> → **New Required** — <fix>

### Verdict
**Request changes** — remaining Required item(s) must land before merge.
```

### Template E — Comment only (clarification)

```markdown
## Review note on PR #<n>

Need clarification before a full verdict:

1. <question about intent/scope>
2. <question about claimed gate evidence>

No approve/reject yet.
```

---

## Worked example patterns (from real reviews)

These are recurring Required classes. Treat them as calibrated examples, not an exhaustive catalog.

### Wrong recoverable command

- Symptom: recovery snippet uses non-existent tool syntax.
- Lens: `code-review-and-quality` correctness + `darwin-skill` failure encoding.
- Severity: **Required**
- Fix pattern: replace with verified commands and keep the if-then branch.

### Mixed security controls

- Symptom: OIDC expiry guidance tells the agent to change unrelated `actions/checkout` credential persistence.
- Lens: correctness + security.
- Severity: **Required**
- Fix pattern: keep controls inside the failing subsystem (re-auth / shorter job / fresh job token).

### Validator-invalid frontmatter

- Symptom: uppercase `name`, top-level `homepage`/`slug`, nested non-string metadata rejected by project pattern.
- Lens: Gate 1 / Gate 5.
- Severity: **Required**

### Optional sprawl

- Symptom: useful but rarely needed platform essays inflate always-loaded `SKILL.md`.
- Lens: `writing-great-skills` progressive disclosure.
- Severity: **Optional** unless the file is so large it crowds out the critical path.

---

## Reviewer checklist (copy into working notes)

```text
[ ] tea whoami is the intended reviewer
[ ] PR metadata + head SHA recorded
[ ] git log phase/fix history inspected
[ ] full diff read (not only stat)
[ ] agentskills validate clean
[ ] git diff --check clean
[ ] Gates 1–9 checked against refactor-guide.md
[ ] code-review-and-quality lens done
[ ] writing-great-skills lens done
[ ] darwin-skill structural lens done
[ ] findings split Required / Optional / Nit
[ ] Gitea review posted with template
[ ] merge performed only when approved and authorized
[ ] re-review verifies each prior Required item with evidence
```

## Relationship to other docs

| Doc | Owns |
|---|---|
| `AGENTS.md` | Workflow dispatch and stable operating principles |
| `docs/refactor-guide.md` | Author-side Gates 1–9 and refactor commit contract |
| `docs/pull-request-template.md` | Author-side PR description evidence layout |
| `docs/review-guide.md` | Reviewer-side procedure, three-lens quality bar, and review comment templates |

When a reusable review anti-pattern appears twice, add a narrow section here rather than expanding `AGENTS.md`.
