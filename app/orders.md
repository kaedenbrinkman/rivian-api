---
title: vehicleOrders
parent: App API
has_children: false
nav_order: 3
---

# vehicleOrders

## Overview

The `vehicleOrders` endpoint returns the list of vehicles you have on order.

`POST https://rivian.com/api/gql/gateway/graphql`

### Request Body

```json
{
  "operationName": "vehicleOrders",
  "variables": {},
  "query": "query vehicleOrders { orders(input: {orderTypes: [PRE_ORDER, VEHICLE], pageInfo: {from: 0, size: 10000}}) { __typename data { __typename id state fulfillmentSummaryStatus items { __typename sku } consumerStatuses { __typename isConsumerFlowComplete } } } }"
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
