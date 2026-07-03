---
title: SupportedFeatures
parent: Vehicle info
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 6
---

# SupportedFeatures

## Overview

The `SupportedFeatures` endpoint returns feature flags for each vehicle on the account. The app uses these to show or hide UI for charging, Gear Guard, PIN, trip planning, Parallax, and other capabilities.

See [Feature flags](/app/feature-flags) for how app remote config and vehicle features combine, and a full flag catalog with an **R1T** example.

The same data is also available nested under `currentUser.vehicles[].vehicle.vehicleState.supportedFeatures` in [`getUserInfo`](/app/account/user-info). This query fetches only the feature list.

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
apollographql-client-name: com.rivian.android.consumer
```

### Request Body

```json
{
  "operationName": "SupportedFeatures",
  "variables": {},
  "query": "query SupportedFeatures { currentUser { vehicles { id vehicle { vehicleState { supportedFeatures { name status } } } } } }"
}
```

### Example Response

Example feature flags for a vehicle named **R1T** (names come from [`getUserInfo`](/app/account/user-info) / [`VehicleNames`](/app/legacy/vehicle-info/vehicle-names), not this query).

```json
{
  "data": {
    "currentUser": {
      "vehicles": [
        {
          "id": "<your-vehicle-id>",
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

Each feature has a `name` (internal code) and `status` (e.g. `AVAILABLE`). Feature availability varies by vehicle model and software version. See [Vehicle supported features](/app/feature-flags/vehicle) for enum ↔ API name mapping.
