# A/B testing

Test one decision at a time where the platform and traffic support it. State the hypothesis, audience, primary metric, guardrail metric, stopping rule, and decision owner before launch.

- Apple Custom Product Pages can tailor product pages to distinct acquisition contexts; verify current eligibility and measurement options in App Store Connect.
- Google Play store listing experiments can compare eligible listing assets. Verify the current experiment types and country availability in Play Console.
- Randomization, traffic allocation, and duration must be sufficient for the decision; do not use a fixed minimum number of days as a proxy for statistical validity.
- Keep a control and avoid overlapping changes that prevent attribution. Stop or roll back if a guardrail degrades materially.

Sources:
- Apple, *Create Custom Product Pages*: https://developer.apple.com/help/app-store-connect/create-custom-product-pages/create-custom-product-pages/
- Google Play Console Help, *Run store listing experiments*: https://support.google.com/googleplay/android-developer/answer/6227309
