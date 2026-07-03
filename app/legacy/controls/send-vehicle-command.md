---
title: sendVehicleCommand
parent: Controls
grand_parent: Legacy
great_grand_parent: App API
has_children: false
---

# sendVehicleCommand

## Overview

The `sendVehicleCommand` endpoint sends a **legacy** remote command to the vehicle. Commands are signed with an HMAC from the phone's private key.

Many commands go through [Parallax `sendParallaxPayload`](/app/parallax/commands/send-payload) instead when remote config flag `parallaxCommand` and the matching vehicle Parallax command feature are enabled (body, comfort, security, energy, OTA). The app still ships this mutation and uses it as a fallback when Parallax is unavailable.

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

The request also requires the ID of your phone key. This is returned from the [EnrollPhone](/app/legacy/controls/enroll-phone) endpoint when you set up your device as a phone key.

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

## Parallax command path

When Parallax commands are active, prefer:

- Mutation: [`sendParallaxPayload`](/app/parallax/commands/send-payload) with a base64 protobuf payload
- Status subscription: [`vehicleCommandStatePx`](/app/parallax/commands/command-status)

Legacy [`getVehicleCommand`](/app/legacy/controls/get-vehicle-command) applies to the HMAC path above.
