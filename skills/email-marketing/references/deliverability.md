# Deliverability

Use this before increasing volume or when mail lands in spam/promotions unexpectedly.

## Authentication Baseline

| Control | Why it matters |
|---------|----------------|
| SPF | Authorizes sending hosts for the domain |
| DKIM | Cryptographic integrity of message content |
| DMARC | Alignment policy; required expectation for bulk senders on major providers |
| BIMI (optional) | Brand mark display after strong DMARC |

Gmail and Yahoo bulk-sender guidance (2024+) expects authenticated mail, easy unsubscribe, and low spam rates for senders of large volumes.

## Warmup

| Stage | Guidance |
|-------|----------|
| New domain/IP | Start ~50–100 messages/day |
| Ramp | Increase ~20% daily over 2–4 weeks when metrics stay healthy |
| Stop ramp | Rising complaints, hard bounces, or sudden spam placement |

## Monitoring

- Google Postmaster Tools (domain reputation, spam rate)
- Blacklist checks (e.g., MXToolbox and provider-specific signals)
- Bounce taxonomy: hard vs soft; remove hard bounces immediately
- Complaint rate: keep **strictly below 0.3%**; target **≤0.1%**

## Diagnosis Order

1. Auth and alignment failures
2. List quality / spam traps / purchased lists
3. Complaint and unsubscribe spikes after content or offer changes
4. Infrastructure (shared IP reputation, reverse DNS)
5. Creative and engagement only after the above are stable

Do not "fix" deliverability by only rewriting subject lines while auth or list quality is broken.
