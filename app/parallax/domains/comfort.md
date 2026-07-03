---
title: Comfort
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 5
---

# Comfort (Parallax)

Climate, cabin, seats, user modes.

## RVMs

| RVM | Protobuf hints | Vehicle state? | Legacy correlate |
| --- | --- | --- | --- |
| `comfort.cabin.climate_hold_setting` | | | Climate hold config |
| `comfort.cabin.cabin_ventilation_setting` | `g70/h0` | | Ventilation setting writes |
| `comfort.cabin.climate_hold_status` | `g70/m0` | | `cabinPreconditioningStatus` |
| `comfort.cabin.pet_mode_status` | | yes | `petModeStatus`, `petModeTemperatureStatus` |
| `comfort.cabin.cabin_preconditioning_status` | | | `cabinPreconditioningStatus`, `cabinPreconditioningType` |
| `comfort.cabin.cabin_temperatures` | | | `cabinClimate*Temperature` |
| `comfort.cabin.defrost_defog_status` | | | `defrostDefogStatus` |
| `comfort.cabin.seat_conditioning_status` | | yes | `seat*Heat`, `seat*Vent`, `steeringWheelHeat` |
| `comfort.cabin.hvac_settings_status` | | yes | HVAC settings aggregate |
| `comfort.user_modes.state` | | | User modes / camp etc. |

### `g70/m0` — climate hold status (also used in other flows)

| Field | Type |
| --- | --- |
| 1 | enum status |
| 2 | enum availability |
| 3 | enum unavailabilityReason |
| 4 | timestamp holdEndTime |

## Commands

Preconditioning, seat heat/vent, defrost, climate hold → `PARALLAX_COMFORT_COMMAND`. Legacy: [`sendVehicleCommand`](/app/legacy/controls/send-vehicle-command) with cabin params.

## Writes

Ventilation and schedule-like comfort settings go through [sendParallaxPayload](/app/parallax/commands/send-payload) as `PARALLAX_OPERATION_REQUEST` protobuf (see `eq/u.smali` + `g70/h0`).
