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
  "query": "query user { user { email { email } phone { formatted } firstName lastName addresses { id type line1 line2 city state country postalCode } newsletterSubscription smsSubscription registrationChannels2FA userId vehicles {id highestPriorityRole __typename } invites (filterStates: [PENDING]) {id inviteState vehicleModel vehicleId creatorFirstName} orderSnapshots(filterTypes: [PRE_ORDER, VEHICLE, RETAIL]) { ...OrderSnapshotsFragment } }} fragment OrderSnapshotsFragment on OrderSnapshot { id total paidTotal subtotal state configurationStatus currency orderDate type fulfillmentSummaryStatus }"
}
```

### Example Response

```json
{
  "data": {
    "user": {
      "email": {
        "email": "<your-email-address>"
      },
      "phone": {
        "formatted": "<your-phone-number>"
      },
      "firstName": "<your-first-name>",
      "lastName": "<your-last-name>",
      "addresses": [
        {
          "id": "<address id>",
          "type": [
            "PRIMARY",
            "SHIPPING"
          ],
          "line1": "<your-street-address>",
          "line2": "",
          "city": "<your-city>",
          "state": "<your-state>",
          "country": "<your-country>",
          "postalCode": "<your-zip>"
        }
      ],
      "newsletterSubscription": true,
      "smsSubscription": true,
      "registrationChannels2FA": {
        "TEXT": true
      },
      "userId": "<your-user-id>",
      "vehicles": [],
      "invites": [],
      "orderSnapshots": [
        {
          "id": "<order id>",
          "total": 97114.69,
          "paidTotal": 10999.69,
          "subtotal": 89250,
          "state": "ORDERED",
          "configurationStatus": "SOFT_LOCKED",
          "currency": "USD",
          "orderDate": "<order date>",
          "type": "VEHICLE",
          "fulfillmentSummaryStatus": "READY_FOR_FULFILLMENT",
          "__typename": "OrderSnapshot"
        },
        {
          "id": "<order id>",
          "total": 796.88,
          "paidTotal": 796.88,
          "subtotal": 750,
          "state": "ORDERED",
          "configurationStatus": null,
          "currency": "USD",
          "orderDate": "<order date>",
          "type": "RETAIL",
          "fulfillmentSummaryStatus": null,
          "__typename": "OrderSnapshot"
        }
      ]
    }
  }
}
```
