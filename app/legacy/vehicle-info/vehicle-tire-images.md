---
title: getVehicleTireImages
parent: Vehicle info
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 10
---

# getVehicleTireImages

## Overview

The `getVehicleTireImages` query returns a wheel diagram image URL for the tire pressure screen. The GraphQL field is `getVehicleWheelImages`.

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
  "operationName": "getVehicleTireImages",
  "variables": {
    "wheelPackage": "DCP_WHEEL_PACKAGE_UNSPECIFIED"
  },
  "query": "query getVehicleTireImages($wheelPackage: DCPWheelPackage!) { getVehicleWheelImages(wheelPackage: $wheelPackage) { wheelPackage url } }"
}
```

### Wheel package values

| `wheelPackage` | Example image |
|----------------|---------------|
| `DCP_WHEEL_PACKAGE_UNSPECIFIED` | `.../WHL-0AS.png` |
| `DCP_WHEEL_PACKAGE_20A_GLOSS_GRAPHITE_BRIGHT` | `.../WHL-20AT.png` |
| `DCP_WHEEL_PACKAGE_20_IN_ADVENTURE1_METALLIC` | `.../WHL-0AS.png` |
| `DCP_WHEEL_PACKAGE_22_IN_AERO2_BLACK` | `.../WHL-2AR.png` |
| `DCP_WHEEL_PACKAGE_22_IN_PERFORMANCE_BRIT48MM` | `.../WHL-2SS.png` |

Images are served from `https://rivian.com/mobile/static/img/v1/features/wheels/`.

### Example Response

```json
{
  "data": {
    "getVehicleWheelImages": {
      "wheelPackage": "DCP_WHEEL_PACKAGE_UNSPECIFIED",
      "url": "https://rivian.com/mobile/static/img/v1/features/wheels/WHL-0AS.png"
    }
  }
}
```

Requires a valid `u-sess` header; unauthenticated requests return `UNAUTHENTICATED`.
