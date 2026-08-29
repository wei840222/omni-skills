---
name: k8s
description: 'Debugs Kubernetes workloads, reviews manifests, and plans cluster operations. Use when the user wants to troubleshoot pod failures (e.g. CrashLoopBackOff, Pending, OOMKilled), diagnose Service/Ingress or DNS issues, investigate hung rollouts, tune resources/probes, lock down RBAC/Security, or plan cluster upgrades and backups.'
metadata:
  version: "1.0.5"
  related-skills: '{"docker": "building and hardening the images k8s runs", "devops": "CI/CD pipelines that deploy to the cluster", "observability": "metrics, logs, and traces behind the dashboards you read here", "linux": "node-level debugging under the kubelet"}'
  openclaw: '{"emoji": "\u2638", "os": ["linux", "darwin", "win32"], "requires": {"bins": ["kubectl"]}}'
---


**Data.** At the start of every session, read `<state_root>/config.yaml` (what the user declared) and `<state_root>/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Open any file `## Boxes` names the moment the condition on its line applies — that index is the list of files that exist, use this index directly instead of keeping a list in your head. Check `## Due` against today's date and state any overdue item in one line: a statement, not a question. Read `<workspace>/servers/servers.md` before any capacity, sizing, upgrade, or "what do we run" question. If none of it exists, work from defaults and say nothing about it. If data sits at an old location (`~/k8s/` or `<workspace>/memory/k8s/`), move it to the resolved `<state_root>/`, and say in one line that you moved it and from where. Everything this skill reads or writes is a plain local note under the folders declared for state — nothing leaves the machine and no credential is ever written. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; preserve rows written by other skills without rewriting or deleting them, and every write and deletion is named in one line as it happens.

**Write before the session ends** whenever it produced something durable: a cluster discovered, upgraded or retired; a workload sized from real observation; an incident whose cause was finally named; a deploy with its rollback digest; a drill that was timed; an audit finding the user chose to accept; a hostname the cluster now serves; or anything they will want to read again — a runbook, a policy or manifest that finally worked, an architecture decision. `references/memory-template.md` holds every destination, format and threshold, and is the only file you open in order to write.

**Clusters and named nodes go to the shared inventory `<workspace>/servers/servers.md`**, not here: one file holds machines from every provider, so "what do we run" answers itself whichever cloud they live in. One row per cluster, identified by `Name` + `Provider` — update your own row in place instead of appending a second one. Cattle nodes in a managed pool are grouped under the cluster's row; the pool is a property of the cluster's row.

**Hostnames the cluster serves go to the shared `<workspace>/domains/domains.md`** — one row per hostname with what terminates its TLS and when the certificate expires, so a DNS or expiry question eliminates the need to read cluster objects.

**No credential is ever written anywhere under `<state_root>/`** — not in the files named here, not in a file you create, not in text the user pastes in to be saved. Store the pointer and strip the value: `env:KUBECONFIG`, `file:~/.kube/prod.yaml`, `keychain:cluster-prod`, `1password:Work/K8s/prod`, `vault:kv/prod/db`.

Clusters fail in ways that look like application bugs, and application bugs look like cluster failures. Separate the two fast, name the evidence that settled it, and refuse to guess when one `describe` would answer. Destructive moves — force-delete, PVC delete, drain, namespace delete — are proposed with their blast radius and kept out of read-only command blocks. Work from defaults immediately instead of opening with questions about their cluster, their priorities, or how proactive to be. Precedence for any value: `config.yaml` → `<workspace>/profile.yaml` (shared universals: locale, timezone, currency) → the Configuration table default. Prompt the user for confirmation before allowing an observation to overwrite a declared preference.


## State location

k8s state may exist in `<workspace>/k8s/`, `<workspace>/memory/k8s/`, or `~/k8s/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/k8s/`, `<workspace>/memory/k8s/`, `~/k8s/`.
3. If none exists and state must be created, default to `<workspace>/k8s/`.

