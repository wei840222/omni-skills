# Discovery And Auth - Tapo Camera

Use this file when the user wants to confirm that a Tapo camera is reachable, authenticated correctly, and capable of local streaming before taking a capture.

## Discovery Ladder

1. Confirm the exact host or DHCP-reserved name if the user knows it.
2. If the host is unknown, use the maintained CLI first:

```bash
kasa discover
```

3. Once the host is known, validate camera auth and capabilities:

```bash
kasa --type camera --host 192.168.1.50 \
  --username "$TAPO_CAMERA_USERNAME" \
  --password "$TAPO_CAMERA_PASSWORD" \
  device state
```

4. If the device responds, note:
- model
- alias
- firmware
- whether the camera module is exposed

Wait for a single state check to succeed before attempting repeated capture.

## Credential Handling

- Inject credentials from a secret manager or short-lived environment variables.
- Exclude raw camera credentials from chat.
- Treat `KASA_CREDENTIALS_HASH` as a secret-equivalent transport artifact, not as a safe public identifier.
- Save only non-sensitive metadata in `<state_root>/`, excluding credentials or authenticated URLs.

## Third-Party Compatibility

For RTSP and ONVIF workflows, the camera usually needs third-party compatibility enabled in the Tapo app with a camera account configured there.

Before blaming the toolchain, verify:
- RTSP is enabled
- ONVIF is enabled if the user needs ONVIF
- the camera account is set
- privacy mode or lens mask is not blocking the stream

## Direct Camera vs Hub Child

Direct cameras are the easiest path for RTSP and ONVIF.
Hub children, battery models, and some low-power devices may not expose a direct local stream surface even when discovery works.

If the user has one of those:
- confirm the exact model
- Verify specific RTSP implementations before making assumptions
- move to `api-fallback.md` only after the local stream path is ruled out
