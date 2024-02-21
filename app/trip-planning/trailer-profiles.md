---
title: GetTrailerProfiles
parent: Trip Planning Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# GetTrailerProfiles

## Overview

The `GetTrailerProfiles` endpoint is used to list saved trailer profiles on a vehicle.

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
  "operationName": "GetTrailerProfiles",
  "variables": {
    "getVehicleId": "<your-vehicle-id>"
  },
  "query": "query GetTrailerProfiles($getVehicleId: String!) { getVehicle(id: $getVehicleId) { trailerProfiles { trailerDefault { __typename ...TrailerProfileFields } trailer1 { __typename ...TrailerProfileFields } trailer2 { __typename ...TrailerProfileFields } trailer3 { __typename ...TrailerProfileFields } } } }  fragment TrailerProfileFields on TrailerProfile { rangeStatus weight onRoadEfficiency offRoadEfficiency name }"
}
```

### Example Response

```json
{
  "data": {
    "getVehicle": {
      "trailerProfiles": null
    }
  }
}
```
