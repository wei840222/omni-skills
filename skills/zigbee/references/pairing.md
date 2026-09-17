# Pairing

## Preconditions

- Coordinator is in the correct permit-join / pairing mode for a short window only.
- Device is factory-reset if it previously belonged to another network.
- Pair close to the coordinator or a strong nearby router first; relocate after join succeeds.
- Have the exact reset gesture ready before enabling join; pairing timeouts are short.

## Reliable sequence

1. Enable join on the coordinator/stack UI or CLI.
2. Put the device into pairing mode immediately.
3. Wait for interview/configure to finish before moving the device far away.
4. Send a real command or force a report to confirm the route, not only a green "paired" badge.
5. Disable open join when done.

## Reset and retries

- Factory reset is commonly a 5-10 second hold, but follow the exact model instructions.
- Some devices need multiple reset attempts before they leave the old network.
- If join fails, check: wrong mode, device not reset, coordinator too far, incompatible firmware, or open join already timed out.

## Safety

- Do not leave permit-join enabled unattended on a reachable network.
- Do not publish network keys into chat logs while debugging joins.
