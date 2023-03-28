---
title: searchOrders
parent: Account Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# searchOrders

## Overview

The `searchOrders` endpoint returns a list of retail orders.

`POST https://rivian.com/api/gql/orders/graphql`

### Request Body

```json
{
  "operationName": "searchOrders",
  "variables": {
    "orderTypes": ["RETAIL"],
    "orderStates": null,
    "pageInfo": {"from": 0, "size": 5},
    "dateRange": null,
    "sortFields": {"orderDate": "DESC"}
  },
  "query": "query searchOrders($input: UserOrderSearchInput!) { searchOrders(input: $input) { total data { id type orderDate state fulfillmentSummaryStatus items { id title type sku __typename } __typename } __typename }}"
}
```

### Example Response

```json
{
  "data": {
    "searchOrders": {
      "total": 1,
      "data": [
        {
          "id": "<order-id>",
          "type": "RETAIL",
          "orderDate": "<order-date>",
          "state": "ORDERED",
          "fulfillmentSummaryStatus": null,
          "items": [
            {
              "id": "<item id>",
              "title": "Rooftop Bike Mount",
              "type": "ACCESSORIES",
              "sku": "ACERBM0001",
              "__typename": "OrderItem"
            },
            {
              "id": "<item id>",
              "title": "Cargo Cross Bars",
              "type": "ACCESSORIES",
              "sku": "ACERCSB003",
              "__typename": "OrderItem"
            }
          ],
          "__typename": "OrderSnapshot"
        }
      ],
      "__typename": "OrderSnapshotSearch"
    }
  }
}
```
