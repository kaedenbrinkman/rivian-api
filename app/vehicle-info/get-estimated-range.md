---
title: GetEstimatedRange
parent: Vehicle Info Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# GetEstimatedRange

## Overview

The `GetEstimatedRange` endpoint returns the estimated range based on battery percentage, current drive mode, and attached trailers.

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
dc-cid: m-android
```

### Request Body

```json
{
  "operationName": "GetEstimatedRange",
  "query": "query GetEstimatedRange($vehicleId: String!, $startSoc: Float!, $driveMode: String, $trailerProfile: String) { getVehicle(id: $vehicleId) { __typename estimatedRange( startSoc: $startSoc driveMode: $driveMode trailerProfile: $trailerProfile ) } }",
  "variables": {
    "startSoc": <starting battery percentage 0-100>,
    "vehicleId": "<your vehicle id>"
  }
}
```

### Example Response

```json
{
    "data": {
        "getVehicle": {
            "__typename": "Vehicle",
            "estimatedRange": <range in kilometers>
        }
    }
}
```
