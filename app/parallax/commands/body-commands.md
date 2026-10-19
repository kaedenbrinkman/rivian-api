---
title: Lock and unlock (body commands)
parent: Commands
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 4
---

# Lock and unlock (body commands)

`POST https://rivian.com/api/gql/gateway/graphql`

The Parallax way to lock and unlock the vehicle, and to open and close closures. It is the [`sendParallaxPayload`](/app/parallax/commands/send-payload) mutation with `isVehicleModelOp: true`, carrying a **signed** protobuf operation. Progress and the result come back on [`vehicleCommandStatePx`](/app/parallax/commands/command-status).

Compared with the legacy [`sendVehicleCommand`](/app/legacy/controls/send-vehicle-command):

- The HMAC is the same kind (same phone key, same derived secret) but travels **inside the protobuf**, and it signs the serialized operation, not `command + timestamp`.
- `requiresWakeup: true` is fixed in the mutation. A sleeping vehicle is woken by the request itself. The app sends **no** `WAKE_VEHICLE` first.
- The command id is chosen by the client (a UUID inside the payload), so you can subscribe to its status before sending it.

Found by decompiling Android app 3.17.0 (the app pins certificates, so MITM capture does not work). Lock and unlock verified on an R1T, 2026-10, from a Home Assistant integration (see below). The closure commands are from the decompile only.

## When the app uses it

The app picks this path when both are true, and otherwise falls back to [`sendVehicleCommand`](/app/legacy/controls/send-vehicle-command):

- remote config flag `parallaxCommand` is on
- the vehicle lists the **`PVS_BD_CMD`** feature (`PARALLAX_BODY_COMMAND`) as `AVAILABLE` in `supportedFeatures`

Other domains use other features (`PVS_COMF_CMD`, `PVS_SEC_CMD`, `PVS_ENRG_CMD`, `PVS_OTA_CMD`).

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
    "model": "body.locks.unlock",
    "parallaxPayloadB64": "<base64 envelope, see below>"
  },
  "query": "mutation SendRemoteCommand($vehicleId: String!, $model: String!, $parallaxPayloadB64: String!) { sendParallaxPayload(payload: $parallaxPayloadB64, meta: { vehicleId: $vehicleId model: $model isVehicleModelOp: true requiresWakeup: true } ) { success sequenceNumber } }"
}
```

`model` is the command's RVM:

| `model` | Command message (operation field 4) |
| --- | --- |
| `body.locks.unlock` | `{ 1: all = true }` (the app always sets `all`; field 2 is `userPreference`) |
| `body.locks.lock` | empty |
| `body.closures.open` | `{ 1: repeated closure }`: open frunk, open liftgate, unlatch tailgate, release left/right side bin, open charge port, open all windows |
| `body.closures.close` | `{ 1: repeated closure }`: close frunk, close liftgate, close charge port, close all windows |

Closure enum, from the app: `FRUNK` 5, `TAILGATE` 6, `LIFTGATE` 7, `SIDE_BIN_LEFT` 8, `SIDE_BIN_RIGHT` 9, `CHARGE_PORT` 10, `TONNEAU` 11, `WINDOW_FRONT_LEFT` 12, `WINDOW_FRONT_RIGHT` 13, `WINDOW_BACK_LEFT` 14, `WINDOW_BACK_RIGHT` 15, `WINDOW_REAR` 16, `GROUP_WINDOWS` 10000. Each command sends exactly one closure:

| Command | Closure sent |
| --- | --- |
| open / close frunk | `FRUNK` |
| open / close liftgate | `LIFTGATE` |
| unlatch tailgate | `TAILGATE` |
| open liftgate and unlatch tailgate | `TAILGATE` on an R1T, otherwise `LIFTGATE` |
| release left / right side bin | `SIDE_BIN_LEFT` / `SIDE_BIN_RIGHT` |
| open / close charge port | `CHARGE_PORT` |
| open / close all windows | `GROUP_WINDOWS` | The tonneau cover has no Parallax command in the app (it stays on the legacy command). `WAKE_VEHICLE` is also legacy only.

## Payload

Standard base64 of the envelope below, field numbers as the app's generated classes declare them. It is the same envelope as [End trip](/app/parallax/commands/end-trip), with the operation as the value and a security block added.

```protobuf
message Envelope {
  Value value = 10;                    // oneof
  google.protobuf.Timestamp lastUpdate = 12;
  bytes correlationId = 16;            // the command id: 16 bytes of a UUID
  SecurityInfo securityInfo = 17;
}
message Value { bytes bytesVal = 2; }  // the serialized Operation

