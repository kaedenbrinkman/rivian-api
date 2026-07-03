---
title: Subscription
parent: Parallax
grand_parent: App API
has_children: false
nav_order: 1
---

# ParallaxMessages subscription

The primary Parallax read path. The app opens one `ParallaxMessages` subscription per vehicle and passes a list of RVM topic strings.

`wss://api.rivian.com/gql-consumer-subscriptions/graphql`

Protocol: **GraphQL over WebSocket** (`graphql-transport-ws`).

## Wire format

Each `next` frame:

```json
{
  "rvm": "energy.high_voltage.battery_state",
  "payload": "<base64 protobuf>",
  "timestamp": 1700000000000
}
```

## Headers

```text
a-sess: <app session token>
u-sess: <user session token>
csrf-token: <csrf token>
apollographql-client-name: com.rivian.android.consumer
```

## Connection flow

1. WebSocket connect with headers above.
2. Send `{"type":"connection_init"}` → wait for `connection_ack`.
3. Send `subscribe` (below).
4. Read `next` frames; optionally send `complete`.

GraphQL variable: **`vehicleId`** (not `vehicleID`).

## Subscribe message

```json
{
  "type": "subscribe",
  "id": "<uuid>",
  "payload": {
    "operationName": "ParallaxMessages",
    "variables": {
      "vehicleId": "<your-vehicle-id>",
      "rvms": ["energy.high_voltage.battery_state", "body.locks.states"]
    },
    "query": "subscription ParallaxMessages($vehicleId: String!, $rvms: [String!]) { parallaxMessages(vehicleId: $vehicleId, rvms: $rvms) { payload timestamp rvm } }"
  }
}
```

## Example response

```json
{
  "id": "<uuid>",
  "type": "next",
  "payload": {
    "data": {
      "parallaxMessages": {
        "payload": "CkIKBAAAADMzT0ARAAAAQOESYEASDw00MytCFWdmOkIdzcwUQhoAIAEwCQ==",
        "timestamp": 1700000000000,
        "rvm": "energy.high_voltage.battery_state"
      }
    }
  }
}
```

Empty `payload` (`""`) is valid — keepalive or cleared state.

## How the app picks RVMs

From enum `cm/c`:

1. **Always** — `subscriptionScope = App` and `isVehicleState = false` ([domain list](/app/parallax/domains)).
2. **+ `PARALLAX_VEHICLE_STATE`** — RVMs with `isVehicleState = true` (locks, gear, range, session status, …).
3. **+ tire feature** — `dynamics.tires.state` (`subscriptionScope = Feature`).

You may subscribe to any subset; the app uses the union for enabled features.

## Example script

[`examples/parallax-subscribe.py`](../../examples/parallax-subscribe.py) — prints `{ rvm, timestamp, payload_b64 }` as JSON lines.

## See also

- [Domains](/app/parallax/domains) — all RVMs by area
- [Decoding](/app/parallax/decoding) — protobuf notes
- [Legacy WebSocket subscriptions](/app/legacy/websocket-subscriptions) — non-Parallax subs on the same URL
