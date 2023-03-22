---
title: EnrollPhone
parent: App API
has_children: false
nav_order: 3
---

# EnrollPhone

## Overview

The `EnrollPhone` endpoint is used to set up a new phone key. Only 2 phones can be enrolled at a time.

For more information on BLE commands, see [BLE API](/ble/).

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
```

### Request Body

```json
{
  "operationName": "EnrollPhone",
  "variables": {
    "attrs": {
      "userId": <your-user-id>,
      "vehicleId": <your-vehicle-id>,
      "publicKey": <your-phone-public-key>,
      "type": <your-phone-model>,
      "name": <your-phone-name>
    }
  },
  "query": "mutation EnrollPhone($attrs: EnrollPhoneAttributes!) { enrollPhone(attrs: $attrs) { __typename success } }"
}
```

### Example Response

```json
{
  "data": {
    "enrollPhone": {
      "__typename": "EnrollPhoneResponse",
      "success": true
    }
  }
}
```
