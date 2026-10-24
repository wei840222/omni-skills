# Official Sources & Technical Specifications

This document records the official Apple Developer documentation and technical guidelines for Apple TestFlight.

## Official Apple TestFlight Documentation

- **Apple TestFlight Overview**: [https://developer.apple.com/testflight/](https://developer.apple.com/testflight/)
  - Beta distribution architecture, platform support (iOS, iPadOS, macOS, tvOS, watchOS, visionOS), and public link onboarding.
- **App Store Connect TestFlight Guide**: [https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/)
  - Group quotas (up to 100 internal testers without review, up to 10,000 external testers via email or public links requiring Beta App Review), and 90-day build lifecycle.
- **App Store Connect REST API**: [https://developer.apple.com/documentation/appstoreconnectapi](https://developer.apple.com/documentation/appstoreconnectapi)
  - REST endpoints for automating build uploads, managing beta groups (`betaGroups`), submitting for beta review (`betaAppReviewSubmissions`), and generating API bearer tokens (JWT).
- **App Store Connect Build Uploads**: [https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/)
  - Distribution procedures, processing stages, and release management through Xcode, altool, or Transporter.
- **Complying with Encryption Export Regulations**: [https://developer.apple.com/documentation/security/complying_with_encryption_export_regulations](https://developer.apple.com/documentation/security/complying_with_encryption_export_regulations)
  - Export compliance declarations (ITSAppUsesNonExemptEncryption) and encryption exemption documentation.
