---
name: fine-tuning
description: Plan, evaluate, and troubleshoot LLM fine-tuning. Use for training-data preparation, provider/model selection, cost estimates, training failures, and privacy review; compare prompting and retrieval before recommending a training job.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎛️"}'
---

## Execution

1. Identify the observed task failure, current prompt/retrieval baseline, labeled examples, expected inference volume, budget, and data residency. If the task is missing current knowledge, test retrieval first; if examples are scarce, improve prompting and collect evidence before training.
2. Select task metrics and a held-out evaluation split before touching training data. Deduplicate and inspect representative examples; keep test items isolated from generation, tuning, and model selection. Read `references/data-prep.md` and `references/evaluation.md` for formats and checks.
3. Compare only providers and models that currently support the required tuning method and region. Read `references/providers.md` and verify the exact model ID, eligibility, modality, quota, and pricing against the vendor account and linked primary documentation before quoting a rate. Estimate training, serving, data preparation, evaluation, and retraining using measured tokens and traffic; read `references/costs.md`.
4. Check permission to use each training example, personal-data minimization, storage location, retention, and deletion obligations. Read `references/compliance.md`; escalate ambiguous legal or data-transfer decisions to the accountable owner.
5. Choose a documented training method and parameter range for the actual model and SDK. Read `references/training.md`. **Authorization checkpoint:** name the exact dataset, provider/account, spend ceiling, and deployment target; obtain the approvals required for data upload, paid training, and deployment. Without them, deliver a plan and runnable local checks only.
6. Compare the candidate with base and few-shot baselines on the same held-out cases; segment errors and measure cost per accepted output. If it underperforms or regresses safety/privacy, keep the baseline and diagnose data, settings, and distribution before another run. Report measured results, unverified claims, and remaining limitations.

## Operational rules

- Match data format and example counts to the selected provider/model; historical numbers are not universal minimums. Human-review a representative sample, check contradictory labels, and record train/validation/test provenance. For a small dataset, retain enough independent holdout cases for a meaningful uncertainty estimate before approving tuning.
- Use a baseline on the same held-out set to decide whether tuning improves the target task. Select LoRA/QLoRA or full tuning from model support, hardware and evaluation results rather than a blanket cost multiplier.
- Treat learning rates, epochs, train/serve precision, and hardware requirements as model- and implementation-specific; start from current vendor documentation and validate on a small run.
- Treat fine-tuning as behavior adaptation, not guaranteed factual knowledge refresh. For changing facts, measure retrieval against tuning; for cost savings, calculate break-even from current rates and observed token distributions.
- Protect source data: obtain legal/security review when required, keep credentials out of datasets and logs, and avoid sending private examples to a third party without authorization.

## Risk → action

| Risk | Action |
|------|--------|
| Stale pricing or retired model IDs | Verify current vendor catalog and dated price page for the target account; mark unavailable figures unknown. |
| An example leaks into the held-out set | Deduplicate by source/group and rebuild the split before scoring. |
| Loss oscillates or diverges | Check formatting and scale, then trial a lower learning rate with a measured validation curve. |
| Training loss improves but real-task accuracy falls | Segment held-out failures and compare to baseline; revise data distribution before retraining. |
| Personal records appear in examples or outputs | Quarantine the affected dataset, obtain the owner-approved remediation path, and retest for memorization. |
| A spreadsheet assumes volume implies ROI | Compute break-even from observed rates, prompt lengths, output lengths, training and operating costs. |

## References

| Need | Read |
|------|------|
| Training data and validation | `references/data-prep.md` |
| Provider/model capability | `references/providers.md` |
| Training configuration | `references/training.md` |
| Holdout evaluation and debugging | `references/evaluation.md` |
| Cost and break-even | `references/costs.md` |
| Privacy and compliance | `references/compliance.md` |
| Official source checks | `references/sources.md` |
| Original behavior disposition | `references/semantic-inventory.md` |
| Evaluation evidence | `references/evaluation-record.md` |
