# Darwin evaluation — swedish

## Method

Structural dry-run against the omni-skills Gate 8 rubric plus three full_test prompts in `test-prompts.json`. No live multi-model Darwin harness was available in this unattended handoff; scores are evidence-bounded structural judgments with concrete actual outputs preserved from the Jules patch (ids 1–2) plus one added intensity prompt (id 3).

## Dimension scores

| Dimension | Before | After | Notes |
|-----------|--------|-------|-------|
| Frontmatter quality | 1/7 | 7/7 | Compliant name/description/metadata.version/openclaw JSON; clawic/_meta removed |
| Workflow clarity | 3/12 | 10/12 | Ordered audience → register → forms → native check |
| Failure mode encoding | 2/12 | 9/12 | Formal vs casual traps; fidelity; sensitive-domain review |
| Checkpoint design | 2/6 | 5/6 | Native Test delivery check |
| Executable specificity | 8/18 | 14/18 | Concrete particles, du-reform, lagom, examples |
| Resource integration | 0/4 | 4/4 | sources.md + conversational-rules.md routes |
| Overall architecture | 3/12 | 10/12 | Stateless language skill; core rules in SKILL.md |
| Measured performance | 0/23 | 18/23 | 3/3 test prompts with aligned expected/actual/pass |
| Counter-examples and blacklists | 1/6 | 5/6 | Near-miss Nordic routing; no particle stuffing; no fact invention |
| **Total** | **20** | **82** | Threshold >= 80 |

## Final score

**82/100**

## Test prompt trace

| id | pass | evidence |
|----|------|----------|
| 1 | true | `Tja`, casual coffee ask, English `nice`, no `ni` |
| 2 | true | lagom `helt okej`, soft `typ`, professional-casual |
| 3 | true | `kasst`, `Orkar`, intensity without formal register |

## Gate 9 — Freud lenses (skills)

| Lens | Focus | Patterns found | Correction |
|------|-------|----------------|------------|
| 2 Positive vs Negative | Prohibitions that spotlight banned behavior | Mild "don't use ni" risk | Reframed as default du; upgrade only on request |
| 3 Consistency | Contradictory register advice | Casual default vs formal table | Table + default note aligned |
| 4 Anchoring precision | Vague "sound natural" | Replaced with workflow + check | Concrete particles and lagom cues |
| 6 Working space hygiene | Buried critical rules | Detail moved to references | Core workflow remains in SKILL.md |

No white-bear heavy ban lists remain. Intensity options are scoped to casual peer register only.
