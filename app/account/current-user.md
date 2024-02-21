---
title: CurrentUserForLogin
parent: Account Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# CurrentUserForLogin

## Overview

The `CurrentUserForLogin` endpoint returns information about the configuration and options for the vehicles in your account.

`POST https://rivian.com/api/gql/gateway/graphql`

### Request Body

```json
{
  "operationName": "CurrentUserForLogin",
  "variables": {},
  "query": "query CurrentUserForLogin { currentUser { __typename ...CurrentUserFields } }  fragment CurrentUserFields on User { id settings { distanceUnit { value timestamp } temperatureUnit { value timestamp } } firstName lastName email address { country } vehicles { id owner roles vin vas { vasVehicleId vehiclePublicKey } vehicle { deviceSlots { phone { max free } } model mobileConfiguration { trimOption { optionId optionName } exteriorColorOption { optionId optionName } interiorColorOption { optionId optionName } driveSystemOption { optionId optionName } tonneauOption { optionId optionName } wheelOption { optionId optionName } driveSystemTowingDriveModes driveSystemDriveModes maxVehiclePower } maintenanceSchedule { sections { items { description isDue } serviceLifetime { __typename ... on MaintenanceDistanceLimit { km mi } ... on MaintenanceDateLimit { year } } } } } settings { name { value } } } enrolledPhones { vas { vasPhoneId publicKey } enrolled { deviceType deviceName vehicleId identityId shortName } } pendingInvites { id invitedByFirstName role status vehicleId vehicleModel email } }"
}
```

### Example Response

```json
{
  "data": {
    "currentUser": {
      "__typename": "User",
      "id": <user-id>,
      "settings": {
        "distanceUnit": null,
        "temperatureUnit": null
      },
      "firstName": <first-name>,
      "lastName": <last-name>,
      "email": <email>,
      "address": {
        "country": "US"
      },
      "vehicles": [
        {
          "id": <vehicle-id>,
          "owner": null,
          "roles": [
            "primary-owner"
          ],
          "vin": <vin>,
          "vas": {
            "vasVehicleId": <vas-vehicle-id>,
            "vehiclePublicKey": <vehicle-public-key>
          },
          "vehicle": {
            "deviceSlots": {
              "phone": {
                "max": 4,
                "free": 0
              }
            },
            "model": "R1T",
            "mobileConfiguration": {
              "trimOption": {
                "optionId": "PKG-ADV",
                "optionName": "Adventure Package"
              },
              "exteriorColorOption": {
                "optionId": "EXP-CYL",
                "optionName": "Compass Yellow"
              },
              "interiorColorOption": {
                "optionId": "INT-BMP",
                "optionName": "Black Mountain"
              },
              "driveSystemOption": {
                "optionId": "MOT-401",
                "optionName": "Quad-Motor AWD"
              },
              "tonneauOption": {
                "optionId": "TON-P01",
                "optionName": "Powered Tonneau Cover"
              },
              "wheelOption": {
                "optionId": "WHL-0AD",
                "optionName": "20\" All-Terrain Dark"
              },
              "driveSystemTowingDriveModes": [
                "everyday",
                "off_road_auto",
                "winter"
              ],
              "driveSystemDriveModes": [
                "everyday",
                "off_road_auto",
                "winter",
                "sport",
                "distance",
                "off_road_rocks",
                "off_road_sport_auto",
                "off_road_sport_drift",
                "off_road_sand"
              ],
              "maxVehiclePower": 215
            },
            "maintenanceSchedule": {
              "sections": [
                {
                  "items": [
                    {
                      "description": "Tire rotation",
                      "isDue": null
                    },
                    {
                      "description": "Multi-point inspection",
                      "isDue": null
                    }
                  ],
                  "serviceLifetime": {
                    "__typename": "MaintenanceDistanceLimit",
                    "km": 12000,
                    "mi": 7500
                  }
                },
                {
                  "items": [
                    {
                      "description": "Brake fluid flush",
                      "isDue": false
                    }
                  ],
                  "serviceLifetime": {
                    "__typename": "MaintenanceDateLimit",
                    "year": 3
                  }
                },
                {
                  "items": [
                    {
                      "description": "Coolant change",
                      "isDue": null
                    },
                    {
                      "description": "Drive unit fluid change (Quad-Motor AWD vehicles only)",
                      "isDue": null
                    }
                  ],
                  "serviceLifetime": {
                    "__typename": "MaintenanceDistanceLimit",
                    "km": 180000,
                    "mi": 112500
                  }
                }
              ]
            }
          },
          "settings": {
            "name": {
              "value": "R1T"
            }
          }
        }
      ],
      "enrolledPhones": [
        {
          "vas": {
            "vasPhoneId": <vas-phone-id>,
            "publicKey": <vas-phone-public-key>
          },
          "enrolled": [
            {
              "deviceType": "phone/rivian",
              "deviceName": <phone-name>,
              "vehicleId": <vehicle-id>,
              "identityId": <phone-id>,
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
