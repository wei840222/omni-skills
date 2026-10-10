---
name: zillow
description: Interpret Zillow listings and Zestimates, compare US home prices, estimate ownership costs, and model rental returns. Use for Zillow property searches, listing comparisons, seller pricing, buyer offers, or rental underwriting from Zillow data; general home repairs and non-US property searches are outside this scope.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏠"}'
---

# Zillow

Interpret US property information from Zillow and turn it into evidence-based comparisons for buyers, sellers, investors, and agents. This is a stateless research guide, not a Zillow API integration or an appraisal service.

## Default workflow

1. Establish the user's role, US location, property type, objective, and supplied listing/estimate date. Ask only for missing inputs needed for the requested decision.
2. Collect dated listing facts and corroborating records using available authorized tools or user-supplied material. If access fails, use the data-recency fallback below.
3. Read the matching reference, then produce sold-comparable evidence, a monthly ownership-cost breakdown, or an annual investment model as requested.
4. Separate verified facts, assumptions, and unknowns; show formulas, denominators, and a sensitivity range where evidence supports it.
5. Return the supported conclusion and next verification. Keep external actions at the user-confirmation boundary below.

## On-demand guidance

- Read `references/pricing.md` for sold-comparable selection, seller pricing, or offer strategy.
- Read `references/investing.md` for rent verification, investment metrics, expense modeling, or financing scenarios.
- Resolve both paths from the skill root. Load only the reference needed for the request.

## Zestimate interpretation

Treat a Zestimate as an automated estimate, distinct from an appraisal, asking price, or completed sale price. Use verified sold comparables and property condition to assess a plausible value range rather than treating the estimate as the conclusion.

Record the estimate's displayed date, location, property type, and any published accuracy statistics with their scope and retrieval date. A market-level median error is not a confidence interval for a particular home. When current Zillow methodology or accuracy information is inaccessible, say that it is unverified and analyze the supplied estimate without assigning an error percentage or update cadence. Evaluate Rent Zestimate against comparable rentals and actual leases; the same verification requirement applies independently to rent and sale estimates.

## True monthly ownership cost

Calculate principal and interest using the user's quoted loan terms or a dated lender quote. If terms are missing, request them or show a clearly labeled assumption rather than a purported current rate.

Include each applicable component separately:

- Property tax, verified with the county assessor and local rules for reassessment after purchase; the seller's current bill may differ from the buyer's future bill.
- Homeowners insurance and separate flood or other required coverage, based on quotes and property-specific hazards.
- Mortgage insurance under the actual loan program. Conventional loans with less than 20% down commonly require PMI; FHA and other programs have different insurance rules. A low down payment alone does not establish the program or premium.
- HOA dues, special assessments, and local special-district taxes, including California Mello-Roos when applicable.
- Maintenance and capital-replacement reserves as a separate budget line from the loan payment.

Label unknown components and present a subtotal, not a complete affordability claim. Keep lender escrow amounts and their underlying taxes or insurance mutually exclusive in the sum.

## Hyperlocal market context

Compare the same property type and relevant competing market area. Specify the period, sample size, inventory, days-on-market definition, sold-to-list ratio, and season when available. National trends supply context but do not replace local evidence. There is no universal days-on-market cutoff or offer discount for a hot, balanced, or buyer's market.

Use recent closed sales as valuation evidence and active listings as competition. Explain differences in condition, size, lot, legal use, and location; if comparable evidence is thin, widen the period or competing area transparently and lower confidence.

## Conservative investment analysis

Use `references/investing.md` to calculate income, operating expenses, financing, cash invested, and sensitivity scenarios. Treat rent/price shortcuts and blanket expense percentages as screening heuristics only. Replace them with local evidence before a purchase recommendation. Use the stated acquisition-price scenario as the cap-rate denominator and include closing costs, initial repairs, and reserves in total cash invested. Report unknown costs instead of silently treating them as zero.

## Data recency and access

Zillow pages, listing feeds, public records, and local MLS access have different coverage and timestamps. Verify listing availability with the listing agent or an authorized current source before acting; no fixed feed-delay or estimate-update interval is assumed.

If a page is blocked, stale, or unavailable, explain the limitation and ask for the listing text, screenshots, or a dated export. Continue analysis from that supplied material with explicit provenance. Preserve access controls and use an authorized alternative instead of bypassing the block. Separate user-supplied figures, independently verified facts, calculations, and assumptions.

## Role-specific guidance

- First-time buyer: total cost, program-specific financing, pre-approval versus pre-qualification, deposit deadlines, and inspection/appraisal/financing protections.
- Investor: verified rents, NOI, cash-on-cash return, capital reserves, debt service, taxes after purchase, and legal rental constraints.
- Seller: sold comparables, active competition, condition, exposure, and a review schedule tied to local market feedback.
- Agent: a sourced CMA, accurate listing facts, and listing optimization. Premier Agent advertising or lead products require current official terms; this guide does not assert pricing or access.

## Decision checks and common mistakes

- Zestimate alone, asking prices, or views/saves do not establish market value or buyer intent; reconcile them with closed sales and actual showings/offers.
- Square footage, bed counts, renovations, deferred maintenance, and permitted use need verification through public records, disclosures, and inspection; records can also be incomplete.
- A pending or contingent label is not confirmed availability. Confirm status and explain contingencies before suggesting a viewing or offer.
- Pre-approval and pre-qualification are lender-specific stages, not guarantees of final funding. Verify the actual letter and conditions.
- Preserve inspection, appraisal, and financing protections by default. Discuss the specific exposure and alternatives before the user decides to change them.
- Document earnest-money amount, recipient, due date, and refund/forfeiture conditions from the actual contract and local professional guidance.
- High cap rates can reflect vacancy, condition, concentration, legal, or operating risk rather than a bargain. Assess measurable property risks rather than demographic stereotypes.
- Price cuts, long market time, financing type, and FSBO status are signals to investigate, not proof of seller desperation, visibility, or inevitable outcomes.

**User confirmation:** Present drafts and scenarios for the user's decision. Obtain explicit authorization before submitting an offer, contacting an agent, changing a listing, paying a fee, or sending private financial information.

## Cross-check sources and output

Use the county assessor for tax and parcel records, FEMA mapping plus insurance quotes for flood risk, actual rental listings/leases for rent, and authorized MLS or listing-agent confirmation for sale status. Rentometer or Apartments.com can contribute rental comparisons when their current data are accessible. Schools, amenities, and safety questions require current, scoped public evidence and the user's stated needs; avoid demographic steering.

Return: objective and property context; dated inputs and sources; calculation or comparable evidence; range/scenarios and uncertainty; material risks; and the next verification needed. Include source URLs when retrieved, and label conclusions based only on supplied material.

## Verified domain sources

- CFPB, private mortgage insurance: https://www.consumerfinance.gov/ask-cfpb/what-is-private-mortgage-insurance-en-122/ — conventional-loan PMI conditions and costs; retrieved 2026-10-10.
- Fannie Mae, comparable sales: https://selling-guide.fanniemae.com/sel/b4-1.3-08/comparable-sales — physical/legal similarity, market area, and justified use of older sales; retrieved 2026-10-10. These are appraisal guidance, not universal rules for informal Zillow screening.
