---
name: mlops
description: Deploy ML models to production with pipelines, monitoring, serving, and
  reproducibility best practices. Load this skill when designing CI/CD for models,
  configuring model serving, setting up drift monitoring, or handling GPU resources.
metadata:
  openclaw: '{"emoji": "🤖", "requires": {"bins": []}, "os": ["linux", "darwin", "win32"],
    "displayName": "MLOps"}'
---

## When to load

Load this skill when you need to:
- Design CI/CD pipelines for machine learning models.
- Configure model serving and scaling infrastructure.
- Set up monitoring and drift detection for production models.
- Implement reproducibility practices.
- Handle GPU infrastructure patterns.

Bypass this skill for ML algorithms, feature engineering, or hyperparameter tuning.

## Progressive Disclosure

Detailed documentation is available in the `references/` directory. Load these files as needed based on the task:

| Topic | File | Key Trap |
|-------|------|----------|
| CI/CD and DAGs | `references/pipelines.md` | Coupling training/inference deps |
| Model serving | `references/serving.md` | Cold start with large models |
| Drift and alerts | `references/monitoring.md` | Only technical metrics |
| Versioning | `references/reproducibility.md` | Not versioning preprocessing |
| GPU infrastructure | `references/gpu.md` | GPU request = full device |

## Critical Traps

**Training-Serving Skew:**
- Preprocessing in notebook ≠ preprocessing in service → silent bugs
- Pandas in notebook → memory leaks in production (use native types)
- Feature store values at training time ≠ serving time without proper joins

**GPU Memory:**
- `requests.nvidia.com/gpu: 1` reserves ENTIRE GPU, not partial memory
- MIG/MPS sharing has real limitations (not plug-and-play)
- OOM on GPU kills pod with no logs

**Model Versioning ≠ Code Versioning:**
- Model artifacts require separate versioning (MLflow, W&B, DVC)
- Training data version + preprocessing version + code version = reproducibility
- Rollback requires keeping old model versions deployable

**Drift Detection Timing:**
- Retraining trigger isn't just "drift > threshold" → cost/benefit matters
- Delayed ground truth makes concept drift detection lag weeks
- Upstream data pipeline changes cause drift without model issues
