---
title: updateWallbox
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 4
---

# updateWallbox

## Overview

The `updateWallbox` endpoint allows you to rename your wallbox.

`POST https://rivian.com/api/gql/chrg/user/graphql`

### Request Body

```json
{
  "operationName": "updateWallbox",
  "variables": {
    "wallboxId": <your-wallbox-id>,
    "name": <new-name>
  },
  "query": "mutation updateWallbox($wallboxId: String!, $wifiId: String, $name: String, $latitude: String, $longitude: String) { updateWallbox(wallboxId: $wallboxId, wifiId: $wifiId, name: $name, latitude: $latitude, longitude: $longitude) { wallboxId userId wifiId name linked latitude longitude chargingStatus power currentVoltage currentAmps softwareVersion model serialNumber maxPower maxVoltage maxAmps } }"
}
```

### Example Response

```json
{
  "data": {
    "updateWallbox": {
      "wallboxId": <your-wallbox-id>,
      "userId": <your-user-id>,
      "wifiId": <your-wifi-ssid>
      "name": <new-name>,
      "linked": true,
      "latitude": <your-wallbox-lat>,
      "longitude": <your-wallbox-lon>,
      "chargingStatus": "AVAILABLE",
      "power": null,
      "currentVoltage": null,
      "currentAmps": null,
      "softwareVersion": "V03.01.49",
      "model": "W1-1113-3RV7",
      "serialNumber": <your-wallbox-serial>,
      "maxPower": "11000",
      "maxVoltage": "224.0",
      "maxAmps": null
    }
  }
}
```
