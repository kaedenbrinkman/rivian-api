---
title: SupportedFeatures
parent: Vehicle Info Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# SupportedFeatures

## Overview

The `SupportedFeatures` endpoint returns the feature flags enabled for all vehicles in your account.

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
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

```json
{
  "data": {
    "currentUser": {
      "vehicles": [
        {
          "id": <vehicle-id>,
          "vehicle": {
            "vehicleState": {
              "supportedFeatures": [
                {
                  "name": "ADDR_SHR",
                  "status": "AVAILABLE"
                },
                {
                  "name": "ADDR_SHR_TXT",
                  "status": "AVAILABLE"
                },
                {
                  "name": "ADDR_SHR_YLP",
                  "status": "AVAILABLE"
                },
                {
                  "name": "CAR_WASH_MODE",
                  "status": "AVAILABLE"
                },
                {
                  "name": "CHARG_CMD",
                  "status": "AVAILABLE"
                },
                {
                  "name": "CHARG_SCHED",
                  "status": "AVAILABLE"
                },
                {
                  "name": "CHARG_SLIDER",
                  "status": "AVAILABLE"
                },
                {
                  "name": "DEFROST_DEFOG",
                  "status": "AVAILABLE"
                },
                {
                  "name": "FRUNK_NXT_ACT",
                  "status": "AVAILABLE"
                },
                {
                  "name": "GEAR_GUARD_VIDEO_SETTING",
                  "status": "AVAILABLE"
                },
                {
                  "name": "HEATED_SEATS",
                  "status": "AVAILABLE"
                },
                {
                  "name": "HEATED_WHEEL",
                  "status": "AVAILABLE"
                },
                {
                  "name": "PET_MODE",
                  "status": "AVAILABLE"
                },
                {
                  "name": "PRECON_CMD_RESP",
                  "status": "AVAILABLE"
                },
                {
                  "name": "PRECON_SCRN_PROT",
                  "status": "AVAILABLE"
                },
                {
                  "name": "RENAME_VEHICLE",
                  "status": "AVAILABLE"
                },
                {
                  "name": "SCHED_DPRT",
                  "status": "AVAILABLE"
                },
                {
                  "name": "SET_TEMP_CMD",
                  "status": "AVAILABLE"
                },
                {
                  "name": "SIDE_BIN_NXT_ACT",
                  "status": "AVAILABLE"
                },
                {
                  "name": "TAILGATE_CMD",
                  "status": "AVAILABLE"
                },
                {
                  "name": "TAILGATE_NXT_ACT",
                  "status": "AVAILABLE"
                },
                {
                  "name": "TRAILER_STATUS",
                  "status": "AVAILABLE"
                },
                {
                  "name": "TRIP_ADD_STOP",
                  "status": "AVAILABLE"
                },
                {
                  "name": "TRIP_PLANNER",
                  "status": "AVAILABLE"
                },
                {
                  "name": "TRIP_PLANNER_DRIVE_MODE",
                  "status": "AVAILABLE"
                },
                {
                  "name": "VENTED_SEATS",
                  "status": "AVAILABLE"
                },
                {
                  "name": "WIN_CALIB_STS",
                  "status": "AVAILABLE"
                },
                {
                  "name": "WIN_NXT_ACT",
                  "status": "AVAILABLE"
                }
              ]
            }
          }
        }
      ]
    }
  }
}
```
