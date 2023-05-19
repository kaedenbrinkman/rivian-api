---
title: SetVehicleName
parent: Vehicle Info Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# getOTAUpdateDetails

## Overview

The `SetVehicleName` endpoint renames your vehicle.

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
  "operationName": "SetVehicleName",
  "variables": {
    "vehicleId": <your-vehicle-id>,
    "name": <new-name>
  },
  "query": "mutation SetVehicleName($vehicleId: String!, $name: String!) { setVehicleName(vehicleId: $vehicleId, name: $name) { value } }"
}
```

### Example Response

```json
{
  "data": {
    "setVehicleName": {
      "value": <new-name>
    }
  }
}
```
