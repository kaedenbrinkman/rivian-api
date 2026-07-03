---
title: Legacy
has_children: true
parent: App API
nav_order: 5
permalink: /app/legacy
---

# Legacy APIs

Pre-Parallax (or parallel) HTTP and WebSocket endpoints still present in the Rivian app. The app uses these when Parallax feature flags are off, for one-shot reads, account metadata, wallbox/public charging, phone-key enrollment, and typed JSON subscriptions alongside Parallax protobuf streams.

For live vehicle protobuf streams and Parallax commands, see [Parallax](/app/parallax).

## WebSocket (non-Parallax)

- [WebSocket subscriptions](/app/legacy/websocket-subscriptions) — `vehicleState`, `chargingSession`, `vehicleCommandState`, and other JSON subs on the same URL as Parallax

## HTTP

### Vehicle state

- [`GetVehicleState`](/app/legacy/vehicle-state) — one-shot typed JSON vehicle state (correlates with many Parallax RVMs)

### Controls (phone key + HMAC commands)

- [Legacy controls](/app/legacy/controls) — `EnrollPhone`, `sendVehicleCommand`, share location, etc.

### Vehicle info

- [Legacy vehicle info](/app/legacy/vehicle-info) — enrollments, OTA release notes, trip planning, images, feature flags

### Charging (HTTP)

- [Legacy charging](/app/legacy/charging) — wallbox, public charging sites, completed session history (not live Parallax session data)

## When the app uses legacy vs Parallax

| Capability | Parallax (preferred) | Legacy fallback |
| --- | --- | --- |
| Live SOC, locks, climate, … | `ParallaxMessages` RVMs | `vehicleState` WebSocket + `GetVehicleState` |
| Remote lock/unlock, HVAC, … | `sendParallaxPayload` | `sendVehicleCommand` + HMAC |
| Command status | `vehicleCommandStatePx` | `vehicleCommandState` / `getVehicleCommand` |
| Live charging graphs (home) | Charging + Energy RVMs | `chargingSession` WebSocket (detail screen) |
| Wallbox / session history | — | HTTP `chrg/user/graphql` |
