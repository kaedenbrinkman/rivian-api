---
title: sendVehicleCommand
parent: Vehicle Controls
has_children: false
nav_order: 3
---

# sendVehicleCommand

## Overview

The `sendVehicleCommand` endpoint is used to send a command to the vehicle. All commands are signed with a HMAC from the phone's private key.

Vehicle commands require an HMAC signature to be sent with the request. The HMAC is generated using the command name and the current timestamp, using a shared key generated from the phone's private key and the vehicle's public key. The vehicle's public key is available in the `vehiclePublicKey` field of the `getUserInfo` endpoint.

## List of Commands

```
WAKE_VEHICLE
OPEN_FRUNK
CLOSE_FRUNK
OPEN_ALL_WINDOWS
CLOSE_ALL_WINDOWS
UNLOCK_ALL_CLOSURES
LOCK_ALL_CLOSURES
ENABLE_GEAR_GUARD_VIDEO
DISABLE_GEAR_GUARD_VIDEO
HONK_AND_FLASH_LIGHTS
OPEN_TONNEAU_COVER
CLOSE_TONNEAU_COVER
```

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
  "operationName": "sendVehicleCommand",
  "variables": {
    "attrs": {
      "command": "UNLOCK_ALL_CLOSURES",
      "hmac": <your-hmac>,
      "timestamp": <command-timestamp>,
      "vasPhoneId": <your-phone-id>,
      "deviceId": <your-device-id>,
      "vehicleId": <your-vehicle-id>
    }
  },
  "query": "mutation sendVehicleCommand($attrs: VehicleCommandAttributes!) { sendVehicleCommand(attrs: $attrs) { __typename id command state } }"
}
```

### Example Response

```json
{
  "data": {
    "sendVehicleCommand": {
      "__typename": "SendVehicleCommandState",
      "id": <some-command-id>,
      "command": "UNLOCK_ALL_CLOSURES",
      "state": 1
    }
  }
}
```
