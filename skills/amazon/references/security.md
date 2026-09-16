# Security Protocols

## Credential Handling

**Storage rules:**
- Ensure Amazon passwords remain outside of agent memory
- Use OS keychain/secrets manager for any stored credentials
- Ensure session tokens are cleared upon expiration
- Treat 2FA codes as one-time use only

**Authentication flow:**
- Agent initiates login context
- Human enters credentials directly to Amazon
- Agent receives session (not credentials)
- Session has limited scope and duration

## Payment Security

**Before any purchase:**
- Display full total including tax/shipping
- Show payment method to be charged
- Confirm shipping address
- Wait for explicit human approval

**Restricted from automation:**
- Adding new payment methods
- Changing default payment
- One-click purchases (too risky)
- Gift card redemption

**Red flags to catch:**
- Price significantly different from expected
- Unusual shipping address
- High-value purchase from new seller
- Multiple orders in short period

## Account Protection

**Monitor for:**
- Unrecognized devices in security settings
- Failed login attempts
- Order confirmation for things not ordered
- Address changes not initiated by user

**If compromise suspected:**
- Change password immediately
- Review and end all sessions
- Check for unauthorized orders
- Enable/verify 2FA

## Automation Safety

**Rate limiting:**
- Implement rate limiting for all Amazon requests
- Implement exponential backoff on errors
- Spread operations across time

**Session management:**
- Respect session timeouts
- Re-authenticate cleanly when expired
- Allow sessions to expire naturally

**Seller account specifics:**
- Higher security — linked to bank accounts
- More aggressive bot detection
- API keys where available (Product Advertising API, SP-API)

## Data Protection

**Restricted from storing:**
- Full credit card numbers
- Amazon account passwords
- Social security / tax IDs
- Bank routing numbers

**OK to store:**
- Order history summaries
- Product watchlists (ASINs)
- Price history data
- Non-sensitive preferences

## Phishing Awareness

**Common Amazon phishing patterns:**
- "Your order couldn't be shipped"
- "Account locked — verify now"
- "You won a prize"
- "Unusual sign-in detected" (ironic)

**Always verify:**
- Check sender domain carefully
- Navigate to Amazon directly rather than clicking links
- Be aware that Amazon only requests passwords on their official login page
- When in doubt, check order history directly
