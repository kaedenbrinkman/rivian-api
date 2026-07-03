---
title: Gear Guard
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 11
---

# Gear Guard streaming (Parallax)

In-vehicle streaming consent and daily limits (distinct from alarm/video **state** in [Security](/app/parallax/domains/security)).

## RVMs

| RVM | Protobuf | Notes |
| --- | --- | --- |
| `gearguard_streaming.privacy.gearguard_streaming_in_vehicle_consent` | `n70/g` | Consent status |
| `gearguard_streaming.privacy.gearguard_streaming_daily_limit` | `n70/b` | `dailyLimit`, `nextResetTimeUnixSec` |

### `n70/b` — daily limit

| Field | Type |
| --- | --- |
| 1 | int32 dailyLimit |
| 2 | int64 nextResetTimeUnixSec |

## Legacy WebSocket

Live view session setup uses **`gearGuardRemoteConfig`** (JSON WebRTC config) — [Legacy subscriptions](/app/legacy/websocket-subscriptions), not these RVMs.

Video monitoring **state** (`gearGuardVideoStatus`): `security.video_monitoring.state` + `GetVehicleState`.
