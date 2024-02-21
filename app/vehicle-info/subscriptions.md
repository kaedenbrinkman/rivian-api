---
title: Subscriptions
parent: Vehicle Info Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# Subscriptions

## Overview

The Rivian mobile app uses websockets to communicate real-time data about the vehicle.

`WEBSOCKET wss://api.rivian.com/gql-consumer-subscriptions/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
```

### Connection Initialization
Send:
```json
{
  "type": "connection_init",
  "payload": {
    "dc-cid": <device-corelation-id>,
    "u-sess": <u-sess>,
    "client-name": "com.rivian.android.consumer",
    "client-version": "2.6.1-2065"
  }
}
```
Receive:
```json
{
  "type": "connection_ack"
}
```

### Subscribe to Tire Pressure State
Send:
```json
{
  "type": "subscribe",
  "id": <subscription-id>,
  "payload": {
    "operationName": "tirePressureState",
    "variables": {
      "vehicleID": <vehicle-id>
    },
    "query": "subscription tirePressureState($vehicleID: String!) { vehicleState(id: $vehicleID) { tirePressureStatusFrontLeft { timeStamp value } tirePressureStatusFrontRight { timeStamp value } tirePressureStatusRearLeft { timeStamp value } tirePressureStatusRearRight { timeStamp value } tirePressureFrontLeft { timeStamp value } tirePressureFrontRight { timeStamp value } tirePressureRearLeft { timeStamp value } tirePressureRearRight { timeStamp value } } }"
  }
}
```

### Subscribe to Vehicle Departure Schedules
Send:
```json
{
  "type": "subscribe",
  "id": <subscription-id>,
  "payload": {
    "operationName": "vehicleDepartureSchedules",
    "variables": {
      "vehicleId": <vehicle-id>
    },
    "query": "subscription vehicleDepartureSchedules($vehicleId: String!) { vehicleDepartureSchedules(vehicleId: $vehicleId) { id name isEnabled occurrence { __typename ... on RepeatsWeekly { days startsAtMin skippedOn } } departureSettings { __typename ... on DepartureSettings { shouldOverrideChargeSchedule comfortSettings { __typename ... on ComfortSettings { surfaceHeatVentLevels { __typename ... on SurfaceHeatVentLevels { frontLeftSeat frontRightSeat rearLeftSeat rearRightSeat steeringWheel } } cabinTempCelsius frontDefogDefrost } } } } } }"
  }
}
```

### Subscribe to Vehicle Cloud Connection
Send:
```json
{
  "type": "subscribe",
  "id": <subscription-id>,
  "payload": {
    "operationName": "vehicleCloudConnection",
    "variables": {
      "vehicleID": <vehicle-id>
    },
    "query": "subscription vehicleCloudConnection($vehicleID: String!) { vehicleCloudConnection(id: $vehicleID) { isOnline lastSync } }"
  }
}
```

