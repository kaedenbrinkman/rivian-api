---
title: planTrip
parent: Trip Planning Endpoints
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
  "operationName": "planTripWithMultiStop",
  "variables": {
    "waypoints": [
      {
        "latitude": <start-lat>,
        "longitude": <start-lng>,
        "waypointType": "OTHER"
      },
      {
        "latitude": <end-lng>,
        "longitude": <end-lng>,
        "entityId": "ChIJjS24muXhR4cRLcTV8XqxMgs",
        "waypointType": "OTHER"
      }
    ],
    "originBearing": 0,
    "vehicleId": <vehicle-id>,
    "startingSoc": 70,
    "startingRangeMeters": 353000,
    "targetArrivalSocPercent": 20,
    "driveMode": "EVERYDAY",
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
    "supportedConnectorTypes": [
      "CCS",
      "J1772"
    ]
  },
  "query": "query planTripWithMultiStop($waypoints: [CoordinatesInput!]!, $originBearing: Float!, $vehicleId: String!, $startingSoc: Float!, $startingRangeMeters: Float, $targetArrivalSocPercent: Float, $driveMode: String, $networkPreferences: [NetworkPreference!], $trailerProfile: String, $avoidAdapterRequired: Boolean, $supportedConnectorTypes: [String!]) { planTripMultiStop(originBearing: $originBearing, vehicleId: $vehicleId, startingSoc: $startingSoc, waypoints: $waypoints, startingRangeMeters: $startingRangeMeters, targetArrivalSocPercent: $targetArrivalSocPercent, driveMode: $driveMode, networkPreferences: $networkPreferences, trailerProfile: $trailerProfile, avoidAdapterRequired: $avoidAdapterRequired, supportedConnectorTypes: $supportedConnectorTypes) { routes { routeResponse destinationReached totalChargingDuration arrivalSOC arrivalReachableDistance waypoints { waypointType entityId name latitude longitude maxPower chargeDuration arrivalSOC arrivalReachableDistance departureSOC departureReachableDistance adapterRequired } energyConsumptionOnLeg batteryEmptyToDestinationDistance batteryEmptyLocationLatitude batteryEmptyLocationLongitude } tripPlanStatus chargeStationsAvailable socBelowLimit } }"
}
```

### Example Response

```json
{
  "data": {
    "planTripMultiStop": {
      "routes": [
        {
          "routeResponse": <large-object-with-route-geometry>,
          "destinationReached": true,
          "totalChargingDuration": 17428,
          "arrivalSOC": 23,
          "arrivalReachableDistance": 117000,
          "waypoints": [
            {
              "waypointType": "DC_CHARGE_STATION",
              "entityId": "riv_chrg_16214382483804747063",
              "name": "1206 N. Canyon Creek Pkwy, Spanish Fork [Electrify America]",
              "latitude": 40.124141693115234,
              "longitude": -111.64026641845703,
              "maxPower": 150,
              "chargeDuration": 4144,
              "arrivalSOC": 16,
              "arrivalReachableDistance": 83000,
              "departureSOC": 97,
              "departureReachableDistance": 505000,
              "adapterRequired": null
            },
            {
              "waypointType": "OTHER",
              "entityId": "ChIJjS24muXhR4cRLcTV8XqxMgs",
              "name": null,
              "latitude": 38.5733155,
              "longitude": -109.5498395,
              "maxPower": null,
              "chargeDuration": 0,
              "arrivalSOC": 23,
              "arrivalReachableDistance": 117000,
              "departureSOC": 23,
              "departureReachableDistance": 117000,
              "adapterRequired": null
            }
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
