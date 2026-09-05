# The metaphor as a translation device

The financial metaphor is for non-engineers; for engineers it is a prioritization frame. Know where it buys alignment and where it breaks.

- Translate debt into carry, not aesthetics. Not "the code is messy" but "each new report takes 3-4 days instead of 1 because the query layer is tangled; fixing it is one sprint and saves 2 days per report, every report, forever." The priced fork wins; "a cleanup sprint" loses.
- Frame the choice as a fork with numbers: "feature Y is 8 days as-is, 5 days if we first spend 3 fixing the auth module, and 5 days every time after." Engineers who ask for "cleanup" lose; engineers who price the fork win.
- Call out debt as a separate line item rather than bundling it into a feature estimate silently. Inflating the feature to "pay debt" erodes trust and gets the debt cut first; call it a separate line item with its own ROI.
- The "we'll clean it up after launch" promise is rarely honored without a booked date and a named owner. Without both, treat it as permanent debt and decide now whether that is acceptable.
- The metaphor breaks in three places: code is never repossessed (no forced payoff without a trigger), interest can drop to zero (debt in untouched code is free, unlike money), and you can pay debt by deleting the code (no financial analogue). Do not push the metaphor past the allocation conversation.
- Report debt as a balance sheet ("we took shortcuts"). Report it as a balance sheet: what each item bought, what it costs now, the planned payoff. The frame is accounting, not confession.
- Security interface: dependency debt with a CVE or EOL date overrides the payoff queue. Translate it for the PM as "this debt has a foreclosure date," the one thing the financial metaphor models exactly.
