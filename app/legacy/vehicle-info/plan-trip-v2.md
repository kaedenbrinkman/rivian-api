---
title: planTripWithMultiStopV2
parent: Vehicle info
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 3
---

# planTripWithMultiStopV2

## Overview

The current trip planner (app 3.17.0). Plans a route between waypoints with charging stops, and returns drive time, charging time, distance and state of charge along the way. Read-only; nothing is sent to the vehicle.

The older [`planTrip`](/app/legacy/vehicle-info/plan-trip) query no longer validates on the gateway (2026-10).

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
```

### Request Body

Only `waypoints` and `vehicle` are required. `vehicle` takes the vehicle id (the same value as `vehicleId` elsewhere).

```json
{
  "operationName": "planTripWithMultiStopV2",
  "variables": {
    "waypoints": [
      { "latitude": <origin-lat>, "longitude": <origin-lng> },
      { "latitude": <dest-lat>, "longitude": <dest-lng> }
    ],
    "vehicle": "<your-vehicle-id>",
    "startingSoc": 69.9,
    "departureTime": 1760000000
  },
  "query": "query planTripWithMultiStopV2($waypoints: [RequestWaypointInput!]!, $vehicle: String!, $startingSoc: Float, $startingRangeMeters: Float, $targetArrivalSocPercent: Float, $driveMode: DriveMode, $networkPreferences: [NetworkPreference!], $trailerProfile: TripPlanTrailerProfile, $hasAdapter: Boolean, $routePreferences: RoutePreferences, $departureTime: UnixTimestamp) { planTrip2(waypoints: $waypoints, vehicle: $vehicle, startingSoc: $startingSoc, startingRangeMeters: $startingRangeMeters, targetArrivalSocPercent: $targetArrivalSocPercent, driveMode: $driveMode, networkPreferences: $networkPreferences, trailerProfile: $trailerProfile, hasAdapter: $hasAdapter, routePreferences: $routePreferences, departureTime: $departureTime) { plans { planIdentifierMetadata { planId abrpRouteId legs { abrpLegId routeRequest } } driveLegs { distanceMeters durationSeconds energyConsumptionKwh polyline5 trafficAlongPolyline { polylineFirstIndex polylineLastIndex level } incidentsAlongPolyline { polylineFirstIndex polylineLastIndex incident } socAlongPolyline { polylineIndex distanceAlongPolylineMeters energyKwh socPercent rangeMeters } efficiency { polylineFirstIndex polylineLastIndex segmentLengthMeters segmentDurationSeconds consumedEnergyKwh } } waypoints { waypointType requestWaypointsIndex charger { adapterRequired entityId name maxPowerKw chargeDurationSeconds } latitude longitude totalTimeAtWaypointSeconds arrivalSOCPercent arrivalRangeMeters arrivalEnergyKwh targetArrivalSocPercent arrivalTimeUTC departureSOCPercent departureRangeMeters departureEnergyKwh departureTimeUTC distanceFromOriginMeters distanceToDestinationMeters isSystemAdded } batteryEmptyLocation { latitude longitude distanceToDestinationMeters } summary { destinationReachable socBelowLimitAtDestination totalChargeDurationSeconds totalDriveDurationSeconds totalDriveDistanceMeters totalTripDurationSeconds arrivalSOCPercent arrivalRangeMeters arrivalEnergyKwh } } status } }"
}
```

Other inputs seen in the app: `routePreferences { avoidTolls avoidFerries avoidHighways }`, `networkPreferences [{ networkId preference }]`, `driveMode`, `trailerProfile`, `hasAdapter`, `targetArrivalSocPercent`, `startingRangeMeters`.

### Example Response

Trimmed to the fields a time-to-leave calculation needs. `totalTripDurationSeconds` includes charging.

```json
{
  "data": {
    "planTrip2": {
      "status": "OK",
      "plans": [
        {
          "driveLegs": [
            { "distanceMeters": 180313, "durationSeconds": 6271 },
            { "distanceMeters": 178776, "durationSeconds": 5910 },
            { "distanceMeters": 241550, "durationSeconds": 8274 }
          ],
          "waypoints": [
            { "waypointType": "OTHER", "charger": null },
            { "waypointType": "DC_CHARGE_STATION", "charger": { "name": "Buttonwillow, CA [Rivian Adventure Network]", "chargeDurationSeconds": 900 } },
            { "waypointType": "DC_CHARGE_STATION", "charger": { "name": "Firebaugh, CA [Rivian Adventure Network]", "chargeDurationSeconds": 832 } },
            { "waypointType": "OTHER", "charger": null }
          ],
          "summary": {
            "destinationReachable": true,
            "totalChargeDurationSeconds": 1732,
            "totalDriveDurationSeconds": 20455,
            "totalDriveDistanceMeters": 600639,
            "totalTripDurationSeconds": 22637,
            "arrivalSOCPercent": 2
          }
        }
      ]
    }
  }
}
```

To turn an address into coordinates first, see [places](/app/legacy/vehicle-info/places).
