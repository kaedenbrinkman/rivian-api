---
title: GetVehicleLastConnection
parent: App API
has_children: false
nav_order: 3
---

# GetVehicleLastConnection

## Overview

The `GetVehicleLastConnection` endpoint returns the last time the vehicle synced with Rivian Cloud.

`POST https://rivian.com/api/gql/gateway/graphql`

### Request Body

```json
{
  "operationName": "GetVehicleLastConnection",
  "variables": {
    "vehicleID": <your-vehicle-id>
  },
  "query": "query GetVehicleLastConnection($vehicleID: String!) { vehicleState(id: $vehicleID) { __typename cloudConnection { __typename lastSync } } }"
}
```

### Example Response

```json
{
  "data": {
    "vehicleState": {
      "__typename": "VehicleState",
      "cloudConnection": {
        "__typename": "VehicleCloudConnection",
        "lastSync": "2023-02-04T01:02:03.665Z"
      }
    }
  }
}
```
