# Pull Request Review Templates

Use these templates when submitting a Skill Review on Gitea. Replace all placeholder text with evidence from the review. Keep the review in English unless the PR discussion is already localized and the user asks otherwise.

Canonical procedure, severity rubric, and three-lens quality bar live in `docs/review-guide.md`. Author-side PR descriptions use `docs/pull-request-template.md`.

Submit through `tea`:

```bash
# Request changes
tea pulls reject <n> "$(cat /tmp/pr-review.md)" --repo wei840222/clawic-skills

# Approve
tea pulls approve <n> "$(cat /tmp/pr-review.md)" --repo wei840222/clawic-skills

# Comment only
tea comments add <n> --description "$(cat /tmp/pr-review.md)" --repo wei840222/clawic-skills
```

---

## Template A — Request changes

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

---

## Template B — Approve

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

---

## Template C — Re-review approve after fixes

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

---

## Template D — Re-review still blocked

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

---

## Template E — Comment only (clarification)

```markdown
## Review note on PR #<n>

Need clarification before a full verdict:

1. <question about intent/scope>
2. <question about claimed gate evidence>

No approve/reject yet.
```
