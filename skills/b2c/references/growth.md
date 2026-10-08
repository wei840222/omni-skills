# Growth loops & acquisition channels

Load when designing compounding growth, choosing channels, or planning the first 100 users.

## Growth loop types

### 1. Viral loop

```text
User → invites friend → friend activates → repeat
```

- **K-factor** ≈ invites sent per user × invitee conversion to activated user.
- K > 1 can compound; K < 1 still reduces CAC when paired with other loops.
- Fits social, multiplayer, collaboration, and share-native products.

### 2. Content loop

```text
Product creates shareable/indexable output → discovery → new user → more output
```

- Examples of the pattern (not endorsements): template galleries, public creations, UGC feeds.
- Requires output worth indexing or sharing plus permissions/privacy clarity.

### 3. Paid loop

```text
$ spent → users acquired → revenue/contribution → reinvest $
```

- Scales linearly; sustainability needs contribution LTV > CAC with room to reinvest.
- Does not compound by itself — pair with retention and preferably another loop.

### 4. Data / network loop

```text
Users → data or network density → better product or liquidity → more users
```

- Examples of the pattern: recommendations that improve with usage; marketplaces with liquidity.
- Defensibility rises when the loop is hard to copy and privacy-respecting.
- NFX documents many network-effect shapes; pick the shape that matches the product rather than claiming “we have network effects” generically: https://www.nfx.com/post/network-effects-manual

Reforge’s framing: **loops replace pure funnel thinking** as the unit of growth design — each loop should name the reinvestment step explicitly: https://www.reforge.com/blog/growth-loops

## Channel selection questions

1. Where does the audience already spend time?
2. What do they search when the problem hurts?
3. Whom do they trust for recommendations?
4. Is the problem discussed publicly (forums, social proof, UGC)?

### Channel matrix (directional only)

| Channel | Typical CAC posture | Volume potential | Time to meaningful scale |
|---------|---------------------|------------------|--------------------------|
| Organic social | Lower cash CAC, high time | Medium | Months |
| SEO / content | Lower cash CAC later | High if intent exists | 12–24 months common |
| Paid social | Medium–high | High | Weeks–months |
| Influencers / creators | Variable | Medium | Months |
| App stores / featured | Medium + ranking work | Medium | Months |
| Referral | Low cash if product pulls | Low–medium | Months |

## First 100 users

1. Launch in communities where the pain is already voiced.
2. Solve one concrete person’s problem end-to-end; capture the story with consent.
3. Build in public only when it creates trust, not noise.
4. Personal network asks beat cold ads before messaging is proven.
5. Waitlists help when scarcity is real and feedback loops are instrumented.

## Anti-patterns → preferred moves

| Instead of | Do |
|------------|----|
| Premature paid scale | Prove retention curve shape and rough LTV before large spend |
| Shipping features as “growth” | Ship loops and distribution surfaces users actually share or return through |
| Paid-only acquisition | Add at least one organic or product-led loop |
| Copying a competitor’s channel mix | Re-derive channels from audience location and unit economics |
| Ignoring notification/habit systems after PMF | Instrument habit loops (streaks, timely value pings) with user control — see Duolingo growth write-up in `references/sources.md` |

## Related sources

See `references/sources.md` (growth loops / network effects / habit growth).
