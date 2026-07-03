---
title: VehicleNames
parent: Vehicle info
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 9
---

# VehicleNames

## Overview

The `VehicleNames` endpoint returns the custom nickname for each vehicle on the account. To set a name, use [`SetVehicleName`](/app/legacy/vehicle-info/set-vehicle-name).

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
apollographql-client-name: com.rivian.android.consumer
```

### Request Body

```json
{
  "operationName": "VehicleNames",
  "variables": {},
  "query": "query VehicleNames { currentUser { vehicles { id settings { name { value } } } } }"
}
```

### Example Response

```json
{
  "data": {
    "currentUser": {
      "vehicles": [
        {
          "id": "<your-vehicle-id>",
          "settings": {
            "name": {
              "value": "My R1T"
            }
          }
        },
        {
          "id": "<your-other-vehicle-id>",
          "settings": {
            "name": {
              "value": "Road Tripper"
            }
          }
        }
      ]
    }
  }
}
```

If a vehicle has no custom name, `name` may be `null`.
