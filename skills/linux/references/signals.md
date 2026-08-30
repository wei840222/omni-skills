# Signals And Exit Codes

Formula: an exit status above 128 means killed by signal `status − 128`. A process can also return those numbers itself, so confirm a real kill in `dmesg -T` or the journal before blaming the kernel.

| Status | Meaning | First move |
|---|---|---|
| 1 | Generic application error | Read the application log, not the OS |
| 126 | Found but not executable | `chmod +x`, a `noexec` mount, or a directory where a binary was expected |
| 127 | Command not found | PATH (cron and units get a minimal one), or a missing shared library — check `ldd` |
| 130 | SIGINT (128+2) | Ctrl-C, or a parent forwarding it |
| 137 | SIGKILL (128+9) | OOM killer first (`dmesg -T \| grep -i oom`), then a stop-timeout escalation |
| 139 | SIGSEGV (128+11) | Native crash — `coredumpctl`, and suspect a library or architecture mismatch |
| 141 | SIGPIPE (128+13) | The reader of a pipe exited first (`head` closing early is the usual cause) |
| 143 | SIGTERM (128+15) | Clean external stop — usually systemd stopping the unit, not a bug |
| 255 | Wrapper failure (ssh and some runtimes) | The transport failed; the remote command may never have run |
