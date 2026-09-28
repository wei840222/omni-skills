# Data Preparation

## Format Requirements

### Example chat format (verify against the chosen provider and method)
```jsonl
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

### Multi-Turn Conversations
```json
{"messages": [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "What's the weather?"},
  {"role": "assistant", "content": "I don't have access to weather data."},
  {"role": "user", "content": "Can you check?"},
  {"role": "assistant", "content": "No, I can't access external services."}
]}
```

## Dataset sizing

There is no universal minimum for every provider and task. Check the selected model's documented requirements, then plot held-out quality against training-set size using representative labeled examples. A small high-quality set is useful for diagnosis; its adequacy is an empirical question, not a fixed threshold.

## Data Quality Checklist

Before training, verify:
- [ ] Consistent format across ALL examples
- [ ] No contradictory examples (same input, different outputs)
- [ ] Examples match production input distribution
- [ ] Representative edge cases are included and tracked by category
- [ ] No duplicate or near-duplicate entries
- [ ] Group-aware train/validation/test split is documented; choose ratios based on dataset size and required evaluation precision

## Validation Script

```python
import json
from collections import Counter

def validate_jsonl(path):
    errors = []
    examples = []
    
    with open(path) as f:
        for i, line in enumerate(f, 1):
            try:
                obj = json.loads(line)
                if "messages" not in obj:
                    errors.append(f"Line {i}: Missing 'messages' key")
                    continue
                    
                messages = obj["messages"]
                roles = [m["role"] for m in messages]
                
                # Check role sequence
                if not roles[-1] == "assistant":
                    errors.append(f"Line {i}: Must end with assistant")
                
                # Check for empty content
                for m in messages:
                    if not m.get("content", "").strip():
                        errors.append(f"Line {i}: Empty content")
                        
                examples.append(obj)
                
            except json.JSONDecodeError:
                errors.append(f"Line {i}: Invalid JSON")
    
    print(f"Total examples: {len(examples)}")
    print(f"Errors: {len(errors)}")
    for e in errors[:10]:
        print(f"  - {e}")
    
    return examples, errors
```

## Deduplication

```python
import hashlib

def dedupe_by_input(examples):
    seen = set()
    unique = []
    
    for ex in examples:
        # Hash user messages only
        user_msgs = [m["content"] for m in ex["messages"] if m["role"] == "user"]
        key = hashlib.md5(str(user_msgs).encode()).hexdigest()
        
        if key not in seen:
            seen.add(key)
            unique.append(ex)
    
    print(f"Removed {len(examples) - len(unique)} duplicates")
    return unique
```

## Synthetic Data Generation

When you need more examples:

```python
# Pseudocode only: choose an authorized current model and validate each label.
# Generated variations must stay in the same train-only source group;
# keep held-out examples and private records out of remote generation.
variations = generate_candidates(authorized_training_example)
reviewed = [v for v in variations if human_label_check(v)]
```

## Common Data Issues

| Issue | Detection | Fix |
|-------|-----------|-----|
| Inconsistent formats | Check output structure variance | Standardize template |
| Contradictions | Hash inputs, compare outputs | Manual review, remove |
| Distribution mismatch | Compare to production logs | Add production examples |
| Missing edge cases | Analyze failure modes | Targeted collection |
| Token length issues | Count tokens per example | Truncate or split |
