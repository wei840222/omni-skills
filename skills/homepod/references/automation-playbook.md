# Home automation reliability playbook

Use this playbook when Home automations are intermittent, delayed, or non-deterministic.

## Record format

For each test, capture the trigger, evaluated conditions, expected action, actual action, and execution latency in `<state_root>/automation-log.md` when the user has enabled notes.

## Stabilization sequence

1. Isolate one canonical test automation and temporarily disable duplicate or overlapping candidates with the user’s approval.
2. Verify that its trigger is unique and observable.
3. Verify that every condition reflects current state.
4. Verify that each target is online, writable, and not being changed by a conflicting scene.
5. Run three controlled trials with the same inputs. Treat differing outcomes as an unstable result and keep the scope narrow.

## Completion criteria

A change is ready to keep when three consecutive trials pass, unrelated rooms and scenes show no side effects, latency stays within the user’s tolerance, and the rollback path is documented for a non-trivial change.
