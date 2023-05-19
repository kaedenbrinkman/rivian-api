---
title: planTrip
parent: Vehicle Info Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# planTrip

## Overview

The `planTrip` endpoint is used for planning charging stops along a route.

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
  "operationName": "planTrip",
  "variables": {
    "origin": {
      "latitude": <your-lat>,
      "longitude": <your-lng>
    },
    "destination": {
      "latitude": <dest-lat>,
      "longitude": <dest-lng>
    },
    "bearing": 0,
    "vehicleId": <your-vehicle-id>,
    "startingSoc": 57.20000076293945,
    "startingRangeMeters": 298000,
    "targetArrivalSocPercent": 20,
    "networkPreferences": [
      {
        "networkId": "10001",
        "preference": 1
      },
      {
        "networkId": "10002",
        "preference": 1
      },
      {
        "networkId": "10031",
        "preference": 1
      },
      {
        "networkId": "10050",
        "preference": 1
      },
      {
        "networkId": "10050",
        "preference": 1
      }
    ]
  },
  "query": "query planTrip($origin: CoordinatesInput!, $destination: CoordinatesInput!, $bearing: Float!, $vehicleId: String!, $startingSoc: Float!, $startingRangeMeters: Float!, $targetArrivalSocPercent: Float, $networkPreferences: [NetworkPreference!]) { planTrip(bearing: $bearing, vehicleId: $vehicleId, startingSoc: $startingSoc, origin: $origin, destination: $destination, startingRangeMeters: $startingRangeMeters, targetArrivalSocPercent: $targetArrivalSocPercent, networkPreferences: $networkPreferences) { routes { routeResponse destinationReached totalChargingDuration arrivalSOC arrivalReachableDistance waypoints { waypointType entityId name latitude longitude maxPower chargeDuration arrivalSOC arrivalReachableDistance departureSOC departureReachableDistance } energyConsumptionOnLeg batteryEmptyToDestinationDistance batteryEmptyLocationLatitude batteryEmptyLocationLongitude } tripPlanStatus chargeStationsAvailable socBelowLimit } }"
}
```

### Example Response

```json
{
  "data": {
    "planTrip": {
      "routes": [
        {
          "routeResponse": <large-object-with-route-data>,
          "destinationReached": true,
          "totalChargingDuration": 702,
          "arrivalSOC": 25,
          "arrivalReachableDistance": 131912.6711788204,
          "waypoints": [
            {
              "waypointType": "DC_CHARGE_STATION",
              "entityId": <station_id>,
              "name": <station_name>,
              "latitude": <station_lat>,
              "longitude": <station_lng>,
              "maxPower": 150,
              "chargeDuration": 313,
              "arrivalSOC": 49,
              "arrivalReachableDistance": 254632.05919842955,
              "departureSOC": 56,
              "departureReachableDistance": 291421.6339635606
            },
            ...
          ],
          "energyConsumptionOnLeg": null,
          "batteryEmptyToDestinationDistance": null,
          "batteryEmptyLocationLatitude": null,
          "batteryEmptyLocationLongitude": null
        }
      ],
      "tripPlanStatus": "Ok",
      "chargeStationsAvailable": true,
      "socBelowLimit": false
    }
  }
}
```
