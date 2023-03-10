---
title: getVehicleCommand
parent: App API
has_children: false
nav_order: 3
---

# getVehicleCommand

## Overview

The `getVehicleCommand` endpoint is used to get the status of a sent vehicle command. When the status is 0, the command has completed.

`POST https://rivian.com/api/gql/gateway/graphql`

### Request Body

```json
{
  "operationName": "getVehicleCommand",
  "variables": {
    "id": <command-id>
  },
  "query": "query getVehicleCommand($id: String!) { getVehicleCommand(id: $id) { __typename id command createdAt state responseCode statusCode } }"
}
```

### Example Response

```json
{
  "data": {
    "getVehicleCommand": {
      "__typename": "GetVehicleCommandState",
      "id": <command-id>,
      "command": "UNLOCK_ALL_CLOSURES",
      "createdAt": "2023-02-04T21:28:25.616180",
      "state": 3,
      "responseCode": null,
      "statusCode": null
    }
  }
}
```