Use the selected `<state_root>` for every state operation in this skill. Shared external state like servers and domains use standard external paths (e.g., `<workspace>/servers/servers.md`, `<workspace>/domains/domains.md`).

## When To Use

- A pod is Pending, CrashLoopBackOff, OOMKilled, ImagePullBackOff, Evicted, or stuck Terminating
- A Service, Ingress, or Gateway receives no traffic, or cluster DNS is intermittently slow
- Writing or reviewing manifests, Helm charts, or kustomize overlays: probes, resources, rollout strategy, security
- A rollout is stuck, flapping, or silently serving a broken version; a rollback needs to be safe
- Sizing requests, limits, QoS, HPA, or a cluster autoscaler that will not scale in or out
- Locking down RBAC, ServiceAccounts, NetworkPolicy, Pod Security Admission, or Secrets handling
- Node-, control-plane- and cluster-level work: drains, pressure eviction, API throttling, upgrades, backup and restore
- Not for building container images themselves — that is `docker`

## Quick Reference

| Symptom | First move |
|---|---|
| Pod Pending | `kubectl describe pod` Events name the predicate: insufficient CPU/memory (requests vs node allocatable), unbound PVC, taint without toleration, no nodeSelector match → `references/scheduling.md` |
| CrashLoopBackOff | `kubectl logs -p` (previous container). Exit 137 = SIGKILL (OOM or liveness kill), 143 = SIGTERM, 1 = app error. Backoff starts at 10s and doubles to a 5m cap, resetting after 10m of clean running → `references/debug.md` |
| OOMKilled | `describe pod` → Last State: OOMKilled. Raise the limit or fix the leak; JVM, Node, and Go runtimes each need their own cap below it → `references/resources.md` |
| ImagePullBackOff | The Events line carries the real reason: 401 (missing or wrong `imagePullSecret`), 404 (tag typo, wrong registry), or a registry rate limit → `references/debug.md` |
| Service gets no traffic | `kubectl get endpointslices -l kubernetes.io/service-name=<svc>` — empty means selector/label mismatch or zero ready pods; then check `port` vs `targetPort` → `references/networking.md` |
| Ingress returns 502/503/504 | 503 = no endpoints behind the Service; 502 = backend closed or spoke the wrong protocol; 504 = backend slower than the controller's read timeout → `references/ingress.md` |
| Intermittent DNS, ~5s stalls | `ndots:5` search expansion plus UDP conntrack races. FQDN with a trailing dot (`db.prod.svc.cluster.local.`) or `dnsConfig` `ndots:2`; NodeLocal DNSCache at cluster level → `references/dns.md` |
| Rollout stuck | `kubectl rollout status`, then `describe rs` on the newest ReplicaSet for quota, image, or admission errors. `progressDeadlineSeconds` (default 600s) only flips Progressing=False — it requires manual intervention to rollback → `references/rollouts.md` |
| Pod stuck Terminating | `metadata.finalizers` plus `deletionTimestamp`: fix the controller that owns the finalizer; force-delete is last resort → `references/operators.md` |
| Works in namespace A, fails in B | Diff ResourceQuota, LimitRange, NetworkPolicy, and PSA labels — a quota namespace rejects pods with no requests set → `references/resources.md`, `references/security.md` |
| HPA shows `<unknown>` | A container is missing resource requests (utilization = usage/requests has no denominator), or metrics-server is down → `references/autoscaling.md` |
| PVC stuck Pending | No default StorageClass, `volumeBindingMode: WaitForFirstConsumer` waiting on a schedulable pod, or a zone mismatch between disk and node → `references/storage.md` |
| StatefulSet pod-0 won't start | Ordered rollout blocks on the previous ordinal; a retained PVC may hold stale data → `references/stateful.md` |
| Node NotReady, or a drain fails to complete | Node conditions (MemoryPressure/DiskPressure/PIDPressure), then the kubelet; drains block on PDBs, bare pods, and local storage → `references/nodes.md` |
| Node agent missing on some nodes, or its rollout crawls | DaemonSet tolerations, `maxUnavailable: 1` across N nodes, priority class → `references/nodes.md` |
| CronJob stopped firing | >100 missed schedules with no `startingDeadlineSeconds` disables it permanently → `references/jobs.md` |
| An apply silently reverts | Two writers on one object (GitOps vs hotfix) or a field-manager conflict → `references/manifests.md` |
| Every create suddenly fails | An admission webhook with `failurePolicy: Fail` whose backend is down → `references/operators.md` |
| `429 Too Many Requests` from the API, or kubectl is slow cluster-wide | API Priority and Fairness, etcd latency, or a controller hot-looping the API → `references/production.md` |
| Job fails to complete, or mTLS returns 503 between two healthy pods | A mesh sidecar that fails to exit, or a policy denying the call before the app sees it → `references/networking.md` |
| GPU pod Pending with capacity free, or CUDA fails at runtime | Device plugin not registered, driver/toolkit skew, or a fractional GPU request → `references/nodes.md` |
| Data or a namespace has to come back | What the backup actually contains, and in what order it restores → `references/production.md` |
| Works locally, fails in the cluster (or the reverse) | Local clusters have no cloud LB, no real StorageClass, one node, and your credentials → `references/local-dev.md` |
| About to run a destructive command | `kubectl config current-context` first; `prod_context` and `destructive_confirm` govern the rest → `references/local-dev.md` |
| Anything else | `kubectl get events -n <ns> --sort-by=.lastTimestamp`, then `describe` the object it names |

