---
title: getVehicleImages
parent: Vehicle Info Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# getVehicleImages

## Overview

The `getVehicleImages` endpoint returns image assets for your vehicles.

If you are just looking for the images from the configurator, see [Configurator API](/configurator/).

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
  "operationName": "GetVehicleImages",
  "query": "query GetVehicleImages($extension: String!, $resolution: String!, $vehicleVersion: String!) { getVehicleOrderMobileImages( resolution: $resolution extension: $extension version: $vehicleVersion ) { __typename orderId url resolution size design placement } getVehicleMobileImages( resolution: $resolution extension: $extension version: $vehicleVersion ) { __typename vehicleId url resolution size design placement overlays { __typename url overlay zIndex } } }",
  "variables": {
    "extension": "png",
    "resolution": "@3x",
    "vehicleVersion": "<your vehicle version>"
  }
}
```
For ```vehicleVersion``` try numbers 1-5.


### Example Response

```json
{
  "data": {
    "getVehicleOrderMobileImages": [
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_front_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "front"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_front_dark_small_hdpi.webp",
        "resolution": "hdpi",
        "size": "small",
        "design": "dark",
        "placement": "front"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_front_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "front"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_front_light_small_hdpi.webp",
        "resolution": "hdpi",
        "size": "small",
        "design": "light",
        "placement": "front"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_overhead_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "overhead"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_overhead_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "overhead"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_rear_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "rear"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_rear_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "rear"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_side-charging_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "side-charging"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_side-charging_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "side-charging"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_side_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "side"
      },
      {
        "__typename": "VehicleMobileImage",
        "orderId": <your-order-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_side_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "side"
      }
    ],
    "getVehicleMobileImages": [
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_front_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "front"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_front_dark_small_hdpi.webp",
        "resolution": "hdpi",
        "size": "small",
        "design": "dark",
        "placement": "front"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_front_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "front"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_front_light_small_hdpi.webp",
        "resolution": "hdpi",
        "size": "small",
        "design": "light",
        "placement": "front"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_overhead_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "overhead"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_overhead_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "overhead"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_rear_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "rear"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_rear_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "rear"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_side-charging_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "side-charging"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_side-charging_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "side-charging"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_side_dark_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "dark",
        "placement": "side"
      },
      {
        "__typename": "VehicleMobileImage",
        "vehicleId": <your-vehicle-id>,
        "url": "https://rivian.com/mobile/static/img/v1/vehicle/r1t/2021/adventure/ext/el-cap-granite/20ad1-brit-at/r1t_2021_adventure_ext_el-cap-granite_20ad1-brit-at_side_light_large_hdpi.webp",
        "resolution": "hdpi",
        "size": "large",
        "design": "light",
        "placement": "side"
      }
    ]
  }
}
```
