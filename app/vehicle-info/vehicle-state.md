---
title: GetVehicleState
parent: Vehicle Info Endpoints
grand_parent: App API
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
      "gnssLocation": {
        "latitude": <your-lat>,
        "longitude": <your-lng>,
        "timeStamp": "2023-05-19T05:27:38.018Z",
        "isAuthorized": true
      },
      "alarmSoundStatus": {
        "timeStamp": "2023-05-19T03:40:10.277Z",
        "value": "false"
      },
      "timeToEndOfCharge": {
        "timeStamp": "2023-05-19T05:23:33.538Z",
        "value": 0
      },
      "doorFrontLeftLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "doorFrontLeftClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "doorFrontRightLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "doorFrontRightClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "doorRearLeftLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "doorRearLeftClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "doorRearRightLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "doorRearRightClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "windowFrontLeftClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "windowFrontRightClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "windowFrontLeftCalibrated": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "Calibrated"
      },
      "windowFrontRightCalibrated": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "Calibrated"
      },
      "windowRearLeftCalibrated": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "Calibrated"
      },
      "windowRearRightCalibrated": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "Calibrated"
      },
      "closureFrunkLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "closureFrunkClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "closureFrunkNextAction": {
        "timeStamp": "2023-05-19T03:38:58.502Z",
        "value": "Open_Allowed"
      },
      "gearGuardLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "unlocked"
      },
      "closureLiftgateLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "closureLiftgateClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "signal_not_available"
      },
      "closureLiftgateNextAction": {
        "timeStamp": "2023-05-19T03:38:58.502Z",
        "value": "SNA"
      },
      "windowRearLeftClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "windowRearRightClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "closureSideBinLeftLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "closureSideBinLeftClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "closureSideBinRightLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "closureSideBinRightClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "closureSideBinLeftNextAction": {
        "timeStamp": "2023-05-19T03:38:58.502Z",
        "value": "SNA"
      },
      "closureSideBinRightNextAction": {
        "timeStamp": "2023-05-19T03:38:58.502Z",
        "value": "SNA"
      },
      "closureTailgateLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "closureTailgateClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "closed"
      },
      "closureTailgateNextAction": {
        "timeStamp": "2023-05-19T03:38:58.502Z",
        "value": "SNA"
      },
      "closureTonneauLocked": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "locked"
      },
      "closureTonneauClosed": {
        "timeStamp": "2023-05-19T03:39:07.506Z",
        "value": "reserved"
      },
      "wiperFluidState": {
        "timeStamp": "2023-05-17T15:04:05.137Z",
        "value": "normal"
      },
      "powerState": {
        "timeStamp": "2023-05-19T05:27:14.532Z",
        "value": "sleep"
      },
      "batteryHvThermalEventPropagation": {
        "timeStamp": "2023-05-19T03:11:19.397Z",
        "value": "nominal"
      },
      "vehicleMileage": {
        "timeStamp": "2023-05-19T01:34:07.521Z",
        "value": 14517537
      },
      "brakeFluidLow": null,
      "gearStatus": {
        "timeStamp": "2023-05-19T05:27:16.011Z",
        "value": "park"
      },
      "tirePressureStatusFrontLeft": {
        "timeStamp": "2023-05-19T03:39:01.306Z",
        "value": "OK"
      },
      "tirePressureStatusValidFrontLeft": {
        "timeStamp": "2023-05-19T03:39:01.306Z",
        "value": "invalid"
      },
      "tirePressureStatusFrontRight": {
        "timeStamp": "2023-05-19T03:39:01.306Z",
        "value": "OK"
      },
      "tirePressureStatusValidFrontRight": {
        "timeStamp": "2023-05-19T03:39:01.306Z",
        "value": "invalid"
      },
      "tirePressureStatusRearLeft": {
        "timeStamp": "2023-05-19T03:39:01.306Z",
        "value": "OK"
      },
      "tirePressureStatusValidRearLeft": {
        "timeStamp": "2023-05-19T03:39:01.306Z",
        "value": "invalid"
      },
      "tirePressureStatusRearRight": {
        "timeStamp": "2023-05-19T03:39:01.306Z",
        "value": "OK"
      },
      "tirePressureStatusValidRearRight": {
        "timeStamp": "2023-05-19T03:39:01.306Z",
        "value": "invalid"
      },
      "batteryLevel": {
        "timeStamp": "2023-05-19T05:09:07.853Z",
        "value": 59.400002
      },
      "chargerState": {
        "timeStamp": "2023-05-19T05:26:14.651Z",
        "value": "charging_ready"
      },
      "batteryLimit": {
        "timeStamp": "2023-05-19T02:13:50.974Z",
        "value": 70
      },
      "remoteChargingAvailable": {
        "timeStamp": "2023-05-19T02:13:50.974Z",
        "value": 0
      },
      "batteryHvThermalEvent": {
        "timeStamp": "2023-05-19T03:11:17.505Z",
        "value": "off"
      },
      "rangeThreshold": {
        "timeStamp": "2023-05-19T05:10:39.844Z",
        "value": "vehicle_range_normal"
      },
      "distanceToEmpty": {
        "timeStamp": "2023-05-19T05:10:39.844Z",
        "value": 307
      },
      "otaAvailableVersionGitHash": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": ""
      },
      "otaAvailableVersionNumber": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 0
      },
      "otaAvailableVersionWeek": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 0
      },
      "otaAvailableVersionYear": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 0
      },
      "otaCurrentVersionGitHash": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": "9804525e"
      },
      "otaCurrentVersionNumber": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 0
      },
      "otaCurrentVersionWeek": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 14
      },
      "otaCurrentVersionYear": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 2023
      },
      "otaDownloadProgress": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 0
      },
      "otaInstallDuration": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 0
      },
      "otaInstallProgress": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 0
      },
      "otaInstallReady": {
        "timeStamp": "2023-05-19T03:11:18.264Z",
        "value": "ota_available"
      },
      "otaInstallTime": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": 0
      },
      "otaInstallType": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": "Convenience"
      },
      "otaStatus": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": "Idle"
      },
      "otaCurrentStatus": {
        "timeStamp": "2023-05-03T05:12:17.214Z",
        "value": "Install_Success"
      },
      "cabinClimateInteriorTemperature": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": 24
      },
      "cabinPreconditioningStatus": {
        "timeStamp": "2023-05-19T03:39:08.206Z",
        "value": "undefined"
      },
      "cabinPreconditioningType": {
        "timeStamp": "2023-05-19T03:39:08.206Z",
        "value": "NONE"
      },
      "petModeStatus": {
        "timeStamp": "2023-05-19T03:11:20.899Z",
        "value": "Off"
      },
      "petModeTemperatureStatus": {
        "timeStamp": "2023-05-19T03:11:20.899Z",
        "value": "Default"
      },
      "cabinClimateDriverTemperature": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": 22
      },
      "gearGuardVideoStatus": {
        "timeStamp": "2023-05-19T01:21:17.963Z",
        "value": "Enabled"
      },
      "gearGuardVideoMode": {
        "timeStamp": "2023-05-19T01:21:17.963Z",
        "value": "Away_From_Home"
      },
      "gearGuardVideoTermsAccepted": {
        "timeStamp": "2023-05-19T01:21:17.963Z",
        "value": "true"
      },
      "defrostDefogStatus": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": "Off"
      },
      "steeringWheelHeat": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": "Off"
      },
      "seatFrontLeftHeat": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": "Off"
      },
      "seatFrontRightHeat": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": "Off"
      },
      "seatRearLeftHeat": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": "Off"
      },
      "seatRearRightHeat": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": "Off"
      },
      "chargerStatus": {
        "timeStamp": "2023-05-17T14:55:05.011Z",
        "value": "chrgr_sts_not_connected"
      },
      "seatFrontLeftVent": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": "Off"
      },
      "seatFrontRightVent": {
        "timeStamp": "2023-05-19T03:39:07.823Z",
        "value": "Off"
      },
      "chargerDerateStatus": null,
      "driveMode": {
        "timeStamp": "2023-05-19T03:12:20.629Z",
        "value": "everyday"
      },
      "serviceMode": {
        "timeStamp": "2023-05-19T03:11:18.355Z",
        "value": "off"
      }
    }
  }
}
```
