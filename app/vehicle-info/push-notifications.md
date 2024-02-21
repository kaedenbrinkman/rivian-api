---
title: RegisterPushNotificationToken
parent: Vehicle Info Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# RegisterPushNotificationToken

## Overview

The `RegisterPushNotificationToken` endpoint registers a push notification token for your account.

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
  "operationName": "RegisterPushNotificationToken",
  "variables": {
    "data": {
      "locale": "en_US",
      "token": <your-push-token>,
      "type": "FCM",
      "userId": <your-user-id>,
      "mobileApp": "CONSUMER_RELEASE"
    }
  },
  "query": "mutation RegisterPushNotificationToken($data: RegistrationInput!) { registerPushNotificationToken(data: $data) { deviceTokenId locale success token } }"
}
```

### Example Response

```json
{
  "data": {
    "registerPushNotificationToken": {
      "deviceTokenId": <your-device-token-id>,
      "locale": "en_US",
      "success": true,
      "token": <your-push-token>
    }
  }
}
```
