# Verified domain sources — Accountant

Research log for Gate 6. Claims below were checked against primary sources during the refactor. Prefer these URLs when a filing-year figure must be re-verified.

## Record retention (US)

- **IRS — How long should I keep records?** https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records  
  Extracted: 3-year ordinary period; 6-year substantial omission (>25% gross income); 7-year worthless securities / bad debt claims; indefinite if no return or fraudulent return; employment tax ≥4 years after later of due or paid; property basis records through disposal year limitations.
- **IRS — Employment tax recordkeeping** https://www.irs.gov/businesses/small-businesses-self-employed/employment-tax-recordkeeping  
  Extracted: keep employment tax records at least four years; lists required contents (EIN, wages, W-4s, deposits, returns).

## Capitalization / de minimis (US)

- **IRS — Tangible property final regulations FAQ** https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations  
  Extracted: de minimis safe harbor **$2,500**/invoice or item without AFS (raised from $500 by Notice 2015-82 for years beginning on/after 2016); **$5,000** with AFS; excludes inventory and land; amounts above the harbor still use ordinary deduct-vs-capitalize analysis.
- **Notice 2015-82 (PDF)** https://www.irs.gov/pub/irs-drop/n-15-82.pdf — threshold increase authority cited by the FAQ.

## Cash method limitation (US)

- **IRC §448** https://www.law.cornell.edu/uscode/text/26/448 — statutory framework and base gross-receipts test language.
- **Rev. Proc. 2024-40 (PDF)** https://www.irs.gov/pub/irs-drop/rp-24-40.pdf  
  Extracted: for taxable years beginning in **2025**, §448(c) average annual gross receipts test ceiling = **$31,000,000**.

## Trust-fund payroll risk (US)

- **IRS — Trust fund recovery penalty** https://www.irs.gov/individuals/international-taxpayers/trust-fund-recovery-penalty  
- **IRC §6672** https://www.law.cornell.edu/uscode/text/26/6672  

## Inventory and revenue frameworks

- **IAS 2 Inventories (IAS Plus summary)** https://www.iasplus.com/en/standards/ias/ias2 — LIFO not permitted under IFRS.
- **KPMG IFRS vs US GAAP inventory note** https://kpmg.com/us/en/articles/2026/inventory-accounting-ifrs-accounting-standards-vs-us-gaap.html — LIFO allowed US GAAP / prohibited IAS 2; NRV write-down reversal differences.
- **IFRS 15 five-step model (ACCA)** https://www.accaglobal.com/gb/en/technical-activities/technical-resources-search/2018/october/IFRS15-revenue-recognition-steps.html  
- **IFRS 15 (IAS Plus)** https://www.iasplus.com/en/standards/ifrs/ifrs15  

## Leases (directional)

- Skill text remains framework-directional (ASC 842 / IFRS 16 ROU asset + liability). Re-check entity effective dates and private-company elections against the entity’s reporting framework before booking first-time lease capitalization.

## Stable domain retained without change

Double-entry mechanics, bank reconciliation identity, cutoff accruals, allowance method for AR, gross-vs-net processor deposits, and reverse-don’t-delete corrections are stable bookkeeping practice and were kept from the pre-refactor skill after consistency review.
