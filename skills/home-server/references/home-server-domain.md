# Home-server operational references

Load this reference when a plan needs source-backed security, container, or network guidance. Apply the source to the user’s stated platform and authorization boundary rather than treating it as a deployment instruction.

## Secure exposure and administration

- CISA recommends MFA for network-device administration, management of administrative credentials, firmware integrity, and regular device monitoring. Apply those controls to routers, switches, and management planes where the hardware supports them.
  Source: [CISA — Securing Network Infrastructure Devices](https://www.cisa.gov/news-events/news/securing-network-infrastructure-devices)
- Use the router/vendor documentation as the authority for model-specific firewall, remote-management, and firmware procedures; confirm the exact device model before proposing changes.

## Docker isolation and production operation

- Docker documents the daemon attack surface, Linux capabilities, namespaces, cgroups, user-namespace remapping, rootless mode, and protection of the Docker socket. Choose the controls compatible with the host and service requirements rather than assuming that containers form a complete security boundary.
  Source: [Docker Engine security](https://docs.docker.com/engine/security/)
- Docker’s Compose production guidance covers keeping a Compose application production-ready and configuring it for the target environment.
  Source: [Docker Compose production](https://docs.docker.com/compose/how-tos/production/)

## Skill-package facts

- The `home-server` package itself is portable guidance; it must not claim a particular router model, container version, image tag, or vendor procedure without verifying the current authoritative documentation.
