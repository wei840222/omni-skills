# Evaluation & Debugging

## Evaluation Strategy

### Always Compare Three Versions

| Version | Purpose |
|---------|---------|
| Base model + prompting | Baseline — what you're trying to beat |
| Base model + few-shot | Improved baseline |
| Fine-tuned model | Your candidate |

### Metrics by Task Type

| Task | Primary Metric | Secondary |
|------|----------------|-----------|
| Classification | F1, Accuracy | Precision, Recall |
| Generation (quality) | Human preference | LLM-as-judge |
| Generation (format) | Exact match rate | Format compliance % |
| Code | Pass@k | Execution success |
| QA | Exact match | ROUGE, semantic sim |
| Summarization | ROUGE-L | Human preference |

## Building Evaluation Sets

### Requirements
- **Size:** choose enough independent, representative cases to detect the target improvement with useful confidence; no universal minimum
- **Distribution:** Match expected production inputs
- **Edge cases:** define and track relevant failure categories, including rare high-impact examples
- **Labels:** Ground truth or reference outputs
- **Strictly separate from training data** — Critical!

### Example Eval Structure

```python
eval_examples = [
    {
        "input": "User query or context",
        "expected": "Correct response",
        "category": "edge_case",  # for segmented analysis
        "difficulty": "hard"
    },
    # ...
]
```

## LLM-as-Judge Evaluation

The code below is a version-dependent sketch requiring an authorized current model, configured `client`, and score parser; it is not a standalone test. Use a validated rubric, blind human checks and calibrated model judgments for subjective outputs; an LLM judge can be biased and is not ground truth.

```python
JUDGE_PROMPT = """
Rate this response on a scale of 1-5:
- 5: Perfect, no issues
- 4: Good, minor issues
- 3: Acceptable, some problems
- 2: Poor, significant issues
- 1: Unacceptable

Input: {input}
Response: {response}
Reference: {reference}

Score (1-5):
"""

def evaluate_with_judge(examples, model):
    scores = []
    for ex in examples:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": JUDGE_PROMPT.format(**ex)}]
        )
        score = extract_score(response.choices[0].message.content)
        scores.append(score)
    return sum(scores) / len(scores)
```

## A/B Comparison

Direct comparison between base and fine-tuned:

```python
COMPARE_PROMPT = """
Which response is better for this input?

Input: {input}

Response A:
{response_a}

Response B:
{response_b}

Winner (A or B or Tie):
"""

def ab_test(examples, base_model, finetuned_model):
    wins = {"base": 0, "finetuned": 0, "tie": 0}
    
    for ex in examples:
        base_response = generate(base_model, ex["input"])
        ft_response = generate(finetuned_model, ex["input"])
        
        # Randomize order to prevent position bias
        if random.random() > 0.5:
            a, b = base_response, ft_response
            mapping = {"A": "base", "B": "finetuned"}
        else:
            a, b = ft_response, base_response
            mapping = {"A": "finetuned", "B": "base"}
        
        winner = judge(ex["input"], a, b)
        if winner == "Tie":
            wins["tie"] += 1
        else:
            wins[mapping[winner]] += 1
    
    return wins
```

## Debugging Training Issues

### Loss Not Decreasing

| Cause | Diagnosis | Fix |
|-------|-----------|-----|
| LR too low | Loss barely moves | Increase LR 2-10x |
| Bad data | Random loss pattern | Audit data quality |
| Format mismatch | Model confused | Fix data format |

### Loss Decreasing Then Diverging

| Cause | Diagnosis | Fix |
|-------|-----------|-----|
| LR too high | Loss explodes mid-training | Reduce LR, add warmup |
| Gradient explosion | Grad norm >100 | Gradient clipping |

### Good Training, Bad Inference

| Cause | Diagnosis | Fix |
|-------|-----------|-----|
| Overfitting | Perfect train, bad eval | More data, regularization |
| Precision mismatch | Different behavior | Match train/serve precision |
| Distribution shift | Eval inputs differ | Align eval with training |

### Model Forgets General Capabilities

| Cause | Diagnosis | Fix |
|-------|-----------|-----|
| High LR | Base skills degraded | Lower LR |
| No diversity | Only task data | Test a representative general-data mix |
| Too many epochs | Overspecialized | Fewer epochs |

## Failure Mode Analysis

After evaluation, categorize failures:

```python
failure_categories = {
    "format": [],      # Wrong structure
    "factual": [],     # Incorrect information
    "incomplete": [],  # Missing required content
    "style": [],       # Wrong tone/voice
    "hallucination": [], # Made up content
    "other": []
}

# Analyze each failure, bucket it, identify patterns
# Use patterns to guide data augmentation for next training round
```
