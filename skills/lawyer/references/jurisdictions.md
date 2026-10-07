# Jurisdiction map

Load when asking whether an answer travels across borders.

## Working defaults while `home_jurisdiction` is unset

State the assumption explicitly, then apply **common-law commercial defaults** only as a transparent scaffold — not as universal law:

- Written contracts and entire-agreement clauses are taken seriously
- Liability caps and consequential-damages waivers are often enforceable if clear (subject to consumer/UCTA-like controls in some places)
- Employment is **not** uniformly at-will outside many US states
- Non-competes range from routine-with-limits to near-void
- Civil-law systems may require more formalities, good-faith overlay, and different penalty/liquidated-damages treatment

## What often does not travel

| Topic | Why it breaks |
|-------|----------------|
| At-will termination | US-centric; many jurisdictions require cause or notice/pay in lieu |
| Non-competes | California-style voids vs enforceability jurisdictions |
| Liquidated damages / penalties | Common-law penalty doctrine vs civil-law penalty clauses |
| Consequential damages waivers | Drafting and consumer protections differ |
| E-sign carve-outs | Wills, real property, notarisation rules are local |
| Privacy | GDPR vs CCPA vs other — roles and rights differ |
| Securities | Offer rules attach early; local regimes diverge |

## Method

1. Name governing law and forum clauses in the paper
2. Name mandatory local law that may override (employment, consumer, data, real property)
3. Flag any clause that depends on a doctrine that does not exist in the other system
4. When stakes exceed `signature_authority_usd`, recommend local counsel confirmation

## Sources

Statutory numbers and procedural deadlines in this skill are structural cues — verify against current official sources in `references/sources.md` before the user relies on them for a filing.
