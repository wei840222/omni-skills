# Battery Devices

## Sleep behavior

- Battery sensors sleep aggressively and often receive commands only when awake.
- Check-in intervals vary widely: some wake every few seconds, others only every hour or on event.
- Reporting thresholds and poll intervals dominate battery life; frequent updates drain faster.

## Design implications

- Never count battery devices as routers.
- Place them after the mains backbone exists.
- For sleepy actuators or configuration writes, wake the device or use the stack's interview/configure retry path.
- After battery replacement, some devices forget the network and require re-pairing.

## Tuning

1. Start with vendor-default reporting; tighten only when the automation truly needs faster updates.
2. Prefer event-driven sensors over high-rate polling where possible.
3. If a sleepy device looks "dead," force a physical trigger and watch whether a fresh route report appears before resetting it.
