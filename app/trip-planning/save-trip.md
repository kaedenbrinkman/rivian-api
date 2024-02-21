---
title: saveTrip
parent: Trip Planning Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# saveTrip

## Overview

The `saveTrip` endpoint is used to save a new trip.

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
  "operationName": "saveTrip",
  "variables": {
    "attrs": {
      "name": "Moab",
      "startingSOC": 68,
      "stops": [
        {
          "name": "",
          "location": {
            "latitude": <lat>,
            "longitude": <lng>
          },
          "type": "VEHICLE_LOCATION"
        },
        {
          "name": "Moab",
          "location": {
            "latitude": 38.5733155,
            "longitude": -109.5498395
          },
          "targetArrivalSOCPercent": 20,
          "type": "POI",
          "placeId": {
            "value": "ChIJjS24muXhR4cRLcTV8XqxMgs",
            "dataProvider": "GOOGLE"
          }
        }
      ],
      "driveMode": "everyday",
      "networkPreferences": [
        {
          "networkId": "10001",
          "preference": 1
        },
        {
          "networkId": "10002",
          "preference": 1
        }
      ],
      "trailerProfile": "NONE",
      "avoidAdapterRequired": false,
      "departureTime": 1708546484
    }
  },
  "query": "mutation saveTrip($attrs: TripPlanInput!) { saveTrip(attrs: $attrs) }"
}
```

### Example Response

```json
{
  "data": {
    "saveTrip": <new-trip-id>
  }
}
```
