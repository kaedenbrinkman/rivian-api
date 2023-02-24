---
title: user
parent: App API
has_children: false
nav_order: 3
---

# getUserInfo

## Overview

The `user` endpoint returns information about the user's account for orders.

`POST https://rivian.com/api/gql/orders/graphql`

### Request Body

```json
{
  "operationName": "user",
  "variables": {},
  "query": "query user { user { email { email } phone { formatted } firstName lastName addresses { id type line1 line2 city state country postalCode } } }"
}
```

### Example Response

```json
{
  "data": {
    "user": {
      "email": {
        "email": "<your-email>"
      },
      "phone": {
        "formatted": "<your-phone>"
      },
      "firstName": "<your-first-name>",
      "lastName": "<your-last-name>",
      "addresses": [
        {
          "id": "<your-address-id>",
          "type": [
            "PRIMARY",
            "SHIPPING"
          ],
          "line1": "<your-street-address>",
          "line2": "",
          "city": "<your-city>",
          "state": "<your-state",
          "country": "<your-country",
          "postalCode": "<your-zip>"
        }
      ]
    }
  }
}
```
