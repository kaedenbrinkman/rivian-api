---
title: ParseAndShareLocationToVehicle
parent: Vehicle Controls
grand_parent: App API
has_children: false
nav_order: 5
---

# ParseAndShareLocationToVehicle

## Overview

The `ParseAndShareLocationToVehicle` endpoint sends a location to the vehicle.

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
    "str": <url-to-share>,
    "vehicleId": <your-vehicle-id>
  },
  "query": "mutation ParseAndShareLocationToVehicle($str: String!, $vehicleId: String!) { parseAndShareLocationToVehicle(str: $str, vehicleId: $vehicleId) { __typename publishResponse { __typename result } } }"
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
