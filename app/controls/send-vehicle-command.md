---
title: sendVehicleCommand
parent: Vehicle Controls
grand_parent: App API
has_children: false
nav_order: 3
---

# sendVehicleCommand

## Overview

The `sendVehicleCommand` endpoint is used to send a command to the vehicle. All commands are signed with a HMAC from the phone's private key.

Vehicle commands require an HMAC signature to be sent with the request. The HMAC is calculated from the command name and timestamp as follows:

```python
import hmac
import hashlib
timestamp = int(time.time())
command_name = "UNLOCK_ALL_CLOSURES"
message = f"{command_name}{timestamp}"
key = b"your_secret_key_here"
hmac = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
```

The request also requires the ID of your phone key. This is returned from the [EnrollPhone](/app/controls/enroll-phone) endpoint when you set up your device as a phone key.

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
