# Sources — Raspberry Pi skill (Gate 6)

Verified during the 2026-10-07 refactor. Prefer these URLs over model memory for power, boot, GPIO, LED, networking, and Docker claims.

## Raspberry Pi official documentation (source repo)

HTML docs site may be Cloudflare-challenged from automation; the public AsciiDoc sources are authoritative and fetchable:

| Topic | URL |
|---|---|
| Documentation repository | https://github.com/raspberrypi/documentation |
| Power supplies | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/raspberry-pi/power-supplies.adoc |
| LED behaviour / blink warnings | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/configuration/led_blink_warnings.adoc |
| GPIO hardware | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/raspberry-pi/gpio-on-raspberry-pi.adoc |
| GPIO from Python | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/os/using-gpio.adoc |
| USB boot modes | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/raspberry-pi/boot-usb.adoc |
| NVMe boot | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/raspberry-pi/boot-nvme.adoc |
| Install OS / Imager | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/getting-started/install.adoc |
| Setting up (headless context) | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/getting-started/setting-up.adoc |
| SSH remote access | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/remote-access/ssh.adoc |
| Networking / DHCP / static IP | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/configuration/configuring-networking.adoc |
| Users | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/configuration/users.adoc |
| External storage | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/configuration/external-storage.adoc |
| Performance / overlay FS | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/configuration/performance.adoc |
| OS updates (`apt` vs `rpi-update`) | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/os/updating.adoc |
| raspi-config | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/configuration/raspi-config.adoc |
| config.txt memory options | https://raw.githubusercontent.com/raspberrypi/documentation/master/documentation/asciidoc/computers/config_txt/memory.adoc |

## Product / datasheet

| Topic | URL |
|---|---|
| Raspberry Pi 5 product brief (PDF) | https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf |
| Datasheets portal | https://datasheets.raspberrypi.com/ |
| OS image index (arm64 example) | https://downloads.raspberrypi.com/raspios_arm64/images/ |
| Bookworm announcement | https://www.raspberrypi.com/news/bookworm-the-new-version-of-raspberry-pi-os/ |

## GPIO ecosystem

| Topic | URL |
|---|---|
| GPIO Zero docs | https://gpiozero.readthedocs.io/en/latest/ |
| pinout.xyz | https://pinout.xyz/ |
| Linux GPIO admin guide | https://www.kernel.org/doc/html/latest/admin-guide/gpio/ |

## Docker / remote access adjacent

| Topic | URL |
|---|---|
| Docker Engine on Raspberry Pi OS (32-bit/armhf; deprecation note) | https://docs.docker.com/engine/install/raspberry-pi-os/ |
| Docker Engine on Debian (64-bit path) | https://docs.docker.com/engine/install/debian/ |
| Tailscale quickstart | https://tailscale.com/kb/1017/install/ |

## Wayback fallback for HTML docs

When `www.raspberrypi.com/documentation/...` returns 403 to bots, use Wayback snapshots such as:

- https://web.archive.org/web/20250901000000/https://www.raspberrypi.com/documentation/computers/getting-started.html

Still cross-check against the GitHub AsciiDoc sources above for the freshest text.
