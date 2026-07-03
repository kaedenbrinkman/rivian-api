---
title: Vehicle supported features
parent: Feature flags
grand_parent: App API
has_children: false
nav_order: 2
---

# Vehicle supported features

Per-vehicle capability flags returned by GraphQL as `{ name, status }`. The app maps `name` strings into enum `VehicleFeature` (`getFeatureName()`) for type-safe checks.

Query: [`SupportedFeatures`](/app/legacy/vehicle-info/supported-features)

## Kotlin enum → API name

All **61** entries in `VehicleFeature`. Where the API string differs from the enum constant, it is shown in the **API name** column.

### Parallax

| Enum | API name | Role |
| --- | --- | --- |
| `PARALLAX_VEHICLE_STATE` | `PX_STATE_ALL` | Parallax vehicle-state RVM subscription |
| `PARALLAX_BODY_COMMAND` | `PVS_BD_CMD` | Body commands via `sendParallaxPayload` |
| `PARALLAX_COMFORT_COMMAND` | `PVS_COMF_CMD` | Comfort / HVAC commands |
| `PARALLAX_SECURITY_COMMAND` | `PVS_SEC_CMD` | Security / alarm commands |
| `PARALLAX_ENERGY_COMMAND` | `PVS_ENRG_CMD` | Energy / charging commands |
| `PARALLAX_OTA_COMMAND` | `PVS_OTA_CMD` | OTA install / schedule commands |
| `CHARGING_SESSION_OVER_PARALLAX` | `CHARG_DATA_PX` | Live charging session over Parallax |
| `VEHICLE_CONNECTIVITY_PARALLAX` | `VEHICLE_CONNECTIVITY_PARALLAX` | Connectivity state over Parallax |

### Parallax state (API only — no `VehicleFeature` enum)

These appear in `SupportedFeatures` alongside the command flags above. They gate Parallax **read** paths by domain:

| API name | Likely domain |
| --- | --- |
| `PVS_BD_ST8` | Body state RVMs |
| `PVS_COMF_ST8` | Comfort state RVMs |
| `PVS_DYN_ST8` | Dynamics (gear, range, tires, …) |
| `PVS_ENRG_ST8` | Energy state RVMs |
| `PVS_MOD_ST8` | Model / metadata state |
| `PVS_OTA_ST8` | OTA state RVMs |
| `PVS_SEC_ST8` | Security state RVMs |
| `PVS_VEH_ST8` | General vehicle state RVMs |

### Energy & charging

| Enum | API name |
| --- | --- |
| `PARKED_ENERGY_MONITOR` | `ENRG_MONTR_PARK` |
| `ACTIVE_ENERGY_MONITOR` | `ENRG_MONTR_ACTIVE` |
| `COLD_WEATHER_BAR` | `ENRG_CLD_WTHR` |
| `SMART_CHARG` | `SMART_CHARG` |
| `CHARG_NTW_EA` | `CHARG_NTW_EA` |
| `CHARG_NTW_IONNA` | `CHARG_NTW_IONNA` |
| `CHARGE_PORT_DOOR_COMMAND` | `CHARG_PORT_DOOR_COMMAND` |
| `CHARGING_TRIP_TARGET` | `CHARG_TRIP_TARGET` |
| `SD_CHARG_ENDS_AT` | `SD_CHARG_ENDS_AT` |
| `TESLA_NACS` | `TESLA_NACS` |

### Body & closures

| Enum | API name |
| --- | --- |
| `TAILGATE_CMD` | `TAILGATE_CMD` |
| `LIFTGATE_CMD` | `LIFTGATE_CMD` |
| `WINDOWS_CMD` | `WINDOWS_CMD` |
| `TAILGATE_NXT_ACT` | `TAILGATE_NXT_ACT` |
| `SIDE_BIN_NXT_ACT` | `SIDE_BIN_NXT_ACT` |
| `TRAILER_STATUS` | `TRAILER_STATUS` |
| `CAR_WASH_MODE` | `CAR_WASH_MODE` |
| `HONK_AND_FLASH_COMMAND` | `HONK_AND_FLASH_COMMAND` |

### Comfort & climate

| Enum | API name |
| --- | --- |
| `CLM_HOLD` | `CLM_HOLD` |
| `AUTO_VENT` | `AUTO_VENT` |
| `LOWER_PET_MODE_TEMPERATURE` | `PET_MODE_LOW_TEMP` |
| `HEATED_SEATS_THIRD` | `HEATED_SEATS_THIRD` |
| `SCHED_DPRT_3RD_ROW` | `SCHED_DPRT_3RD_ROW` |

### Security & Gear Guard

