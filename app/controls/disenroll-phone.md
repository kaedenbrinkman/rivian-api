---
title: DisenrollPhone
parent: Vehicle Controls
grand_parent: App API
has_children: false
nav_order: 3
---

# DisenrollPhone

## Overview

The `DisenrollPhone` endpoint is used to remove a phone key.

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
  "operationName": "DisenrollPhone",
  "variables": {
    "attrs": {
      "enrollmentId": <phone-id-to-disenroll>
    }
  },
  "query": "mutation DisenrollPhone($attrs: DisenrollPhoneAttributes!) { disenrollPhone(attrs: $attrs) { __typename success } }"
}
```

### Example Response

```json
{
  "data": {
    "disenrollPhone": {
      "__typename": "DisenrollPhoneResponse",
      "success": true
    }
  }
}
```
