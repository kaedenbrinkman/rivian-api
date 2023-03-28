---
title: getUserInfo
parent: Account Endpoints
has_children: false
nav_order: 3
---

# getUserInfo

## Overview

The `getUserInfo` endpoint returns information about the user's account.

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
  "operationName": "getUserInfo",
  "variables": {},
  "query": "query getUserInfo { currentUser { __typename id firstName lastName email address { __typename country } vehicles { __typename id name owner roles vin vas { __typename vasVehicleId vehiclePublicKey } vehicle { __typename model mobileConfiguration { __typename trimOption { __typename optionId optionName } exteriorColorOption { __typename optionId optionName } interiorColorOption { __typename optionId optionName } } vehicleState { __typename supportedFeatures { __typename name status } } otaEarlyAccessStatus } settings { __typename name { __typename value } } } enrolledPhones { __typename vas { __typename vasPhoneId publicKey } enrolled { __typename deviceType deviceName vehicleId identityId shortName } } pendingInvites { __typename id invitedByFirstName role status vehicleId vehicleModel email } } }"
}
```

### Example Response

```json
{
  "data": {
    "currentUser": {
      "__typename": "User",
      "id": <your-user-id>,
      "firstName": <your-first-name>,
      "lastName": <your-last-name>,
      "email": <your-email>,
      "address": {
        "__typename": "UserAddress",
        "country": "US"
      },
      "vehicles": [
        {
          "__typename": "UserVehicle",
          "id": <your-vehicle-id>,
          "name": null,
          "owner": null,
          "roles": [
            "primary-owner"
          ],
          "vin": <your-vin>,
          "vas": {
            "__typename": "UserVehicleAccess",
            "vasVehicleId": <your-vas-vehicle-id>,
            "vehiclePublicKey": <your-vehicle-public-key>
          },
          "vehicle": {
            "__typename": "Vehicle",
            "model": <vehicle-model>,
            "mobileConfiguration": {
              ... options ...
            },
            "vehicleState": {
              "__typename": "VehicleState",
              "supportedFeatures": [
                ... vehicle's supported app features ...
              ]
            },
            "otaEarlyAccessStatus": false
          },
          "settings": {
            "__typename": "UserVehicleSettingsMap",
            "name": null
          }
        }
      ],
      "enrolledPhones": [
        {
          "__typename": "UserEnrolledPhone",
          "vas": {
            "__typename": "UserEnrolledPhoneAccess",
            "vasPhoneId": <phone-key-id>,
            "publicKey": <phone-public-key>
          },
          "enrolled": [
            {
              "__typename": "UserEnrolledPhoneEntry",
              "deviceType": "phone/rivian",
              "deviceName": <phone-name>,
              "vehicleId": <your-vehicle-id>,
              "identityId": <your-identity-id>,
              "shortName": ""
            }
          ]
        }
      ],
      "pendingInvites": []
    }
  }
}
```
