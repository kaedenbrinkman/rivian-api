---
title: Logout
parent: Account Endpoints
grand_parent: App API
has_children: false
nav_order: 10
---

# Logout

## Overview

The `Logout` mutation ends the current user session. On logout the app also deregisters push notification tokens.

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
  "operationName": "Logout",
  "variables": {},
  "query": "mutation Logout { logout { success } }"
}
```

### Example Response

```json
{
  "data": {
    "logout": {
      "success": true
    }
  }
}
```

## Related calls on logout

The app also sends these mutations before or alongside `Logout`:

- `DeregisterPushNotificationToken` — removes the FCM token for the user
- `liveNotificationDeregisterStartToken` — deregisters the live notification start token