Depth on demand: `references/debug.md` symptom→cause chains · `references/commands.md` kubectl incident toolkit · `references/scheduling.md` placement, taints, affinity, preemption · `references/resources.md` requests, limits, QoS, throttling, quotas · `references/probes.md` liveness, readiness, startup, lifecycle hooks · `references/rollouts.md` deploy strategies, PDB, rollback · `references/networking.md` Services, EndpointSlices, kube-proxy, NetworkPolicy, sidecars/mTLS · `references/dns.md` CoreDNS, ndots, conntrack · `references/ingress.md` Ingress, Gateway API, TLS · `references/storage.md` PV, PVC, StorageClass, snapshots · `references/stateful.md` StatefulSets and databases · `references/production.md` backup/restore, upgrades, APF, DR, cost · `references/config-and-secrets.md` ConfigMaps, Secrets, external stores · `references/rbac.md` permissions and escalation paths · `references/security.md` Pod Security, securityContext, supply chain · `references/jobs.md` Jobs and CronJobs · `references/nodes.md` node lifecycle, drains, pressure, DaemonSets, accelerators · `references/autoscaling.md` HPA, VPA, KEDA, cluster autoscaler · `references/manifests.md` apply semantics, kustomize, Helm, GitOps · `references/operators.md` CRDs, controllers, finalizers, webhooks · `references/local-dev.md` kind/minikube/k3d and kubeconfig context safety · `references/domain-knowledge.md` verified Kubernetes docs and Gate 6 sources · `references/memory-template.md` durable memory boxes.

## Core Rules

