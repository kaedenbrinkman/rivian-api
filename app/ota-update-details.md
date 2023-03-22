---
title: getOTAUpdateDetails
parent: App API
has_children: false
nav_order: 3
---

# getOTAUpdateDetails

## Overview

The `getOTAUpdateDetails` endpoint returns the release notes for the current and available OTA updates.

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
  "operationName": "getOTAUpdateDetails",
  "variables": { "vehicleId": <your-vehicle-id> },
  "query": "query getOTAUpdateDetails($vehicleId: String!) { getVehicle(id: $vehicleId) { availableOTAUpdateDetails { url version locale } currentOTAUpdateDetails { url version locale } } }"
}
```

### Example Response

```json
{
  "data": {
    "getVehicle": {
      "availableOTAUpdateDetails": {
        "url": "https://rivian.com/mobile/static/update-details/yUp3B144cthczZ6Y.pdf",
        "version": "2023.06.02",
        "locale": "en-US"
      },
      "currentOTAUpdateDetails": {
        "url": "https://rivian.com/mobile/static/update-details/t0pwa-pJkP0aGkmj.pdf",
        "version": "2023.02.03",
        "locale": "en-US"
      }
    }
  }
}
```
