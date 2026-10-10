# YARN operations — Hadoop

CLI forms follow Apache Hadoop YarnCommands. Prefer live site XML over default
sentinels when tuning memory.

## Architecture snapshot

```text
ResourceManager
├── Scheduler + ApplicationManager
├── Node heartbeats / allocations
└── Optional HA active/standby pair

NodeManager (per node)
├── Launches containers
├── Reports resource usage
└── Local resource localization

ApplicationMaster (per app)
├── Requests containers
├── Runs app-specific control loop
└── Handles task retries
```

## Applications

```bash
# List
yarn application -list
yarn application -list -appStates ALL
yarn application -list -appStates RUNNING,ACCEPTED,FAILED,KILLED,FINISHED
yarn application -list -appTypes MAPREDUCE
yarn application -list -appTypes SPARK

# Status / control
yarn application -status application_1234567890123_0001
yarn application -kill application_1234567890123_0001

# Queue move (current docs: -changeQueue; older -movetoqueue is deprecated alias)
yarn application -changeQueue application_1234567890123_0001 -queue high_priority
```

Valid `-appStates` filters include `ALL`, `NEW`, `NEW_SAVING`, `SUBMITTED`,
`ACCEPTED`, `RUNNING`, `FINISHED`, `FAILED`, `KILLED` (see YarnCommands).

### Logs

```bash
yarn logs -applicationId application_1234567890123_0001
yarn logs -applicationId <app_id> -containerId <container_id>
yarn logs -applicationId <app_id> -log_files stdout
yarn logs -applicationId <app_id> -log_files stderr
yarn logs -applicationId <app_id> > app_logs.txt
```

## Queues and nodes

```bash
yarn queue -status default
yarn queue -status root.production

yarn node -list
yarn node -list -all
yarn node -list -states RUNNING
yarn node -status <node_id>
```

### Decommission sketch

1. Add the node to the cluster exclude list used by your distribution.
2. `yarn rmadmin -refreshNodes` (optionally graceful forms supported by the version).
3. Wait for containers to drain; then remove host-level services.

## ResourceManager admin

```bash
yarn rmadmin -getServiceState rm1
yarn rmadmin -getServiceState rm2
yarn rmadmin -transitionToStandby rm1 --forcemanual    # confirm blast radius
yarn rmadmin -transitionToActive rm2 --forcemanual

yarn rmadmin -refreshQueues
yarn rmadmin -refreshNodes
yarn rmadmin -refreshAdminAcls
yarn rmadmin -refreshUserToGroupsMappings
```

## Memory and CPU knobs

Read **live** values first:

```bash
# Examples — paths vary by distribution packaging
rg -n "yarn.nodemanager.resource.memory-mb|yarn.scheduler.minimum-allocation-mb|yarn.scheduler.maximum-allocation-mb" /etc/hadoop/conf/yarn-site.xml
rg -n "mapreduce.map.memory.mb|mapreduce.reduce.memory.mb|mapreduce.map.java.opts|mapreduce.reduce.java.opts" /etc/hadoop/conf/mapred-site.xml
```

Apache default XML (current docs tree) uses sentinels such as:

| Property | Docs default signal | Meaning for operators |
|----------|---------------------|------------------------|
| `yarn.nodemanager.resource.memory-mb` | `-1` | Often auto-detected; set explicitly on real clusters |
| `yarn.nodemanager.resource.cpu-vcores` | `-1` | Same |
| `yarn.scheduler.minimum-allocation-mb` | `1024` | Minimum container ask |
| `yarn.scheduler.maximum-allocation-mb` | `8192` | Max container ask (raise if jobs need more) |
| `mapreduce.map.memory.mb` / `reduce` | `-1` | Derived unless overridden |
| `mapreduce.map.speculative` / `reduce` | `true` | Straggler reruns |
| `mapreduce.task.timeout` | `600000` ms | Task without progress |

### Safe tuning pattern

```text
1. Observe failure (AM/container logs, exit code)
2. Read live NM total memory and scheduler min/max
3. Set container MB for map/reduce/executor
4. Set JVM -Xmx to a value clearly below container MB
5. Re-run one canary job before fleet-wide defaults
```

Job-level overrides (examples):

```bash
# MapReduce
-Dmapreduce.map.memory.mb=4096
-Dmapreduce.map.java.opts=-Xmx3276m
-Dmapreduce.reduce.memory.mb=8192
-Dmapreduce.reduce.java.opts=-Xmx6553m

# Spark-on-YARN (spark-submit flags; still bounded by YARN max allocation)
--executor-memory 4g --driver-memory 2g
```

### Speculative execution

```bash
-Dmapreduce.map.speculative=true|false
-Dmapreduce.reduce.speculative=true|false
```

Keep enabled for cheap stragglers; disable when duplicate work is costly or unsafe.

## Container failure signals

| Signal | Likely meaning | First checks |
|--------|----------------|--------------|
| Exit `137` | SIGKILL / host OOM killer | NM logs, cgroup limits, heap vs container |
| YARN killed for memory | Physical memory over container limit | Raise container or cut heap/overhead |
| Stuck `ACCEPTED` | No room / queue max / AM cannot launch | `queue -status`, `node -list`, AM diagnostics |
| Launch failed | Local resources, bad env, permissions | NM launch logs, distributed cache paths |

## Capacity vs Fair (operator view)

- **Capacity scheduler:** percentage capacities, user limits, hierarchical queues
  (`capacity-scheduler.xml`).
- **Fair scheduler:** weights / fair shares (`fair-scheduler.xml` or distribution
  equivalent).

Always identify the active scheduler class from live `yarn-site.xml` before
editing queue math.
