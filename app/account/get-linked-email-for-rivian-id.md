---
title: getLinkedEmailForRivianId
parent: Account Endpoints
has_children: false
nav_order: 3
---

# getLinkedEmailForRivianId

## Overview

The `getLinkedEmailForRivianId` shows email addresses for third-party accounts linked to your Rivian account.

`POST https://rivian.com/api/gql/chrg/user/graphql`

### Request Body

```json
{
  "operationName": "getLinkedEmailForRivianId",
  "variables": {},
  "query": "query getLinkedEmailForRivianId { chargepoint { getLinkedEmailForRivianId { email } } }"
}
```

### Example Response

```json
{
  "data": {
    "chargepoint": {
      "getLinkedEmailForRivianId": {
        "email": "<your-email-address>"
      }
    }
  }
}
```
