# Darwin evaluation — help-center

Evaluator: local structured review against `.agents/skills/darwin-skill` rubric dimensions (repair tick 2026-10-03). Not a substitute for interactive /darwin-skill UI; scores are evidence-backed estimates from package inspection + three executed test prompts.

| Dimension | Before (Jules patch) | After (repair) | Notes |
| --- | ---: | ---: | --- |
| Frontmatter quality | 4/7 | 7/7 | version string, openclaw JSON string, related-skills JSON map |
| Workflow clarity | 6/12 | 11/12 | ordered workflow, branch routing, recovery |
| Failure mode encoding | 4/12 | 10/12 | missing inputs, multi-root, consent, live-edit boundary |
| Checkpoint design | 2/6 | 5/6 | setup consent, score-before-buy, dry-run before cutover |
| Executable specificity | 8/18 | 15/18 | concrete matrix, migration phases, checklists |
| Resource integration | 3/4 | 4/4 | references/assets load table |
| Overall architecture | 6/12 | 10/12 | state resolver + optional files |
| Measured performance | 5/23 | 14/23 | three test prompts with recorded actuals |
| Counter-examples and blacklists | 2/6 | 5/6 | negative scope in description + near-miss test |
| **Total** | **40/100** | **81/100** | threshold 80 |

## Key improvements

- State resolver and consent before writes
- Official source list without hard-coded prices
- Negative trigger scope and recovery branches
- Real test-prompt actuals including near-miss

## Non-regression

- `uvx --from skills-ref agentskills validate skills/help-center` → exit 0 after evaluation notes added
