# HomePod network diagnostics

Use this flow when playback stalls, Siri responses time out, devices disappear from Home, or multiroom playback desynchronizes.

## Triage

1. Establish scope: one device, one room, or the whole home.
2. Capture a baseline: HomePod model and software version, active Wi-Fi context, and home-hub status.
3. Test the likely layer: local link quality, router multicast or policy behavior, then account or Apple-service dependency.

| Observation | Likely layer | First action |
|---|---|---|
| One HomePod drops from AirPlay | Local link | Validate signal and nearby interference |
| All automations stop together | Home hub or router | Verify home-hub status and recent router changes |
| Siri responds but the action fails | Permission or service path | Validate Home app control and account access |
| Playback starts then desynchronizes | Local link | Stabilize the network condition and rerun the same room sequence |

## Evidence loop

After each change, rerun the same two validation actions and record comparable results when persistent notes are enabled. Change one layer at a time: preserve the router configuration while testing a device-side adjustment, then test the network change separately. Escalate from restart and targeted checks to reset only after collecting a reproducible trace and reviewing Apple’s current reset guidance.