### Subscribe to Vehicle State
Send:
```json
{
  "type": "subscribe",
  "id": <subscription-id>,
  "payload": {
    "operationName": "vehicleState",
    "variables": {
      "vehicleID": <vehicle-id>
    },
    "query": "subscription vehicleState($vehicleID: String!) { vehicleState(id: $vehicleID) { __typename ...vehicleStateFields } }  fragment vehicleStateFields on VehicleState { gnssLocation { latitude longitude timeStamp isAuthorized } gnssSpeed { timeStamp value } gnssAltitude { timeStamp value } gnssError { timeStamp positionVertical positionHorizontal speed bearing } alarmSoundStatus { timeStamp value } timeToEndOfCharge { timeStamp value } doorFrontLeftLocked { timeStamp value } doorFrontLeftClosed { timeStamp value } doorFrontRightLocked { timeStamp value } doorFrontRightClosed { timeStamp value } doorRearLeftLocked { timeStamp value } doorRearLeftClosed { timeStamp value } doorRearRightLocked { timeStamp value } doorRearRightClosed { timeStamp value } windowFrontLeftClosed { timeStamp value } windowFrontRightClosed { timeStamp value } windowFrontLeftCalibrated { timeStamp value } windowFrontRightCalibrated { timeStamp value } windowRearLeftCalibrated { timeStamp value } windowRearRightCalibrated { timeStamp value } windowsNextAction { timeStamp value } closureFrunkLocked { timeStamp value } closureFrunkClosed { timeStamp value } closureFrunkNextAction { timeStamp value } gearGuardLocked { timeStamp value } closureLiftgateLocked { timeStamp value } closureLiftgateClosed { timeStamp value } closureLiftgateNextAction { timeStamp value } windowRearLeftClosed { timeStamp value } windowRearRightClosed { timeStamp value } closureSideBinLeftLocked { timeStamp value } closureSideBinLeftClosed { timeStamp value } closureSideBinRightLocked { timeStamp value } closureSideBinRightClosed { timeStamp value } closureSideBinLeftNextAction { timeStamp value } closureSideBinRightNextAction { timeStamp value } closureTailgateLocked { timeStamp value } closureTailgateClosed { timeStamp value } closureTailgateNextAction { timeStamp value } closureTonneauLocked { timeStamp value } closureTonneauClosed { timeStamp value } wiperFluidState { timeStamp value } powerState { timeStamp value } batteryHvThermalEventPropagation { timeStamp value } twelveVoltBatteryHealth { timeStamp value } vehicleMileage { timeStamp value } brakeFluidLow { timeStamp value } gearStatus { timeStamp value } batteryLevel { timeStamp value } chargerState { timeStamp value } batteryLimit { timeStamp value } remoteChargingAvailable { timeStamp value } batteryHvThermalEvent { timeStamp value } rangeThreshold { timeStamp value } distanceToEmpty { timeStamp value } otaAvailableVersionGitHash { timeStamp value } otaAvailableVersion { timeStamp value } otaCurrentVersionGitHash { timeStamp value } otaCurrentVersion { timeStamp value } otaDownloadProgress { timeStamp value } otaInstallDuration { timeStamp value } otaInstallProgress { timeStamp value } otaInstallReady { timeStamp value } otaInstallTime { timeStamp value } otaInstallType { timeStamp value } otaStatus { timeStamp value } otaCurrentStatus { timeStamp value } cabinClimateInteriorTemperature { timeStamp value } cabinPreconditioningStatus { timeStamp value } cabinPreconditioningType { timeStamp value } petModeStatus { timeStamp value } petModeTemperatureStatus { timeStamp value } cabinClimateDriverTemperature { timeStamp value } gearGuardVideoStatus { timeStamp value } gearGuardVideoMode { timeStamp value } gearGuardVideoTermsAccepted { timeStamp value } defrostDefogStatus { timeStamp value } steeringWheelHeat { timeStamp value } seatFrontLeftHeat { timeStamp value } seatFrontRightHeat { timeStamp value } seatRearLeftHeat { timeStamp value } seatRearRightHeat { timeStamp value } chargerStatus { timeStamp value } seatFrontLeftVent { timeStamp value } seatFrontRightVent { timeStamp value } chargerDerateStatus { timeStamp value } driveMode { timeStamp value } serviceMode { timeStamp value } trailerStatus { timeStamp value } btmFfHardwareFailureStatus { timeStamp value } btmIcHardwareFailureStatus { timeStamp value } btmLfdHardwareFailureStatus { timeStamp value } btmRfHardwareFailureStatus { timeStamp value } btmRfdHardwareFailureStatus { timeStamp value } carWashMode { timeStamp value } chargePortState { timeStamp value } chargingTimeEstimationValidity { timeStamp value } limitedAccelCold { timeStamp value } limitedRegenCold { timeStamp value } rearHitchStatus { timeStamp value } }"
  }
}
```

Once subscriptions are established, the server will send updates to the client as the vehicle state changes.

### Receiving Data
Receive:
```json
{
  "id": <subscription-id>,
  "type": "next",
  "payload": {
    "data": {
      "vehicleState": {
        "tirePressureStatusFrontLeft": {
          "timeStamp": "2024-02-18T16:10:29.653Z",
          "value": "unknown"
        },
        "tirePressureStatusFrontRight": {
          "timeStamp": "2024-02-18T16:10:29.653Z",
          "value": "unknown"
        },
        "tirePressureStatusRearLeft": {
          "timeStamp": "2024-02-18T16:10:29.653Z",
          "value": "unknown"
        },
        "tirePressureStatusRearRight": {
          "timeStamp": "2024-02-18T16:10:29.653Z",
          "value": "unknown"
        },
        "tirePressureFrontLeft": {
          "timeStamp": "2024-02-18T16:10:29.653Z",
          "value": null
        },
        "tirePressureFrontRight": {
          "timeStamp": "2024-02-18T16:10:29.653Z",
          "value": null
        },
        "tirePressureRearLeft": {
          "timeStamp": "2024-02-18T16:10:29.653Z",
          "value": null
        },
        "tirePressureRearRight": {
          "timeStamp": "2024-02-18T16:10:29.653Z",
          "value": null
        }
      }
    }
  }
}
```

