---
title: WebSocket subscriptions
parent: Legacy
grand_parent: App API
has_children: false
nav_order: 1
---

# Legacy WebSocket subscriptions

The app opens several GraphQL subscriptions on the same WebSocket endpoint as [Parallax](/app/parallax/subscription):

`wss://api.rivian.com/gql-consumer-subscriptions/graphql`

Protocol: **GraphQL over WebSocket** (`graphql-transport-ws`).

These subscriptions return **typed JSON** (not base64 Parallax protobuf). They run in parallel with `ParallaxMessages` when both are enabled.

## Headers

```text
a-sess: <app session token>
u-sess: <user session token>
csrf-token: <csrf token>
apollographql-client-name: com.rivian.android.consumer
```

## Connection flow

Same as Parallax: `connection_init` → `connection_ack` → `subscribe` → `next` frames.

GraphQL variable is typically **`vehicleId`** (string).

## Subscriptions

| Subscription | Purpose | Notes |
| --- | --- | --- |
| `vehicleState` | Full typed JSON vehicle state | Used when `PARALLAX_VEHICLE_STATE` is off or as supplement; overlaps [`GetVehicleState`](/app/legacy/vehicle-state) |
| `vehicleStateWidget` | Widget-sized `vehicleState` fragment | Home screen widget |
| `chargingSession` | Charging chart / liveData JSON | Observed on charging **detail** screen; home charging often uses Parallax RVMs instead |
| `vehicleCloudConnection` | Online status / last sync | Pairs with [`GetVehicleLastConnection`](/app/legacy/vehicle-info/vehicle-last-connection) |
| `vehicleCommandState` | Legacy command status by command id | For [`sendVehicleCommand`](/app/legacy/controls/send-vehicle-command) HMAC path |
| `vehicleCommandStatePx` | Parallax command result protobuf | Documented under [Parallax command status](/app/parallax/commands/command-status) |
| `tirePressureState` | Tire pressure fields | Subset of vehicle state |
| `vehicleDepartureSchedules` | Departure schedule updates | |
| `VehicleConsentStatus` | GNSS consent state | |
| `gearGuardRemoteConfig` | Live view WebRTC config | JSON config for Gear Guard streaming |

## Example: vehicleState

```json
{
  "type": "subscribe",
  "id": "<uuid>",
  "payload": {
    "operationName": "VehicleState",
    "variables": { "vehicleId": "<your-vehicle-id>" },
    "query": "subscription VehicleState($vehicleId: String!) { vehicleState(vehicleId: $vehicleId) { ... } }"
  }
}
```

Exact selection sets vary by app version; correlate `next` payloads with [`GetVehicleState`](/app/legacy/vehicle-state) response fields.

## Example: chargingSession

Used on the charging dive screen for typed `liveData` / chart fields. For protobuf live charging on the home screen, subscribe to [Charging domain](/app/parallax/domains/charging) RVMs via `ParallaxMessages` instead.

## Example: vehicleCommandState (legacy commands)

After [`sendVehicleCommand`](/app/legacy/controls/send-vehicle-command), poll completion via this subscription or the HTTP [`getVehicleCommand`](/app/legacy/controls/get-vehicle-command) query. When `state` is `0`, the command has finished.

For Parallax commands, use [`vehicleCommandStatePx`](/app/parallax/commands/command-status) instead.

## Related

- [Parallax subscription](/app/parallax/subscription) — `ParallaxMessages` protobuf stream
- [Legacy controls](/app/legacy/controls) — HMAC command path
- [Charging domain](/app/parallax/domains/charging) — Parallax charging RVMs
