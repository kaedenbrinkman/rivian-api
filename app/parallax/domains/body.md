---
title: Body
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 3
---

# Body (Parallax)

Doors, closures, windows, trailer.

## RVMs

| RVM | Vehicle state? | Legacy `GetVehicleState` |
| --- | --- | --- |
| `body.locks.states` | yes | `door*Locked`, `closure*Locked`, `gearGuardLocked` |
| `body.closures.states` | | `door*Closed`, `closure*Closed`, `closure*NextAction` |
| `body.windows.states` | | `window*Closed`, `windowsNextAction`, `window*Calibrated` |
| `body.trailer.state` | | Trailer connection state |

## Protobuf

Body RVMs are vehicle-state topics. In `cm/c.parseRvmData()` many map to generic handlers; full message types are in `g70/*` / related packages (exact class per RVM requires further smali tracing).

Practical approach:

1. Subscribe with `PARALLAX_VEHICLE_STATE` enabled.
2. Capture payloads while toggling locks/windows via app or [commands](/app/parallax/commands).
3. Correlate enum changes with legacy [`GetVehicleState`](/app/legacy/vehicle-state) string values (`locked` / `unlocked`, `open` / `closed`).

## Commands

Lock/unlock, windows, frunk, liftgate, tailgate, charge port, side bins → `PARALLAX_BODY_COMMAND` when enabled. Fallback: legacy [controls](/app/legacy/controls).
