---
title: GetVehicle
parent: App API
has_children: false
nav_order: 3
---

# GetVehicle

## Overview

The `GetVehicle` endpoint returns details on the given vehicle, including who has access to it.

`POST https://rivian.com/api/gql/gateway/graphql`

### Request Body

```json
{
  "operationName": "GetVehicle",
  "variables": {
    "getVehicleId": <your-vehicle-id>
  },
  "query": "query GetVehicle($getVehicleId: String) { getVehicle(id: $getVehicleId) { __typename invitedUsers { __typename ... on ProvisionedUser { devices { __typename type mappedIdentityId id hrid deviceName isPaired isEnabled } firstName lastName email roles userId } ... on UnprovisionedUser { email inviteId status } } } }"
}
```

### Example Response

```json
{
  "data": {
    "getVehicle": {
      "__typename": "Vehicle",
      "invitedUsers": [
        {
          "__typename": "ProvisionedUser",
          "devices": [
            {
              "__typename": "ProvisionedUserDevice",
              "type": "fob/rivian",
              "mappedIdentityId": <mapped-identity-id>,
              "id": <fob-id>,
              "hrid": "NA",
              "deviceName": "Rivian Fob",
              "isPaired": true,
              "isEnabled": true
            },
            {
              "__typename": "ProvisionedUserDevice",
              "type": "nfc_card/rivian",
              "mappedIdentityId": <mapped-identity-id>,
              "id": <nfc-card-id>,
              "hrid": <card-sn>,
              "deviceName": "Rivian NFC Card",
              "isPaired": true,
              "isEnabled": true
            }
          ],
          "firstName": <first-name>,
          "lastName": <last-name>,
          "email": <email>,
          "roles": [
            "driver"
          ],
          "userId": <user-id>
        },
        {
          "__typename": "ProvisionedUser",
          "devices": [],
          "firstName": <first-name>,
          "lastName": <last-name>,
          "email": <email>,
          "roles": [
            "driver"
          ],
          "userId": <user-id>
        },
        ...
      ]
    }
  }
}
```
