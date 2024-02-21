---
title: getSavedTrips
parent: Trip Planning Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# getSavedTrips

## Overview

The `getSavedTrips` endpoint is used to fetch your saved trips.

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
  "operationName": "getSavedTrips",
  "variables": {},
  "query": "query getSavedTrips { getSavedTrips { id name startingSOC stops { name location { latitude longitude } targetArrivalSOCPercent type placeId { value dataProvider } } driveMode networkPreferences { networkId preference } trailerProfile avoidAdapterRequired createdAt updatedAt departureTime } }"
}
```

### Example Response

```json
{
  "data": {
    "getSavedTrips": []
  }
}
```
