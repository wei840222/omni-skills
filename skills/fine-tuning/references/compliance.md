# Compliance & Security

## PII Detection

The regex snippet below is a limited triage example, not a complete detector or proof that a dataset is safe. It can miss identifiers and misclassify values; obtain appropriate privacy review before data transfer.

### Before Training: Scan and review a representative dataset

```python
import json
import re

PII_PATTERNS = {
    "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "phone": r'\b(\+?1?[-.\s]?)?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}\b',
    "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
    "ip_address": r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
    "credit_card": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
}

def scan_for_pii(text):
    findings = []
    for pii_type, pattern in PII_PATTERNS.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            findings.append({
                "type": pii_type,
                "value": match.group(),
                "position": match.span()
            })
    return findings

def audit_dataset(path):
    report = {"total_examples": 0, "pii_found": []}
    
    with open(path) as f:
        for i, line in enumerate(f, 1):
            obj = json.loads(line)
            report["total_examples"] += 1
            
            for msg in obj.get("messages", []):
                findings = scan_for_pii(msg.get("content", ""))
                if findings:
                    report["pii_found"].append({
                        "line": i,
                        "findings": findings
                    })
    
    return report
```

### PII Remediation Options

| Option | Pros | Cons |
|--------|------|------|
| Remove examples | Simple | Data loss |
| Redact with [PII] | Preserves structure | May confuse model |
| Pseudonymize | Preserves patterns | Complex to implement |
| Synthetic replacement | Best quality | Expensive |

## GDPR Compliance

### Article 6: Lawful Basis

Have qualified counsel or the responsible privacy officer determine the applicable lawful basis; none of the options below is automatic merely because training is useful. Before training, document:
- [ ] **Consent** — Users agreed to AI training
- [ ] **Legitimate interest** — Business need documented
- [ ] **Contract** — Training necessary for service
- [ ] **Legal obligation** — Required by law

### Article 17: Right to Erasure

Requirements for compliant fine-tuning:
- Track which data points went into training
- Plan for re-training if erasure requested
- Document data retention periods

### Records of Processing (ROPA)

Document for each fine-tuning activity:
- Purpose of processing
- Categories of data subjects
- Data retention period
- Third-party processors (OpenAI, cloud GPUs)
- Technical safeguards

## On-Premise Training

### When Required
- Sensitive data cannot leave environment
- Regulated industry (healthcare, finance)
- Government contracts
- Internal policy restrictions

### Setup Options

| Tool | Requirements | Best For |
|------|--------------|----------|
| Unsloth | Verify model, quantization and GPU | Adapter tuning |
| Axolotl | Verify recipe and GPU | Custom training configurations |
| vLLM + LoRA | Verify serving requirements | Adapter serving, not training |
| MLX (Mac) | Verify supported Apple Silicon device | Local model adaptation |

### Air-Gapped Training

```bash
# Pre-download everything
pip download torch transformers unsloth -d ./packages/
huggingface-cli download meta-llama/Llama-3.1-8B --local-dir ./models/

# Transfer to air-gapped system
# Install from local
pip install --no-index --find-links=./packages/ torch transformers unsloth
```

## Audit Logging

### What to Log

| Event | Data to Capture |
|-------|-----------------|
| Training start | Dataset hash, model, hyperparams, user |
| Training complete | Model hash, metrics, duration |
| Data access | Who, when, what dataset |
| Model deployment | Version, endpoint, approver |

### Audit Log Schema

```python
audit_log = {
    "timestamp": "2024-01-15T10:30:00Z",
    "event_type": "training_started",
    "actor": "user@company.com",
    "resources": {
        "dataset_hash": "sha256:abc123...",
        "base_model": "meta-llama/Llama-3.1-8B",
        "output_path": "/models/ft-v1/"
    },
    "parameters": {
        "epochs": 3,
        "learning_rate": 2e-4,
        "lora_rank": 16
    },
    "justification": "Customer support automation project"
}
```

## Data Handling Checklist

Before training:
- [ ] Automated PII triage and human privacy review completed; detected and missed risks assessed
- [ ] Lawful basis documented
- [ ] Data retention policy defined
- [ ] Third-party DPA signed (if using cloud)
- [ ] Audit logging enabled
- [ ] Deletion procedure documented

After training:
- [ ] Training data securely deleted or archived
- [ ] Model documented in inventory
- [ ] Access controls configured
- [ ] Monitoring enabled

## Memorization Risk Assessment

Fine-tuned models may reproduce sensitive training strings. Select private canary examples with documented permission, define a realistic adversarial prompt set and a leakage criterion, then test outputs with authorized access controls. Record exact matches and near matches separately; a generic similarity cutoff or a fixed 5% threshold cannot establish privacy compliance. If unacceptable leakage is observed, quarantine the candidate and assess data removal, redaction, retraining and provider deletion options with the privacy owner. Differential privacy is an option only when the chosen training stack actually supports and validates it.
