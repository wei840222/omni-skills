# Commands That Lie

| Tool | What it seems to say | What is true |
|---|---|---|
| `free` "free" column | Memory is nearly gone | Cache is reclaimable; only `available` answers "can I start something" |
| Load average | The CPU is overloaded | It counts D-state tasks too — high load with idle CPU is a storage incident |
| `top` %CPU | Above 100% is a bug | It is per-core: 400% = four cores saturated |
| `iostat` %util | The disk is maxed out | Meaningless on SSD/NVMe with parallel queues — judge by `await` and queue depth |
| `df` vs `du` | One of them is wrong | Both are right: deleted-but-open files or shadowed mounts explain the gap |
| `ps aux` %MEM | These workers use 40 GB | Shared pages are counted once per process — use PSS (`smaps_rollup`, `smem`) |
| `which` | This is what runs | It misses aliases, functions, and builtins — `type -a <cmd>` |
| `ping` | The service is up | It proves ICMP only — `nc -zv host port` or call the service |
| `dig` | The name resolves | Applications resolve through NSS, which `dig` bypasses — `getent hosts` |
| `df` on a thin volume | Half the disk is free | Thin-provisioned and overlay storage can exhaust underneath the filesystem |
| `du -sh *` | This is the directory total | It skips dotfiles — `du -sh .` |
| `uptime` 400 days | The host is reliable | It has never proven it can boot; reboot on a schedule you choose |
