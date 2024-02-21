---
title: Charger Details
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# Charger Details

## Overview

The charger details endpoint allows the user to view details about one or more DC charging stations by their unique ids.

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
```

`POST https://rivian.com/api/gql/gateway/graphql`

### Example Request

```json
{
  "operationName": "ChargerDetails",
  "variables": {
    "ids": [
      "riv_chrg_8904951906489915924",
      "riv_chrg_16214382483804747063"
    ]
  },
  "query": "query ChargerDetails($ids: [String!]!, $userLocation: GeoCoordinatesInput) { chargerByIds(ids: $ids, userLocation: $userLocation) { id name location { addressComponents { type shortName longName } formattedAddress coordinate { latitude longitude } navCoordinate { latitude longitude } } distance driveDetails { driveDistance driveDuration detourDistance detourDuration } chargingStation { network networkId maxKw note chargers { locationId pluginDependency connectors { id evseId evseUid name level maxKw chargingPrice { level description amount currency lastUpdateTime symbol type unit } type free vend state } } operatingHours { alwaysOpen hours { close day open } } } adapterRequired } }"
}
```

### Example Response

```json
{
  "data": {
    "chargerByIds": [
      {
        "id": "riv_chrg_8904951906489915924",
        "name": "Walmart 3454 - Perry, UT",
        "location": {
          "addressComponents": [
            {
              "type": "STREET",
              "shortName": "1200 S. Commerce Way",
              "longName": "1200 S. Commerce Way"
            },
            {
              "type": "CITY",
              "shortName": "Perry",
              "longName": "Perry"
            },
            {
              "type": "COUNTRY",
              "shortName": "USA",
              "longName": "United States"
            },
            {
              "type": "POSTAL_CODE",
              "shortName": "84302",
              "longName": "84302"
            },
            {
              "type": "STATE",
              "shortName": "UT",
              "longName": "Utah"
            }
          ],
          "formattedAddress": "1200 S. Commerce Way, Perry, UT 84302, USA",
          "coordinate": {
            "latitude": 41.48497,
            "longitude": -112.02923
          },
          "navCoordinate": {
            "latitude": 41.48497,
            "longitude": -112.02923
          }
        },
        "distance": 0,
        "driveDetails": null,
        "chargingStation": {
          "network": "Electrify America",
          "networkId": "10027",
          "maxKw": 150,
          "note": "",
          "chargers": [
            {
              "locationId": "US-EAN-L145006",
              "pluginDependency": "AFTER",
              "connectors": [
                {
                  "id": "US-EAN-P145006:5:1",
                  "evseId": "US-EAN-E145006:5",
                  "evseUid": "EAN145011",
                  "name": "Walmart 3454 - Perry, UT",
                  "level": "DCFC",
                  "maxKw": 150,
                  "chargingPrice": {
                    "level": null,
                    "description": "Check Electrify America’s app or the charger display for energy price and fees.",
                    "amount": 1,
                    "currency": "USD",
                    "lastUpdateTime": null,
                    "symbol": "*",
                    "type": null,
                    "unit": null
                  },
                  "type": "CCS",
                  "free": false,
                  "vend": "PAID",
                  "state": "UNKNOWN"
                },
                {
                  "id": "US-EAN-P145006:6:1",
                  "evseId": "US-EAN-E145006:6",
                  "evseUid": "EAN145012",
                  "name": "Walmart 3454 - Perry, UT",
                  "level": "DCFC",
                  "maxKw": 150,
                  "chargingPrice": {
                    "level": null,
                    "description": "Check Electrify America’s app or the charger display for energy price and fees.",
                    "amount": 1,
                    "currency": "USD",
                    "lastUpdateTime": null,
                    "symbol": "*",
                    "type": null,
                    "unit": null
                  },
                  "type": "CCS",
                  "free": false,
                  "vend": "PAID",
                  "state": "UNKNOWN"
                },
                {
                  "id": "US-EAN-P145006:7:1",
                  "evseId": "US-EAN-E145006:7",
                  "evseUid": "EAN145013",
                  "name": "Walmart 3454 - Perry, UT",
                  "level": "DCFC",
                  "maxKw": 150,
                  "chargingPrice": {
                    "level": null,
                    "description": "Check Electrify America’s app or the charger display for energy price and fees.",
                    "amount": 1,
                    "currency": "USD",
                    "lastUpdateTime": null,
                    "symbol": "*",
                    "type": null,
                    "unit": null
                  },
                  "type": "CCS",
                  "free": false,
                  "vend": "PAID",
                  "state": "UNKNOWN"
                },
                {
                  "id": "US-EAN-P145006:8:1",
                  "evseId": "US-EAN-E145006:8",
                  "evseUid": "EAN145014",
                  "name": "Walmart 3454 - Perry, UT",
                  "level": "DCFC",
                  "maxKw": 150,
                  "chargingPrice": {
                    "level": null,
                    "description": "Check Electrify America’s app or the charger display for energy price and fees.",
                    "amount": 1,
                    "currency": "USD",
                    "lastUpdateTime": null,
                    "symbol": "*",
                    "type": null,
                    "unit": null
                  },
                  "type": "CCS",
                  "free": false,
                  "vend": "PAID",
                  "state": "UNKNOWN"
                }
              ]
            }
          ],
          "operatingHours": {
            "alwaysOpen": true,
            "hours": [
              {
                "close": 86400,
                "day": "SUNDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "MONDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "TUESDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "WEDNESDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "THURSDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "FRIDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "SATURDAY",
                "open": 0
              }
            ]
          }
        },
        "adapterRequired": false
      },
      {
        "id": "riv_chrg_16214382483804747063",
        "name": "Walmart 4068 - Spanish Fork, UT",
        "location": {
          "addressComponents": [
            {
              "type": "STREET",
              "shortName": "1206 N. Canyon Creek Pkwy",
              "longName": "1206 N. Canyon Creek Pkwy"
            },
            {
              "type": "CITY",
              "shortName": "Spanish Fork",
              "longName": "Spanish Fork"
            },
            {
              "type": "COUNTRY",
              "shortName": "USA",
              "longName": "United States"
            },
            {
              "type": "POSTAL_CODE",
              "shortName": "84660",
              "longName": "84660"
            },
            {
              "type": "STATE",
              "shortName": "UT",
              "longName": "Utah"
            }
          ],
          "formattedAddress": "1206 N. Canyon Creek Pkwy, Spanish Fork, UT 84660, USA",
          "coordinate": {
            "latitude": 40.12414,
            "longitude": -111.64027
          },
          "navCoordinate": {
            "latitude": 40.12414,
            "longitude": -111.64027
          }
        },
        "distance": 0,
        "driveDetails": null,
        "chargingStation": {
          "network": "Electrify America",
          "networkId": "10027",
          "maxKw": 150,
          "note": "",
          "chargers": [
            {
              "locationId": "US-EAN-L121757",
              "pluginDependency": "AFTER",
              "connectors": [
                {
                  "id": "US-EAN-P121757:5:1",
                  "evseId": "US-EAN-E121757:5",
                  "evseUid": "EAN121762",
                  "name": "Walmart 4068 - Spanish Fork, UT",
                  "level": "DCFC",
                  "maxKw": 150,
                  "chargingPrice": {
                    "level": null,
                    "description": "Check Electrify America’s app or the charger display for energy price and fees.",
                    "amount": 1,
                    "currency": "USD",
                    "lastUpdateTime": null,
                    "symbol": "*",
                    "type": null,
                    "unit": null
                  },
                  "type": "CCS",
                  "free": false,
                  "vend": "PAID",
                  "state": "UNKNOWN"
                },
                {
                  "id": "US-EAN-P121757:6:1",
                  "evseId": "US-EAN-E121757:6",
                  "evseUid": "EAN121763",
                  "name": "Walmart 4068 - Spanish Fork, UT",
                  "level": "DCFC",
                  "maxKw": 150,
                  "chargingPrice": {
                    "level": null,
                    "description": "Check Electrify America’s app or the charger display for energy price and fees.",
                    "amount": 1,
                    "currency": "USD",
                    "lastUpdateTime": null,
                    "symbol": "*",
                    "type": null,
                    "unit": null
                  },
                  "type": "CCS",
                  "free": false,
                  "vend": "PAID",
                  "state": "UNKNOWN"
                },
                {
                  "id": "US-EAN-P121757:7:1",
                  "evseId": "US-EAN-E121757:7",
                  "evseUid": "EAN121764",
                  "name": "Walmart 4068 - Spanish Fork, UT",
                  "level": "DCFC",
                  "maxKw": 150,
                  "chargingPrice": {
                    "level": null,
                    "description": "Check Electrify America’s app or the charger display for energy price and fees.",
                    "amount": 1,
                    "currency": "USD",
                    "lastUpdateTime": null,
                    "symbol": "*",
                    "type": null,
                    "unit": null
                  },
                  "type": "CCS",
                  "free": false,
                  "vend": "PAID",
                  "state": "UNKNOWN"
                },
                {
                  "id": "US-EAN-P121757:8:1",
                  "evseId": "US-EAN-E121757:8",
                  "evseUid": "EAN121765",
                  "name": "Walmart 4068 - Spanish Fork, UT",
                  "level": "DCFC",
                  "maxKw": 150,
                  "chargingPrice": {
                    "level": null,
                    "description": "Check Electrify America’s app or the charger display for energy price and fees.",
                    "amount": 1,
                    "currency": "USD",
                    "lastUpdateTime": null,
                    "symbol": "*",
                    "type": null,
                    "unit": null
                  },
                  "type": "CCS",
                  "free": false,
                  "vend": "PAID",
                  "state": "UNKNOWN"
                }
              ]
            }
          ],
          "operatingHours": {
            "alwaysOpen": true,
            "hours": [
              {
                "close": 86400,
                "day": "SUNDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "MONDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "TUESDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "WEDNESDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "THURSDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "FRIDAY",
                "open": 0
              },
              {
                "close": 86400,
                "day": "SATURDAY",
                "open": 0
              }
            ]
          }
        },
        "adapterRequired": false
      }
    ]
  }
}
```
