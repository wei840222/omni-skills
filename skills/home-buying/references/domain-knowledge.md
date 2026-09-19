# Home Buying — Domain Knowledge

Load this file when verifying affordability math, inspection/contingency posture, closing readiness claims, or offer-ladder defaults against primary sources.

## Affordability and all-in monthly cost

- Underwrite total housing cost, not list price alone: principal and interest, taxes, insurance, HOA, utilities, and maintenance reserves.
  - CFPB — Owning a home / costs beyond the mortgage — https://www.consumerfinance.gov/owning-a-home/
  - CFPB — Explore interest rates (rate-sensitivity context) — https://www.consumerfinance.gov/owning-a-home/explore-rates/
  - Freddie Mac — Primary Mortgage Market Survey (benchmark rate series) — https://www.freddiemac.com/pmms

- Closing-cost and cash-to-close planning ranges vary by market and loan program; treat 2%–5% closing-cost bands as planning defaults, not guarantees.
  - CFPB — What are closing costs? — https://www.consumerfinance.gov/ask-cfpb/what-are-closing-costs-en-176/
  - CFPB — Your home loan toolkit (shopping and closing process) — https://www.consumerfinance.gov/consumer-tools/mortgages/resources/

## Due diligence, contingencies, and inspection risk transfer

- Convert inspection findings into seller fix, seller credit, or explicit buyer-accepted risk before removing contingencies.
  - CFPB — Should I get a home inspection? — https://www.consumerfinance.gov/ask-cfpb/should-i-get-a-home-inspection-en-178/
  - InterNACHI — Standards of Practice (scope of a general home inspection) — https://www.nachi.org/sop.htm
  - HUD — Buying a home / home inspection overview — https://www.hud.gov/buying

## Offer strategy and competitive markets

- Price is only one lever; credits, repairs, timing, and contingency set change risk transfer.
  - NAR — Buyer representation and offer process orientation — https://www.nar.realtor/
  - CFPB — Mortgage shopping and LOAN Estimate timing obligations — https://www.consumerfinance.gov/owning-a-home/process/

## Closing readiness

- Track lender conditions, appraisal, title/escrow, insurance binder, and final walkthrough as a dated critical path.
  - CFPB — Closing disclosure and closing day checklist framing — https://www.consumerfinance.gov/owning-a-home/close/
  - CFPB — What is a Closing Disclosure? — https://www.consumerfinance.gov/ask-cfpb/what-is-a-closing-disclosure-en-1983/

## Safety / non-goals

- This skill is decision-system guidance and local memory only. It does not submit offers, pull MLS data, or call lender/title APIs by default.
- Prefer portable `<state_root>/` notes over host-absolute paths; never store full account numbers or government IDs in skill memory.
