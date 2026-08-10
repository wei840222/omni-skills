# Pull Request Review Templates

Use these templates when submitting a Skill Review on GitHub. Replace all placeholder text with evidence from the review. Keep the review in English unless the PR discussion is already localized and the user asks otherwise.

Canonical procedure, severity rubric, three-lens quality bar, and Oracle-style craft rules live in `docs/review-guide.md`. Author-side PR descriptions use `docs/pull-request-template.md`.

## Craft rules for every review body

- **Bottom line first.** Verdict, then 2–3 sentences. No filler openings.
- **One clear path.** Each Required item gets exactly one recommended fix.
- **Actionable.** Required items use Current → Evidence → Fix.
- **Evidence anchors.** Cite path, section, quoted instruction, commit SHA, or validator output.
- **Effort tags.** `Quick` (<1h) / `Short` (1–4h) / `Medium` (1–2d) / `Large` (3d+).
- **Confidence tags.** Add `high` / `medium` / `low` when the judgment is not high-confidence.
- **Stop at working-well.** Optional ≤3, Nit ≤3 unless exhaustive notes were requested.

Submit through `gh`:

```bash
# Request changes
gh pr review <n> --request-changes --body-file /tmp/pr-review.md --repo wei840222/omni-skills

# Approve
gh pr review <n> --approve --body-file /tmp/pr-review.md --repo wei840222/omni-skills

# Comment only
gh pr comment <n> --body-file /tmp/pr-review.md --repo wei840222/omni-skills
```

---

## Template A — Request changes

```markdown
## Review: <short title> — request changes

Reviewed with **code-review-and-quality** + **writing-for-agents** + **darwin-skill** (structural / dry-run).

### Bottom line
<2-3 sentences: overall direction, why blocked, what must change.>

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
   - Evidence: <command, docs, quoted text, or observed behavior>
   - Fix: <single concrete replacement or acceptance criteria>
   - Effort: <Quick|Short|Medium|Large>
   - Confidence: <high|medium|low>

2. **<title>** (`<section or file>`)
   - Current: ...
   - Evidence: ...
   - Fix: ...
   - Effort: ...
   - Confidence: ...

### Optional / Consider
<!-- max 3 -->
3. **Consider: <title>** — Effort: <Quick|Short|Medium|Large>
   - <non-blocking guidance; one preferred path>

### Nit
<!-- max 3 -->
- <tiny cleanup>

### What looks solid
- <keep momentum; list real strengths>

### Axis snapshot
| Axis | Notes |
|---|---|
| Correctness | <pass / blocked by ...> |
| writing-for-agents | <notes> |
| darwin (structural) | <notes; no fake precision score required> |
| Gates 1–9 | <pass list / fail list> |

After the Required items are fixed, this should be a straightforward approve.
```

---

## Template B — Approve

```markdown
## Review: <short title> — approve

Reviewed with **code-review-and-quality** + **writing-for-agents** + **darwin-skill** (structural / dry-run).

### Bottom line
<2-3 sentences: why this is safe to merge now.>

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
<!-- max 3 optional follow-ups -->
- <optional follow-up> — Effort: <Quick|Short|Medium|Large>

Merging as authorized.
```

---

## Template C — Re-review approve after fixes

```markdown
## Re-review: <short title> — approve

### Bottom line
Previous Required items are fixed; safe to merge.

Delta reviewed at `<short-sha>` (`<fix-commit subject>`).

### Previous Required items
1. <item> → **Fixed** — <one-line evidence>
2. <item> → **Fixed** — <one-line evidence>

### Recheck
- Gate 1: `uvx --from skills-ref agentskills validate skills/<slug>` → **Valid**
- No new Required findings in the delta

**Approve** and merge.
```

---

## Template D — Re-review still blocked

```markdown
## Re-review: <short title> — request changes

### Bottom line
<1-2 sentences on what remains blocking.>

Delta reviewed at `<short-sha>`.

### Previous Required items
1. <item> → **Fixed** — <evidence>
2. <item> → **Still open** — <what remains wrong>
   - Fix: <single remaining path>
   - Effort: <Quick|Short|Medium|Large>
   - Confidence: <high|medium|low>
3. <new item if introduced> → **New Required** — <fix>
   - Current: ...
   - Evidence: ...
   - Fix: ...
   - Effort: ...
   - Confidence: ...

### Verdict
**Request changes** — remaining Required item(s) must land before merge.
```

---

## Template E — Comment only (clarification)

```markdown
## Review note on PR #<n>

### Bottom line
Need clarification before a full verdict.

1. <question about intent/scope>
2. <question about claimed gate evidence>

No approve/reject yet.
```
