---
title: places
parent: Trip Planning Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# places

## Overview

The `places` endpoint is used to query places.

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
  "operationName": "Places",
  "variables": {
    "params": {
      "userLocation": {
        "latitude": <lat>,
        "longitude": <lng>
      },
      "query": "moab",
    }
  },
  "query": "query Places($params: PlacesQueryParams!) { places(params: $params) { dataProvider results { id name distance location { addressComponents { type shortName longName } coordinate { latitude longitude } navCoordinate { latitude longitude } formattedAddress } driveDetails { detourDistance detourDuration driveDistance driveDuration } } } }"
}
```

### Example Response

```json
{
  "data": {
    "places": {
      "dataProvider": "GOOGLE",
      "results": [
        {
          "id": "ChIJjS24muXhR4cRLcTV8XqxMgs",
          "name": "Moab",
          "distance": 2119243,
          "location": {
            "addressComponents": [
              {
                "type": "CITY",
                "shortName": "Moab",
                "longName": "Moab"
              },
              {
                "type": "COUNTY",
                "shortName": "Grand County",
                "longName": "Grand County"
              },
              {
                "type": "STATE",
                "shortName": "UT",
                "longName": "Utah"
              },
              {
                "type": "COUNTRY",
                "shortName": "US",
                "longName": "United States"
              },
              {
                "type": "POSTAL_CODE",
                "shortName": "84532",
                "longName": "84532"
              }
            ],
            "coordinate": {
              "latitude": 38.5733155,
              "longitude": -109.5498395
            },
            "navCoordinate": {
              "latitude": 38.5732889,
              "longitude": -109.54984
            },
            "formattedAddress": "Moab, UT 84532, USA"
          },
          "driveDetails": {
            "detourDistance": null,
            "detourDuration": null,
            "driveDistance": 1919243,
            "driveDuration": 58721
          }
        },
        ...
      ]
    }
  }
}
```
