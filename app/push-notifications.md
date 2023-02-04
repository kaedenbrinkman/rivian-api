---
title: RegisterPushNotificationToken
parent: App API
has_children: false
nav_order: 3
---

# RegisterPushNotificationToken

## Overview

The `RegisterPushNotificationToken` endpoint registers a push notification token for your account.

`POST https://rivian.com/api/gql/gateway/graphql`

### Request Body

```json
{
  "operationName": "RegisterPushNotificationToken",
  "variables": {
    "data": {
      "locale": "en_US",
      "token": <your-push-token>,
      "type": "FCM",
      "userId": <your-user-id>
    }
  },
  "query": "mutation RegisterPushNotificationToken($data: RegistrationInput!) { registerPushNotificationToken(data: $data) { __typename deviceTokenId locale success token } }"
}
```

### Example Response

```json
{
  "data": {
    "registerPushNotificationToken": {
      "__typename": "RegistrationResponse",
      "deviceTokenId": <your-device-token-id>,
      "locale": "en_US",
      "success": true,
      "token": <your-push-token>
    }
  }
}
```
