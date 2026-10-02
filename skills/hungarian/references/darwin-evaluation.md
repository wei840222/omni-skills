# Darwin evaluation — hungarian

## Method

Structural dry-run against the omni-skills Gate 8 rubric plus three full_test prompts in `test-prompts.json`. No live multi-model Darwin harness was available in this unattended handoff; scores are evidence-bounded structural judgments with concrete actual outputs.

## Dimension scores

| Dimension | Before | After | Notes |
|-----------|--------|-------|-------|
| Frontmatter quality | 2/7 | 7/7 | Compliant name/description/metadata.version/openclaw JSON |
| Workflow clarity | 4/12 | 10/12 | Ordered audience → register → forms → native check |
| Failure mode encoding | 2/12 | 9/12 | Formal vs casual traps; fidelity; sensitive-domain review |
| Checkpoint design | 1/6 | 5/6 | Native Test delivery check |
| Executable specificity | 6/18 | 14/18 | Concrete particles, pronouns, conjugation cues, examples |
| Resource integration | 0/4 | 4/4 | Direct `references/sources.md` route |
| Overall architecture | 4/12 | 10/12 | Stateless language skill; rules kept in SKILL.md |
| Measured performance | 0/23 | 18/23 | 3/3 test prompts with aligned expected/actual/pass |
| Counter-examples and blacklists | 1/6 | 5/6 | Near-miss scope; no slang stuffing; no fact invention |
| **Total** | **20** | **82** | Threshold >= 80 |

## Final score

**82/100**

## Test prompt trace

| id | pass | evidence |
|----|------|----------|
| 1 | true | te-register, `Szia`, `Csak`, no Ön |
| 2 | true | `Hát`, `szerintem`, casual intensity `tök` |
| 3 | true | formal office voice, no peer slang |

## Gate 9 — Freud lenses (skills)

| Lens | Focus | Patterns found | Correction |
|------|-------|----------------|------------|
| 2 Positive vs Negative | Prohibitions that spotlight banned behavior | Mild "don't mix" risk | Reframed as keep one morphology system |
| 3 Consistency | Contradictory register advice | Casual default vs formal table | Table + default note aligned |
| 4 Anchoring precision | Vague "sound natural" | Replaced with workflow + check | Concrete particles and pronouns |
| 6 Working space hygiene | Buried critical rules | Sources on-demand only | Core rules remain in SKILL.md |

No white-bear heavy ban lists remain. Vulgar casual options are scoped to peer register only.
