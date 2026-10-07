# Raspberry Pi Maintenance Rules

Domain rules for flagship Raspberry Pi SBCs. Prefer model-specific official docs in `sources.md` when a claim is version-sensitive.

## Power Supply Issues

- Undervoltage is a hardware stop-the-line: on Pi 1–4 the red PWR LED dims/flickers when the 5 V rail sags; random crashes, SD corruption, and “weird” USB behavior often follow.
- All models need a stable ~5.1 V supply; current rises with model and peripherals.
- Official guidance (Raspberry Pi documentation power-supplies):
  - Pi 1 / 2 / 3: 2.5 A micro-USB supply recommended
  - Pi 4 / 400: 3 A USB-C supply recommended
  - Pi 5: 27 W USB-C Power Supply recommended
- USB peripherals share the board power budget — use a powered hub for multiple hungry devices.
- Prefer the official PSU over bargain chargers that cannot hold voltage under load.
- No Raspberry Pi model supports USB-PPS negotiation quirks as a design target; third-party multi-port PD supplies can renegotiate when another device is plugged in.

## Storage Reliability

- microSD cards wear out under heavy writes (databases, container volumes, verbose logs); months-to-failure is common on cheap cards.
- Prefer USB mass-storage or NVMe boot where the model supports it (Pi 3B+ and later flagship USB host boot paths; Pi 5 NVMe via PCIe/M.2 HAT+). Keep microSD for light workloads or bootloader-only roles when root lives on SSD.
- Use reputable cards (high endurance / known brands). Generic no-name cards are a reliability defect, not a cost optimization.
- For kiosks and appliances, enable an overlay/read-only root (`raspi-config` Performance → overlay filesystem) so power loss does not corrupt the writable layer.
- External disks: identify with `lsblk`/`blkid`, mount by UUID in `fstab`, install `exfat-fuse` / `ntfs-3g` only when the filesystem requires it. Raspberry Pi OS Lite does not automount.

## GPIO Dangers

- User GPIO is **3.3 V logic only**. 5 V on an input can permanently damage the SoC; there is no on-board 5 V protection on those pins.
- Header is 40-pin, 2.54 mm pitch on current boards (unpopulated on non-H Zero/Pico variants).
- Two 5 V pins and two 3.3 V pins exist on the header for powering peripherals — do not treat 5 V pins as GPIO inputs.
- Default pin roles matter: I2C (GPIO2/3), SPI, UART (GPIO14/15), and hardware PWM (GPIO12/13/18/19) need explicit free-up via `raspi-config` / device-tree overlays when you need those pins as GPIO.
- Do not drive motors or high-current loads from GPIO — use an H-bridge or motor controller board.
- LEDs need series resistors. Add users to the `gpio` group for non-root access. `pinout` (GPIO Zero) shows the live map.
- Prefer GPIO Zero for Python examples; verify alternate-function conflicts before enabling stacks (HATs, fans, overlays).

## Network Setup Traps

- Set Wi-Fi country/regulatory domain or the radio may refuse to associate.
- Headless SSH on a fresh image:
  - Prefer Raspberry Pi Imager → Customisation → Remote Access → Enable SSH (password or public key).
  - Manual fallback: empty file named `ssh` (no extension) in the boot firmware partition (`/boot/firmware/ssh` on running systems), then reboot. `ssh.txt` is wrong.
- Default SSH server is disabled until enabled.
- Prefer **DHCP reservation on the router** for stable addresses. Device-local static IP via `nmcli` is supported but easy to misconfigure (pool conflicts, wrong gateway/DNS).
- Do **not** port-forward SSH to the internet. Use Tailscale, Raspberry Pi Connect, Cloudflare Tunnel, or WireGuard instead.
- Hostname: ASCII letters, digits, hyphens only; mDNS as `hostname.local` on typical home LANs.

## Docker on Pi

- Match image architecture: `linux/arm64` on 64-bit OS, `linux/arm/v7` on 32-bit. Many `amd64`-only images will not run.
- 32-bit userland memory ceilings hurt large workloads — prefer 64-bit Raspberry Pi OS on 4 GB+ boards.
- Official Docker docs still publish a Raspberry Pi OS (32-bit/armhf) Engine install path and note 32-bit deprecation toward Engine v29+; on 64-bit Pi OS follow the Debian/arm64 Engine install path instead of cargo-culting outdated `apt` docker packages.
- Convenience script `curl -fsSL https://get.docker.com | sh` remains a common bootstrap; still verify the installed arch and version afterward.
- Keep container writable layers and volumes off failing microSD media — bind-mount to SSD/NVMe.

## Headless Setup

- Configure hostname, Wi-Fi, user, and SSH in Raspberry Pi Imager **before** first boot.
- Default `pi`/raspberry-style first-user flows are deprecated; create a custom username and strong password (or key-only SSH).
- First boot can take several minutes (filesystem resize, generate keys) — wait before declaring the board dead.
- After boot: `sudo apt update && sudo apt full-upgrade` for the current major OS; major-version jumps (e.g. Bookworm → newer) are reinstall-from-image, not in-place dist-upgrade theater.
- Prefer APT for normal firmware/kernel updates; `rpi-update` is for explicit engineering/testing instructions only.

## Performance Tuning

- Headless boards can reduce GPU memory reservation when no display is required (`config.txt` memory options such as low `gpu_mem` where still applicable to the platform generation).
- Prefer zram over swap-on-SD for low-RAM models.
- Disable unused radios/desktop components when the role is appliance-only.
- Pi 5: be aware of USB current-limit and PCIe speed options in `raspi-config` when attaching hungry NVMe/USB devices.
- Overlays/read-only root for kiosk durability (see Storage).

## Troubleshooting Patterns

- **Pi 1–4:** red PWR LED off/flickering → power integrity first; green ACT flashing patterns encode boot/storage activity and some fault classes (see official LED behaviour docs).
- **Pi 5 / 500 / 500+:** bi-colour LED — red at apply-power, green when firmware/OS is up; green flashes off for microSD activity (may not flash the same way when root is on NVMe/SSD).
- Red-only / no boot attempt → supply, cable, or polyfuse/port issues before OS recovery.
- No HDMI output — connect display before power on many configurations; hot-plug is unreliable.
- Kernel panic on boot after heavy SD writes → assume media corruption; reflash known-good image onto fresh media.
- SSH connection refused — confirm SSH enabled, correct IP/mDNS name, user, and local firewall.
- When USB host boot was OTP-enabled on older Pi 3-class boards, remember OTP is permanent; do not casually program boot OTP.

## Decision boundaries

| Symptom / goal | Do this first | Hand off when |
|---|---|---|
| Crashes + undervoltage LED | Replace PSU / remove USB load | Generic kernel panic with solid 5 V |
| DB/container eats SD | Move root/data to SSD/NVMe | Pure Docker app bug on healthy disk |
| HAT uses 5 V sensors | Level shift / reject module | Higher-level home-automation design (`smart-home`/`iot`) |
| Need remote shell | Tailscale / Pi Connect / WireGuard | Cloud VPC design unrelated to the Pi |
| Generic apt/systemd failure | Still fine here if board-local | Multi-host Linux fleet → `linux` |
