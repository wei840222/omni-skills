## Baseline hardening

- **Floor:** WPA2-Personal (AES/CCMP). **Prefer:** WPA3-Personal with Simultaneous Authentication of Equals (SAE) when every needed client supports it ([Wi-Fi Alliance security overview](https://www.wi-fi.org/discover-wi-fi/security)).
- Standardize on WPA2-Personal (AES) or WPA3-Personal; migrate any remaining WEP or original WPA/TKIP BSS to those modes.
- Leave **WPS** (push-button and PIN) turned off on production APs. PIN mode is a well-known brute-force path even with a strong passphrase.
- A **hidden SSID** still leaks in probe behavior; clients often broadcast the name when searching. Treat hiding as cosmetic, not access control.
- **MAC allow-lists** are trivial to bypass once addresses are observed on the air — use only as light inventory hygiene, never as the main lock.

## Guest and IoT networks

- Put untrusted and IoT devices on an **isolated guest SSID** so they cannot initiate connections to primary LAN hosts.
- Use a **separate passphrase** (`<GUEST_WLAN_PASSPHRASE>`) so you can rotate guest access without rotating the main network.
- Enable guest **bandwidth limits** when the AP supports them to stop a single guest from saturating airtime/WAN.
- For typical homes, a captive portal is optional; a WPA2/WPA3 passphrase on an isolated SSID is enough.

## Admin plane

- Change the default router admin password; keep admin off guest SSIDs.
- Prefer HTTPS/on-LAN admin only; avoid exposing WUI to the WAN.
- Store passphrases outside git; examples use placeholders only.
