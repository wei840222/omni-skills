# Monitor Templates

Execution guidance for the static definitions listed directly in SKILL.md. User-confirmed targets and grants take precedence over examples.

## HTTP Endpoint

Load the corresponding definition from `assets/monitor-examples.json` listed in SKILL.md.

Agent runs: `curl -s -o /dev/null -w "%{http_code}" --max-time 10 URL`

## SSL Certificate

Load the corresponding definition from `assets/monitor-examples.json` listed in SKILL.md.

Agent runs: `openssl s_client` + parse expiry

## Process Running

Load the corresponding definition from `assets/monitor-examples.json` listed in SKILL.md.

Agent runs: `pgrep -x postgres`

## Disk Space

Load the corresponding definition from `assets/monitor-examples.json` listed in SKILL.md.

Agent runs: `df -h /`

## Custom Check (User-Defined)

Load the corresponding definition from `assets/monitor-examples.json` listed in SKILL.md.

User provides the command, agent runs it.

## Remote Server (Requires SSH)

Load the corresponding definition from `assets/monitor-examples.json` listed in SKILL.md.

User must explicitly grant SSH access to server1.

## TCP Port

Verify the local `nc` variant and its timeout/zero-I/O flags before a single-port connection check. This is a reachability observation, not an application health verdict.
