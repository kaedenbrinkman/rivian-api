---
title: Commands
has_children: true
parent: Parallax
grand_parent: App API
nav_order: 3
permalink: /app/parallax/commands
---

# Parallax commands

Remote commands and vehicle-model writes when `parallaxCommand` and per-domain `PARALLAX_*_COMMAND` features are enabled.

- [sendParallaxPayload](/app/parallax/commands/send-payload) — gateway mutation
- [Command status (`vehicleCommandStatePx`)](/app/parallax/commands/command-status) — WebSocket subscription

Fallback when Parallax is off: [Legacy controls](/app/legacy/controls).

## Command domains (feature flags)

| Feature | Example commands |
| --- | --- |
| `PARALLAX_BODY_COMMAND` | Lock/unlock, windows, frunk, liftgate, charge port, side bins |
| `PARALLAX_COMFORT_COMMAND` | Preconditioning, seat heat/vent, defrost, climate hold |
| `PARALLAX_SECURITY_COMMAND` | Panic, Gear Guard, video sessions |
| `PARALLAX_ENERGY_COMMAND` | Start/stop charge, charge limit |
| `PARALLAX_OTA_COMMAND` | Install now |

Settings edits (ventilation, schedules) use the same write path with `PARALLAX_OPERATION_REQUEST` protobuf envelopes, not only one-shot remote commands.
