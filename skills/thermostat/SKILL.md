---
name: thermostat
description: Adjust thermostat setpoints, diagnose room comfort issues, estimate setback savings, and configure away/vacation or smart-home thermostat schedules. Use when the user asks to change temperature, troubleshoot HVAC comfort, plan setbacks, or set vacation freeze protection.
metadata:
  version: "1.0.1"
  openclaw: "{\"emoji\":\"🌡️\"}"
  related-skills:
    smart-home: skills/smart-home
    home: skills/home
---
## When to load references

- `references/basics.md`: Load for modes, holds, fan settings, remote sensors, and scheduling setup.
- `references/troubleshooting.md`: Load to diagnose comfort problems, HVAC issues, or error codes.
- `references/efficiency.md`: Load to calculate energy savings, debunk myths, and optimize settings from the user schedule.
- `references/integration.md`: Load to integrate with HomeKit, Alexa, Google Home, Home Assistant, or Matter and to configure automations.
- `references/away.md`: Load to configure vacation modes, freeze protection, and humidity control.
- `references/sources.md`: Load for DOE/ENERGY STAR/insurance source notes behind setback and freeze-protection guidance.

## Before adjusting temperature

**Gather context:**
- Current temp and setpoint
- Heating or cooling mode?
- Smart thermostat or basic?
- Any specific room complaints?
- Heat pump vs furnace/AC when efficiency or recovery is in scope

**Smart thermostats:** Adjust via voice, app command, or API integration.
**Basic thermostats:** Guide the user to physical adjustment; suggest portable workarounds only when safe and attended.

## Reliable defaults

- Change temperature in small steps (±2–3°F) unless the user gives an exact setpoint.
- Check holds before blaming the schedule.
- Prefer 3–5°F setbacks for heat pumps; deeper setbacks can trigger expensive aux heat.
- Vacation bounds start at minimum 55°F (freeze protection) and maximum 85°F (humidity/mold risk) unless policy or climate requires stricter limits.
- For whole-home automation beyond the thermostat, load related skill `smart-home`.
