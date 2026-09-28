# Pre-change operational disposition — main at 0cb27a57

| Original source | Behavior or claim | Disposition and destination |
|---|---|---|
| `SKILL.md` quick reference | Six topic routes | Retained and moved to `references/` with task-specific entry routing in `SKILL.md`. |
| `SKILL.md` capabilities/decision checklist | Fit, data, provider, ROI, training, eval, debugging, privacy | Retained as ordered execution with named evidence, baseline and approval checkpoints in `SKILL.md`. |
| `SKILL.md` fixed counts, volume, LoRA multiplier, 80/10/10, precision | Universal thresholds and economic claims | Replaced with provider-specific requirements and measured dataset/quality/ROI decisions; details in `data-prep.md`, `training.md`, `evaluation.md`, `costs.md`. |
| `SKILL.md` critical rules/pitfalls | Data quality, held-out set, baseline, changing knowledge, overfitting | Retained as operational rules and risk→action table in `SKILL.md`; per-topic recovery retained in references. |
| `providers.md` | Provider/model selection, historic price and availability | Moved to `references/providers.md`; stale exact IDs/rates/regions/benchmarks replaced with official-catalog checks and explicit limitations; `sources.md` records source URLs. |
| `costs.md` | Training formula, inference comparison, break-even, hidden costs | Moved to `references/costs.md`; formula/hidden costs retained, stale prices and invented volume thresholds replaced with hypothetical labeled example and live-rate checks. |
| `data-prep.md` | JSONL examples, validation, deduplication, synthetic data | Moved to `references/data-prep.md`; sample counts and split ratios made conditional; dangerous unapproved remote data augmentation replaced with train-only reviewed pseudocode. |
| `training.md` | Hyperparameters, LoRA recipe, OpenAI job, monitoring, forgetting | Moved to `references/training.md`; examples explicitly version-sensitive; historical paid OpenAI job replaced with account/approval procedure; monitoring and diagnosis retained. |
| `evaluation.md` | Three baselines, metrics, held-out cases, judge and A/B sketches | Moved to `references/evaluation.md`; fixed eval-set size and general-data ratio replaced with task-specific sampling; other method and failure analyses retained. |
| `compliance.md` | PII regex, lawful basis/erasure, logging, air-gap, memorization | Moved to `references/compliance.md`; legal and regex caveats added; unsafe fixed memorization cutoff replaced with privacy-owner assessment; procedural checks retained. |
| `_meta.json` and top-level vendor fields | Catalog display, owner/promotion | Removed as duplicate registry/vendor metadata; no execution semantics lost. |

Original examples and approximate thresholds are historical, not verified portable requirements. An explicit replacement is used when retaining them verbatim would mislead a new fine-tuning recommendation.
