# File-operation knowledge sources

Read this reference only when explaining the safety rationale behind duplicate verification or recoverable deletion. These sources inform the workflow; they are not runtime dependencies.

## Duplicate verification

- **NIST, FIPS PUB 180-4: Secure Hash Standard** — https://csrc.nist.gov/pubs/fips/180-4/upd1/final
  - A full cryptographic digest is the final duplicate-verification step after size and small-content filters. The filters reduce work; only the full digest determines whether files are treated as identical.

## Recoverable deletion

- **freedesktop.org, Trash specification** — https://freedesktop.org/wiki/Specifications/trash-spec/
  - Trash is a recoverable-deletion model. This skill therefore prefers a host-native trash interface and requires an explicit user-approved recovery location when no such interface is available.
