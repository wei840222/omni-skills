# 2.4GHz Interference

Zigbee shares the 2.4GHz band with Wi-Fi. Channel overlap is a first-class design input, not an afterthought.

## Practical channel map

| Zigbee channel | Rough Wi-Fi conflict | Notes |
|----------------|----------------------|-------|
| 11 | Wi-Fi channel 1 region | Common default and often crowded |
| 15-20 | Mid Wi-Fi overlap risk | Depends on local AP plan |
| 25 | Near Wi-Fi channel 11 edge | Often used to escape low-channel Wi-Fi |
| 26 | Region/stack dependent | Verify adapter and regional support before relying on it |

Exact center frequencies and legal limits vary by region and adapter. Re-check `references/sources.md` and the stack docs before locking a production channel.

## Planning rules

- Default Zigbee channel 11 is often the worst choice in homes that leave Wi-Fi on channel 1.
- Pick non-overlapping Zigbee and Wi-Fi plans once, then keep them stable.
- Changing the Zigbee channel usually requires re-pairing all devices. Do not channel-hop casually after the mesh is populated.
- Dense apartment Wi-Fi can still hurt a "free" channel; add routers and improve placement before endless channel roulette.

## Mitigation order

1. Separate Zigbee from the loudest home Wi-Fi primary channel.
2. Move the coordinator away from APs, USB3 ports, and metal enclosures.
3. Add mains-powered routers so leaves are not one weak hop from the stick.
4. Only then consider a coordinated channel migration with a full re-pair window.
