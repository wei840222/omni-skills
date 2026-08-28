---
name: dropshipping
description: Build and scale dropshipping businesses with product research, supplier management, order automation, compliance checks, and multi-channel operations. Use when evaluating products/margins, vetting suppliers, automating order forwarding, handling chargebacks, or diversifying stores and cash flow.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📦"}'
  related-skills: '{"ecommerce":"For general ecommerce knowledge and platform comparison","sell":"For general selling and sales techniques"}'
---

## Core Workflow

### Product Research
- Validate demand: Google Trends, TikTok trending, competitor analysis
- Calculate REAL margins: product + shipping + platform fees (8-15%) + payment fees (3%) + ads (CAC) + returns (10-15%) + chargebacks
- Minimum viable margin: 20%+ after ALL costs — below 15% is dangerous
- Red flags: saturated products, trademark issues, no tracking, unreliable suppliers

### Supplier Evaluation
- Maintain backup suppliers instead of depending on a single source
- Verify stock before promising delivery (many lie)
- Test with sample orders before scaling
- Track: response time, shipping accuracy, defect rate, tracking updates
- For China suppliers: 15-30 day shipping is NORMAL — set expectations accordingly

### Order Operations
- Automate order forwarding to suppliers (DSers, AutoDS, CJ)
- Proactive tracking updates reduce support tickets 40%
- Monitor: orders stuck >7 days, tracking not updating, supplier excuses
- Fraud detection: mismatched billing/shipping, disposable emails, high-risk countries

### Customer Service
- 80% of tickets are "where's my order?" — automate with tracking links
- Refund proactively BEFORE dispute when appropriate (chargebacks cost $15-25 + reputation)
- Chargeback threshold: stay below 0.5% (>1% = processor warning, >2% = account closure)

## Critical Compliance

### Legal Requirements
- EU: 14-day return right (mandatory), 2-year warranty, VAT/OSS registration if >€10k sales
- US: Sales tax nexus varies by state ($100k or 200 transactions threshold typical)
- Ensure authorization before selling trademarked products and verify health claims before listing
- Customs: declare real values, warn customers about potential duties

### Platform Rules
- Shopify: chargebacks >1% = risk of ban
- Amazon: ODR >1% = suspension risk, late shipment >4% = problems
- PayPal: new accounts get 20-30% held for 90 days
- Ad accounts: policy violations = ban — have backup accounts

## Scaling Checklist

1. **Multi-store**: centralized inventory view, localized pricing, per-country compliance
2. **Cash flow**: predict 90 days ahead, negotiate payment terms with suppliers
3. **Team**: SOPs for common tasks, escalation rules for complex issues
4. **Diversification**: no >30% revenue from single product/supplier/platform

## State location

If persistent tracking of suppliers, margins, or products is needed, create state files under `<state_root>/dropshipping/`. Preferred formats are Markdown or JSON.

## Quick Reference

| Reference File | Description | When to load |
| --- | --- | --- |
| `references/integrations.md` | E-commerce Integrations Reference | Load when setting up Shopify, WooCommerce, suppliers (AliExpress, CJ), or automation tools. |
| `references/risks.md` | Risk Assessment Frameworks | Load when calculating real margins, navigating platform rules, or handling chargebacks and compliance. |
| `references/suppliers.md` | Supplier Evaluation Templates | Load when evaluating new suppliers, scoring existing suppliers, or dealing with supplier quality issues. |
| `references/domain-knowledge.md` | Dropshipping Domain Knowledge | Load when needing historical context, market growth stats, or general dropshipping economics. |
