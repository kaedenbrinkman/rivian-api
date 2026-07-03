---
title: Charging Sites
parent: Charging
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 2
---

# chargingSites

## Overview

The `chargingSites` query searches for public charging locations near a map position. The app uses this for the charging map UI.

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
  "operationName": "chargingSites",
  "variables": {
    "filter": {
      "userLocation": {
        "latitude": <user-latitude>,
        "longitude": <user-longitude>
      },
      "searchLocation": {
        "latitude": <map-center-latitude>,
        "longitude": <map-center-longitude>
      },
      "networkIds": [],
      "connectorTypes": ["J1772", "CCS", "NACS"],
      "maxResults": 1000,
      "hideIncompatible": false,
      "hideAdapterNeeded": false,
      "hideLowScore": false,
      "vehicleChargePortType": "CCS",
      "showRestrictedSites": false
    }
  },
  "query": "query chargingSites($filter: ChargingSiteQueryParams!) { chargingSites(filter: $filter) { id networkId location { latitude longitude } maxKw totalCount availableCount outOfOrder unknownAvailability adapterRequired compatible openNow rivianOnly } }"
}
```

Set `vehicleChargePortType` to `NACS` or `CCS` to match the selected vehicle. `connectorTypes` filters which plug types to include.

### Example Response

```json
{
  "data": {
    "chargingSites": [
      {
        "id": "<site-id>",
        "networkId": "<network-id>",
        "location": {
          "latitude": 28.5383,
          "longitude": -81.3792
        },
        "maxKw": 350,
        "totalCount": 8,
        "availableCount": 5,
        "outOfOrder": 0,
        "unknownAvailability": 1,
        "adapterRequired": false,
        "compatible": true,
        "openNow": true,
        "rivianOnly": false
      }
    ]
  }
}
```

Returns an empty array when no sites match the filter or map area.