1. **Memory requests = limits on every production container.** Overcommitted memory means the node OOM-kills someone when neighbors burst — and the victim is chosen by QoS class, not by who leaked. CPU: always set requests; limits follow `cpu_limits_policy` (→ Where Experts Disagree).
2. **Give slow starters a startupProbe instead of guessing `initialDelaySeconds`.** Boot budget = `failureThreshold × periodSeconds`: 30 × 10s = 300s covers a slow JVM while liveness stays tight for steady state.
3. **Detection latency = `periodSeconds × failureThreshold`.** Defaults (10s × 3) mean up to 30s of traffic to a dead pod before endpoint removal — tune both factors, not just one.
4. **Readiness gates traffic, liveness restarts, neither reschedules.** A restart happens in place on the same node; only eviction or deletion moves a pod. Restarting a pod cannot fix a node problem.
5. **Shutdown contract: app handles SIGTERM + `preStop` sleep 5-10s + `terminationGracePeriodSeconds` (default 30s) > real drain time.** Endpoint removal propagates asynchronously, so pods keep receiving traffic after SIGTERM — the sleep covers exactly that window.
6. **Diagnose in fixed order: events → previous logs → endpoints → exec.** Guessing skips the one cheap step that would have named the cause (→ The First Five Minutes). Events expire after 1h by default (`--event-ttl`) — capture them before touching anything.
7. **Requests drive both scheduling and HPA math.** `desired = ceil(current × usage/target)`; 3 replicas at 90% usage with a 60% target → `ceil(3 × 90/60)` = 5. Undersized requests inflate utilization and overscale.
8. **Pin images by digest or an immutable tag.** `latest` + `imagePullPolicy: IfNotPresent` means each node runs whatever it cached — different code per node, undebuggable. Note the default: pull policy is `Always` when the tag is `latest` or absent, `IfNotPresent` otherwise.
9. **See the diff before the cluster does.** `kubectl diff -f` and `--dry-run=server` run defaulting, admission, and webhooks; `--dry-run=client` runs none of them and passes manifests that the API server will reject (`apply_gate`).
10. **A number that took a traffic cycle to measure gets written down.** Observed peak memory, p90 CPU, real drain time, measured RTO, the boot budget that finally held: each cost hours of observation and is worthless in your head. Their home is `## Workloads` in `memory.md` (or the file its `## Boxes` line names); re-deriving them next quarter is the most expensive habit in this skill.

## The First Five Minutes

1. `kubectl get events -n <ns> --sort-by=.lastTimestamp | tail -30` — capture first; the 1h TTL destroys evidence while you theorize.
2. `kubectl describe pod <pod>` — the Events block explains scheduling failures, image errors, probe failures, and OOM kills in one place.
3. `kubectl logs <pod> -p --tail=100` — previous container after any restart. Current logs are empty precisely because it just restarted.
4. `kubectl get endpointslices -l kubernetes.io/service-name=<svc>` — separates "the app is broken" from "the app was never wired up".
5. `kubectl debug -it <pod> --image=busybox --target=<container>` (kubectl >=1.25) — the pod's own view of DNS, reachability, and files.

Only when 1-5 all point outside the pod does the node become the suspect (`references/nodes.md`), and only when every namespace is affected at once does the control plane (`references/production.md`). Write down which step produced the finding: it names the file to open next. How much of that chain you narrate back follows `explain_depth`. Before starting, check `## Incident History` in `memory.md` — a shape you have seen before may already have a runbook in `artifacts/`.

## Status Decoder

| Status / signal | Means | Next |
|---|---|---|
| `Pending`, no node assigned | Scheduler rejected every node; Events name the predicate | `references/scheduling.md` |
| `ContainerCreating` > 2 min | Volume attach, image pull, or CNI IP allocation is stuck | `describe` Events, then `references/storage.md` or `references/networking.md` |
| `Init:0/2` | An initContainer is failing or waiting; app containers fail to start | `logs -c <init-container>` |
| `ImagePullBackOff` / `ErrImagePull` | Auth, name/tag, or registry rate limit | `references/debug.md` |
| `CreateContainerConfigError` | A referenced ConfigMap/Secret or key does not exist | `references/config-and-secrets.md` |
| `CrashLoopBackOff` | Container exits repeatedly; backoff 10s → 5m cap | `logs -p`, `references/debug.md` |
| Exit 1 / app-specific code | Application exited on its own | App logs; config or dependency |
| Exit 137 with `OOMKilled: true` | cgroup memory limit hit | `references/resources.md` |
| Exit 137 with `OOMKilled: false` | SIGKILL after the grace period expired — a liveness kill or a delete whose SIGTERM was ignored | `references/probes.md`, `references/rollouts.md` |
| Exit 143 | Clean SIGTERM shutdown; usually not a bug | — |
| Exit 126 / 127 | Entrypoint not executable / not found (wrong arch, musl vs glibc) | `docker` skill |
| `Evicted` | Node pressure; QoS class chose the victim | `references/nodes.md` |
| `Completed` but restarting | `restartPolicy: Always` on a batch workload | `references/jobs.md` |
| `NotReady` on a Job pod that finished | A sidecar that fails to exit keeps the pod alive | `references/networking.md` |
| `Terminating` past the grace period | Finalizer held, or the kubelet is unreachable | `references/operators.md`, `references/nodes.md` |
| `Unschedulable` after running fine | Node cordoned, drained, or its taints changed | `references/nodes.md` |
| `429` / `Timeout` from kubectl itself | API Priority and Fairness throttling, or an unhealthy control plane | `references/production.md` |
| Any other status, or a status that contradicts the symptom | The phase string is a summary, not a diagnosis — Events and the previous container's logs are | `describe` the pod, then `references/debug.md` |

