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
