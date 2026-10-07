# Inbound review order

Load when a contract landed and someone must mark it up.

## Fixed read order

Read in this order **before** page-1 narrative:

1. **Parties** — exact registered legal names and entity forms; trade names are not parties
2. **Term** — initial term, auto-renewal, notice window, counting unit
3. **Money** — fees, payment terms, late interest, suspension, disputed invoices
4. **Cap** — limitation of liability **and** every carve-out in the same pass (Rule 2)
5. **Indemnity** — scope, control of defence, survival vs cap
6. **IP** — ownership of deliverables vs background; licence back
7. **Exit** — termination for convenience/cause, cure, prepaid fees, wind-down

Then definitions, warranties/SLA, confidentiality, data protection, assignment/change of control, governing law/forum, entire agreement, order-of-precedence, signature blocks.

## Side and posture

Apply `default_side` and `risk_posture` from config. The same clause is a win for one side and a loss for the other — say which column you are playing.

## Deliverable shape

1. Real exposure number (cap + carve-outs + insurance gap if known)
2. Must-change / should-change / accept list
3. Computed dates for `## Due`
4. Red Flags scan result
5. Proposed redline language only for must/should items

## Playbook vs bespoke

Under `signature_authority_usd`, playbook fallbacks are fine. Above it, bespoke review: do not rubber-stamp mechanical positions on the one deal that was different.