message Operation {
  string model = 1;                    // the RVM, same as the mutation's `model`
  OperationType operation = 2;         // enum; 3 = PARALLAX_OPERATION_REQUEST
  bytes uuid = 3;                      // the same 16 bytes as correlationId
  bytes bytesVal = 4;                  // the serialized command message; omitted when empty
  google.protobuf.Timestamp createdAt = 5;
  // 6 (scope) is never set by the app
  string vehicleId = 7;
}

message SecurityInfo {
  Signature signature = 1;
  string mappedIdentity = 2;           // your phone's identityId for this vehicle
}
message Signature {
  SignatureType type = 1;              // enum; 1 = HMAC-SHA256
  bytes bytes = 2;                     // 32 raw bytes (not hex)
}
```

Both timestamps are `seconds = ms / 1000`, `nanos = (ms % 1000) * 1000000`.

The app encodes the payload with Android's default Base64 flags, which wrap lines (End trip uses no wrapping). The server accepted unwrapped Base64 in testing.

Example unlock for `1760000000123` ms, decoded:

```text
10: Value { 2: Operation {
      1: "body.locks.unlock"
      2: 3
      3: <16 bytes, the command id>
      4: { 1: true }
      5: Timestamp { 1: 1760000000, 2: 123000000 }
      7: "<your-vehicle-id>" } }
12: Timestamp { 1: 1760000000, 2: 123000000 }
16: <the same 16 bytes>
17: SecurityInfo { 1: { 1: 1, 2: <32 bytes> }, 2: "<your-identity-id>" }
```

### Signature

```text
secret    = HKDF-SHA256(ECDH(phone private key, vehicle public key), salt = none, info = empty, 32 bytes)
signature = HMAC-SHA256(secret, serialized Operation)
```

- The secret is the one the legacy HMAC uses; the vehicle public key is `vas.vehiclePublicKey` from the user's vehicles. See [EnrollPhone](/app/legacy/controls/enroll-phone).
- The data signed is exactly the bytes placed in `Value.bytesVal`, so build the operation once and sign those bytes.
- `mappedIdentity` is `enrolledPhones[].enrolled[].identityId` for the enrolled phone (matched on its public key) and this vehicle. This is the value legacy commands send as `deviceId`.
- There is no nonce, `vasPhoneId` or `deviceId` in the payload or variables. The only values that change per command are the two timestamps and the command UUID; whether the server enforces freshness was not tested.
- If the app cannot sign, it sends the literal bytes `InvalidHMac` and still submits; on this path it does not fall back to the legacy command. Whether the server rejects a bad signature was **not** tested.

A stdlib-only encoder with tests (built from this page): [home-assistant-rivian `parallax_command.py`](https://github.com/ibain/home-assistant-rivian/blob/1.5.18b1/custom_components/rivian/parallax_command.py).

## Response

```json
{
  "data": {
    "sendParallaxPayload": {
      "success": true,
      "sequenceNumber": 0
    }
  }
}
```

`success` only means Rivian accepted the command for delivery. The app ignores `sequenceNumber`, and subscribes to [`vehicleCommandStatePx`](/app/parallax/commands/command-status) only after `success: true`, using the UUID from the payload as `commandId`. Because you choose the UUID, you can subscribe first and miss no early progress, as the Home Assistant integration does.

## Observed

R1T, October 2026, one command each, from Home Assistant with debug logging:

| Case | Sequence |
| --- | --- |
| Unlock, vehicle **asleep** | sent 0 s, `waking up` 1.5 s, `waking up` again 15 s, vehicle awake 21 s, `executing` 22 s, `complete` with status success 26 s, locks report unlocked 26 s |
| Lock, vehicle awake | sent 0 s, `executing` 10.3 s, `complete` with status success 10.6 s, locks report locked 10.6 s |

So in this one test a body command woke a sleeping vehicle (it had been asleep for about two minutes). The same `requiresWakeup: true` on the trip copilot message did **not**; that command was queued and delivered at the next wake (see [End trip](/app/parallax/commands/end-trip)).

## What the app does not do

- It does not send `WAKE_VEHICLE` before a command. `WAKE_VEHICLE` is sent only by the "vehicle is sleeping" sheet's Wake button, and when scheduling a software update (only if the vehicle is asleep).
- It does not resend a cloud command that times out; it reports the failure.
- With a phone connected over Bluetooth it tries Bluetooth first, then falls back to the cloud, which is a second attempt. The Bluetooth wait is 3 s for most commands (15 s for frunk, windows and tonneau). On vehicles with `PVS_OVER_BLE`, lock and unlock go through a Bluetooth data tunnel with a much longer overall timeout.

## Not tested

- A bad or missing signature, a wrong `mappedIdentity`, or a stale timestamp.
- Closure commands (`body.closures.*`).
- Failure paths: a vehicle without cell coverage, a command refused by the vehicle.
- What the server does if `PVS_BD_CMD` is missing.
