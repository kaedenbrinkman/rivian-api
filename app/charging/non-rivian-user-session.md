---
title: getNonRivianUserSession
parent: Charging Endpoints
has_children: false
nav_order: 3
---

# getNonRivianUserSession

## Overview

The `getNonRivianUserSession` endpoint returns information about non-Rivian charging sessions.

`POST https://rivian.com/api/gql/chrg/user/graphql/`

### Request Body

```json
{
  "operationName": "getNonRivianUserSession",
  "variables": {},
  "query": "query getNonRivianUserSession { getNonRivianUserSession { __typename chargerId transactionId isRivianCharger vehicleChargerState { __typename value updatedAt } } }"
}
```

### Example Response

```json
{
  "data": {
    "getNonRivianUserSession": {
      "__typename": "NonRivianUserSessionData",
      "chargerId": null,
      "transactionId": null,
      "isRivianCharger": false,
      "vehicleChargerState": {
        "__typename": "StringValueRecord",
        "value": "charging_ready",
        "updatedAt": ""
      }
    }
  }
}
```
