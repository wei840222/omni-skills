# Official Sources & Kubernetes Specifications

This document records the official Kubernetes documentation and SIG standards for cluster operations, API deprecations, and workload manifests.

## Official Kubernetes Documentation

- **Kubernetes Documentation Home**: [https://kubernetes.io/docs/home/](https://kubernetes.io/docs/home/)
  - Core architectural concepts (Control Plane, Nodes, Workloads, Services, Storage, Cluster Administration).
- **Kubernetes Deprecated API Migration Guide**: [https://kubernetes.io/docs/reference/using-api/deprecation-guide/](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)
  - Lifecycle deprecation schedule across releases (e.g. Ingress `networking.k8s.io/v1`, removal of `PodSecurityPolicy` in favor of Pod Security Admission, FlowControl).
- **Gateway API (SIG Network)**: [https://gateway-api.sigs.k8s.io/](https://gateway-api.sigs.k8s.io/)
  - Next-generation service networking standard, GatewayClass, Gateway, and HTTPRoute specifications replacing legacy Ingress limitations.
- **Pod Security Admission (PSA)**: [https://kubernetes.io/docs/concepts/security/pod-security-admission/](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
  - Namespace-level security levels (`privileged`, `baseline`, `restricted`) and enforcement modes (`enforce`, `audit`, `warn`).
