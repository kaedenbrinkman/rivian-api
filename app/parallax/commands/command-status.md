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

`commandId` is assigned when the app issues `sendParallaxPayload`.

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

Legacy alternative: [`vehicleCommandState`](/app/legacy/websocket-subscriptions) / [`getVehicleCommand`](/app/legacy/controls/get-vehicle-command).
