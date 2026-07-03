---
title: Energy
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 1
---

# Energy (Parallax)

HV/LV battery telemetry and edge-compute energy graphs.

## RVMs

### High / low voltage

| RVM | Protobuf (APK) | Notes |
| --- | --- | --- |
| `energy.high_voltage.battery_state` | `l70/p` | Decoded in `cq/f.smali` |
| `energy.high_voltage.battery_characteristics` | `l70/h` | Decoded in `cq/f.smali` |
| `energy.low_voltage.battery_state` | `l70/*` | 12V battery; decoder in `cq/f` |

#### `l70/p` — high voltage battery state

| Field | Type | Content |
| --- | --- | --- |
| 1 `charge_state` | `l70/k` | SOC %, pack kWh, range km |
| 2 `temperature_state` | `l70/l` | Cell avg/max/min °C |
| 3 `thermal_event` | `l70/m` | Thermal event flags |
| 4 `power_output` | int32 | Power output enum/state |
| 5 `requires_calibration` | bool | |
| 6 `cold_weather_state` | enum | Cold weather impact |

**`l70/k` (charge_state)**

| Field | Type | Legacy correlate |
| --- | --- | --- |
| 1 | double | `GetVehicleState.batteryLevel` (SOC %) |
| 2 | double | Pack energy kWh |
| 3 | float | `GetVehicleState.distanceToEmpty` (range; units may differ) |

Sample decode (`CkIKBAAAADMzT0A...`): SOC **58.2%**, **125.1 kWh**, cell temps ~41/45/36 °C.

### Edge-compute graphs (`energy_edge_compute.graphs.*`)

| RVM | Protobuf | Key fields |
| --- | --- | --- |
| `energy_edge_compute.graphs.charge_session_breakdown` | `k70/b` | `totalKwh`, `packKwh`, `thermalKwh`, `currentPower`, `sessionCost` (`tk/b`), `chargingState`, `timeRemainingMins`, … |
| `energy_edge_compute.graphs.charging_graph_global` | `k70/i` | repeated `globalChargingGraphBar` → `k70/g` |
| `energy_edge_compute.graphs.cold_weather_soc` | `k70/k` | `socPercGreen`, `socPercBlue`, `coldRangeImpactKm` |
| `energy_edge_compute.graphs.parked_energy_distributions` | `k70/o` | Parked energy distribution chart |

#### `k70/g` — graph bar

| Field | Type |
| --- | --- |
| 1 | int32 SOC |
| 2 | float power |
| 3 | int64 startTimeMs |
| 4 | int64 endTimeMs |
| 5 | int32 timeEstimationValidityStatus |
| 6 | int32 chargingState |
| 7 | int32 barContext |

#### Sample `charge_session_breakdown`

~53 kWh total, ~123 kW power, ~$37.81 USD session cost, `chargingState` = 3 (active).

## Charging overlap

Session **status** RVMs live under [Charging domain](/app/parallax/domains/charging); graphs and HV state are subscribed together during active sessions.

## Legacy correlate

[`GetVehicleState`](/app/legacy/vehicle-state): `batteryLevel`, `distanceToEmpty`, `chargerState`, `batteryHvThermalEvent`, `timeToEndOfCharge`.

Legacy typed charging JSON: [`chargingSession`](/app/legacy/websocket-subscriptions) subscription on the charging dive screen.