| Enum | API name |
| --- | --- |
| `GEAR_GUARD_STREAMING` | `V_GGVS` |
| `GEAR_GUARD_VIDEO_DOWNLOADING` | `V_GGVD` |
| `LIVE_CAM` | `LIVE_CAM` |
| `MOTION_CAM` | `MOTION_CAM` |
| `VIDEO_DOWNLOADING_FW_SUPPORT` | `VIDEO_DOWNLOADING` |

### Navigation & trip

| Enum | API name |
| --- | --- |
| `TRIP_NAV_PX` | `TRIP_NAV_PX` |
| `TRIP_PLANNER_TRAILERS` | `TRIP_PLANNER_TRAILERS` |
| `SAVED_LOCATIONS` | `SAVED_LOCATIONS` |
| `V_SATMAP` | `V_SATMAP` |
| `SEARCH_PLUS` | `V_SRCH_PLUS` |

### Access, keys & drive auth

| Enum | API name |
| --- | --- |
| `KEY_PAAK` | `KEY_PAAK` |
| `KEY_FOB_2` | `KEY_FOB_2` |
| `PASSIVE_ENTRY_PROTO_V2` | `PASSIVE_ENTRY_PROTO_V2` |
| `HMAC_TIMEOUT_90S` | `HMAC_TIMEOUT_90S` |
| `TWO_FACTOR_DRIVE` | `TWO_FACTOR_DRIVE` |
| `ORPHANED_PHONE_KEY_RECOVERY_HANDLING` | `ORPHANED_PHONE_KEY_RECOVERY_HANDLING` |

### OTA & schedules

| Enum | API name |
| --- | --- |
| `SCHED_OTA` | `SCHED_OTA` |
| `SCHED_DPRT` | `SCHED_DPRT` |
| `ICE_RESTART` | `ICE_RESTART` |

### Profile, PIN & intelligence

| Enum | API name |
| --- | --- |
| `PIN_PROFILE` | `PIN_PROFILE` |
| `RVA` | `RVA` |
| `RVA_MEM` | `RVA_MEM` |
| `AUTONOMY_PLUS` | `AUTONOMY_PLUS` |
| `INTERIOR_CAMERA` | `INTERIOR_CAMERA` |
| `PRIV_PREF` | `PRIV_PREF` |

### Other

| Enum | API name |
| --- | --- |
| `ACTIVE_USR` | `ACTV_USR` |
| `MOBILE_WHEEL_SWAP` | `MOBILE_WHEEL_SWAP` |
| `CONN_SUB` | `CONN_SUB` |
| `HLWN_25` | `HLWN_25` |
| `HLWN_25_G2` | `HLWN_25_G2` |

### Additional API names (observed in responses, not in `VehicleFeature` enum)

| API name | Notes |
| --- | --- |
| `ACTIVE_TRIP` | Active navigation trip UI |
| `CHARG_CLEAN_NRG` | Clean energy / charging insights |
| `CONNECT_PLUS` | Connect+ subscription (likely maps from `CONN_SUB`) |
| `CLM_HOLD_AUTO_VENT` | Climate hold + auto vent combo |
| `PET_COMFORT_CONTROL` | Pet comfort mode controls |
| `PIN_KEY_DRIVE` | PIN required to drive |
| `PREMIUM_SPEAKER` | Premium audio package |
| `TRIP_ADD_STOP` | Add stop on active trip |
| `WATCH_GEN1_PAIRING` | Apple Watch gen-1 pairing |

## Example: R1T

Illustrative response for an **R1T** on the account (vehicle display name `"R1T"`). Actual flags vary by model year, firmware, and subscription.

