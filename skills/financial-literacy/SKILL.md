---
name: financial-literacy
description: Provide structured financial education for budgeting, debt, credit, taxes, investing fundamentals, valuation, portfolio risk, and finance research. Use when users need an explanation, comparison, calculation framework, or source-grounded financial analysis rather than a personalized directive.
metadata:
  version: "1.2.0"
  openclaw: '{"emoji":"💰"}'
  related-skills: '{"accountant":"Provides accounting-focused financial guidance and bookkeeping.","banking":"Covers banking products, accounts, and financial institution services.","invest":"Focuses on investment execution and portfolio construction.","personal-finance-tracker":"Tracks daily expenses, budgets, and net worth over time.","stock-market":"Provides market data, stock analysis, and trading information."}'
---

# Financial Literacy

Use this skill for education and decision frameworks. Keep a clear boundary between explaining choices and selecting a product, trade, tax position, or allocation for a specific person.

## Response Workflow

1. **Classify the request.** Identify the user's level (regular person, student, professional, researcher, educator, or individual investor), objective, and whether the question needs a current or jurisdiction-specific fact.
2. **Collect only decision-critical context.** For taxes, regulation, or a personal investment decision, ask for jurisdiction, time horizon, liquidity needs, risk capacity, and relevant constraints. If it is unavailable, give a conceptual explanation and state which missing facts would change the answer.
3. **Ground changeable claims.** Load `references/current-us-sources.md` for United States tax, credit, investor-protection, or market-mechanics facts. Use a primary source, publication date, and applicable year; treat it as an example rather than a substitute for the user's jurisdiction.
4. **Show the model.** State inputs, assumptions, formula, and the effect of changing key assumptions. Keep calculations separate from recommendations and label estimates as estimates.
5. **Deliver a decision-ready answer.** Give a plain-language explanation, material trade-offs and downside, a low-risk next action, and source links for facts that can change. When facts about the user's circumstances are missing, label the conclusion as a general educational framework based on the stated facts and name the missing facts that could change it.

## Safety and Accuracy

- Use jurisdiction-specific primary sources before stating current tax, regulatory, product, or market facts.
- Separate legal or regulatory requirements from common practice and educational heuristics.
- Express outcomes as historical results or scenario ranges; identify the assumptions and uncertainty behind each range.
- For individualized financial, tax, or legal decisions, explain the framework and point to a suitably licensed or qualified professional in the user's jurisdiction.
- Treat current prices, rates, fees, yields, limits, and filing thresholds as perishable data; provide the as-of date and source.

## For Regular People: Understand Without Jargon

1. **Explain interest with the user's numbers.** For a simple annual illustration, interest ≈ balance × APR; clarify that many cards calculate interest daily and that the statement terms control the actual charge.
2. **Explain credit scores as a model, not a checklist.** For FICO Scores, payment history, amounts owed, length of history, new credit, and credit mix are the five general categories. Their relative importance can vary by credit profile.
3. **Compare debt payoff approaches.** Name both avalanche (highest rate first) and snowball (smallest balance first), then calculate the interest and timeline trade-off using balances, APRs, minimum payments, and any extra payment. State that avalanche favors lower interest cost while snowball favors early balance-completion milestones.
4. **Explain marginal taxes by layers.** Use the user's tax year, filing status, jurisdiction, and taxable-income assumptions. A higher bracket applies only to the income in that bracket.
5. **Begin investing with purpose and horizon.** Distinguish emergency or short-term savings from money that can tolerate investment volatility over a longer horizon.
6. **Suggest one observable next action.** Examples include listing balances and APRs, reviewing a statement's interest calculation, or tracking purchases for two weeks.

## For Students: Foundations and Rigor

1. **Teach time value of money first.** Show present value, future value, discounting, and the intuition that a dollar's value depends on timing and risk.
2. **State model assumptions.** CAPM, DCF, and efficient-market frameworks simplify reality; name assumptions about markets, taxes, transaction costs, and behavior before drawing conclusions.
3. **Build valuation from explicit inputs.** For a DCF, state cash-flow forecast, discount rate, terminal-value method, and sensitivity range. Show how output changes when each input moves.
4. **Separate evidence from interpretation.** Present established findings, contested findings, and the limitations of the sample or identification strategy separately.
5. **Apply theory to a case.** Use a real company or dataset only when its source, date, units, and limitations are available to the reader.

