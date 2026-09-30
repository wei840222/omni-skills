# WireGuard sources

Checked 2026-09-30. Re-open the live page before restating protocol or tooling claims.

## Project and protocol

- **WireGuard official site** — product overview and entry points.
  - https://www.wireguard.com/
- **Quick start** — first-tunnel orientation.
  - https://www.wireguard.com/quickstart/
- **Install** — platform packages and apps.
  - https://www.wireguard.com/install/
- **Cross-platform** — client matrix and shared concepts.
  - https://www.wireguard.com/xplatform/
- **Protocol page** — design summary and cryptography overview.
  - https://www.wireguard.com/protocol/
- **Whitepaper (PDF)** — formal protocol description.
  - https://www.wireguard.com/papers/wireguard.pdf

## Tools man pages

- **`wg(8)`** — keygen, show, set, syncconf.
  - https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8
- **`wg-quick(8)`** — conf format, DNS, PreUp/PostUp, routing helpers.
  - https://git.zx2c4.com/wireguard-tools/about/src/man/wg-quick.8

## Adjacent standards note

- RFC 9227 is reachable general reading on related IETF work; prefer the WireGuard project pages and man pages for operator defaults used by this skill.
  - https://datatracker.ietf.org/doc/html/rfc9227

## What this skill does not treat as a live measurement

Example tunnel subnets, keepalive `25`, and ListenPort `51820` are common operational defaults/examples—not universal mandates. Provider firewall UI labels and mobile app field names change; verify on the target platform.
