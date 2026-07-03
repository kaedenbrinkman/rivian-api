---
title: Controls
has_children: true
parent: Legacy
grand_parent: App API
nav_order: 2
permalink: /app/legacy/controls
---

# Legacy vehicle controls

Phone-key enrollment and **HMAC-signed** remote commands. The app prefers [Parallax commands](/app/parallax/commands) when `parallaxCommand` and per-domain `PARALLAX_*_COMMAND` features are enabled.

## Enrollment

Vehicle commands require an enrolled phone key (up to 2 devices). Enrollment exchanges a public key for a key id used in command requests.

## Endpoints

- [`EnrollPhone`](/app/legacy/controls/enroll-phone) — enroll a new phone key
- [`DisenrollPhone`](/app/legacy/controls/disenroll-phone) — remove a phone key
- [`ParseAndShareLocationToVehicle`](/app/legacy/controls/share-location) — send a destination to the vehicle
- [`sendVehicleCommand`](/app/legacy/controls/send-vehicle-command) — HMAC remote command
- [`getVehicleCommand`](/app/legacy/controls/get-vehicle-command) — poll legacy command status (HTTP)

Command completion over WebSocket: [`vehicleCommandState`](/app/legacy/websocket-subscriptions).

Modern alternative: [sendParallaxPayload](/app/parallax/commands/send-payload) + [vehicleCommandStatePx](/app/parallax/commands/command-status).