Receive:
```json
{
  "id": <subscription-id>,
  "type": "next",
  "payload": {
    "data": {
      "vehicleState": {
        "__typename": "VehicleState",
        "gnssLocation": null,
        "gnssSpeed": null,
        "gnssAltitude": null,
        "gnssError": null,
        "alarmSoundStatus": null,
        "timeToEndOfCharge": null,
        "doorFrontLeftLocked": null,
        "doorFrontLeftClosed": null,
        "doorFrontRightLocked": null,
        "doorFrontRightClosed": null,
        "doorRearLeftLocked": null,
        "doorRearLeftClosed": null,
        "doorRearRightLocked": null,
        "doorRearRightClosed": null,
        "windowFrontLeftClosed": null,
        "windowFrontRightClosed": null,
        "windowFrontLeftCalibrated": null,
        "windowFrontRightCalibrated": null,
        "windowRearLeftCalibrated": null,
        "windowRearRightCalibrated": null,
        "windowsNextAction": null,
        "closureFrunkLocked": null,
        "closureFrunkClosed": null,
        "closureFrunkNextAction": null,
        "gearGuardLocked": null,
        "closureLiftgateLocked": null,
        "closureLiftgateClosed": null,
        "closureLiftgateNextAction": null,
        "windowRearLeftClosed": null,
        "windowRearRightClosed": null,
        "closureSideBinLeftLocked": null,
        "closureSideBinLeftClosed": null,
        "closureSideBinRightLocked": null,
        "closureSideBinRightClosed": null,
        "closureSideBinLeftNextAction": null,
        "closureSideBinRightNextAction": null,
        "closureTailgateLocked": null,
        "closureTailgateClosed": null,
        "closureTailgateNextAction": null,
        "closureTonneauLocked": null,
        "closureTonneauClosed": null,
        "wiperFluidState": null,
        "powerState": null,
        "batteryHvThermalEventPropagation": null,
        "twelveVoltBatteryHealth": null,
        "vehicleMileage": null,
        "brakeFluidLow": null,
        "gearStatus": null,
        "batteryLevel": null,
        "chargerState": null,
        "batteryLimit": null,
        "remoteChargingAvailable": null,
        "batteryHvThermalEvent": null,
        "rangeThreshold": null,
        "distanceToEmpty": null,
        "otaAvailableVersionGitHash": null,
        "otaAvailableVersion": null,
        "otaCurrentVersionGitHash": null,
        "otaCurrentVersion": null,
        "otaDownloadProgress": null,
        "otaInstallDuration": null,
        "otaInstallProgress": null,
        "otaInstallReady": null,
        "otaInstallTime": null,
        "otaInstallType": null,
        "otaStatus": null,
        "otaCurrentStatus": null,
        "cabinClimateInteriorTemperature": null,
        "cabinPreconditioningStatus": null,
        "cabinPreconditioningType": null,
        "petModeStatus": null,
        "petModeTemperatureStatus": null,
        "cabinClimateDriverTemperature": null,
        "gearGuardVideoStatus": null,
        "gearGuardVideoMode": null,
        "gearGuardVideoTermsAccepted": null,
        "defrostDefogStatus": null,
        "steeringWheelHeat": null,
        "seatFrontLeftHeat": null,
        "seatFrontRightHeat": null,
        "seatRearLeftHeat": null,
        "seatRearRightHeat": null,
        "chargerStatus": null,
        "seatFrontLeftVent": null,
        "seatFrontRightVent": null,
        "chargerDerateStatus": null,
        "driveMode": null,
        "serviceMode": null,
        "trailerStatus": null,
        "btmFfHardwareFailureStatus": {
          "timeStamp": "2024-02-21T19:40:22.725Z",
          "value": "dtc_not_set"
        },
        "btmIcHardwareFailureStatus": null,
        "btmLfdHardwareFailureStatus": null,
        "btmRfHardwareFailureStatus": null,
        "btmRfdHardwareFailureStatus": {
          "timeStamp": "2024-02-21T19:40:24.420Z",
          "value": "dtc_not_set"
        },
        "carWashMode": null,
        "chargePortState": null,
        "chargingTimeEstimationValidity": null,
        "limitedAccelCold": null,
        "limitedRegenCold": null,
        "rearHitchStatus": null
      }
    }
  }
}
```

### Close a Subscription
Send:
```json
{
  "type": "complete",
  "id": <subscription-id>
}
```
