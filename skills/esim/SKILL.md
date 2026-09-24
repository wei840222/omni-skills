---
name: esim
description: >
  Implement and troubleshoot eSIM activation, carrier integration, and RSP
  development. Use for SGP.22 consumer profiles, SGP.02 M2M profiles, SGP.32
  IoT, SM-DP+ activation codes, iOS CTCellularPlanProvisioning, and Android
  EuiccManager. Not for physical SIM cloning, arbitrary third-party
  provisioning, or production SM-DP+ go-live without GSMA SAS.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📱","os":["linux","darwin","win32"],"displayName":"eSIM"}'
---

## When to load

Load this skill when the task is to:

- Integrate an eSIM activation flow in an iOS or Android app.
- Design or operate SM-DP+ / RSP infrastructure (consumer, M2M, or IoT).
- Parse an activation code or QR payload and recover a failed download.
- Separate consumer RSP (SGP.22) from M2M RSP (SGP.02) and IoT RSP (SGP.32).

Leave this skill unloaded for physical SIM logistics, generic mobile UI, or billing that does not touch profile download or enablement.

## State location

This skill does not persist state. Keep activation codes, EID values, and MatchingIDs in the caller's secret store; do not write them into the skill directory.

## Load path

Read `references/esim-core-concepts.md` before giving platform, activation-code, certification, or troubleshooting guidance. Read `references/sources.md` when a claim needs a citation or a freshness check.

## Decision order

1. Name the RSP family first: consumer SGP.22, M2M SGP.02, or IoT SGP.32. Treat them as separate architectures.
2. Confirm the caller is a carrier app, an OEM LPA, or an SM-DP+ operator. A third-party app without that role cannot provision an arbitrary profile.
3. Parse the activation code before retrying a QR scan. Format, confirmation-code suffix, and one-time MatchingId decide the next action.
4. For production SM-DP+, treat GSMA SAS-SM as a go-live prerequisite, and keep production EIDs off test environments.
5. After a profile installs with no service, check enabled state and active line, then restart the radio. A download failure mid-transfer is an ES9+ connectivity retry, not a code rewrite.
