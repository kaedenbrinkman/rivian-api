---
title: paymentMethods
parent: Account Endpoints
has_children: false
nav_order: 3
---

# paymentMethods

## Overview

The `paymentMethods` endpoint returns user payment methods.

`POST https://rivian.com/api/gql/orders/graphql`

### Request Body

```json
{
  "operationName": "paymentMethods",
  "variables": {},
  "query": "query paymentMethods { paymentMethods { id type default card { lastFour brand expiration postalCode } } }"
}
```

### Example Response

```json
{
  "data": {
    "paymentMethods": [
      {
        "id": "<payment id>",
        "type": "CREDIT_CARD",
        "default": true,
        "card": {
          "lastFour": "<your-cc-last-4>",
          "brand": "<your-cc-type>",
          "expiration": "MM/YY",
          "postalCode": "<your-zipcode>"
        }
      }
    ]
  }
}
```
