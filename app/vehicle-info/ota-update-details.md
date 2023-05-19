---
title: getOTAUpdateDetails
parent: Vehicle Info Endpoints
grand_parent: App API
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
      "availableOTAUpdateDetails": null,
      "currentOTAUpdateDetails": {
        "url": "https://rivian.com/mobile/static/update-details/ExNUZJYaOKW9mobx.pdf",
        "version": "2023.14.0",
        "locale": "en-US"
      }
    }
  }
}
```
