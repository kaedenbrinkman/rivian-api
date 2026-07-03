---
title: sendParallaxPayload
parent: Commands
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 1
---

# sendParallaxPayload

`POST https://rivian.com/api/gql/gateway/graphql`

Operation name in APK: **`SendRemoteCommand`**.

## When used

Requires remote config **`parallaxCommand`** plus the matching **`PARALLAX_*_COMMAND`** vehicle feature. Otherwise the app uses [sendVehicleCommand](/app/legacy/controls/send-vehicle-command).

## Headers

```text
a-sess: <app session token>
u-sess: <user session token>
csrf-token: <csrf token>
```

## Request

```json
{
  "operationName": "SendRemoteCommand",
  "variables": {
    "vehicleId": "<your-vehicle-id>",
    "model": "<vehicle-model>",
    "parallaxPayloadB64": "<base64-encoded-protobuf>"
  },
  "query": "mutation SendRemoteCommand($vehicleId: String!, $model: String!, $parallaxPayloadB64: String!) { sendParallaxPayload(payload: $parallaxPayloadB64, meta: { vehicleId: $vehicleId model: $model isVehicleModelOp: true requiresWakeup: true } ) { success sequenceNumber } }"
}
```

- **`model`** — model string from the vehicle identity record.
- **`parallaxPayloadB64`** — nested protobuf built by the app (`z70/*` envelopes + domain messages). MITM capture is the practical way to inspect real payloads.

## Response

```json
{
  "data": {
    "sendParallaxPayload": {
      "success": true,
      "sequenceNumber": 42
    }
  }
}
```

Track completion with [`vehicleCommandStatePx`](/app/parallax/commands/command-status).
