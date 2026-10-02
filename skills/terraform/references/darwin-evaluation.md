# Darwin evaluation (Gate 8)

**Evaluation date:** 2026-10-03
**Package:** `skills/terraform`
**Final score:** **84 / 100** (threshold ≥ 80)
**Method:** Structural dry-run over final `SKILL.md`, `references/*`, `references/sources.md`, and three recorded full_test `actual` strings in `test-prompts.json`. No live `terraform apply`, backend mutation, or cloud credentials during scoring.

## Dimension scores

| Dimension | Score | Notes |
|---|---:|---|
| Frontmatter quality | 6.5/7 | Imperative + trigger-rich description; negative scope; `metadata.version` string; related-skills to existing slugs; openclaw emoji JSON |
| Workflow clarity | 10/12 | Quick reference → core rules → plan triage → deeper references; apply only after saved-plan review |
| Failure mode encoding | 10/12 | Permanent diff, locks, cycles, inconsistent apply, stale plan, lost state, provider majors covered |
| Checkpoint design | 5.5/6 | destroy_gate, saved-plan contract, explicit confirmation for force-unlock/state surgery |
| Executable specificity | 15/18 | Concrete version floors, commands, jq destroy counter, backend/partial-config patterns |
| Resource integration | 4/4 | references/ + assets/memory-template + sources loaded on demand |
| Overall architecture | 10/12 | Portable `<state_root>`, clawic/`_meta` removed, progressive disclosure |
| Measured performance | 19/23 | Three full_test actuals align with expected AWS-split, inconsistent-apply, and moved-block guidance |
| Counter-examples and blacklists | 4/6 | Traps table + near-miss routing to aws/ansible/cloud-choice skills |
| **Total** | **84/100** | pass |

## Full-test provenance

Executed as skill-conditioned answers against the repaired package text:

1. S3 inline args review — AWS provider split resources + plan discipline.
2. Inconsistent result after apply — diagnose attribute mismatch; no reckless state surgery.
3. Module rename destroy plan — `moved` blocks and zero-diff success criteria.

All three `pass: true` with expected/actual alignment in `test-prompts.json`.

## Iteration notes

- Jules patch supplied Gates 1–5 layout and Freud-oriented rewrites but left empty Related/Feedback sections, a broken OpenTofu divergence sentence, and only two thin tests without sources/Darwin artifacts.
- This pass fixed wording defects, added official source URLs, expanded tests to three evidenced scenarios, and recorded an 84/100 structural score ≥ 80.
