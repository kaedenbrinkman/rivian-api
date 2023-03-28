---
title: getWallboxStatus
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# getWallboxStatus

## Overview

The `getWallboxStatus` endpoint returns information about the status of a wallbox. Currently this information is the same as what is returned by `getRegisteredWallboxes`.

`POST https://rivian.com/api/gql/chrg/user/graphql/`

### Request Body

```json
{
  "operationName": "getWallboxStatus",
  "variables": {
    "wallboxId": <your-wallbox-id>
  },
  "query": "query getWallboxStatus($wallboxId: String!) { getWallboxStatus(wallboxId: $wallboxId) { __typename wallboxId userId wifiId name linked latitude longitude chargingStatus power currentVoltage currentAmps softwareVersion model serialNumber maxPower maxVoltage maxAmps } }"
}
```

### Example Response

```json
{
  "data": {
    "getWallboxStatus": {
      "__typename": "WallboxRecord",
      "wallboxId": <your-wallbox-id>,
      "userId": <your-user-ud>,
      "wifiId": <your-wifi-ssid>,
      "name": <your-wallbox-name>,
      "linked": true,
      "latitude": <your-wallbox-latitude>,
      "longitude": <your-wallbox-longitude>,
      "chargingStatus": "AVAILABLE",
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
  }
}
```
