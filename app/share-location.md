---
title: ParseAndShareLocationToVehicle
parent: App API
has_children: false
nav_order: 3
---

# ParseAndShareLocationToVehicle

## Overview

The `ParseAndShareLocationToVehicle` endpoint sends a location to the vehicle.

`POST https://rivian.com/api/gql/gateway/graphql`

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
