---
title: Charging Schedule
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# Charging Schedule

## Overview

The charging schedule endpoint allows the user to get/set a charge schedule including location and amperage.

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
```

`POST https://rivian.com/api/gql/gateway/graphql`

### Set Charging Schedule

```json
{
    "operationName": "SetChargingSchedule",
    "variables": {
        "vehicleId": <your-vehicle-id>,
        "chargingSchedules": [{
            "weekDays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday" <optional:, "Saturday", "Sunday">],
            "startTime": <minutes-after-midnight-to-start-charging>,
            "duration": <duration-in-minutes>,
            "location": {
                "latitude": <latitidue-for-schedule>,
                "longitude": <longitude-for-schedule>
            },
            "amperage": <amps>,
            "enabled": true
        }]
    },
    "query": "mutation SetChargingSchedule($vehicleId: String!, $chargingSchedules: [InputChargingSchedule!]!) { setChargingSchedules(vehicleId: $vehicleId, chargingSchedules: $chargingSchedules) { success } }"
}
```

### Example Response

```json
{
  "data": {
    "getVehicle": {
      "chargingSchedules": [
        {
          "startTime": 210,
          "duration": 210,
          "location": {
            "latitude": <lat>,
            "longitude": <lng>
          },
          "amperage": 48,
          "enabled": false,
          "weekDays": []
        }
      ]
    }
  }
}
```

`POST https://rivian.com/api/gql/gateway/graphql`

### Get the Charging Schedule

```json
{
    "operationName": "GetChargingSchedule",
    "variables": {
        "vehicleId": <your-vehicle-id>
    },
    "query": "query GetChargingSchedule($vehicleId: String!) { getVehicle(id: $vehicleId) { chargingSchedules { startTime duration location { latitude longitude } amperage enabled weekDays } } }"
}
```

### Example Response

```json
{
    "data": {
        "getVehicle": {
            "chargingSchedules": [{
                "startTime": 1320,
                "duration": 360,
                "location": {
                    "latitude": 40.50505677290137,
                    "longitude": -89.05740992302492
                },
                "amperage": 44,
                "enabled": true,
                "weekDays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            }]
        }
    }
}
```
