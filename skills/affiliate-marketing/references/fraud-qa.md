# Fraud And QA

Use this before approving payouts and after unusual spikes.

## Fraud Signals

| Signal | Typical meaning |
|--------|-----------------|
| self-referrals | internal abuse or coupon misuse |
| cookie stuffing | false attribution (often via pop-ups, hidden iframes, HTTP/301 redirects, or malicious browser extensions) where an affiliate claims credit for sales they did not drive. |
| fake leads or low-quality forms | payout gaming |
| trademark bidding | channel conflict and policy risk |
| bot traffic | artificial clicks with no real intent |
| payout spike without matching quality | fraud, leakage, or misattribution |
| referrer obfuscation | attempting to hide traffic sources by laundering clicks through multiple redirects. |

## QA Rules

- Review reversals, refunds, and lead validation together.
- Compare click growth to qualified conversion growth.
- Check whether partner traffic converts downstream or only appears good on the first click.
- Audit coupon spread beyond approved placements.
- Audit affiliate traffic sources for hidden iframes or suspicious redirects that indicate cookie stuffing.
- Monitor browser extensions for deceptive behavior (e.g. automatically setting cookies on merchant sites or evading detection).

## Payout Hold Triggers

Pause or review payouts when:
- conversion quality drops sharply
- unauthorized promo methods appear
- the partner sends traffic from banned sources
- attribution disputes cannot be reconciled quickly

It is cheaper to delay a payout review than to normalize abuse.
