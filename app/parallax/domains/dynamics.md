---
title: Dynamics
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 4
---

# Dynamics (Parallax)

Motion, location, tires, range.

## RVMs

| RVM | Protobuf hints | Vehicle state? | Legacy correlate |
| --- | --- | --- | --- |
| `dynamics.vehicle.drive_mode` | `g70/*` | yes | `driveMode` |
| `dynamics.vehicle.gear` | | yes | `gearStatus` |
| `dynamics.vehicle.range` | | yes | `distanceToEmpty`, `rangeThreshold` |
| `dynamics.vehicle.odometer` | | | `vehicleMileage` |
| `dynamics.vehicle.gnss` | | | `gnssLocation` (also consent-gated) |
| `dynamics.vehicle.location` | | | Known location / place |
| `dynamics.tires.state` | `i70/*` | feature flag | `tirePressureStatus*`, `tirePressure*` |

### Tires (`i70/f`, `i70/g`)

`dynamics.tires.state` uses feature scope (not only `PARALLAX_VEHICLE_STATE`). Fields include tire position, pressure, status, validity, TPMS monitor status.

Legacy parallel: WebSocket `tirePressureState` subscription (JSON fragment of `vehicleState`).

## Navigation overlap

Trip routing uses [Navigation domain](/app/parallax/domains/navigation); dynamics covers raw vehicle motion/location signals.

## Decoding

Odometer and GNSS payloads: capture and `protoc --decode_raw`; map floats/integers to `GetVehicleState` numeric fields (odometer often stored in fixed-point meters).
