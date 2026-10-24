# Wagering Mathematics & Industry Authorities

This document records the foundational mathematical literature, probability models, odds conversion formulas, and responsible gaming resources utilized in betting analysis.

## Mathematical Foundations & Sizing Theory

- **Kelly Criterion**:
  - Primary source: Kelly, J. L. (1956). *A New Interpretation of Information Rate*. Bell System Technical Journal, 35(4), 917-926.
  - Formula: $f^* = \frac{bp - q}{b} = \frac{p(b + 1) - 1}{b}$ where $b$ is net odds received (decimal odds minus 1), $p$ is probability of winning, and $q = 1 - p$.
  - Practical usage: Fractional Kelly (e.g., quarter-Kelly or eighth-Kelly) is standard to prevent ruin under parameter estimation error.
- **Thorp, Edward O.**:
  - Application of information theory and Kelly staking to repeated wagers and financial markets: [https://www.edwardothorp.com/](https://www.edwardothorp.com/)
  - Thorp, E. O. (2006). *The Kelly Criterion in Blackjack Sports Betting, and the Stock Market*. Handbook of Asset and Liability Management.

## Odds Conversion & Overround (Vig)

- **Decimal Odds to Implied Probability**:
  $$P_{\text{implied}} = \frac{1}{\text{Decimal Odds}}$$
- **American Odds to Implied Probability**:
  - If Odds $> 0$: $P = \frac{100}{\text{Odds} + 100}$
  - If Odds $< 0$: $P = \frac{|\text{Odds}|}{|\text{Odds}| + 100}$
- **Vig / Overround Removal (No-Vig Fair Odds)**:
  $$\text{Fair } P_i = \frac{P_{i,\text{implied}}}{\sum_{j=1}^n P_{j,\text{implied}}}$$

## Responsible Gaming Authorities & Support

- **National Council on Problem Gambling (NCPG)**:
  - Official resource: [https://www.ncpgambling.org/](https://www.ncpgambling.org/)
  - National Problem Gambling Helpline (1-800-GAMBLER).
- **International Centre for Responsible Gaming (ICRG)**:
  - Independent peer-reviewed research on gambling disorder and harm reduction: [https://www.icrg.org/](https://www.icrg.org/)
