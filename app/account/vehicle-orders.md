---
title: vehicleOrders
parent: Account Endpoints
has_children: false
nav_order: 3
---

# vehicleOrders

## Overview

The `vehicleOrders` endpoint returns the list of vehicles you have on order.

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
  "operationName": "vehicleOrders",
  "variables": {},
  "query": "query vehicleOrders { orders(input: {orderTypes: [PRE_ORDER, VEHICLE], pageInfo: {from: 0, size: 10000}}) { __typename data { __typename id state configurationStatus fulfillmentSummaryStatus items { __typename sku } consumerStatuses { __typename isConsumerFlowComplete } } } }"
}
```

### Example Response

```json
{
  "data": {
    "orders": {
      "__typename": "OrderSearch",
      "data": [
        {
          "__typename": "Order",
          "id": <your-order-id>,
          "state": "ORDERED",
          "configurationStatus": "SOFT_LOCKED",
          "fulfillmentSummaryStatus": "VEHICLE_DELIVERED",
          "items": [
            {
              "__typename": "OrderItem",
              "sku": <wallbox-model>
            },
            {
              "__typename": "OrderItem",
              "sku": <vehicle-model>
            }
          ],
          "consumerStatuses": {
            "__typename": "ConsumerVehicleStatuses",
            "isConsumerFlowComplete": true
          }
        }
      ]
    }
  }
}
```
