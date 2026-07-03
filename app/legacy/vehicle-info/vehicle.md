---
title: GetVehicle
parent: Vehicle info
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 11
---

# GetVehicle

## Overview

The `GetVehicle` endpoint returns drivers and keys for a specific vehicle, including legacy phone/fob/NFC devices and Car Key (CCC) devices.

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
  "operationName": "GetVehicle",
  "variables": {
    "getVehicleId": "<your-vehicle-id>"
  },
  "query": "query GetVehicle($getVehicleId: String) { getVehicle(id: $getVehicleId) { invitedUsers { __typename ... on ProvisionedUser { cccDevices { type mappedIdentityId id deviceName isPaired isEnabled cccKeyId cccStatus phonePublicKey cccDeviceType cccFriendKey wccLevel } devices { type mappedIdentityId id hrid deviceName isPaired isEnabled phonePublicKey wccLevel keyDeviceSubtype } firstName lastName email roles userId isCredentialed } ... on UnprovisionedUser { email inviteId status isCredentialed } } } }"
}
```

### Example Response

```json
{
  "data": {
    "getVehicle": {
      "invitedUsers": [
        {
          "__typename": "ProvisionedUser",
          "cccDevices": [
            {
              "type": "ccc_key/rivian",
              "mappedIdentityId": "<mapped-identity-id>",
              "id": "<device-id>",
              "deviceName": "My Phone",
              "isPaired": true,
              "isEnabled": true,
              "cccKeyId": "<ccc-key-id>",
              "cccStatus": 1,
              "phonePublicKey": "<phone-public-key>",
              "cccDeviceType": "PHONE",
              "cccFriendKey": false,
              "wccLevel": "WCC3"
            }
          ],
          "devices": [
            {
              "type": "phone/rivian",
              "mappedIdentityId": "<mapped-identity-id>",
              "id": "<device-id>",
              "hrid": null,
              "deviceName": "My Phone",
              "isPaired": true,
              "isEnabled": true,
              "phonePublicKey": "<phone-public-key>",
              "wccLevel": "WCC3",
              "keyDeviceSubtype": "PHONE"
            },
            {
              "type": "fob2/rivian",
              "mappedIdentityId": "<mapped-identity-id>",
              "id": "<device-id>",
              "hrid": "<fob-serial>",
              "deviceName": "",
              "isPaired": true,
              "isEnabled": true,
              "phonePublicKey": "",
              "wccLevel": null,
              "keyDeviceSubtype": ""
            },
            {
              "type": "nfc_card/rivian",
              "mappedIdentityId": "<mapped-identity-id>",
              "id": "<device-id>",
              "hrid": "<card-serial>",
              "deviceName": "Rivian NFC Card",
              "isPaired": true,
              "isEnabled": true,
              "phonePublicKey": "",
              "wccLevel": null,
              "keyDeviceSubtype": ""
            }
          ],
          "firstName": "<first-name>",
          "lastName": "<last-name>",
          "email": "<email>",
          "roles": ["primary-owner"],
          "userId": "<user-id>",
          "isCredentialed": true
        },
        {
          "__typename": "UnprovisionedUser",
          "email": "<email>",
          "inviteId": "<invite-id>",
          "status": "COMPLETED",
          "isCredentialed": true
        }
      ]
    }
  }
}
```

Device `type` values include `phone/rivian`, `fob2/rivian`, `nfc_card/rivian`, and `ccc_key/rivian`.
