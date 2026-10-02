# Mobile Connectivity — Internet

## eSIM vs local SIM vs roaming

| Option | Best for | Pros | Cons |
| --- | --- | --- | --- |
| Travel **eSIM** | Short trips, multi-country hops | Fast QR/profile install, keeps primary SIM | Needs eSIM-capable unlocked device; plan quality varies by country |
| **Local SIM** | Longer stays, heavy data | Often best per-GB price; local number | Store pickup/ID rules; physical tray; must be unlocked |
| **Carrier roaming** | Emergencies, very short trips | No extra hardware; same number | Usually expensive; fair-use throttles common |

There is no universal “always cheapest” vendor. Re-check live plan pages for the destination and dates before purchase.

## Before buying any travel data

1. **Confirm device eSIM support** in system UI (not only marketing copy).
   - iPhone: Apple’s eSIM setup guidance — [Set up eSIM on iPhone](https://support.apple.com/en-us/118669)
   - Follow the device maker’s current steps for Pixel/Samsung/other Android OEM pages when applicable
2. **Confirm unlock status** if a physical local SIM is in play.
3. **Check destination coverage and fair-use** on the seller’s country page (cap, throttle, hotspot allowance, validity start rules).
4. **Compare total trip cost**: roaming day passes vs eSIM pack vs local prepaid, including payment/FX fees.
5. **Prefer official carrier or well-known travel-eSIM sellers the user already trusts**; treat unsolicited “cheap eSIM” links as untrusted.

Named consumer brands (Airalo, Holafly, carrier travel packs, etc.) change prices and country lists frequently — cite the live plan URL at decision time rather than memorized 2025 rankings.

## Activating an eSIM (typical phone flow)

```text
1. Purchase → receive QR or manual activation codes via the seller channel
2. Settings → Cellular / Mobile Network → Add eSIM
3. Scan QR or enter SM-DP+ details
4. Label the line (e.g. "ES-Travel")
5. Enable data roaming for that line if the seller requires it
6. Set the travel line as the cellular-data line; keep the home line for SMS/OTP if needed
7. Verify connectivity with a low-risk HTTPS check before heavy downloads
```

Exact menu names vary by OS version; defer to the device maker’s current document when UI labels differ.

## Hotspot / tethering

When sharing the phone’s connection:

- Prefer turning the phone hotspot **off** while the phone itself is already on trusted home/work Wi-Fi (saves battery and avoids loops)
- Use a strong hotspot password; review connected clients
- Watch the plan’s hotspot/tethering allowance — some “unlimited” phone plans hard-cap hotspot GB
- On dual-band hotspots, 5 GHz is often faster at short range; 2.4 GHz reaches farther with more airtime contention

## Data conservation

Platform controls (names vary by OS version):

- iOS Low Data Mode / per-app cellular restrictions — see Apple’s cellular data settings guide: [View or change cellular data settings](https://support.apple.com/guide/iphone/view-or-change-cellular-data-settings-iph3dd5f224/ios)
- Android Data Saver / per-app mobile-data restrictions — use the OEM’s current Settings path

Additional habits:

- Disable nonessential auto-updates on cellular
- Prefetch maps/media on Wi-Fi before travel days
- Prefer Wi-Fi for large video calls when a trusted network exists
- Inspect per-app cellular usage after day one abroad