```json
{
  "data": {
    "currentUser": {
      "vehicles": [
        {
          "id": "<your-vehicle-id>",
          "name": "R1T",
          "vehicle": {
            "vehicleState": {
              "supportedFeatures": [
                { "name": "ACTIVE_TRIP", "status": "AVAILABLE" },
                { "name": "ACTV_USR", "status": "AVAILABLE" },
                { "name": "AUTO_VENT", "status": "AVAILABLE" },
                { "name": "CAR_WASH_MODE", "status": "AVAILABLE" },
                { "name": "CHARG_DATA_PX", "status": "AVAILABLE" },
                { "name": "CHARG_NTW_EA", "status": "AVAILABLE" },
                { "name": "CHARG_NTW_IONNA", "status": "AVAILABLE" },
                { "name": "CHARG_PORT_DOOR_COMMAND", "status": "AVAILABLE" },
                { "name": "CHARG_CLEAN_NRG", "status": "AVAILABLE" },
                { "name": "SMART_CHARG", "status": "AVAILABLE" },
                { "name": "CHARG_TRIP_TARGET", "status": "AVAILABLE" },
                { "name": "CONNECT_PLUS", "status": "AVAILABLE" },
                { "name": "CLM_HOLD", "status": "AVAILABLE" },
                { "name": "CLM_HOLD_AUTO_VENT", "status": "AVAILABLE" },
                { "name": "ENRG_CLD_WTHR", "status": "AVAILABLE" },
                { "name": "ENRG_MONTR_ACTIVE", "status": "AVAILABLE" },
                { "name": "ENRG_MONTR_PARK", "status": "AVAILABLE" },
                { "name": "VIDEO_DOWNLOADING", "status": "AVAILABLE" },
                { "name": "LIVE_CAM", "status": "AVAILABLE" },
                { "name": "V_GGVS", "status": "AVAILABLE" },
                { "name": "HMAC_TIMEOUT_90S", "status": "AVAILABLE" },
                { "name": "KEY_PAAK", "status": "AVAILABLE" },
                { "name": "V_SRCH_PLUS", "status": "AVAILABLE" },
                { "name": "V_SATMAP", "status": "AVAILABLE" },
                { "name": "MOBILE_WHEEL_SWAP", "status": "AVAILABLE" },
                { "name": "MOTION_CAM", "status": "AVAILABLE" },
                { "name": "PVS_BD_CMD", "status": "AVAILABLE" },
                { "name": "PVS_BD_ST8", "status": "AVAILABLE" },
                { "name": "PVS_COMF_CMD", "status": "AVAILABLE" },
                { "name": "PVS_COMF_ST8", "status": "AVAILABLE" },
                { "name": "PVS_DYN_ST8", "status": "AVAILABLE" },
                { "name": "PVS_ENRG_CMD", "status": "AVAILABLE" },
                { "name": "PVS_ENRG_ST8", "status": "AVAILABLE" },
                { "name": "PVS_MOD_ST8", "status": "AVAILABLE" },
                { "name": "PVS_OTA_CMD", "status": "AVAILABLE" },
                { "name": "PVS_OTA_ST8", "status": "AVAILABLE" },
                { "name": "PVS_SEC_CMD", "status": "AVAILABLE" },
                { "name": "PVS_SEC_ST8", "status": "AVAILABLE" },
                { "name": "PVS_VEH_ST8", "status": "AVAILABLE" },
                { "name": "PX_STATE_ALL", "status": "AVAILABLE" },
                { "name": "PASSIVE_ENTRY_PROTO_V2", "status": "AVAILABLE" },
                { "name": "PET_COMFORT_CONTROL", "status": "AVAILABLE" },
                { "name": "PET_MODE_LOW_TEMP", "status": "AVAILABLE" },
                { "name": "PIN_KEY_DRIVE", "status": "AVAILABLE" },
                { "name": "PIN_PROFILE", "status": "AVAILABLE" },
                { "name": "PREMIUM_SPEAKER", "status": "AVAILABLE" },
                { "name": "RVA", "status": "AVAILABLE" },
                { "name": "RVA_MEM", "status": "AVAILABLE" },
                { "name": "SAVED_LOCATIONS", "status": "AVAILABLE" },
                { "name": "SCHED_DPRT", "status": "AVAILABLE" },
                { "name": "SCHED_OTA", "status": "AVAILABLE" },
                { "name": "SD_CHARG_ENDS_AT", "status": "AVAILABLE" },
                { "name": "SIDE_BIN_NXT_ACT", "status": "AVAILABLE" },
                { "name": "TAILGATE_CMD", "status": "AVAILABLE" },
                { "name": "TAILGATE_NXT_ACT", "status": "AVAILABLE" },
                { "name": "TESLA_NACS", "status": "AVAILABLE" },
                { "name": "TRAILER_STATUS", "status": "AVAILABLE" },
                { "name": "TRIP_ADD_STOP", "status": "AVAILABLE" },
                { "name": "TRIP_NAV_PX", "status": "AVAILABLE" },
                { "name": "TRIP_PLANNER_TRAILERS", "status": "AVAILABLE" },
                { "name": "TWO_FACTOR_DRIVE", "status": "AVAILABLE" },
                { "name": "VEHICLE_CONNECTIVITY_PARALLAX", "status": "AVAILABLE" },
                { "name": "WATCH_GEN1_PAIRING", "status": "AVAILABLE" },
                { "name": "WINDOWS_CMD", "status": "AVAILABLE" }
              ]
            }
          }
        }
      ]
    }
  }
}
```

To fetch only features (without nesting under `vehicleState`), use the query on the [SupportedFeatures](/app/legacy/vehicle-info/supported-features) page.

## See also

- [Feature flags overview](/app/feature-flags) — how app + vehicle layers combine
- [App remote config](/app/feature-flags/app) — Firebase flags such as `parallaxCommand`
- [Parallax](/app/parallax) — behavior when Parallax flags are on
