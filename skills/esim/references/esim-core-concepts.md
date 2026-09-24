# eSIM operating rules

## RSP families

- Consumer RSP is GSMA SGP.22: the device LPA pulls a profile from SM-DP+ with an activation code or QR payload.
- M2M RSP is GSMA SGP.02: a server-driven push model. It is not a configuration flag on SGP.22.
- IoT RSP is GSMA SGP.32 (published May 2023, per the Embedded SIM overview): server-driven remote profile management for unattended, large-scale IoT. It does not replace SGP.22 consumer activation.
- Verify the applicable family before writing an integration plan. Reusing a consumer activation-code flow on an M2M or IoT estate fails closed.
- Treat the three SGP numbers as architecture labels until the GSMA PDF for that release is opened. This environment could not fetch gsma.com (HTTP 403).

## Platform access

### Apple

- In-app download uses `CTCellularPlanProvisioning` (Core Telephony, iOS 12+).
- The class is available only to carrier apps that hold the `com.apple.CommCenter.fine-grained` entitlement with `public-cellular-plan` in its value array.
- Call `supportsCellularPlan()` and read `supportsEmbeddedSIM` before `addPlan`. A regional hardware variant can lack an eUICC even when the marketing name matches.
- A third-party app without that entitlement cannot provision an arbitrary eSIM. App Review rejects flows that claim otherwise.

Source: https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning

### Android

- The LPA is a system app in the build image. It bridges SM-DP+ and the eUICC. The framework routes eUICC operations through the discovered LPA.
- Carrier apps use `EuiccManager` (`Context.EUICC_SERVICE`) for `downloadSubscription()`, `switchToSubscription()`, and `deleteSubscription()` on profiles that carrier owns.
- OEM LPA authors extend `EuiccService` and use `EuiccCardManager` ES10x functions. Those calls require the caller to be an LPA; the framework enforces that.
- Check eSIM support on the device before any download. Callbacks can take seconds or minutes.
- For apps targeting Android 14 or higher, a mutable `PendingIntent` used with these APIs names a component or package. An implicit mutable intent throws.

Source: https://source.android.com/docs/core/connect/esim-overview

Carrier-privilege signing (certificate match with the UICC) is a separate Android mechanism for carrier-privileged apps. It is not a substitute for `EuiccManager` ownership rules, and it still requires a carrier agreement.

## Activation codes

- Consumer payload shape: `LPA:1$<SM-DP+ address>$<MatchingId>`. Optional fields may be omitted; parse on `$`, do not assume three tokens.
- A trailing `$1` means the flow requires a confirmation code and uses a shorter timeout. Prompt for that code instead of retrying the same QR.
- MatchingId values are commonly single-use. SM-DP+ rejects a reused MatchingId; generate a new activation code.
- The QR image is only an encoding of that string. Recovery operates on the activation-code text.

## Certification and environments

- Production SM-DP+ go-live in carrier practice requires a GSMA security accreditation for the subscription-management site. This handoff could not re-fetch the SAS page (gsma.com HTTP 403). Tell the operator to confirm the current SAS-SM scope on GSMA before scheduling a production cutover; do not invent a certificate number.
- Keep production EIDs out of test SM-DP+ environments. Use test eUICCs for development.
- The entitlement server is separate from RSP. iOS carrier features that depend on entitlement still need that integration after the profile is installed.

## Subscriber-facing recovery

- Activation QR codes commonly expire in a carrier-defined window (often 24–72 hours). An "invalid" scan after that window needs a new code, not a client retry loop.
- Deleting a profile on device is permanent for that copy. Recovery is a new activation code from the carrier.
- A carrier-locked device rejects a profile from a non-native carrier. Check lock status before promising compatibility.
- Profile transfer between devices is not the default path. Expect a new activation per device.
- MVNOs usually ride an MNO SM-DP+ or an aggregator (G+D, IDEMIA, Thales). ES2+ access follows a business agreement; it is not a self-serve API signup.
- Number port-in can require a physical SIM step before eSIM activation. Confirm the carrier process before designing a pure-eSIM port.

## Troubleshooting

| Symptom | Next action |
|---|---|
| Profile already exists | Delete the existing profile, or request a new MatchingId. Do not reuse the failed code. |
| Download fails mid-transfer | ES9+ needs stable HTTPS. Retry on a better connection; the activation code is still the same artifact. |
| Installed, no service | Confirm the profile is enabled and selected as the active line, then restart the radio. |
| Android resolvable error | Surface the framework resolvable-error path so the user can complete it. Log `EXTRA_EMBEDDED_SUBSCRIPTION_DETAILED_CODE`. |
