---
title: Get Non Rivian User Session
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 3
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
         "chargerId":"USCPIL13538041",
         "transactionId":"USCPI2218433371",
         "isRivianCharger":false,
         "vehicleChargerState":{
            "value":"charging_active",
            "updatedAt":"2023-06-08T01:49:28.899Z"
         }
      }
   }
}
```
