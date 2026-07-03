---
title: Security
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 6
---

# Security (Parallax)

Alarm, immobilizer, Gear Guard video, phone key diagnostics.

## RVMs

| RVM | Protobuf hints | Vehicle state? | Legacy correlate |
| --- | --- | --- | --- |
| `security.alarm.state` | | | `alarmSoundStatus` |
| `security.access.immobilizer_state` | | | Immobilizer / service mode adjacent |
| `security.video_monitoring.state` | | yes | `gearGuardVideoStatus`, `gearGuardVideoMode` |
| `security.access.btm` | | yes | Phone key / BTM link state |
| `security.access.passive_entry_debug` | | | Debug |
| `security.access.vas_fault` | | | VAS fault reporting |

Gear Guard **streaming** consent/limits: [Gear Guard domain](/app/parallax/domains/gear-guard) (`gearguard_streaming.privacy.*`).

## Commands

Panic, Gear Guard enable/disable, video sessions → `PARALLAX_SECURITY_COMMAND`.

Legacy: `HONK_AND_FLASH_LIGHTS`, `ENABLE_GEAR_GUARD_VIDEO`, etc. via [sendVehicleCommand](/app/legacy/controls/send-vehicle-command).

## Related legacy WebSocket

`gearGuardRemoteConfig` — WebRTC live view config (not Parallax protobuf). See [Legacy subscriptions](/app/legacy/websocket-subscriptions).
