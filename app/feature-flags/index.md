---
title: Feature flags
has_children: true
parent: App API
nav_order: 4
permalink: /app/feature-flags
---

# Feature flags

The app gates most new behavior behind **two independent layers**. Both must pass (when a vehicle feature is required) before UI or API paths activate.

## Two layers

| Layer | Source | Scope | Checked via |
| --- | --- | --- | --- |
| **App remote config** | Firebase Remote Config | Account / app install | Boolean keys like `parallaxCommand` (`wy/b` enum in APK) |
| **Vehicle supported features** | Rivian GraphQL | Per vehicle | `SupportedFeatures` query — `{ name, status }` pairs |

The app combines them in `xy/a` (`FeatureGate`):

1. **App flags** — every listed remote-config key in a gate must be `true` (Firebase `RemoteConfigManager`, `js/d`).
2. **Vehicle feature** — if the gate lists a `VehicleFeature`, that vehicle’s supported-feature map must contain the matching API `name` with status **`AVAILABLE`**.

Parallax paths typically need **both** an app flag and a vehicle flag (see [Parallax gating](/app/feature-flags#parallax-gating) below).

## Vehicle feature statuses

GraphQL returns a string `status` per feature. The app maps these to `l30/hd`:

| Status | Meaning |
| --- | --- |
| `AVAILABLE` | Feature enabled for this vehicle |
| `UPDATE_FIRMWARE` | Requires a vehicle software update before use |
| `UNKNOWN__` | Unrecognized / fallback |

Only `AVAILABLE` passes `UserVehicleKt.isFeatureSupported()`.

## How to fetch vehicle features

Dedicated query (also nested under `getUserInfo` and `VehiclesAndEnrollments`):

- [`SupportedFeatures`](/app/legacy/vehicle-info/supported-features) — `POST https://rivian.com/api/gql/gateway/graphql`

The app caches the list in `SupportedVehicleFeatures` and resolves by `vehicleId`.

## App remote config

Fetched from **Firebase Remote Config** at startup (`js/d` / `RemoteConfigManager`). Keys use camelCase strings (e.g. `parallaxCommand`), mapped from Kotlin enum `wy/b`.

Full list: [App remote config flags](/app/feature-flags/app).

## Vehicle supported features

Server-driven list keyed by short API `name` strings (e.g. `PVS_BD_CMD`, `CHARG_DATA_PX`). Kotlin enum `VehicleFeature` maps friendly names to those API strings via `getFeatureName()`.

Full catalog and an **R1T** example response: [Vehicle supported features](/app/feature-flags/vehicle).

## Parallax gating

Common Parallax gates (app flag **and** vehicle feature):

| Capability | App remote config (`wy/b`) | Vehicle API name (`VehicleFeature`) |
| --- | --- | --- |
| Parallax vehicle-state RVMs | `parallaxVehicleState` | `PX_STATE_ALL` (`PARALLAX_VEHICLE_STATE`) |
| Parallax commands (any domain) | `parallaxCommand` | (per-domain row below) |
| Body commands | `parallaxCommand` | `PVS_BD_CMD` |
| Comfort commands | `parallaxCommand` | `PVS_COMF_CMD` |
| Security commands | `parallaxCommand` | `PVS_SEC_CMD` |
| Energy / charging commands | `parallaxCommand` | `PVS_ENRG_CMD` |
| OTA commands | `parallaxCommand` | `PVS_OTA_CMD` |
| Live charging session over Parallax | — | `CHARG_DATA_PX` |
| Parallax connectivity UI | `vehicleConnectivityParallax` | `VEHICLE_CONNECTIVITY_PARALLAX` |

When gated off, the app uses [Legacy](/app/legacy) JSON WebSocket / HMAC command paths instead. See [Parallax](/app/parallax).

## Related docs

- [SupportedFeatures endpoint](/app/legacy/vehicle-info/supported-features) — GraphQL query reference
- [Parallax](/app/parallax) — transport and RVMs affected by flags
- [Legacy controls](/app/legacy/controls) — fallback when Parallax command flags are off
