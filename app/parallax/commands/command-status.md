---
title: Command status
parent: Commands
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 2
---

# vehicleCommandStatePx

WebSocket subscription for Parallax command completion. Returns a base64 protobuf **`payload`**, not legacy JSON command fields.

Same URL and headers as [ParallaxMessages](/app/parallax/subscription).

## Subscribe

```json
{
  "type": "subscribe",
  "id": "<uuid>",
  "payload": {
    "operationName": "vehicleCommandStatePx",
    "variables": {
      "vehicleId": "<your-vehicle-id>",
      "commandId": "<command-id>"
    },
    "query": "subscription vehicleCommandStatePx($vehicleId: String!, $commandId: String!) { vehicleCommandStatePx(vehicleId: $vehicleId, commandId: $commandId) { payload } }"
  }
}
```

`commandId` is the command's UUID as a string: the 16 bytes the client puts in the payload (envelope field 16 and operation field 3). The client chooses it, so you can subscribe **before** sending and miss no early progress (the app itself subscribes after the send is accepted).

## Response

```json
{
  "type": "next",
  "payload": {
    "data": {
      "vehicleCommandStatePx": {
        "payload": "<base64 protobuf>"
      }
    }
  }
}
```

## Payload

Standard base64 of this protobuf, field numbers as the app's generated classes declare them:

```protobuf
message CommandState {
  bytes refUuid = 1;                 // the command id
  string refModel = 2;               // e.g. "body.locks.unlock"
  Progress progress = 3;
  oneof result {
    OperationError operationError = 4;
    bytes data = 5;                  // a serialized CommandResult
  }
}
enum Progress { UNSPECIFIED = 0; VEHICLE_WAKING_UP = 1; VALIDATING = 2; EXECUTING = 3; COMPLETE = 4; }

message CommandResult { Status responseStatus = 1; Error error = 2; }
enum Status { UNDEFINED = 0; SUCCESS = 1; FAIL = 2; INVALID_REQUEST = 3; NOT_SUPPORTED = 4; TIMEOUT = 5; }
message Error { int32 code = 1; string message = 2; }
message OperationError { int32 error = 1; string message = 2; } // field 1 is an enum the app never reads; values not decompiled
```

- Progress 1 to 3 are intermediate; `COMPLETE` is the last message. `VEHICLE_WAKING_UP` can repeat.
- Success is `COMPLETE` with `data.responseStatus == SUCCESS`. A failure is `COMPLETE` with another status or an `operationError`; there is no separate failed progress value.
- The app only tells `SUCCESS` apart from every other status. It also counts a result as failed, even with status `SUCCESS`, when `error.code` is one of: invalid HMAC (1031), invalid timestamp (1042), phone id not paired over Bluetooth (1045), phone id not on the whitelist, public key missing (1047), remote command streaming unavailable, or the Gear Guard active limit reached. I found no fallback to the legacy command on any status.

Observed for an unlock sent to a sleeping R1T: `VEHICLE_WAKING_UP` twice, then `EXECUTING`, then `COMPLETE` with `SUCCESS`, 26 s after the send. See [Lock and unlock](/app/parallax/commands/body-commands#observed).

Legacy alternative: [`vehicleCommandState`](/app/legacy/websocket-subscriptions) / [`getVehicleCommand`](/app/legacy/controls/get-vehicle-command).
