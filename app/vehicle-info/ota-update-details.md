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
        "url": "https://dc-service-prod-techpubs-r1-docs.s3.us-east-1.amazonaws.com/Vehicle/R1T/UpdateDetails/20240302/PDF-digital/US/en-US/update-details-20240302.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=...",
        "version": "2023.14.0",
        "locale": "en-US"
      }
    }
  }
}
```
