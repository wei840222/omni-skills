# Zillow rental investment analysis

## Build the annual model

1. Verify achievable rent using current comparable rentals and actual leases where available. Match property type, condition, size, location, utilities, and lease terms. Record source and date; Rent Zestimate alone is an unverified input, not guaranteed income.
2. Compute scheduled gross rent = monthly rent × 12. Subtract vacancy and collection loss once, then add other supported income to obtain effective gross income.
3. Itemize operating expenses: reassessed property tax, insurance, management, routine repairs/maintenance, owner-paid utilities, HOA, licensing, and recurring operating charges. Separate mortgage payments, income tax, depreciation, and capital replacements from operating expenses.
4. Compute NOI = effective gross income − operating expenses. Show capital-replacement reserves separately; state the lender's NOI convention if it differs.
5. Calculate annual principal-and-interest debt service from the actual loan terms. If a payment includes escrow, count taxes and insurance as operating costs once and exclude that escrow portion from debt service.
6. Cash flow before income tax = NOI − debt service − capital-replacement reserves. Total cash invested includes down payment (or cash purchase price), closing costs, initial rehabilitation, and initial reserves; identify costs financed instead of paid in cash.
7. Compare base and downside scenarios for rent, vacancy, maintenance, insurance, taxes, and financing. Keep unknowns explicit and show only computable metrics.

## Metrics and denominator checks

- Cap rate = annual NOI / stated acquisition-price scenario. It excludes debt service and is distinct from an all-in yield using total acquisition cost. Label the denominator rather than substituting a list price silently.
- Cash-on-cash return = annual pre-tax cash flow / total cash invested. Report it only with a known positive cash-investment denominator.
- GRM = acquisition price / scheduled annual gross rent. It ignores expenses and financing; use it only for comparable screening.
- The 1% rent/price rule and 50% expense rule are rough screens, not underwriting standards or expense floors. Replace them with verified line items.
- DSCR = NOI / annual debt service, using the lender's defined numerator and denominator. With no debt service, DSCR is not applicable. A required ratio is lender/product-specific, not universally 1.25.

Cap rate, cash-on-cash, GRM, and vacancy targets depend on market, property, costs, and risk tolerance. A 6% cap rate or 8% cash-on-cash return is not automatically attractive. Closing and rehabilitation costs require quotes or labeled scenarios rather than a fixed percentage.

## Financing and negative leverage

Compare an all-cash case with a financed case using the same operating assumptions. For amortizing debt, the mortgage constant is annual principal-and-interest debt service divided by the loan balance. A cap rate below that constant can reduce current cash yield on equity relative to the unlevered yield; mortgage interest rate alone misses principal amortization. Assess actual cash flow, reserves, loan terms, and risk rather than declaring an investment profitable or unprofitable from the rate comparison.

## Market and legal diligence

Verify demand, employment concentration, comparable lease activity, vacancy, physical condition, insurability, flood exposure, taxes after purchase, and local rental/permit rules. If voucher rents, short-term use, rent controls, deposits, or eviction processes matter, obtain current jurisdiction-specific evidence and qualified local advice. Treat demographic stereotypes as unrelated to property underwriting; use measurable risks and the user's stated investment criteria.

## Worked hypothetical example

Assume a $300,000 acquisition price, $2,500 monthly scheduled rent, 5% vacancy/collection loss, $9,000 annual operating expenses, $15,000 annual debt service, $2,000 annual capital reserve, and $80,000 total cash invested including initial costs and reserves:

- Scheduled rent: $30,000; loss: $1,500; effective gross income: $28,500.
- NOI: $19,500; cap rate: 6.5%; GRM: 10.
- Cash flow before income tax after the annual capital reserve: $2,500; cash-on-cash: 3.125%.
- DSCR: 1.30 under the stated NOI convention; compare it with the actual lender's requirement.
- At 10% vacancy with everything else unchanged: NOI $18,000, cash flow $1,000, cash-on-cash 1.25%, DSCR 1.20.

All numbers are hypothetical inputs, not Zillow observations or market benchmarks. If financing, operating expenses, or cash invested is missing, request the missing inputs and mark the affected metric unverified. Separate mortgage qualification income from investment cash-flow modeling; lender income rules do not substitute for itemized property economics.
