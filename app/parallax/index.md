---
title: Parallax
has_children: true
parent: App API
nav_order: 3
permalink: /app/parallax
---

# Parallax

Live vehicle data and many remote commands in the Rivian app use **Parallax**: protobuf payloads keyed by **RVM** (remote vehicle message) strings, delivered over GraphQL WebSocket or sent via gateway mutations.

## Transport

| Direction | Endpoint | Mechanism |
| --- | --- | --- |
| Subscribe (read) | `wss://api.rivian.com/gql-consumer-subscriptions/graphql` | [`ParallaxMessages`](/app/parallax/subscription) |
| Command status | same WebSocket URL | [`vehicleCommandStatePx`](/app/parallax/commands/command-status) |
| Write / commands | `POST https://rivian.com/api/gql/gateway/graphql` | [`sendParallaxPayload`](/app/parallax/commands/send-payload) |

Every read update looks like `{ rvm, payload, timestamp }` where `payload` is base64 protobuf.

## Feature flags

| Flag / feature | Effect |
| --- | --- |
| `parallaxVehicleState` + `PX_STATE_ALL` | Adds vehicle-state RVMs to the subscription |
| `parallaxCommand` + `PVS_*_CMD` | Routes remote commands through `sendParallaxPayload` |

Full gating model and flag catalogs: [Feature flags](/app/feature-flags).

When flags are off, the app falls back to [Legacy](/app/legacy) APIs (`vehicleState`, `sendVehicleCommand`, etc.).

## Documentation map

### Core

- [Subscription (`ParallaxMessages`)](/app/parallax/subscription) — connect, subscribe, RVM selection rules
- [Decoding payloads](/app/parallax/decoding) — protobuf recovery from the APK
- [Commands](/app/parallax/commands) — `sendParallaxPayload` and command status

### Domains

Each page lists RVMs, known protobuf classes, fields, and legacy JSON correlates where known.

- [Domains overview](/app/parallax/domains) — full RVM catalog
- [Energy](/app/parallax/domains/energy) — HV/LV battery, edge-compute graphs
- [Charging session](/app/parallax/domains/charging) — session status, graphs, schedule
- [Body](/app/parallax/domains/body) — locks, closures, windows, trailer
- [Dynamics](/app/parallax/domains/dynamics) — gear, range, odometer, location, tires
- [Comfort](/app/parallax/domains/comfort) — HVAC, seats, climate hold, pet mode
- [Security](/app/parallax/domains/security) — alarm, immobilizer, Gear Guard video, BTM
- [Access](/app/parallax/domains/access) — passive entry
- [OTA](/app/parallax/domains/ota) — schedule, state, deployment
- [Navigation](/app/parallax/domains/navigation) — trip info and progress
- [Geofence](/app/parallax/domains/geofence) — favorite geofences
- [Gear Guard streaming](/app/parallax/domains/gear-guard) — consent and daily limits
- [Vehicle meta](/app/parallax/domains/vehicle) — wheels, power mode, network
- [Devices](/app/parallax/domains/devices) — phone key table

## Example script

[`examples/parallax-subscribe.py`](../../examples/parallax-subscribe.py) — minimal WebSocket subscriber; prints JSON lines `{ rvm, timestamp, payload_b64 }`.
