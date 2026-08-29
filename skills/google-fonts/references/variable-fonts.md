## Variable Fonts

- Prefer variable builds for families that expose a Variable badge (for example Inter, Roboto Flex, Montserrat, Open Sans) when multiple weights are needed.
- Request a weight axis range with `wght@100..900` to download one variable file instead of many static files.
- In CSS, set any `font-weight` inside the supported axis range (for example `font-weight: 450`).
- Confirm the Variable badge on the Google Fonts family page before assuming axis-range syntax will work.
