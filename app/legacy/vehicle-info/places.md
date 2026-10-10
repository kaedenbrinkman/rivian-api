---
title: places (geocoding)
parent: Vehicle info
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 4
---

# places and PlaceByUrl

## Overview

The app's map search. `places` turns free text (a business name, an address, a city) into Google place results with coordinates; `PlaceByUrl` resolves a map share link. Both are read-only and need only the session headers.

Not to be confused with `SearchPlaces`, which searches Rivian's own locations (service centers, spaces).

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
```

## places

Only `query` is required. `userLocation` biases ranking (and `distance` is measured from it). Other `PlacesQueryParams` fields seen in the app: `locale`, `requestContext`, `dataProvider`, `nextToken`, `maxResults`, `location`, `filter`, `autocomplete`.

```json
{
  "operationName": "places",
  "variables": {
    "params": {
      "query": "Costco Goleta",
      "userLocation": { "latitude": <your-lat>, "longitude": <your-lng> },
      "maxResults": 3
    }
  },
  "query": "query places($params: PlacesQueryParams!) { places(params: $params) { dataProvider queryPredictions { query } results { id name distance location { addressComponents { type shortName longName } coordinate { latitude longitude } navCoordinate { latitude longitude } formattedAddress } driveDetails { detourDistance detourDuration driveDistance driveDuration } googleRating { averageRating ratingCount } operatingHours { openNow alwaysOpen hours { close day open } nextSwitch } icon } } }"
}
```

### Example Response

```json
{
  "data": {
    "places": {
      "dataProvider": "GOOGLE",
      "queryPredictions": [],
      "results": [
        {
          "id": "ChIJ3-PcaK5A6YARvoqmzSvMfIA",
          "name": "Costco Wholesale",
          "distance": 161927,
          "location": {
            "formattedAddress": "7095 Market Pl Dr #474c, Goleta, CA 93117, USA",
            "coordinate": { "latitude": 34.4280052, "longitude": -119.8747787 },
            "navCoordinate": { "latitude": 34.4283714, "longitude": -119.8741895 }
          },
          "driveDetails": { "driveDistance": 161927, "driveDuration": 6158 }
        }
      ]
    }
  }
}
```

`navCoordinate` is the road-side point to navigate to; `coordinate` is the place itself. A plain street address returns `name: null`. The search copes with a person's name in front of an address (it still returns the address), which the vehicle's own lookup in [ParseAndShareLocationToVehicle](/app/legacy/controls/share-location) does not.

## PlaceByUrl

Resolves a share link (`https://maps.app.goo.gl/...` and similar) to one place. Anything that is not a real share link is treated as text and gives unrelated results; plain text returns `null`.

```json
{
  "operationName": "PlaceByUrl",
  "variables": {
    "url": "https://maps.app.goo.gl/<id>",
    "userLocation": { "latitude": <your-lat>, "longitude": <your-lng> }
  },
  "query": "query PlaceByUrl($url: String!, $userLocation: GeoCoordinatesInput) { placeByUrl(url: $url, userLocation: $userLocation) { id name location { formattedAddress coordinate { latitude longitude } navCoordinate { latitude longitude } } } }"
}
```

Response: a single object with the same `id`, `name` and `location` shape as a `places` result, or `null`.
