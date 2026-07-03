---
title: Domains
has_children: true
parent: Parallax
grand_parent: App API
nav_order: 4
permalink: /app/parallax/domains
---

# Parallax domains

All RVM strings known from enum `cm/c`. Each domain page lists protobuf hints, legacy JSON correlates, and `isVehicleState` gating.

| Domain | RVM count | Page |
| --- | ---: | --- |
| Energy | 6 | [Energy](/app/parallax/domains/energy) |
| Charging session | 7 | [Charging](/app/parallax/domains/charging) |
| Body | 4 | [Body](/app/parallax/domains/body) |
| Dynamics | 7 | [Dynamics](/app/parallax/domains/dynamics) |
| Comfort | 10 | [Comfort](/app/parallax/domains/comfort) |
| Security | 6 | [Security](/app/parallax/domains/security) |
| Access | 2 | [Access](/app/parallax/domains/access) |
| OTA | 3 | [OTA](/app/parallax/domains/ota) |
| Navigation | 2 | [Navigation](/app/parallax/domains/navigation) |
| Geofence | 1 | [Geofence](/app/parallax/domains/geofence) |
| Gear Guard streaming | 2 | [Gear Guard](/app/parallax/domains/gear-guard) |
| Vehicle meta | 3 | [Vehicle](/app/parallax/domains/vehicle) |
| Devices | 1 | [Devices](/app/parallax/domains/devices) |

## Master RVM table

| RVM | Domain doc | Vehicle state? |
| --- | --- | --- |
| `energy.high_voltage.battery_state` | Energy | |
| `energy.high_voltage.battery_characteristics` | Energy | |
| `energy.low_voltage.battery_state` | Energy | |
| `energy_edge_compute.graphs.*` (4 RVMs) | Energy | |
| `charging.session.*` (6 RVMs) | Charging | partial |
| `charging.schedule.time_window` | Charging | |
| `body.*` (4 RVMs) | Body | partial |
| `dynamics.vehicle.*` (6 RVMs) | Dynamics | partial |
| `dynamics.tires.state` | Dynamics | feature flag |
| `comfort.*` (10 RVMs) | Comfort | partial |
| `security.*` (6 RVMs) | Security | partial |
| `vehicle_access.*` (2 RVMs) | Access | |
| `ota.*` (3 RVMs) | OTA | |
| `navigation.*` (2 RVMs) | Navigation | |
| `geofence.geofence_service.favoriteGeofences` | Geofence | |
| `gearguard_streaming.privacy.*` (2 RVMs) | Gear Guard | |
| `vehicle.wheels.vehicle_wheels` | Vehicle | |
| `vehicle.power.state` | Vehicle | |
| `vehicle.network.state` | Vehicle | |
| `device_table.vas_keyper.devices` | Devices | |

**Vehicle state?** — included only when vehicle feature `PARALLAX_VEHICLE_STATE` is enabled (plus always-on App-scoped topics).

See [Subscription](/app/parallax/subscription) for how the app builds the `rvms` array.
