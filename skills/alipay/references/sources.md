# Research Sources — Alipay Open Platform & Global Payments

Primary documentation, gateway endpoints, and security specifications for Alipay integrations.

## Official Platform Documentation

- **Alipay Open Platform Documentation** — https://opendocs.alipay.com/open/
  - Core architecture, app creation, sandbox configuration, and developer toolkits.
- **API Gateway & Request Signing (RSA2 / SM2)** — https://opendocs.alipay.com/common/02kdnc
  - SHA256withRSA (RSA2) signature generation and verification, certificate-based signing, and character encoding requirements.
- **Asynchronous Notification & Verification** — https://opendocs.alipay.com/open/203/105286
  - POST callback parameter parsing, signature verification with Alipay public key, and idempotent response handling (`success`).
- **Sandbox Environment Guide** — https://open.alipay.com/develop/sandbox/app
  - Gateway endpoint (`https://openapi-sandbox.dl.alipaydev.com/gateway.do`), sandbox test accounts, and wallet app APKs.
