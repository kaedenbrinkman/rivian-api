---
title: GetVehicleState
parent: App API
has_children: false
nav_order: 3
---

# GetVehicleState

## Overview

The `GetVehicleState` endpoint returns information about the status of a vehicle, such as speed, location, and closure statuses.

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
  "operationName": "GetVehicleState",
  "variables": {
    "vehicleID": <your-vehicle-id>
  },
  "query": "query GetVehicleState($vehicleID: String!) { vehicleState(id: $vehicleID) { __typename gnssLocation { __typename latitude longitude timeStamp } alarmSoundStatus { __typename timeStamp value } timeToEndOfCharge { __typename timeStamp value } doorFrontLeftLocked { __typename timeStamp value } doorFrontLeftClosed { __typename timeStamp value } doorFrontRightLocked { __typename timeStamp value } doorFrontRightClosed { __typename timeStamp value } doorRearLeftLocked { __typename timeStamp value } doorRearLeftClosed { __typename timeStamp value } doorRearRightLocked { __typename timeStamp value } doorRearRightClosed { __typename timeStamp value } windowFrontLeftClosed { __typename timeStamp value } windowFrontRightClosed { __typename timeStamp value } windowFrontLeftCalibrated { __typename timeStamp value } windowFrontRightCalibrated { __typename timeStamp value } windowRearLeftCalibrated { __typename timeStamp value } windowRearRightCalibrated { __typename timeStamp value } closureFrunkLocked { __typename timeStamp value } closureFrunkClosed { __typename timeStamp value } gearGuardLocked { __typename timeStamp value } closureLiftgateLocked { __typename timeStamp value } closureLiftgateClosed { __typename timeStamp value } windowRearLeftClosed { __typename timeStamp value } windowRearRightClosed { __typename timeStamp value } closureSideBinLeftLocked { __typename timeStamp value } closureSideBinLeftClosed { __typename timeStamp value } closureSideBinRightLocked { __typename timeStamp value } closureSideBinRightClosed { __typename timeStamp value } closureTailgateLocked { __typename timeStamp value } closureTailgateClosed { __typename timeStamp value } closureTonneauLocked { __typename timeStamp value } closureTonneauClosed { __typename timeStamp value } wiperFluidState { __typename timeStamp value } powerState { __typename timeStamp value } batteryHvThermalEventPropagation { __typename timeStamp value } vehicleMileage { __typename timeStamp value } brakeFluidLow { __typename timeStamp value } gearStatus { __typename timeStamp value } tirePressureStatusFrontLeft { __typename timeStamp value } tirePressureStatusValidFrontLeft { __typename timeStamp value } tirePressureStatusFrontRight { __typename timeStamp value } tirePressureStatusValidFrontRight { __typename timeStamp value } tirePressureStatusRearLeft { __typename timeStamp value } tirePressureStatusValidRearLeft { __typename timeStamp value } tirePressureStatusRearRight { __typename timeStamp value } tirePressureStatusValidRearRight { __typename timeStamp value } batteryLevel { __typename timeStamp value } chargerState { __typename timeStamp value } batteryLimit { __typename timeStamp value } remoteChargingAvailable { __typename timeStamp value } batteryHvThermalEvent { __typename timeStamp value } rangeThreshold { __typename timeStamp value } distanceToEmpty { __typename timeStamp value } otaAvailableVersionNumber { __typename timeStamp value } otaAvailableVersionWeek { __typename timeStamp value } otaAvailableVersionYear { __typename timeStamp value } otaCurrentVersionNumber { __typename timeStamp value } otaCurrentVersionWeek { __typename timeStamp value } otaCurrentVersionYear { __typename timeStamp value } otaDownloadProgress { __typename timeStamp value } otaInstallDuration { __typename timeStamp value } otaInstallProgress { __typename timeStamp value } otaInstallReady { __typename timeStamp value } otaInstallTime { __typename timeStamp value } otaInstallType { __typename timeStamp value } otaStatus { __typename timeStamp value } otaCurrentStatus { __typename timeStamp value } cabinClimateInteriorTemperature { __typename timeStamp value } cabinPreconditioningStatus { __typename timeStamp value } cabinPreconditioningType { __typename timeStamp value } petModeStatus { __typename timeStamp value } petModeTemperatureStatus { __typename timeStamp value } cabinClimateDriverTemperature { __typename timeStamp value } gearGuardVideoStatus { __typename timeStamp value } gearGuardVideoMode { __typename timeStamp value } gearGuardVideoTermsAccepted { __typename timeStamp value } defrostDefogStatus { __typename timeStamp value } steeringWheelHeat { __typename timeStamp value } seatFrontLeftHeat { __typename timeStamp value } seatFrontRightHeat { __typename timeStamp value } seatRearLeftHeat { __typename timeStamp value } seatRearRightHeat { __typename timeStamp value } chargerStatus { __typename timeStamp value } seatFrontLeftVent { __typename timeStamp value } seatFrontRightVent { __typename timeStamp value } chargerDerateStatus { __typename timeStamp value } driveMode { __typename timeStamp value } } }"
}
```

### Example Response

```json
{
  "data": {
    "vehicleState": {
      "__typename": "VehicleState",
      ...
    }
  }
}
```
