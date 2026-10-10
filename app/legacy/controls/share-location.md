---
title: ParseAndShareLocationToVehicle
parent: Controls
grand_parent: Legacy
great_grand_parent: App API
has_children: false
---

# ParseAndShareLocationToVehicle

## Overview

The `ParseAndShareLocationToVehicle` endpoint sends a destination to the vehicle. It opens in Trip Details on the center display. Session headers only; no phone key.

`str` is run through a server-side place search, so it accepts more than a URL: a place name (`Costco Goleta`), a business name with its address, a street address, a Google Maps share link (`https://maps.app.goo.gl/...`), or `lat,lng`. Observed on an R1T (2026-10): all of those resolve; a person's name in front of an address resolves to the wrong business, and a hand-built Google search URL (`/maps/search/?api=1&query=...`) is searched as text. `lat,lng` lands on the right spot but is named after the nearest business.

App 3.17.0 adds an optional `requiresWakeup` argument.

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
  "operationName": "ParseAndShareLocationToVehicle",
  "variables": {
    "str": <place-name-address-or-share-link>,
    "vehicleId": <your-vehicle-id>,
    "requiresWakeup": true
  },
  "query": "mutation ParseAndShareLocationToVehicle($str: String!, $vehicleId: String!, $requiresWakeup: Boolean) { parseAndShareLocationToVehicle(str: $str, vehicleId: $vehicleId, requiresWakeup: $requiresWakeup) { __typename publishResponse { __typename result } } }"
}
```

### Example Response

```json
{
  "data": {
    "parseAndShareLocationToVehicle": {
      "__typename": "ParseAndShareLocationToVehicleResponse",
      "publishResponse": {
        "__typename": "PublishResponse",
        "result": 0
      }
    }
  }
}
```

`result: 0` means the request was accepted, not that the place was found; it is `0` for the misses above too.

If a trip is already open on the vehicle, the new destination is added as the **first stop**. To replace it, send [End trip](/app/parallax/commands/end-trip) first.
