---
title: VehiclesAndEnrollments
parent: Vehicle info
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 12
---

# VehiclesAndEnrollments

## Overview

The `VehiclesAndEnrollments` endpoint is the primary vehicle list query used on app startup. It returns all vehicles on the account along with configuration, key enrollment slots, phone keys, Car Key (CCC) keys, and pending driver invites.

Similar data is available from [`getUserInfo`](/app/account/user-info), but the app calls this query repeatedly to refresh vehicle and enrollment state.

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
  "operationName": "VehiclesAndEnrollments",
  "variables": {},
  "query": "query VehiclesAndEnrollments { currentUser { id vehicles { id owner roles assetGroup vin vas { cccOwnerKeySetupStatus cccVehicleId vasVehicleId vehiclePublicKey } vehicle { deviceSlots { phone { max free } fob2 { max free } } model modelYear mobileConfiguration { trimOption { optionId optionName } exteriorColorOption { optionId optionName } interiorColorOption { optionId optionName } driveSystemOption { optionId optionName } tonneauOption { optionId optionName } wheelOption { optionId optionName } driveSystemTowingDriveModes driveSystemDriveModes maxVehiclePower chargePort } cccCapable cccEnabled cccReady legacyEnabled maintenanceSchedule { sections { items { description isDue } serviceLifetime { __typename ... on MaintenanceDistanceLimit { km mi } ... on MaintenanceDateLimit { year } } } } maintenanceScheduleModel { requestType section serviceRequestData { key concern } limit { type valueMiles valueKm valueYears } labors } maintenanceSupportUrls { url purpose } locationConsentRequest { requesterName recipientName timestamp } } } enrolledPhones { vas { vasPhoneId publicKey } enrolled { deviceType deviceName keyDeviceSubtype vehicleId identityId shortName wccLevel phoneModel } } enrolledCCCKeys { vehicleId identityId cccEndpointId cccKeyId cccVehicleId cccStatus phonePublicKey cccDeviceType cccDeviceDisabled mappedIdentityId deviceId type cccFriendKey cccFriendKeyFriendlyName } pendingInvites { id invitedByFirstName role status vehicleId vehicleModel email } } }"
}
```

### Example Response

```json
{
  "data": {
    "currentUser": {
      "id": "<your-user-id>",
      "vehicles": [
        {
          "id": "<your-vehicle-id>",
          "owner": "<owner-user-id>",
          "roles": ["owner"],
          "assetGroup": [],
          "vin": "<your-vin>",
          "vas": {
            "cccOwnerKeySetupStatus": false,
            "cccVehicleId": null,
            "vasVehicleId": "<vas-vehicle-id>",
            "vehiclePublicKey": "<vehicle-public-key>"
          },
          "vehicle": {
            "deviceSlots": {
              "phone": { "max": 4, "free": 0 },
              "fob2": { "max": 2, "free": 2 }
            },
            "model": "R1T",
            "modelYear": 2022,
            "mobileConfiguration": {
              "trimOption": { "optionId": "PKG-ADV", "optionName": "Adventure Package" },
              "exteriorColorOption": { "optionId": "EXP-FGR", "optionName": "Forest Green" },
              "interiorColorOption": { "optionId": "INT-OAK", "optionName": "Black Mountain + Warm Ash Wood" },
              "driveSystemOption": { "optionId": "MOT-402", "optionName": "Dual-Motor AWD" },
              "tonneauOption": { "optionId": "TON-P02", "optionName": "Powered Tonneau Cover" },
              "wheelOption": { "optionId": "WHL-2AD", "optionName": "22\" Road Wheels" },
              "driveSystemTowingDriveModes": ["everyday", "off_road_auto", "winter"],
              "driveSystemDriveModes": ["everyday", "off_road_auto", "winter", "sport", "distance", "off_road_rocks", "off_road_sport_auto", "off_road_sport_drift", "off_road_sand"],
              "maxVehiclePower": 215,
              "chargePort": "CCS"
            },
            "cccCapable": false,
            "cccEnabled": false,
            "cccReady": false,
            "legacyEnabled": true,
            "maintenanceSchedule": {
              "sections": [
                {
                  "items": [{ "description": "Tire rotation", "isDue": true }],
                  "serviceLifetime": { "__typename": "MaintenanceDistanceLimit", "km": 15000, "mi": 9000 }
                }
              ]
            },
            "maintenanceScheduleModel": [
              {
                "requestType": "tireRotation4Tires",
                "section": "maintenance",
                "serviceRequestData": { "key": "tireRotation", "concern": "Maintenance - Tire Rotation" },
                "limit": { "type": "distance", "valueMiles": 9000, "valueKm": 15000, "valueYears": 0 },
                "labors": ["220010019"]
              }
            ],
            "maintenanceSupportUrls": [
              { "url": "https://rivian.com/support/article/r1-tire-service-guide", "purpose": "tireServiceGuide" },
              { "url": "https://rivian.com/support/article/r1-vehicle-maintenance", "purpose": "maintenanceSchedule" }
            ],
            "locationConsentRequest": null
          }
        }
      ],
      "enrolledPhones": [
        {
          "vas": {
            "vasPhoneId": "<phone-key-id>",
            "publicKey": "<phone-public-key>"
          },
          "enrolled": [
            {
              "deviceType": "phone/rivian",
              "deviceName": "My Phone",
              "keyDeviceSubtype": "PHONE",
              "vehicleId": "<your-vehicle-id>",
              "identityId": "<identity-id>",
              "shortName": "",
              "wccLevel": "WCC3",
              "phoneModel": "Pixel 7"
            }
          ]
        }
      ],
      "enrolledCCCKeys": [
        {
          "vehicleId": "<your-vehicle-id>",
          "identityId": "<identity-id>",
          "cccKeyId": "<ccc-key-id>",
          "cccVehicleId": "<ccc-vehicle-id>",
          "cccStatus": 1,
          "phonePublicKey": "<phone-public-key>",
          "cccDeviceType": "PHONE",
          "cccDeviceDisabled": false,
          "mappedIdentityId": "<mapped-identity-id>",
          "deviceId": "<device-id>",
          "type": "ccc_key/rivian",
          "cccFriendKey": false,
          "cccFriendKeyFriendlyName": null
        }
      ],
      "pendingInvites": []
    }
  }
}
```

The response includes one entry per vehicle on the account. `maintenanceScheduleModel` also contains glass replacement and tire replacement request types not shown above.
