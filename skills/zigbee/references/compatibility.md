# Compatibility

"Zigbee compatible" implies a radio family, not guaranteed interoperability with every hub or stack.

## Vendor reality

- Some devices only work reliably with their vendor hub or a narrow allowlist.
- Xiaomi/Aqara devices are known to drop off generic coordinators without stack-specific handling, keepalives, or quirks support.
- Tuya Zigbee devices often expect their gateway behavior and may not pair cleanly with Zigbee2MQTT or other generic coordinators without confirmed model support.
- Not all Zigbee is equal: power reporting, binding support, OTA, and multi-endpoint behavior differ by firmware.

## Before buying or promising support

1. Identify the exact model, not just the brand brochure name.
2. Check the chosen stack's device list or issue history for that model.
3. Prefer devices with maintained converters/quirks over "works on my vendor app only."
4. If the user already standardized on one ecosystem hub, do not casually mix hostile firmware without a recovery plan.

## Integration boundaries

- When the user needs MQTT topics, ACLs, or broker hardening, hand off to the `mqtt` skill after the device is joined.
- When the question is hub choice, VLAN, or whole-home automation patterns, hand off to `smart-home` / `iot`.
- Keep this skill focused on mesh join, route, and Zigbee-specific failure modes.
