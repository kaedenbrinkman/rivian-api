---
title: CurrentUser
parent: Account Endpoints
grand_parent: App API
has_children: false
nav_order: 4
---

# CurrentUser

## Overview

The `CurrentUser` query returns the logged-in user's profile and settings. It uses the same fields as [`CurrentUserForLogin`](/app/account/current-user-for-login) and is called throughout the app to refresh units, contact info, and preferences.

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
apollographql-client-name: com.rivian.android.consumer
```

### Request Body

```json
{
  "operationName": "CurrentUser",
  "variables": {},
  "query": "query CurrentUser { currentUser { __typename ...CurrentUserFields } }  fragment CurrentUserFields on User { id settings { distanceUnit { value timestamp } temperatureUnit { value timestamp } pressureUnit { value timestamp } locationSharingConsent { consent expiry timestamp } } firstName lastName email emailVerified primaryPhone { phone countryCode national formatted } address { id types line1 line2 city state postalCode country state } hasNewsletterSubscription hasSmsSubscription hasNewsletterSmsSubscription registrationChannels { type } }"
}
```

### Example Response

```json
{
  "data": {
    "currentUser": {
      "__typename": "User",
      "id": "<your-user-id>",
      "settings": {
        "distanceUnit": { "value": "Imperial", "timestamp": 1700000000000 },
        "temperatureUnit": { "value": "Fahrenheit", "timestamp": 1700000000000 },
        "pressureUnit": { "value": "Psi", "timestamp": 1700000000000 },
        "locationSharingConsent": { "consent": true, "expiry": null, "timestamp": 1700000000000 }
      },
      "firstName": "<first-name>",
      "lastName": "<last-name>",
      "email": "<email>",
      "emailVerified": true,
      "primaryPhone": {
        "phone": "<phone>",
        "countryCode": "US",
        "national": "<formatted-national>",
        "formatted": "<formatted-international>"
      },
      "address": {
        "id": "<address-id>",
        "types": ["PRIMARY"],
        "line1": "<street>",
        "line2": "",
        "city": "<city>",
        "state": "<state>",
        "postalCode": "<postal-code>",
        "country": "US"
      },
      "hasNewsletterSubscription": true,
      "hasSmsSubscription": true,
      "hasNewsletterSmsSubscription": false,
      "registrationChannels": [{ "type": "TEXT" }]
    }
  }
}
```
