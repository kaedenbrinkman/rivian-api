---
title: CheckByRivianId
parent: Charging Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# CheckByRivianId

## Overview

The `CheckByRivianId` shows third-party accounts linked to your Rivian account.

`POST https://rivian.com/api/gql/chrg/user/graphql`

### Request Body

```json
{
  "operationName": "CheckByRivianId",
  "variables": {},
  "query": "query CheckByRivianId { chargepoint { checkByRivianId } }"
}
```

### Example Response

```json
{
  "data": {
    "chargepoint": {
      "checkByRivianId": true
    }
  }
}
```
