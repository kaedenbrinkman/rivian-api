---
title: delivery
parent: App API
has_children: false
nav_order: 3
---

# delivery

## Overview

The `delivery` endpoint returns details on the delivery status of a vehicle order.

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
  "operationName": "delivery",
  "variables": {
    "orderId": <your-order-id>
  },
  "query": "query delivery($orderId: ID!) { delivery(orderId: $orderId) { __typename status carrier deliveryAddress { __typename addressLine1 addressLine2 city state country zipcode } appointmentDetails { __typename appointmentId startDateTime endDateTime timeZone } vehicleVIN } }"
}
```

### Example Response

```json
{
  "data": {
    "delivery": {
      "__typename": "Delivery",
      "status": "DELIVERY_ACCEPTED",
      "carrier": "RIVIAN",
      "deliveryAddress": {
        "__typename": "DeliveryAddressDetails",
        "addressLine1": <your-delivery-address>,
        "addressLine2": null,
        "city": <your-delivery-city>,
        "state": <your-delivery-state>,
        "country": <your-delivery-country>,
        "zipcode": <your-delivery-zipcode>
      },
      "appointmentDetails": {
        "__typename": "DeliveryAppointment",
        "appointmentId": <your-delivery-appointment-id>,
        "startDateTime": <your-delivery-start-date-time>,
        "endDateTime": <your-delivery-end-date-time>,
        "timeZone": "America/Los_Angeles"
      },
      "vehicleVIN": <your-vehicle-vin>
    }
  }
}
```
