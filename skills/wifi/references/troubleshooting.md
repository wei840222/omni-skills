## Band selection

- 2.4 GHz penetrates walls better but is congested — neighboring BSS and household interferers share the band.
- 5 GHz is typically faster with shorter range — edge rooms may need another AP rather than forcing a weak 5 GHz associate.
- Same SSID on multiple bands can leave clients sticky on a weak 5 GHz BSS — check client band-steering and RSSI before blaming the ISP.
- 6 GHz (Wi-Fi 6E and Wi-Fi 7 capable gear) needs client and AP support — unsupported clients fall back to 5 GHz or 2.4 GHz.
- **Wi-Fi 7 (802.11be)** introduces Multi-Link Operation (MLO), which can use multiple bands/links together for lower latency and higher throughput when both AP and client implement it ([Wi-Fi Alliance Wi-Fi 7](https://www.wi-fi.org/discover-wi-fi/wi-fi-certified-7)).

## Channel interference

- 2.4 GHz has three generally non-overlapping 20 MHz channels in most regions: **1, 6, 11** — other center channels overlap those primaries.
- "Auto" channel pick can land on a busy DFS or crowded channel — scan neighbors and set manually in dense apartments.
- 5 GHz offers more channels; **DFS** channels may pause for radar detection and cause brief disconnects near airports/weather radar.
- Microwave ovens commonly slam 2.4 GHz near channel 11 — kitchen dead zones are often interference, not "broken Wi-Fi".
- USB 3.0 devices and some poorly shielded docks radiate into 2.4 GHz — move the stick/dock or prefer 5/6 GHz for the affected client.

## Speed issues

- "Connected" is not "good" — read RSSI/noise; roughly below about −70 dBm interactive use suffers.
- WLAN is a shared medium — more active stations cut per-client airtime.
- PHY rate marketing numbers are peak; real application throughput is often ~50–70% of the link rate under good conditions.
- Legacy 2.4 GHz rates and protection mechanisms slow the whole BSS — isolate ancient IoT on a guest SSID when possible.

## Connection drops

- Expiring DHCP leases force renew/reconnect — shorten lease while testing, lengthen for stability once healthy.
- Seamless roaming needs client/AP support for assisting standards (commonly discussed as 802.11k/v/r families) — identical SSID alone only gives basic association handoff.
- Client power-save can create ping spikes — disable aggressive save on latency-sensitive endpoints when diagnosing.
- Driver/firmware regressions are common — update or roll back the Wi-Fi stack before replacing hardware.

## Diagnostics order

1. Ping the **router LAN IP** (not a public IP) to separate WLAN from WAN/ISP.
2. Walk the space while watching RSSI and retry rate.
3. Run a channel scan; prefer least-crowded non-overlapping channels.
4. Treat sustained packet loss above ~1% on an idle BSS as a signal to chase interference, duty cycle, or range — not as normal.
