# Research Sources — rental

Gate 6 anchors for domain knowledge used in this refactor. Prefer primary statutes, agency guidance, and platform docs over secondary summaries.

## Tenant and landlord basics (US-oriented defaults; always check local law)

- **U.S. Department of Housing and Urban Development — Fair Housing** — protected classes and discrimination prohibitions for housing providers via https://www.hud.gov/program_offices/fair_housing_equal_opp
- **U.S. Department of Housing and Urban Development — Tenant rights overview** — federal entry points and consumer housing resources via https://www.hud.gov/topics/rental_assistance
- **Consumer Financial Protection Bureau — Security deposits and fees** — consumer guidance on deposits, fees, and rental application practices via https://www.consumerfinance.gov/ask-cfpb/what-should-i-know-about-security-deposits-and-fees-when-renting-en-2113/
- **FTC — Rental listing scams** — common advance-fee and fake-landlord scam patterns via https://consumer.ftc.gov/articles/rental-listing-scams

## Lease review and notice norms

- **Nolo — Landlord right of entry** — typical notice expectations and state variation framing via https://www.nolo.com/legal-encyclopedia/landlord-right-entry-tenant-privacy-rights-29921.html
- **Nolo — Late fees and rent** — late-fee reasonableness and enforceability caveats by jurisdiction via https://www.nolo.com/legal-encyclopedia/late-fees-rent-29903.html

Keep skill guidance jurisdiction-aware: entry notice, deposit caps, late-fee limits, and eviction process are state/local rules. Prefer the user's jurisdiction primary source when known.

## Vacation rentals

- **Airbnb Help Center — Hosting** — listing, pricing, and guest communication baseline via https://www.airbnb.com/help/article/13
- **Airbnb Help Center — Reviews** — review timing and response norms via https://www.airbnb.com/help/article/13
- **VRBO Help — Owners / travelers** — alternate platform booking and host workflow entry via https://help.vrbo.com/

## Vehicle and equipment rentals

- **NHTSA — Car rental safety tips** — inspection and documentation hygiene for renters via https://www.nhtsa.gov/road-safety
- **FTC — Rental cars** — consumer guidance on fees, insurance add-ons, and contract review via https://consumer.ftc.gov/articles/rental-cars
- **Major lessor fee disclosures** — confirm airport surcharges, young-driver, and additional-driver fees on the specific lessor site before quoting numbers (Hertz / Enterprise / National / Avis current rate rules).

## Pricing and vacancy economics

- Market rent comps should come from live listings and recent leases in the same micro-market; skill formulas remain adjustment frameworks, not appraisals.
- Vacancy cost framing (`daily vacancy ≈ monthly rent / 30`) is an operations heuristic for landlords, not a tax or accounting rule.

## Obsolete / removed coupling

- Removed clawic.com homepage and `_meta.json` package registry metadata (Gate 5).
- Role guides relocated under `references/` with explicit when-to-load routing (Gate 2 / Gate 7).
