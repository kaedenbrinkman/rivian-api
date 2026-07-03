---
title: GetReverseGeocode
parent: Vehicle info
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 4
---

# GetReverseGeocode

## Overview

The `GetReverseGeocode` query converts coordinates into a formatted address. The app uses this for vehicle location labels and map pins.

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
  "operationName": "GetReverseGeocode",
  "variables": {
    "params": {
      "geocode": {
        "latitude": <latitude>,
        "longitude": <longitude>
      },
      "userLocation": {
        "latitude": <user-latitude>,
        "longitude": <user-longitude>
      }
    }
  },
  "query": "query GetReverseGeocode($params: ReverseGeocodeQueryParams!) { reverseGeocode(params: $params) { id name location { addressComponents { type shortName longName } formattedAddress coordinate { latitude longitude } navCoordinate { latitude longitude } } distance } }"
}
```

`geocode` is the point to look up. `userLocation` is used to compute `distance` (meters from the user).

### Example Response

```json
{
  "data": {
    "reverseGeocode": [
      {
        "id": "<place-id>",
        "name": null,
        "location": {
          "addressComponents": [
            { "type": "STREET", "shortName": "Main St", "longName": "Main Street" },
            { "type": "CITY", "shortName": "Orlando", "longName": "Orlando" },
            { "type": "STATE", "shortName": "FL", "longName": "Florida" },
            { "type": "COUNTRY", "shortName": "US", "longName": "United States" },
            { "type": "POSTAL_CODE", "shortName": "32801", "longName": "32801" }
          ],
          "formattedAddress": "123 Main St, Orlando, FL 32801, USA",
          "coordinate": {
            "latitude": 28.5383,
            "longitude": -81.3792
          },
          "navCoordinate": {
            "latitude": 28.5384,
            "longitude": -81.3791
          }
        },
        "distance": 1500
      }
    ]
  }
}
```
