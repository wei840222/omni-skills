---
name: pay
description: Advises on payment method selection, rewards optimization, dispute handling, and payment security. Triggers on payment questions, card selection, and fraud issues.
metadata:
  openclaw: '{"emoji":"💳"}'
---

## Triggers

Activate on: "how should I pay", "which card", payment method questions, dispute help, fraud concerns, bill management.

**Before acting on payments:** Verify explicit user confirmation before initiating or authorizing any payments.

## Quick Decision: Which Card?

When user asks "which card should I use?":

1. **Check if category bonus applies** (groceries, gas, dining, travel)
2. If yes → Use card with that bonus
3. If no bonus → Use highest flat-rate cashback card
4. **International?** → Use no-foreign-fee card

When the user asks about which card to use or category details, load `references/cards.md`.

## Payment Method Selection

| Method | Best for | Watch out |
|--------|----------|-----------|
| Credit card | Most purchases | Pay full balance monthly |
| Debit card | Budget control | Less fraud protection |
| Cash | Negotiation, privacy | No protection if lost |
| Bank transfer | Large purchases, rent | Hard to reverse |
| Digital wallet | Convenience | Still uses underlying card |

## Fraud & Security

**If card stolen or suspicious charge:**
1. Freeze card immediately (app or call)
2. Check recent transactions
3. Report fraud to bank
4. Request new card number

**Red flags — never do this:**
- Give full card number over phone (unsolicited call)
- Pay via gift cards or wire for purchases
- Click links in "fraud alert" texts

When handling fraud, suspicious charges, or security concerns, read `references/security.md` before acting.

## Disputes & Chargebacks

**Before disputing:**
1. Contact merchant first (often faster)
2. Document everything (screenshots, receipts)
3. Know time limits (usually 60-120 days)

**Chargeback reasons that work:**
- Item not received
- Item significantly not as described  
- Unauthorized charge
- Merchant won't honor refund policy

When a user wants to file a dispute or chargeback, load `references/disputes.md` for scripts and processes.

## Bill Management

**Autopay rules:**
- Fixed bills (rent, subscriptions) → Autopay full amount
- Variable bills (utilities, credit cards) → Autopay minimum or manual
- Always: Calendar reminder 3 days before due

**Missed payment?** Call immediately — many issuers waive first late fee if you ask.

## Rewards Basics

- **Statement credit / cashback:** Simplest, automatic value
- **Points:** Can be worth more if transferred to travel partners
- **When in doubt:** Cashback is never wrong

When a user asks about rewards, points, or shopping portals, load `references/rewards.md` for optimization strategies.
