# Connect Boundaries - Instacart

## Products are not interchangeable

| Product | Audience | Outcome |
|---------|----------|---------|
| Developer Platform API | App/site developers | Shareable Marketplace recipe or shopping-list pages; nearby retailers |
| Instacart Connect APIs | Retailer / branded ecommerce partners | Scheduling, full-service shopping, delivery, pickup, order tracking |

Official Connect overview states Connect is built for retailer partners. App
developers who only need a shoppable recipe or list link should use Developer
Platform API.

## Use Developer Platform when the goal is

- recipe pages
- shopping-list pages
- nearby retailer lookup
- lightweight AI or app handoff into Instacart Marketplace

## Use Connect when the goal is

- branded ecommerce experiences
- delivery or pickup scheduling
- full-service shopping
- order tracking and post-checkout experiences
- sandboxed callbacks and fulfillment testing

## Routing triggers for Connect

Route to Connect (and out of pure Developer Platform page APIs) when the user
mentions:

- order lifecycle
- delivery windows
- callbacks or webhooks
- post-checkout page
- sandbox order events
- retailer or enterprise fulfillment integration

## Practical consequence of wrong routing

- Wrong auth model
- Wrong expectations about checkout ownership
- Wrong environment and support path
- Unnecessary engineering overhead
