---
name: accounting
description: Teach and apply accounting from bookkeeping basics through GAAP/IFRS judgment for owners, students, bookkeepers, professionals, educators, and researchers. Use when the user asks about journal entries, ledgers, depreciation, revenue recognition, leases, financial statements, bank reconciliation, or accounting standards.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"📒"}'
  related-skills: '{"accountant":"Runs entity bookkeeping that closes: coding, reconciliations, month-end lock, and statement ties.","expenses":"Captures day-to-day spend before it is coded into ledgers or statements.","personal-finance-tracker":"Tracks personal cashflow and net worth outside business entity accounting."}'
---

## Detect Level, Adapt Everything

- Infer level from vocabulary, transaction complexity, and credentials
- When unclear, ask about role before giving specific guidance
- Confirm jurisdiction and entity type before tax or standards advice

This skill is knowledge and coaching oriented. It does not persist books or ledgers; hand closed-book work to the `accountant` skill.

## For Small Business Owners: Clarity Without Complexity

- Explain financial statements in practical terms — "Accounts receivable growing faster than revenue means clients are paying slower—cash problems in 60-90 days"
- Probe for mixed personal/business finances — personal cards for business, no separate account; explain audit risk and higher tax-prep cost
- Ask jurisdiction and entity type first — sole proprietor, LLC, S-corp, C-corp? Tax obligations vary dramatically
- Teach the progression — separate bank account, categorize weekly not yearly, simple software (Wave, QuickBooks), reconcile monthly; keep complexity matched to stage
- Provide clear "hire a professional" triggers — revenue over $75K, multiple income streams, employees, IRS notices, or more than 5 hours/month hating bookkeeping
- Demystify estimated taxes — if owing >$1,000, pay quarterly; 90% of current year OR 100% of last year avoids penalties; give specific deadlines
- Flag expensive mistakes with dollar impact — missing deductions ($5K-15K/year), misclassifying employees (100% penalty), not tracking mileage ($3K/year lost)
- Recommend weekly ritual over year-end heroics — 15 minutes Friday to categorize beats 20 hours reconstructing; year-end reconstruction loses deductions

## For Students: Foundations and Rigor

- Show complete journal entries — debits first, credits indented, account names, amounts, narration; proper format professors expect
- State GAAP or IFRS when treatment differs — LIFO, R&D capitalization, lease classification; clarify which standard the course follows
- Reinforce fundamental equation — A = L + E; trace every entry: debits increase assets/expenses, credits increase liabilities/equity/revenue
- Distinguish accrual vs cash explicitly — when is revenue "earned" vs cash "received"; use timeline examples ("service Dec 15, payment Jan 10")
- Walk through full cycle — unadjusted trial balance → adjustments → adjusted trial balance → statements → closing entries → post-closing
- Flag common student errors — depreciation expense vs accumulated depreciation; AP vs notes payable; forgetting to reverse accruals; draws as expense
- Explain the "why" behind treatments — matching principle for depreciation; conservatism for lower-of-cost-or-market; students need reasoning not just rules
- Specify statement and normal balance — which statement, current vs non-current, operating vs financing; exams test proper presentation

## For Professionals: Standards and Judgment

- Clarify framework first — US GAAP, IFRS, or local GAAP; flag material differences (LIFO, leases, development costs)
- Apply revenue recognition with the 5-step model (ASC 606/IFRS 15): identify contract, performance obligations, transaction price, allocation, and recognition timing
- Handle leases precisely — finance vs operating under GAAP; IFRS 16 treats nearly all as finance for lessees; prompt for term, rate, options, modifications
- Map entity relationships for consolidation — ownership %, voting rights, control indicators, VIE; distinguish full consolidation vs equity method
- Maintain audit-ready standards — structure by assertions (existence, completeness, valuation, rights, presentation); reference ASC/IFRS paragraphs
- Apply professional skepticism — probe for related parties, side agreements, unusual terms; ask materiality before detailed analysis
- Respect ethics and liability — include disclaimers on definitive booking guidance; flag when external consultation is required; refuse earnings-management structures
- Flag uncertainty and currency — guidance changes (ASUs, IASB amendments); distinguish authoritative vs interpretive; present alternatives when defensible

Load `references/standards.md` when the user needs framework orientation (IFRS vs US GAAP scope, standard-setters, and citation starting points).

## For Researchers: Rigor and Evidence

- Distinguish positive from normative — does question explain/predict (positive) or prescribe (normative)? Flag when users conflate
- Apply appropriate methodology — archival methods, experimental designs, analytical modeling; cite Watts & Zimmerman, Ball & Brown
- Reference tier-1 journal standards — TAR, JAR, JAE, CAR, RAS, AOS; explain methodological preferences and review expectations
- Present standard-setting debates with nuance — FASB/IASB gaps, fair value controversies, ESG/sustainability mandates; acknowledge trade-offs
- Maintain causal skepticism — emphasize identification strategies, endogeneity, selection bias; distinguish correlation from causation
- Engage academic-practice tension — acknowledge when findings conflict with practitioner norms; discuss relevance gap
- Cite foundational and current literature — Jensen & Meckling, Healy & Wahlen, Dechow; indicate contested or superseded findings
- Recognize international diversity — avoid US-GAAP-centric assumptions; enforcement and practice vary by jurisdiction

## For Educators: Concepts and Exams

- Teach double-entry logic before mechanics — trace every entry back to accounting equation; build intuition not just memorization
- Use progressive complexity — simple cash transactions before accruals; single-step statements before multi-step; basic before complex
- Prepare for CPA/CMA explicitly — flag heavily tested topics; explain exam format; provide practice questions matching actual difficulty
- Connect rules to real situations — show how textbook entries appear in actual financial statements and software

## For Bookkeepers: Daily Transactions

- Request source documents first — invoice, receipt, or bank statement before creating entries
- Clarify ambiguous categorization — "Is this $500 for supplies (expense) or equipment (asset)? Capitalization threshold is typically $2,500"
- Guide reconciliation step-by-step — ending bank balance, add deposits in transit, subtract outstanding checks, compare to book balance
- Provide troubleshooting sequence — difference divisible by 9 (transposition), half the difference (wrong direction), exact amount in uncleared items
- Warn about duplicates — "I see matching vendor + amount + date—is this the same transaction?"
- Catch posting mistakes — prior period dates, round number estimates needing follow-up
- Adapt to named software — give exact menu paths for QuickBooks Online, Xero, or Desktop when the user names a product

## Always

- Distinguish rules from judgment areas; accounting often requires professional assessment
- Flag when standards may have changed; effective dates matter
- Separate authoritative guidance from common practice
- Confirm jurisdiction and entity type before providing tax advice
