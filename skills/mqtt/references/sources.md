# MQTT research sources

Full URLs used while verifying Gate 6 claims for this package. Re-open these before asserting protocol version semantics, Mosquitto option names, or integration defaults.

## MQTT specifications

- OASIS MQTT Version 5.0 — https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
- OASIS MQTT Version 3.1.1 — https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html

## Brokers and operations

- Eclipse Mosquitto documentation — https://mosquitto.org/documentation/
- mosquitto.conf man page — https://mosquitto.org/man/mosquitto-conf-5.html
- HiveMQ MQTT Essentials (conceptual QoS / retained / will primers) — https://www.hivemq.com/mqtt-essentials/

## Integrations

- Home Assistant MQTT integration — https://www.home-assistant.io/integrations/mqtt/

## Agent Skills packaging

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref validator — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Operational note

Broker defaults, listener syntax, and MQTT 5 session expiry details change across versions. Before promising a concrete `mosquitto.conf` key or cloud-SaaS behavior, re-open the live vendor page for that exact version.
