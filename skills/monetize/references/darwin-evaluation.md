# Darwin Evaluation — Gate 8

Evaluated 2026-08-21 against the nine-dimension rubric in `.agents/skills/darwin-skill/SKILL.md`. Test execution records are retained in `../test-prompts.json`; three English scenarios were executed as decision-packet dry runs against the refactored skill and met their expected behavior (3/3 pass).

| Dimension | Weight | Rating /10 | Weighted score | Evidence |
|---|---:|---:|---:|---|
| Frontmatter quality | 7 | 9 | 6.3 | Trigger-focused capability and boundary in `SKILL.md` frontmatter. |
| Workflow clarity | 12 | 9 | 10.8 | Five ordered steps and a concrete output format. |
| Failure mode encoding | 12 | 9 | 10.8 | Unknown-input marking, range/policy verification, and guardrail decision path. |
| Checkpoint design | 6 | 8 | 4.8 | Decision inputs, policy check, experiment review, and next measurement date. |
| Executable specificity | 18 | 9 | 16.2 | Formulas, packet schema, metric/guardrail definition, and reference routing. |
| Resource integration | 4 | 10 | 4.0 | Direct, one-level routes to topical references and research record. |
| Overall architecture | 12 | 9 | 10.8 | Concise entry point with progressive disclosure and route boundary. |
| Measured performance | 23 | 9 | 20.7 | Three recorded scenario outputs cover SaaS pricing, mixed-store mobile/sponsorship, and creator-course validation. |
| Counter-examples and blacklists | 6 | 8 | 4.8 | Explicitly distinguishes hypotheses from facts and routes legal/implementation work to specialists. |
| **Total** | **100** |  | **89.2/100** | **Pass (threshold: 80)** |

## Iteration outcome

The score is supported by the retained tests and rubric review. The main instruction was tightened before this evaluation to require explicit unknowns, a single testable offer, one-variable experimentation, customer-impact guardrails, and a structured decision packet. No score-driven change weakened current-policy checks, safety, portability, or source fidelity.
