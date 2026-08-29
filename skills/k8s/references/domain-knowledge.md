# Kubernetes Domain Knowledge

Verified source notes used for Gate 6 research during the `k8s` refactor. Prefer these official docs over memory when cluster behavior is disputed.

## Workload lifecycle and probes

- Pod lifecycle — phases, restart policy, and termination via https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
- Configure Liveness, Readiness and Startup Probes — via https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
- Container Lifecycle Hooks (`preStop` / `postStart`) — via https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/

## Resources, QoS, and scheduling

- Resource Management for Pods and Containers — via https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- Pod Quality of Service Classes — via https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/
- Assigning Pods to Nodes (affinity, taints/tolerations, node selectors) — via https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
- Taints and Tolerations — via https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/

## Networking and traffic

- Service — via https://kubernetes.io/docs/concepts/services-networking/service/
- EndpointSlices — via https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
- DNS for Services and Pods (`ndots`, search domains) — via https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
- Ingress — via https://kubernetes.io/docs/concepts/services-networking/ingress/
- Gateway API overview — via https://gateway-api.sigs.k8s.io/

## Storage and stateful workloads

- Persistent Volumes — via https://kubernetes.io/docs/concepts/storage/persistent-volumes/
- Storage Classes — via https://kubernetes.io/docs/concepts/storage/storage-classes/
- StatefulSets — via https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/

## Security, RBAC, and admission

- Using RBAC Authorization — via https://kubernetes.io/docs/reference/access-authn-authz/rbac/
- Pod Security Admission — via https://kubernetes.io/docs/concepts/security/pod-security-admission/
- Configure a Security Context for a Pod or Container — via https://kubernetes.io/docs/tasks/configure-pod-container/security-context/

## Cluster operations

- Deployments (rolling update / rollback) — via https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- Disruptions and PodDisruptionBudgets — via https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
- Horizontal Pod Autoscaling — via https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
- API Priority and Fairness — via https://kubernetes.io/docs/concepts/cluster-administration/flow-control/

## Obsolete knowledge corrected

- Prefer portable `<state_root>` / `<workspace>/...` paths over hard-coded `~/Clawic/data/...` locations.
- Prefer EndpointSlices over legacy Endpoints for Service readiness checks.
- Prefer startupProbe for slow booters instead of guessing a large `initialDelaySeconds`.
- Route DaemonSet / control-plane / backup depth into existing `references/nodes.md` and `references/production.md` rather than inventing absent standalone files.
