# Training Configuration

## Hyperparameter starting points (illustrative, verify for actual model/SDK)

These ranges are examples rather than portable defaults; inspect the current trainer API and model recipe before running a job.

### For Supervised Fine-Tuning (SFT)

| Parameter | Default | Range | Notes |
|-----------|---------|-------|-------|
| Learning rate | 2e-4 | 1e-5 to 5e-4 | Lower for larger models |
| Epochs | 1-3 | 1-5 | More = overfitting risk |
| Batch size | 4-8 | 2-32 | Higher = more stable, more VRAM |
| Warmup ratio | 0.03 | 0.01-0.1 | 3% of total steps |
| Weight decay | 0.01 | 0-0.1 | Regularization |

### For LoRA/QLoRA

| Parameter | Default | Notes |
|-----------|---------|-------|
| Rank (r) | 16 | 8-64, higher = more capacity |
| Alpha | 16 | Usually equals rank |
| Dropout | 0 | 0-0.1, use if overfitting |
| Target modules | All attention | q, k, v, o, gate, up, down proj |

### For RLHF/DPO/GRPO

| Parameter | Default | Notes |
|-----------|---------|-------|
| Learning rate | 5e-6 | 10-50x lower than SFT |
| Beta (DPO) | 0.1 | Controls preference strength |
| Epochs | 1 | Usually single pass |

## Training with Unsloth (version-sensitive illustrative sketch)

The following sketch references a third-party trainer API whose signatures may change. `dataset` and `TrainingArguments` must be defined/imported for the installed versions; this block is not a tested standalone script. Validate the model license, GPU capacity and trainer documentation before running.

```python
from unsloth import FastLanguageModel

# Load base model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Meta-Llama-3.1-8B",
    max_seq_length=2048,
    load_in_4bit=True,  # QLoRA
)

# Apply LoRA
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", 
                    "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    use_gradient_checkpointing="unsloth",
)

# Train
from trl import SFTTrainer

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=2048,
    args=TrainingArguments(
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        warmup_steps=10,
        max_steps=100,
        learning_rate=2e-4,
        output_dir="outputs",
    ),
)

trainer.train()
```

## Managed training preparation

OpenAI restricted self-serve fine-tuning job creation beginning 2026-05-07 and tightened eligibility on 2026-07-02; see `sources.md`. For any provider, confirm eligibility and the exact model/method/region, validate data with the current vendor format, calculate a spending ceiling, then obtain explicit authorization before uploading a dataset or creating a paid job. Generate SDK code only after checking the installed SDK signature. There is no executable default job-creation example here because a copied historical model ID would mislead new accounts.

## Monitoring Training

### Key Metrics to Watch

| Metric | Healthy | Problem |
|--------|---------|---------|
| Training loss | Decreasing smoothly | Jumping, not decreasing |
| Validation loss | Decreasing, then stable | Increasing = overfitting |
| Gradient norm | Stable, <10 | Exploding (>100) or vanishing (<0.001) |
| Learning rate | Following schedule | N/A |

### Overfitting Signals

1. Training loss continues dropping while val loss increases
2. Model memorizes training examples verbatim
3. Performance on held-out test set degrades

### Fixes for Overfitting

- Reduce epochs (try 1-2 instead of 3+)
- Add dropout (0.05-0.1)
- Reduce learning rate
- Add more training data
- Early stopping based on val loss

## Preventing Catastrophic Forgetting

Problem: Model loses general capabilities while learning specific task.

Solutions:
1. **Mix representative general data** — choose a tested ratio when preserving general capabilities matters
2. **Lower learning rate** — Slow learning preserves base knowledge
3. **Regularization** — Weight decay, dropout
4. **Elastic Weight Consolidation** — Advanced technique for critical params

If general capabilities matter, select a representative, permitted general-data mix and compare held-out general-task metrics before and after; choose the ratio empirically.
