# Signing and provisioning

## Core rules

- "Automatic" signing still needs a selected development team in Signing & Capabilities.
- Provisioning profile mismatch: bundle ID must match the profile App ID exactly, including case.
- "No signing certificate": open Keychain Access; confirm the certificate is valid, trusted, and not expired; confirm the private key is present.
- Device not registered: add the device UDID in the developer portal, then regenerate/download the profile.
- Headless CI: automatic signing is unreliable. Prefer manual signing with installed cert + profile, or a tightly controlled keychain unlock path.

## CI / archive signing

- Archive uses the Release configuration by default and requires valid distribution signing for device/App Store destinations.
- Simulator builds often bypass the distribution signing path that archive requires — treat them as different proof.
- `-allowProvisioningUpdates` only helps when the CI identity can access the needed portal credentials and keychain items; it is not a substitute for missing certs.

## Capabilities and entitlements

- Capability toggles in Xcode must match the entitlements file.
- Push notifications need the App ID capability **and** a profile that includes it.
- Associated Domains need a correct `apple-app-site-association` file on the server.
- Keychain sharing needs an explicit access group; the default is not "share everything".

## Safe recovery order

1. Confirm `DEVELOPMENT_TEAM`, `PRODUCT_BUNDLE_IDENTIFIER`, and profile name via `-showBuildSettings`.
2. Confirm certificate + private key in Keychain.
3. Refresh profiles in Xcode or re-download for CI.
4. Only then rotate certs / regenerate profiles.
