# Browser Flow - Glovo

Use this flow when Glovo is controlled through the user's real browser session.

## Read first

1. Confirm the active tab is actually Glovo (title + URL on `glovoapp.com` or local Glovo domain).
2. Read the visible account state and **active address / city**.
3. If the address is missing, solve that before browsing stores.

## Main flow

1. **Home**
   - verify signed-in state
   - verify active city or address
   - decide food, groceries, pharmacy, or convenience intent
2. **Discovery**
   - browse category cards or use search
   - compare store ETA, minimum, fee, and promo state
   - open only the most relevant 1–3 stores
3. **Store**
   - verify store name, ETA, fees, and any minimum order
   - read menu sections before adding items
   - if the store is closed or low-signal, back out early
4. **Cart**
   - inspect existing cart state before changing it
   - add or edit only what the user asked for
   - re-check substitutions, notes, and promo effects after every major edit
5. **Checkout**
   - read the full summary page
   - require explicit confirmation before the final live order action

## Verification loop

- After every navigation, re-read the page or capture a screenshot.
- Verify click success by observing DOM or visible page changes.
- If the visible state is ambiguous, refresh the read before the next action.

## Practical notes

- Glovo often gates meaningful browsing behind an active address ([Glovo home](https://glovoapp.com/)).
- The real total can change after delivery fee, service fee, promo, and tip.
- A saved browser session is useful and also raises the risk of accidental live actions—stay in the approved control mode.
