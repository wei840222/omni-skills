---
name: vibe-research
description: >
  Run human-directed, AI-led research cycles: gap finding, literature
  synthesis, hypothesis generation, analysis design, execution logging, and
  cited write-up. Use when the human sets the research question and success
  criteria while the agent owns scanning, drafting protocols, and synthesis.
  Prefer `in-depth-research` for exhaustive multi-source investigation with
  halt criteria, `synthesize` when documents are already provided, `literature`
  for literary-text analysis, and `market-research` / `competitor-research`
  for TAM or rivalry audits.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔬"}'
  related-skills: '{"competitor-research":"Competitor audits and positioning when the ask is market rivalry rather than open-ended scientific inquiry.","digest":"Recurring curated monitoring instead of a one-shot research cycle.","in-depth-research":"Exhaustive multi-source investigation with explicit halt criteria when the ask is depth-first answering rather than hypothesis-led cycles.","literature":"Literary close reading and critical essays instead of empirical research pipelines.","market-research":"TAM/SAM/SOM, segmentation, and demand validation before build-or-enter decisions.","multi-engine-web-search":"Cross-engine discovery and filters before committing to a full vibe-research cycle.","synthesize":"Reconcile user-provided documents without opening a fresh external research loop."}'
---

This skill is stateless. It does not store local configuration or persistent user research state.

## Role

**Vibe research** means the human directs the question, constraints, and acceptance bar; the agent leads literature synthesis, hypothesis drafting, analysis design, execution logging, and cited synthesis. Traditional research stays human-executed. Deep research (`in-depth-research`) prioritizes exhaustive answering with halt criteria. This skill prioritizes an explicit multi-phase cycle with human checkpoints before high-stakes claims ship.

## Workflow

1. Capture the human's question, domain constraints, depth budget, and success criteria.
2. Load only the reference needed for the current phase.
3. Produce the phase artifact (gap map, synthesis, hypotheses, protocol, or report) with citations and confidence tags.
4. Pause for human validation on methodology and load-bearing findings before irreversible publication or high-stakes advice.
5. Log steps for reproducibility; escalate when evidence conflicts, ethics apply, or domain expertise is required.

## Load the relevant reference

| Reference | Load when |
| --- | --- |
| `references/pipeline.md` | Running gap identification through synthesis phases or choosing an output shape. |
| `references/risks.md` | Mitigating hallucination, bias, rigor loss, skill erosion, or integrity risk; deciding when to escalate. |

## Critical rules

1. **Human vision, agent execution** — do not silently change the research question or success criteria.
2. **Cite or mark inference** — every factual claim needs a source; mark model inference separately.
3. **Triangulate load-bearing facts** — prefer 3+ independent sources; check circular citation.
4. **Confidence tags** — label high / medium / low; say when evidence is thin.
5. **Human validates key findings** — especially before publication, policy, medical, legal, or financial stakes.
6. **Disclose AI involvement** — final accountability stays with the human author of record.
7. **Route adjacent asks** — user-supplied docs → `synthesize`; rivalry/TAM → market/competitor skills; literary text → `literature`.
