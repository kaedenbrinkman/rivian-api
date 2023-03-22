---
title: planTrip
parent: App API
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
csrf-token: <your CSRF token from the previous request>
```

### Request Body

```json
{
  "operationName": "planTrip",
  "variables": {
    "origin": {
      "latitude": <origin-latitude>,
      "longitude": <origin-longitude>
    },
    "destination": {
      "latitude": <destination-latitude>,
      "longitude": <destination-longitude>
    },
    "bearing": 0,
    "vehicleId": <your-vehicle-id>,
    "startingSoc": <your-current-soc>
  },
  "query": "query planTrip($origin: CoordinatesInput!, $destination: CoordinatesInput!, $bearing: Float!, $vehicleId: String!, $startingSoc: Float!) { planTrip(bearing: $bearing, vehicleId: $vehicleId, startingSoc: $startingSoc, origin: $origin, destination: $destination) { __typename routes { __typename routeResponse destinationReached totalChargingDuration arrivalSOC arrivalReachableDistance chargeStops { __typename entityId name maxPower chargeDuration arrivalSOC arrivalReachableDistance departureSOC departureReachableDistance latitude longitude } energyConsumptionOnLeg batteryEmptyToDestinationDistance batteryEmptyLocationLatitude batteryEmptyLocationLongitude } tripPlanStatus chargeStationsAvailable socBelowLimit } }"
}
```

### Example Response

```json
UNKNOWN
```
