---
title: End trip (SendUpdatedTrip)
parent: Commands
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 3
---

# End trip (`SendUpdatedTrip`)

`POST https://rivian.com/api/gql/gateway/graphql`

Clears the vehicle's active trip, the way the app's **End Trip** button does. The app uses the same mutation to push an edited multi-stop trip; the end-trip payload is the degenerate case: an empty plan whose route id is `end_trip_<ms>`.

Session headers only. No phone key or HMAC is involved. `requiresWakeup: true` is fixed in the mutation, but in testing it did **not** wake a sleeping vehicle: Rivian queued the command and delivered it at the next wake.

Found by decompiling Android app 3.17.0 (the app pins certificates, so MITM capture does not work). Verified on an R1T, 2026-10.

## Headers

```text
a-sess: <app session token>
u-sess: <user session token>
csrf-token: <csrf token>
```

## Request

```json
{
  "operationName": "SendUpdatedTrip",
  "variables": {
    "vehicleId": "<your-vehicle-id>",
    "payload": "<base64 Parallax envelope, see below>"
  },
  "query": "mutation SendUpdatedTrip($vehicleId: String!, $payload: String!) { sendParallaxPayload(payload: $payload, meta: { vehicleId: $vehicleId model: \"c2v_navigation.trip_copilot.updated_trip\" isVehicleModelOp: false requiresWakeup: true } ) { success sequenceNumber } }"
}
```

## Payload

Standard base64 (no line wrapping) of this protobuf, field numbers as the app's generated classes declare them:

```protobuf
// Parallax c2v envelope
message Envelope {
  Value value = 10;                   // oneof; the app sets case 10 for trip_copilot
  google.protobuf.Timestamp lastUpdate = 12;
  bytes correlationId = 16;           // 16 random bytes (a UUID)
}
message Value { bytes bytesVal = 2; } // serialized UpdatedTrip

message UpdatedTrip {
  PlanIdentifierMetadata planIdentifierMetadata = 1;
  Preferences preferences = 2;        // present but empty for End Trip
  Publisher publisher = 3;
}
message PlanIdentifierMetadata {
  string abrpRouteId = 1;             // "end_trip_<epoch ms>" for End Trip
  repeated Leg legs = 2;              // empty for End Trip
}
message Leg { string abrpLegId = 1; string googleRouteRequest = 2; Waypoint destination = 3; }
message Waypoint { string name = 1; GeoCoordinate coordinate = 2; string placeId = 3; bool isChargeStop = 4; bool isSystemAdded = 5; }
message GeoCoordinate { double latitude = 1; double longitude = 2; }
message Preferences { float currentArrivalSoCPercentage = 1; float defaultArrivalSoCPercentage = 2; repeated string excludeOptions = 3; repeated string evChargeFilters = 4; }
message Publisher { string userId = 1; }  // currentUser.id
```

The app sets `lastUpdate.seconds = ms / 1000` and `lastUpdate.nanos = ms % 1000000000`. (Signed body commands use `(ms % 1000) * 1000000`; see [Lock and unlock](/app/parallax/commands/body-commands).)

Example End Trip payload for user `user-placeholder` at `1760000000000` ms, decoded:

```text
10: Value { 2: UpdatedTrip { 1: { 1: "end_trip_1760000000000" }, 2: {}, 3: { 1: "user-placeholder" } } }
12: Timestamp { 1: 1760000000, 2: 0 }
16: <16 bytes>
```

A stdlib-only encoder: [home-assistant-rivian `api_ext.py`](https://github.com/ibain/home-assistant-rivian/blob/fork/main/custom_components/rivian/api_ext.py).

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

The trip disappears from the vehicle display and the app within a few seconds.

## Related

A destination sent with [ParseAndShareLocationToVehicle](/app/legacy/controls/share-location) while a trip is open is **added as the first stop**, not replaced. Send End Trip first to replace.
