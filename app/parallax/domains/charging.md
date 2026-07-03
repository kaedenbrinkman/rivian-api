---
title: Charging
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 2
---

# Charging session (Parallax)

Live charging session state, controls, and schedule — distinct from [Energy graphs](/app/parallax/domains/energy) but subscribed together while charging.

## Session RVMs

| RVM | Protobuf | Decoder | Vehicle state? |
| --- | --- | --- | --- |
| `charging.session.status` | `f70/v` | `cq/f.smali` | yes |
| `charging.session.time_estimation` | `g70/e0` | `cm/c` | yes |
| `charging.session.notification` | — | `cm/c` | |
| `charging.session.soc_slider` | — | `cm/c` | |
| `charging.session.trip_target` | — | `cm/c` | |
| `charging.session.remote_command` | — | `cm/c` | yes |
| `charging.schedule.time_window` | `r70/i` | `cm/c` | |

### `f70/v` — session status

| Field | Type | Notes |
| --- | --- | --- |
| 1 | enum | `plugConnectionStatus` |
| 2 | enum | `displayStatus` — see `f70/t` (`DISPLAY_STATUS_CHARGING_ACTIVE`, `DISPLAY_STATUS_CHARGING_READY`, …) |
| 3 | enum | `evseType` |

Example: `CAEQAQ==` → plug status **1**, display status **1** (charging ready).

Maps loosely to legacy `GetVehicleState.chargerState` / `chargerStatus` (string enums vs int).

### `g70/e0` — time estimation

| Field | Type |
| --- | --- |
| 1 | int32 `holdTimeDurationSeconds` |

### Schedule — `r70/i`

Repeated schedule entries (`r70/p`): daily repeat (`r70/l`) or single occurrence (`r70/s`), tied to `charging.schedule.time_window`.

## Recommended subscribe list (charging only)

```json
"rvms": [
  "energy_edge_compute.graphs.charging_graph_global",
  "energy_edge_compute.graphs.charge_session_breakdown",
  "energy_edge_compute.graphs.cold_weather_soc",
  "energy.high_voltage.battery_state",
  "energy.high_voltage.battery_characteristics",
  "charging.session.status",
  "charging.session.time_estimation",
  "charging.session.trip_target",
  "charging.session.soc_slider",
  "charging.session.notification",
  "charging.session.remote_command",
  "charging.schedule.time_window"
]
```

## Graph payloads

Detailed graph/breakdown schemas: [Energy domain](/app/parallax/domains/energy).

Example `charging_graph_global` payloads update frequently during a session (long base64 blobs with repeated `k70/g` bars).

## Remote commands

Start/stop charge and charge limit may use [Parallax commands](/app/parallax/commands) (`PARALLAX_ENERGY_COMMAND`) or legacy [sendVehicleCommand](/app/legacy/controls/send-vehicle-command).

## Legacy

- WebSocket [`chargingSession`](/app/legacy/websocket-subscriptions) — typed JSON chart/liveData on charging **detail** screen (not observed on the home screen in captures).
- HTTP charging APIs: [Legacy charging](/app/legacy/charging) (wallbox, public charging, session history).
