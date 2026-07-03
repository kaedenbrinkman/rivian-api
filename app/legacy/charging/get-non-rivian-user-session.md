---
title: Get Non Rivian User Session
parent: Charging
grand_parent: Legacy
great_grand_parent: App API
has_children: false
nav_order: 6
---

# Non Rivian User Session

# getNonRivianUserSession

## Overview

The `getNonRivianUserSession` gets current non-Rivian charging session information

`POST https://rivian.com/api/gql/chrg/user/graphql`

### Request Body

```json
{
  "operationName": "getNonRivianUserSession",
  "variables": {},
  "query": "query getNonRivianUserSession \n{ getNonRivianUserSession { chargerId transactionId isRivianCharger vehicleChargerState { value updatedAt } } }"
}
```

### Example Response

```json
{
   "data":{
      "getNonRivianUserSession":{
         "chargerId":"USCPIL24649152",
         "transactionId":"USCPI3329544482",
         "isRivianCharger":false,
         "vehicleChargerState":{
            "value":"charging_active",
            "updatedAt":"2023-01-15T12:05:00.000Z"
         }
      }
   }
}
```
