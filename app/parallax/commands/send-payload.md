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

- **`model`** — the command's RVM, e.g. `body.locks.unlock`, or a fixed model such as `c2v_navigation.trip_copilot.updated_trip`. For signed commands the same string is inside the payload; the trip copilot message carries no model.
- **`parallaxPayloadB64`** — nested protobuf built by the app (`z70/*` envelopes + domain messages). The app pins certificates, so MITM capture of the phone fails; decompiling the APK (jadx) and reading the generated protobuf-lite descriptors is the practical way. The envelope seen for `c2v_navigation.trip_copilot.updated_trip` is `{ 10: value { 2: bytes }, 12: Timestamp, 16: correlationId (16 random bytes) }`; see [End trip](/app/parallax/commands/end-trip) for a full worked payload.
- Remote commands (lock, unlock, closures) add a signed security block as field 17 of the envelope and put an `Operation` message (RVM, request type, command id, command bytes, vehicle id) in the value; see [Lock and unlock](/app/parallax/commands/body-commands).
- Not every Parallax send is a vehicle-model op: the trip copilot mutation uses `isVehicleModelOp: false` with a fixed `model` and no signature.
- `requiresWakeup: true` is in every send. It wakes a sleeping vehicle for body commands; for the trip copilot message it did not, and the command was delivered at the next wake.

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
