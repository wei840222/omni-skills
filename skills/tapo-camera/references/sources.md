# Sources - Tapo Camera

Primary references for local Tapo discovery, RTSP/ONVIF capture, and helper tooling. Re-check these pages before hard firmware or API claims.

## Discovery and device control

- **python-kasa documentation** — local TP-Link/Kasa/Tapo discovery and device control via https://python-kasa.readthedocs.io/
- **python-kasa GitHub repository** — library behavior, camera module notes, and release history via https://github.com/python-kasa/python-kasa
- **python-kasa PyPI** — package install surface used by the skill helper via https://pypi.org/project/python-kasa/

## Local streaming and capture

- **FFmpeg Protocols: RTSP** — one-frame still capture transport and URL handling via https://ffmpeg.org/ffmpeg-protocols.html#rtsp
- **ONVIF developers overview** — device-service capability checks on LAN via https://www.onvif.org/profiles/developers/
- **TP-Link Tapo support hub** — product/model support entry point for RTSP/ONVIF third-party compatibility guidance via https://www.tp-link.com/us/support/download/tapo/

## Security and local-first boundaries

- Keep camera credentials and authenticated RTSP URLs out of chat, git, and durable notes.
- Prefer maintained `python-kasa` + local RTSP/`ffmpeg` before any unofficial API fallback.
- Default to one still image on the trusted LAN; cloud upload is explicit opt-in only.