## For Professionals: Decision Support, Not Directives

1. **Match method to context.** DCF is most useful when cash-flow assumptions can be modeled; comparable-company and precedent-transaction analyses depend on defensible peer and transaction selection; asset-based analysis can inform asset-intensive or liquidation contexts.
2. **Disclose valuation assumptions.** State the discount rate, growth assumptions, terminal-value method, comparable-selection rules, and bull/base/bear scenarios.
3. **Define metrics before comparing.** Clarify trailing versus forward P/E, the treatment of stock-based compensation in EBITDA, and the benchmark used for risk-adjusted returns.
4. **Apply the relevant regulatory framework.** Identify the jurisdiction and role before characterizing duties or disclosure requirements. For United States examples, use current SEC and FINRA material rather than treating a historical rule summary as current law.
5. **Use dated primary data.** Prefer filings, central-bank releases, issuer materials, and methodology notes; label stale or unavailable data instead of implying recency.

## For Researchers: Rigor and Evidence

1. **Classify the evidence.** State whether the design is experimental, quasi-experimental, or observational, and identify plausible endogeneity channels.
2. **Report uncertainty and materiality.** Distinguish statistical significance from economic significance; report standard errors or confidence intervals and relevant effect sizes.
3. **Protect against data mining.** Specify the hypothesis, sample construction, multiple-testing treatment, and out-of-sample plan before interpreting a factor or signal.
4. **Make replication possible.** Record data sources, retrieval dates, transformations, exact sample filters, and code needed to reproduce the result.
5. **Treat finance research as revisable.** Separate consensus, active debate, and preliminary evidence; explain what later data could change the conclusion.

## For Educators: Pedagogy and Progression

1. **Assess the learner's starting point.** Use their existing vocabulary and a familiar example before introducing technical terms.
2. **Use concrete numbers with labeled assumptions.** For example, show compounding with a stated annual return, contribution schedule, horizon, taxes, and fees; label the result as an illustration rather than a forecast.
3. **Build foundations before complexity.** Confirm the learner understands saving, borrowing, diversification, and basic instruments before options, leverage, or advanced valuation.
4. **Pair each benefit with a trade-off.** Contrast multiple approaches without presenting any as universally optimal.

## For Individual Investors: Risk and Discipline

1. **Start with loss capacity.** Ask what loss would materially affect the user's goals, cash needs, or ability to remain invested before discussing position size or instrument complexity.
2. **Quantify downside scenarios.** Show the dollar loss and portfolio effect under a stated adverse-price scenario, including the assumption that a loss can exceed an expected range.
3. **Explain order mechanics before discussing exits.** A stop order can trigger a market order and execute away from its stop price in a fast-moving market; use the brokerage's current documentation for available order types and conditions.
4. **Match complexity to demonstrated understanding.** Explain leverage, derivatives, concentration, liquidity, and tax consequences before comparing strategies that use them.
5. **Identify jurisdiction-specific tax questions.** For United States wash-sale or capital-gains questions, load the current IRS material; obtain the user's jurisdiction and transaction dates before applying a rule.

## Failure Recovery and Gotchas

| Trigger | First response | If still unresolved |
| --- | --- | --- |
| Current rate, threshold, product term, or regulation lacks a dated primary source | Give the stable concept and identify the missing fact. | Locate a current primary source before stating a numeric or legal conclusion. |
| Calculation inputs are incomplete | List assumptions and show a conditional example. | Ask for the minimum inputs needed to calculate a scenario. |
| User requests a personalized trade, allocation, tax filing position, or legal conclusion | Explain the decision framework and relevant risks. | Direct the user to an appropriately qualified professional for their jurisdiction. |
| A source conflicts with another source | Prefer the applicable regulator, issuer, or original study and state the conflict. | Keep the conclusion conditional until the authoritative source is resolved. |
