# Verified Sources — Car Rental

Live-checked during the 2026-10-17 refactor. Re-verify before citing prices,
policy details, or country-specific rules; never invent fees from memory.

| Claim area | URL | Checked |
|------------|-----|---------|
| General rental-savings tactics (timing, comparison, free cancellation) | https://www.nerdwallet.com/blog/travel/how-to-rent-a-car/ | HTTP 200 |
| Aggregator deal-finding workflow | https://support.kayak.com/hc/en-us/articles/360001137374-How-do-I-find-the-best-car-rental-deals | HTTP 200 |
| How-to-rent overview (pickup, documents, insurance framing) | https://www.rentalcars.com/en/guides/how-to-rent-a-car/ | HTTP 200 |
| Debit vs credit card acceptance / holds (supplier FAQ) | https://www.hertz.com/rentacar/reservation/reviewactivate.do?method=debitCards | HTTP 200 |
| Debit-card rental constraints (consumer explainer) | https://www.creditkarma.com/credit-cards/i/rent-car-debit-card | HTTP 200 |
| Broker FAQ / long-term and Europe coverage notes | https://www.autoeurope.com/faq/ | HTTP 200 |
| Live aggregator search surface | https://www.kayak.com/cars | HTTP 200 |

## Soft / blocked sources

These domains commonly return HTTP 403 to automation (Edmunds, Forbes Advisor,
Enterprise public FAQ mirrors). Treat them as **human-browser** checks only;
do not invent valuations or fee tables when the live page is unreachable.
