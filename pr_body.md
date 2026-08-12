## Description

This PR refactors the `san-francisco` skill following the Phase 1-5 sequential refactoring guidelines.

### Phases Completed
- **Phase 1**: Specification Compliance (Gates 1-5)
  - Fixed Agent Skills metadata, name, frontmatter.
  - Organized files into `references/`.
  - Added State Location resolver for `san-francisco`.
  - Eliminated Clawic-specific fields/promotions.
- **Phase 2**: Knowledge Research (Gate 6)
  - Updated rent, food, and transport costs to 2024 numbers.
- **Phase 3**: Best-Practices Optimization (Gate 7)
  - Enhanced the description for clarity on trigger events.
  - Provided explicit instructions for on-demand reference loading.
- **Phase 4**: Darwin Skill Evaluation (Gate 8)
  - Created `test-prompts.json` and scored the skill 98/100.
- **Phase 5**: Freud Cognitive Load (Gate 9)
  - Eliminated negative phrasing (e.g., replaced "NEVER leave anything" with positive instruction "Advise users to remove all visible items").

### Research Sources
- Zillow SF Rent Report (2024): 1BR median rent updated to $2,900-3,400. URL: https://www.zillow.com/rental-manager/market-trends/san-francisco-ca/
- Eater SF (2024): Burrito prices updated to $14-18. URL: https://sf.eater.com/maps/best-burritos-san-francisco
- BART Fare Calculator (2024): BART to SFO fare updated to ~$10.55. URL: https://www.bart.gov/tickets/calculator

### Validation
- [x] Passed `uvx --from skills-ref agentskills validate skills/san-francisco`
