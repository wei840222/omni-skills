# Automation Paths — Walmart

Choose the path that matches the real operating surface. Default to planning
only until the user approves an apply mode.

## Path 1: Consumer browser automation

Use this for ordinary Walmart.com grocery and household orders.

Preferred stable entry points:

- Account → Purchase History → Reorder all (authenticated account UI)
- My Items → Reorder
- order detail pages for edit, reschedule, and recovery
- Chat with Shopper / Live Shopper during active delivery shopping

Good browser-automation tasks:

- rebuild a prior order
- add or remove items from a draft basket
- set fulfillment mode to pickup, delivery, or shipping
- review substitution settings before checkout
- reschedule or recover an order inside Walmart's documented edit flows

Keep it user-mediated:

- refresh live price, stock, and time-slot state before apply
- require explicit confirmation before checkout or order mutation
- halt when login, MFA, or sensitive payment steps appear
- never capture credentials in chat

## Path 2: Marketplace API automation

Use this only for seller or solution-provider work documented on the Walmart
Developer Portal:

- https://developer.walmart.com/us-marketplace
- https://developer.walmart.com/us-marketplace/reference/tokenapi
- https://developer.walmart.com/us-marketplace/docs/marketplace-recipes

What the official portal supports for partners:

- items
- inventory
- orders
- pricing and promotions
- returns
- shipping and reports

This is **not** consumer grocery automation. If the user wants to automate their
own shopping account, route them to Path 1 instead of Marketplace APIs.

Do not present `marketplace.walmartapis.com` as a public consumer docs site.
Unauthenticated root checks fail; partner OAuth endpoints require Marketplace
registration.

## Path 3: Text to Shop and app-native flows

Walmart also exposes user-facing flows like Text to Shop, app check-in, and live
shopper messaging.

Use them as supported product features, not as undocumented APIs:

- help the user choose when they are the fastest path
- use only the official interactions behind them
- treat them as account-native actions the user can confirm and review

## Practical automation order

1. Load household memory and decide basket mode.
2. Pick the safest entry path: reorder, My Items, or fresh cart.
3. Build or adjust the basket.
4. Review substitutions and split-fulfillment risk.
5. Confirm timeslot and delivery mode.
6. Ask for explicit final confirmation before checkout.

## Hard boundaries

- No credential capture in chat
- No hidden background ordering
- No pharmacy execution without explicit confirmation
- No claims of a public consumer Walmart grocery API unless the user provides a
  verified one
