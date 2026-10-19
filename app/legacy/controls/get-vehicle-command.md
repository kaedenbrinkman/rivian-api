---
title: getVehicleCommand
parent: Controls
grand_parent: Legacy
great_grand_parent: App API
has_children: false
---

# getVehicleCommand

## Overview

The `getVehicleCommand` endpoint returns the status of a command sent via legacy [`sendVehicleCommand`](/app/legacy/controls/send-vehicle-command) (HMAC / phone-key path).

For Parallax commands (`sendParallaxPayload`), the app subscribes to [`vehicleCommandStatePx`](/app/parallax/commands/command-status) on the WebSocket endpoint instead. When `state` is 0 in the legacy query, the command has completed.

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
  "operationName": "getVehicleCommand",
  "variables": {
    "id": <command-id>
  },
  "query": "query getVehicleCommand($id: String!) { getVehicleCommand(id: $id) { __typename id command createdAt state responseCode statusCode } }"
}
```

### Example Response

```json
{
  "data": {
    "getVehicleCommand": {
      "__typename": "GetVehicleCommandState",
      "id": <command-id>,
      "command": "UNLOCK_ALL_CLOSURES",
      "createdAt": "2023-01-15T12:05:00.000Z",
      "state": 3,
      "responseCode": null,
      "statusCode": null
    }
  }
}
```

## States

`state` is an integer. The same values come back from the `vehicleCommandState` subscription and from `sendVehicleCommand`'s own response. From the Android app (3.17.0):

| `state` | Name in the app | Final? |
| --- | --- | --- |
| 0 | COMPLETE | yes |
| 1 | QUEUED | no |
| 2 | SYNC | no |
| 3 | PROCESSING | no |
| 4 | FAILED_TO_EXECUTE | yes |
| 5 | WAKE (the app shows "Waking vehicle") | no |
| 6 | FAILED_CONNECTIVITY | yes |
| 7 | FAILED_VIN_MAPPING_TO_VEHICLE | yes |
| other | unknown | yes |

Verified: a `WAKE_VEHICLE` sent to an R1T that never answered (a suspected cell dead spot) later read `state: 6`. The rest is from the decompile.

The app stops following a command at the first final state. It does not follow `WAKE_VEHICLE` at all: that subscription is cancelled after its first event.

## Response codes

For `COMPLETE`, the app reads `responseCode` to decide whether the vehicle did the command. From the decompile, not tested:

| `responseCode` | Meaning |
| --- | --- |
| `null` or `928` | success |
| `929` | failed |
| other | success only if the app maps the code to a success for that command (for example `258` is the `UNLOCK_ALL_CLOSURES` success); unmapped codes count as failures |
| `1031` | invalid HMAC |
| `1042` | invalid timestamp |
| `1045` | `vasPhoneId` not paired over Bluetooth |
| `1047` | public key missing |
| `22` | close command received, not done: actuation disabled |

## How long the app waits

The app waits 60 s for a command to finish (90 s for vehicles with the `HMAC_TIMEOUT_90S` feature, 120 s if the vehicle was asleep when it was sent). On a timeout it reports the failure and does **not** resend the command.