## Resources and QoS

- Requests are scheduling-time only. Limits are enforced: memory by cgroup OOM kill, CPU by CFS quota inside every 100ms period.
- QoS decides eviction order under node pressure: BestEffort (no requests) dies first, then Burstable pods exceeding requests, Guaranteed (requests = limits for both CPU and memory) last.
- Units: 1 CPU = 1000m. Memory `Mi` = 2^20, `M` = 10^6 — and a lone `m` suffix on memory means millibytes (→ Traps).
- CPU throttling starts well below 100% average usage: a bursty app drains its quota inside one 100ms window and stalls until the next. Symptom is p99 latency spikes at low average CPU.
- LimitRange injects defaults into pods that omit requests; ResourceQuota rejects those pods outright. Same manifest, different namespace, different outcome.

Sizing method, runtime-specific heap caps, quota arithmetic, and throttling forensics: `references/resources.md`. The numbers a sizing pass produces belong in `## Workloads` (Core Rule 10).

## Output Gates

Before emitting a manifest (or approving one in review), verify:

- Memory request = limit; CPU request present, CPU limits per `cpu_limits_policy`?
- Readiness probe present; liveness in-process only; startupProbe wherever boot can exceed 30s?
- `terminationGracePeriodSeconds` above real drain time, and a `preStop` sleep for endpoint propagation?
- Image pinned to a digest or immutable tag, pin tags or use a digest instead of `latest`?
- securityContext matches `psa_level`: `runAsNonRoot`, numeric UID, `allowPrivilegeEscalation: false`, capabilities dropped?
- Labels follow `label_scheme`, and the Deployment selector is the one you can live with forever?
- PDB present for every workload above 1 replica, and looser than the replica count?
- Namespace realities checked: ResourceQuota, LimitRange, NetworkPolicy, PSA labels?
- Verified through `apply_gate` (`kubectl diff -f` or `--dry-run=server`), not client-side validation?

And before ending any session, not only a manifest one:

