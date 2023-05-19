---
title: getCompletedSessionSummaries
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 4
---

# getCompletedSessionSummaries

## Overview

The `getCompletedSessionSummaries` endpoint shows a summary of your past charging sessions.

`POST https://rivian.com/api/gql/chrg/user/graphql`

### Request Body

```json
{
  "operationName": "getCompletedSessionSummaries",
  "variables": {},
  "query": "query getCompletedSessionSummaries {\n  getCompletedSessionSummaries {\n    chargerType\n    currencyCode\n    paidTotal\n    startInstant\n    endInstant\n    totalEnergyKwh\n    rangeAddedKm\n    city\n    transactionId\n    vehicleId\n    vehicleName\n    vendor\n    isRoamingNetwork\n    isPublic\n    isHomeCharger\n    meta {\n      transactionIdGroupingKey\n      dataSources\n    }\n  }\n}\n"
}
```

### Example Response

```json
{
  "data": {
    "getCompletedSessionSummaries": [
      {
        "chargerType": "WALLBOX",
        "currencyCode": null,
        "paidTotal": null,
        "startInstant": "2022-12-14T21:35:59.222Z",
        "endInstant": "2022-12-14T23:25:49.316Z",
        "totalEnergyKwh": 11.1234,
        "rangeAddedKm": null,
        "city": <your-city>,
        "transactionId": "12345",
        "vehicleId": null,
        "vehicleName": null,
        "vendor": "Home",
        "isRoamingNetwork": false,
        "isPublic": false,
        "isHomeCharger": true,
        "meta": {
          "transactionIdGroupingKey": ",12345",
          "dataSources": [
            "TXN:12345"
          ]
        }
      },
      ...
    ]
  }
}
```
