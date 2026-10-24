# Official Sources & Deployment Standards

This document records the official standards, GitOps frameworks, and supply chain security specifications for software deployment.

## GitOps & Deployment Engines

- **Argo CD Documentation**: [https://argo-cd.readthedocs.io/en/stable/](https://argo-cd.readthedocs.io/en/stable/)
  - Declarative GitOps continuous delivery, automated sync policies, rollback strategies, and health assessment checks.
- **Flux CD Documentation**: [https://fluxcd.io/flux/](https://fluxcd.io/flux/)
  - GitOps Toolkit components, Kustomize/Helm controllers, automated image updates, and multi-tenant reconciliation.

## Software Supply Chain & Artifact Security

- **SLSA (Supply-chain Levels for Software Artifacts)**: [https://slsa.dev/](https://slsa.dev/)
  - Security framework for source integrity, build provenance generation, and tamper-resistant deployment controls.
- **Sigstore Security Documentation**: [https://docs.sigstore.dev/](https://docs.sigstore.dev/)
  - Container signing, keyless verification via OIDC identity, and immutable artifact provenance logging.
