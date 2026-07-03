---
title: Vehicle
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 12
---

# Vehicle meta (Parallax)

Wheels UI, power modes, cloud connectivity.

## RVMs

| RVM | Protobuf | Notes |
| --- | --- | --- |
| `vehicle.wheels.vehicle_wheels` | `q70/r` | Wheel/tire display config, TPMS presentation |
| `vehicle.power.state` | | `GetVehicleState.powerState` (sleep/standby/…) |
| `vehicle.network.state` | | Cloud/cellular connectivity |

### `q70/r` — wheels

Nested device/wheel metadata used by tire UI (pairs with [Dynamics tires](/app/parallax/domains/dynamics) for pressure data).

## Legacy

- [`getVehicleTireImages`](/app/legacy/vehicle-info/vehicle-tire-images) — static diagram assets (HTTP).
- [`GetVehicleLastConnection`](/app/legacy/vehicle-info/vehicle-last-connection) — last cloud sync (HTTP).
- WebSocket `vehicleCloudConnection` — online/lastSync JSON.
