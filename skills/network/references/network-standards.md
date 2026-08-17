# Network standards reference

Load this reference when verifying a port-range, private-address, DNS, TLS, or certificate-lifetime claim before advising a user or changing network configuration.

## Authoritative sources

- [IANA Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) — System Ports (0–1023), User Ports (1024–49151), and Dynamic and/or Private Ports (49152–65535). Treat registrations as conventions; choose firewall policy from the actual service and traffic.
- [RFC 1918 — Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918) — private IPv4 address blocks: `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.
- [RFC 2181 §10.1 — Clarifications to the DNS Specification](https://www.rfc-editor.org/rfc/rfc2181#section-10.1) — a CNAME owner name cannot hold other resource-record types. Check the DNS provider’s documentation for any apex-alias implementation.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — TLS 1.3 protocol specification and TLS 1.2 implementation updates.
- [Let’s Encrypt integration guide](https://letsencrypt.org/docs/integration-guide/) — certificate and TLS-operation guidance. Confirm certificate lifetime and renewal behavior with the current issuer documentation instead of relying on a fixed duration.

## Verification rule

For a live network incident, collect the target hostname, address family, transport protocol, port, client location, timestamp, and a redacted command result. Interpret the result in the context of the configured resolver, route, firewall, and service listener; one probe does not establish a global outage.
