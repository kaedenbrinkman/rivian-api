---
title: Get Live Charging Session Data
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# Get Live Charging Session Data

# getLiveSessionData

## Overview

The `getLiveSessionData` gets live charging session information for a vehicle.

`POST https://rivian.com/api/gql/chrg/user/graphql`

### Request Body

```json
{
  "operationName": "getLiveSessionData",
  "variables": {
    "vehicleId": <your-vehicle-id>
    },
  "query": "query getLiveSessionData($vehicleId: ID) { getLiveSessionData(vehicleId: $vehicleId) { isRivianCharger isFreeSession vehicleChargerState { value updatedAt } chargerId startTime timeElapsed timeRemaining { value updatedAt } kilometersChargedPerHour { value updatedAt } power { value updatedAt } rangeAddedThisSession { value updatedAt } totalChargedEnergy { value updatedAt } timeRemaining { value updatedAt } vehicleChargerState { value updatedAt } kilometersChargedPerHour { value updatedAt } currentPrice } }"
}
```

### Example Response

```json
{
   "data":{
      "getLiveSessionData":{
         "isRivianCharger":false,
         "isFreeSession":false,
         "vehicleChargerState":{
            "value":"charging_active",
            "updatedAt":"2023-06-08T22:53:20.578Z"
         },
         "chargerId":"USCPIL13538041",
         "startTime":"2023-06-08T20:03:49.021983Z",
         "timeElapsed":"10236",
         "timeRemaining":{
            "value":"4070",
            "updatedAt":"2023-06-08T22:54:15.072Z"
         },
         "kilometersChargedPerHour":{
            "value":31,
            "updatedAt":"2023-06-08T22:54:07.781Z"
         },
         "power":{
            "value":10,
            "updatedAt":"2023-06-08T22:53:20.578Z"
         },
         "rangeAddedThisSession":{
            "value":90,
            "updatedAt":"2023-06-08T22:54:07.781Z"
         },
         "totalChargedEnergy":{
            "value":25,
            "updatedAt":"2023-06-08T22:53:20.578Z"
         },
         "currentPrice":0
      }
   }
}
```
