# Three numbers per item: interest, blast radius, payoff cost

Every item carries three. The #1 ranks with all three; the #1000 ranks by gut annoyance.

- **Interest (carry)** = (time lost per change) x (change frequency). A complex file nobody touches has zero interest; a simple file touched weekly with a bad abstraction compounds fast. Estimate it as: how much longer does a typical change here take than it should, times how often.
- **Blast radius** = how many distinct changes the debt touches. Local (one module) vs structural (every cross-cutting change pays). Structural debt is far costlier per line than local; prioritize it out of proportion to its size.
- **Payoff cost** = refactor effort + regression risk + opportunity cost of the feature you are not shipping. The #1 budgets the regression risk explicitly (characterization tests, staged rollout); the #1000 estimates only the refactor hours.
- Pay when **fix cost < ~2-3x one quarter's carry**: the fix pays back within 2-3 quarters. Below that ratio, leave it with a comment and a trigger; the payoff capital is better elsewhere.
- High interest + high blast radius + low payoff cost = the highest-ROI work in the codebase. Low interest + high payoff cost = never worth a dedicated effort; fold it into boy-scout cleanup when you are already there.
- Interest compounds on test debt and architecture debt: each change layered on top makes the next one harder. Duplication and doc debt are mostly flat; they do not worsen on their own.
- Wait for upcoming changes before paying debt on code. Speculative refactoring is debt creation: you spend now, the code drifts, and you re-pay when the change finally arrives.
