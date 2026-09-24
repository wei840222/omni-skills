# Sources checked 2026-09-25

These URLs were fetched in this handoff and returned HTTP 200. GSMA.com returned HTTP 403 from this environment, so SGP.22 / SGP.02 / SGP.32 numbers below are background identifiers from the Embedded SIM overview, not a claim that the PDF text was re-read.

## RSP families

- Embedded SIM — GSMA maintains separate consumer (SGP.22), M2M (SGP.02), and IoT (SGP.32, May 2023) remote-SIM-provisioning specifications. https://en.wikipedia.org/wiki/Embedded_SIM

## Apple

- `CTCellularPlanProvisioning` — carrier-app class for downloading and installing a carrier eSIM; requires `com.apple.CommCenter.fine-grained` with `public-cellular-plan`. iOS 12+. https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning

## Android

- Implement eSIM — LPA is a system app bridging SM-DP+ and the eUICC; carrier apps use `EuiccManager` (`downloadSubscription()`, `switchToSubscription()`, `deleteSubscription()`). Android 14 mutable `PendingIntent`s name a component or package. https://source.android.com/docs/core/connect/esim-overview

Carrier-specific heuristics (QR lifetime often 24–72 hours, port-in sometimes requiring a physical SIM, aggregator choice) stay labeled as heuristics. Confirm them with the carrier before promising a deadline or a vendor.
