---
title: getRegisteredWallboxes
parent: Account Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# getRegisteredWallboxes

## Overview

The `getRegisteredWallboxes` endpoint returns the list of Rivian L2 Chargers that have been provisioned to your account.

`POST https://rivian.com/api/chrg/user/graphql`

### Request Body

```json
{
  "operationName": "getRegisteredWallboxes",
  "variables": {},
  "query": "query getRegisteredWallboxes { getRegisteredWallboxes { __typename wallboxId userId wifiId name linked latitude longitude chargingStatus power currentVoltage currentAmps softwareVersion model serialNumber maxPower maxVoltage maxAmps } }"
}
```

### Example Response

```json
{
  "data": {
    "getRegisteredWallboxes": [
      {
        "__typename": "WallboxRecord",
        "wallboxId": <your-wallbox-id>,
        "userId": <your-user-id>,
        "wifiId": <your-wifi-ssid>,
        "name": <your-wallbox-name>,
        "linked": true,
        "latitude": <your-wallbox-latitude>,
        "longitude": <your-wallbox-longitude>,
        "chargingStatus": "DISCONNECTED",
        "power": null,
        "currentVoltage": null,
        "currentAmps": null,
        "softwareVersion": "V03.01.49",
        "model": "W1-1113-3RV7",
        "serialNumber": <your-wallbox-serial-number>,
        "maxPower": "11000",
        "maxVoltage": "224.0",
        "maxAmps": null
      }
    ]
  }
}
```