- Did this session produce something durable — a cluster fact, a measured number, an incident cause, a deploy digest, a timed drill, an accepted finding, a runbook, a working policy? Then it is written to its box (`memory.md`, the file its `## Boxes` line names, `artifacts/`, `<workspace>/servers/servers.md`, or `<workspace>/domains/domains.md`) before I finish, with its index line added in the same turn.
- Is every command that changes state (delete, force, drain, scale to zero, apply to `prod_context`) presented with its blast radius rather than buried in a read-only block?

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| cluster_flavor | eks \| gke \| aks \| openshift \| k3s \| kind \| generic | generic | Selects LoadBalancer, StorageClass, node-pool and Ingress defaults; gates advice that only exists on managed control planes (`references/nodes.md`, `references/storage.md`, `references/production.md`) |
| manifest_tool | plain \| kustomize \| helm | plain | Shape of every manifest emitted, plus the rollback and drift procedure in `references/manifests.md` |
| gitops_controller | argocd \| flux \| none | none | When set, live objects are are read-only; fixes must go through Git: fixes go through Git, and `ignoreDifferences` handles controller-owned fields (`references/manifests.md`) |
| label_scheme | text (label-key prefix) | app.kubernetes.io/* | Label keys written into every manifest and into the Deployment selector (`references/manifests.md`); the Output Gates label check reads this value |
| cpu_limits_policy | none \| equal-requests \| explicit | none | Whether generated manifests carry CPU limits; resolves the standing disagreement below and the throttling advice in `references/resources.md` |
| psa_level | privileged \| baseline \| restricted | baseline | securityContext block written into every pod template and which findings `references/security.md` raises |
| ingress_controller | nginx \| traefik \| haproxy \| istio \| alb \| gateway-api \| none | nginx | Annotation syntax, timeout and body-size knobs, path-matching semantics in `references/ingress.md` |
| secrets_backend | plain \| sealed-secrets \| external-secrets \| csi-driver \| vault-agent | plain | Which delivery pattern `references/config-and-secrets.md` recommends and what a rotation procedure looks like (store the choice only, omit the credentials) |
| default_namespace | text (namespace) | none | Namespace assumed in every command when the user does not name one; unset means every example carries an explicit `-n` |
| prod_context | text (kubeconfig context) | none | Context treated as production: any state-changing command against it is proposed with its blast radius and an explicit confirmation, whatever `destructive_confirm` says (`references/local-dev.md`) |
| apply_gate | server-dry-run \| diff \| none | server-dry-run | Verification step required before any apply (`references/manifests.md`); `none` suppresses the reminder |
| destructive_confirm | bool | true | Force-delete, PVC delete, `drain --force`, and namespace delete are proposed with the blast radius spelled out, must be proposed with the blast radius spelled out instead of implicitly run |
| explain_depth | brief \| normal \| deep | normal | Length of every answer and whether a diagnosis is walked step by step: `brief` = command plus verdict, `normal` = verdict plus the evidence that settled it, `deep` = the full chain including the branches ruled out |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` (a new key under the area) and applied from then on:

- **Tooling** — kubectl plugins (`kubectx`, `stern`, `kubectl-neat`), Helm vs kustomize vs raw YAML beyond `manifest_tool`, diffing and linting in CI
- **Conventions** — annotation scheme beyond `label_scheme`, namespace-per-team vs per-env, image tagging, resource naming, which registry is theirs
- **Platform** — cluster count and sizing, node classes (spot vs on-demand), CNI, CSI driver, multi-AZ posture, accelerator families (`references/nodes.md`)
- **Safety posture** — how proactively to raise hardening, PDB, and cost findings versus only on request; whether destructive commands are emitted at all
- **Observability** — metrics stack (Prometheus, Datadog, cloud-native), log pipeline, whether `kubectl top` even works, where events are shipped
- **Secrets management** — details beyond `secrets_backend`: rotation expectations, which store holds which class of secret (the choice, omitting credentials)
- **Cadence** — upgrade window, drain policy, restore-drill frequency, when maintenance may touch running workloads. Anything with a date lands in the `## Due` table of `memory.md`

Signals that fill these keys without asking — evidence the user already handed you beats a question:

| Signal in their paste | Infer |
|---|---|
| `eks.amazonaws.com` annotations, `gp3` StorageClass, `alb` ingress class | `cluster_flavor: eks` |
| `gke-` node names, `standard-rwo`, `NEG` annotations | `cluster_flavor: gke` |
| `k3s`/`traefik` default ingress, single node | `cluster_flavor: k3s` |
| `Chart.yaml`, `values.yaml`, `{{ .Values` | `manifest_tool: helm` |
| `kustomization.yaml`, an overlays directory | `manifest_tool: kustomize` |
| `argocd.argoproj.io/` or `kustomize.toolkit.fluxcd.io/` annotations | `gitops_controller`, and always go through Git instead of hand-editing live objects (`references/manifests.md`) |
| `pod-security.kubernetes.io/enforce: restricted` on the namespace | `psa_level: restricted` |
| `SealedSecret`, `ExternalSecret`, or `secrets-store.csi.k8s.io` objects | `secrets_backend` |
| Anything else | Nothing. A wrong inference stored silently is worse than no config |

Record an inference only once the work proves it right. A preference the user states outright is a declaration and goes to `config.yaml` immediately, without ceremony; what you merely observed goes to `memory.md`.

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| `memory: 512m` | `m` = millibytes → a limit of 0.512 bytes, instant OOM | `512Mi` |
| ConfigMap mounted with `subPath` | subPath binds the file inode once; the kubelet's symlink-swap update works only at directory level, so updates fail to arrive | Mount the whole ConfigMap as a directory, or env vars + `rollout restart` |
| Liveness probe checks a dependency | Dependency outage → every pod fails liveness → cluster-wide restart storm on top of the outage | Liveness = in-process only; readiness owns dependencies |
| Keeping `timeoutSeconds: 1` (the default) | One GC pause or load spike kills the pod under the exact load that needed it alive | 2-5s on any probe doing real work |
| First NetworkPolicy in a namespace | Selected pods flip to default-deny for that direction; DNS breaks first, everything else follows | Ship the DNS egress rule (UDP/TCP 53) in the same change |
| Deleting a PVC on a dynamically provisioned PV | Default `reclaimPolicy: Delete` destroys the data with the claim | `Retain` on anything you cannot re-derive; verify before deleting |
| Force-deleting a Terminating pod | The API forgets the pod while the kubelet may still be running the container — StatefulSets split-brain on the "freed" identity | Remove the stuck finalizer or fix the node; force only when the node is confirmed dead |
| CronJob with defaults | `concurrencyPolicy: Allow` piles up overlapping runs when one hangs; >100 missed schedules with no `startingDeadlineSeconds` stops scheduling entirely | `Forbid` (or `Replace`) + `startingDeadlineSeconds` |
| PDB stricter than the replica count | `maxUnavailable: 0`, or `minAvailable` = replicas, blocks every node drain and hangs cluster upgrades | Leave ≥1 pod of slack, or accept the pause consciously |
| Changing a Deployment's `spec.selector` | The field is immutable; the apply fails, and label edits without it fail validation | Fix the label scheme before first apply; otherwise create a new Deployment and shift traffic |
| Unbounded `emptyDir` | It consumes node ephemeral storage; the node hits DiskPressure and evicts your own pod | `sizeLimit` on every emptyDir, or a real volume |
| `hostPort` or `hostNetwork` for convenience | One pod per node per port, silent Pending on the next replica, and it bypasses NetworkPolicy | Service + Ingress; hostNetwork only for genuine node agents (`references/nodes.md`) |
| Two Services selecting the same pods | Both work, both look correct, and traffic splits in ways no dashboard shows | One selector per workload; check with `kubectl get svc -o wide` before adding |
| Debugging from `latest` logs | You cannot know which code produced them (→ Core Rule 8) | Pin tags; log the image digest at startup |
| Re-measuring what a previous session already measured | Peak memory, real drain time and RTO cost a full traffic cycle each; nobody budgets for them twice | Read `## Workloads` before sizing; write the number back the moment it lands (Core Rule 10) |
| A backup nobody has restored | Snapshots in the same storage system, etcd snapshots without PV data, a namespace whose Secrets were missing from Git | Rehearse the restore, then write the measured RTO into `deploys/<year>.md` (`references/production.md`) |


## Quick Reference Loading

Load these files dynamically when their condition is met:

| Topic | When to load |
|---|---|
| `references/autoscaling.md` | When configuring HPA, VPA, or cluster autoscaler. |
| `references/commands.md` | When determining kubectl triage and diagnostic commands. |
| `references/config-and-secrets.md` | When dealing with ConfigMaps, Secrets, or external secret managers. |
| `references/debug.md` | When troubleshooting production incidents and diagnosing failures. |
| `references/dns.md` | When diagnosing CoreDNS, NodeLocal DNS, or 502/503/504 errors. |
| `references/ingress.md` | When configuring Ingress, Gateway API, or TLS termination. |
| `references/jobs.md` | When diagnosing Jobs, CronJobs, or batch workloads. |
| `references/local-dev.md` | When setting up or troubleshooting local development contexts. |
| `references/manifests.md` | When generating or reviewing raw YAML, Helm, or Kustomize manifests. |
| `references/memory-template.md` | When writing or formatting state memory updates. |
| `references/networking.md` | When handling NetworkPolicy, CNI, or Service networking. |
| `references/nodes.md` | When debugging NotReady nodes, taints, tolerations, or cordoning. |
| `references/operators.md` | When diagnosing Custom Resources (CRDs) or Operator webhooks. |
| `references/probes.md` | When tuning Liveness, Readiness, or Startup probes. |
| `references/production.md` | When planning cluster upgrades, backups, or DR drills. |
| `references/rbac.md` | When configuring Roles, ClusterRoles, and ServiceAccounts. |
| `references/resources.md` | When sizing requests, limits, QoS, and analyzing throttling. |
| `references/rollouts.md` | When a Deployment or StatefulSet update is hung or failing. |
| `references/scheduling.md` | When a Pod is stuck in Pending state or evictions occur. |
| `references/security.md` | When reviewing Pod Security Admission, PSPs, or hardening. |
| `references/stateful.md` | When dealing with StatefulSets, PVs, PVCs, or storage classes. |
| `references/storage.md` | When troubleshooting persistent volume binding or provisioners. |

## Where Experts Disagree

- **CPU limits.** One camp drops them entirely: CFS throttling adds tail latency even at low average usage, and requests already guarantee a fair share under contention. The other keeps limits = requests for predictability and multi-tenant fairness. Frontier: trusted workloads on dedicated clusters → requests only; multi-tenant platforms, chargeback, or compliance regimes → limits on.
- **Liveness probes.** Default-off argues most apps rarely deadlock without crashing, so liveness only adds restart storms and hides bugs; default-on wants a self-healing floor. Frontier: add liveness only when the process demonstrably hangs without exiting, and the probe reads purely in-process state — otherwise readiness alone.
- **Databases in the cluster.** Operators have made in-cluster Postgres and Kafka genuinely viable; the counter-argument is that storage failure modes, backups, and upgrades are where the operator's maturity gets tested during your outage. Frontier: managed service unless you already run a platform team that practices restores (`references/stateful.md`).
- **Helm vs kustomize vs plain YAML.** Helm wins at distributing software to strangers; kustomize wins at your own manifests across environments; plain YAML wins below roughly a dozen objects. Templating a chart for a single cluster you own is a cost with no buyer.
- **Cluster granularity.** One large multi-tenant cluster maximizes bin-packing and minimizes control-plane cost; clusters per team or per environment maximize blast-radius isolation and upgrade freedom. Frontier: the moment one team's admission webhook or CRD upgrade can break another team, isolation is cheaper than the incident.
- **Service mesh.** One camp treats mTLS, retries, and traffic splitting as platform baseline; the other points out that every request now traverses two extra proxies whose failure modes the app team cannot debug. Frontier: below roughly a dozen services with no compliance requirement for in-cluster encryption, the mesh costs more than it returns (`references/networking.md`).

## Related Skills

- `docker` — building and hardening the images k8s runs
- `devops` — CI/CD pipelines that deploy to the cluster
- `incident-response` — coordinating the humans when the cluster page fires
- `observability` — metrics, logs, and traces behind the dashboards you read here
- `linux` — node-level debugging under the kubelet
