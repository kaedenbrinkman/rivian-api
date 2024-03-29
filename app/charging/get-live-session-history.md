---
title: Get Live Charging Session History
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# Get Live Charging Session History

# getLiveSessionHistory

## Overview

The `getLiveSessionHistory` gets live charging session history for a vehicle.

`POST https://rivian.com/api/gql/chrg/user/graphql`

### Request Body

```json
{
  "operationName": "getLiveSessionHistory",
  "variables": {
    "vehicleId": <your-vehicle-id>
    },
  "query": "query getLiveSessionHistory($vehicleId: ID) { getLiveSessionHistory(vehicleId: $vehicleId) { chartData { kw time } } }"
}
```

### Example Response

```json
{
   "data":{
      "getLiveSessionHistory":{
         "chartData":[
            {
               "kw":0,
               "time":"2023-06-08T20:03:49.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:05:10.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:06:31.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:07:52.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:09:13.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:10:34.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:11:55.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:13:16.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:14:37.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:15:58.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:17:19.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:18:40.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:20:01.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:21:22.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:22:43.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:24:04.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:25:25.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:26:46.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:28:07.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:29:28.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:30:49.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:32:10.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:33:31.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:34:52.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:36:13.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:37:34.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:38:55.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:40:16.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:41:37.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:42:58.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:44:19.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:45:40.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:47:01.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:48:22.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:49:43.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:51:04.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:52:25.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:53:46.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:55:07.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:56:28.021983Z"
            },
            {
               "kw":9,
               "time":"2023-06-08T20:57:38.539091Z"
            }
         ]
      }
   }
}
```
