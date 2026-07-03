---
title: User PIN
parent: Account Endpoints
grand_parent: App API
has_children: false
nav_order: 9
---

# User PIN

## Overview

The user PIN locks your driver profile on the vehicle. When enabled, personal in-cabin services — Rivian Assistant, Google Calendar, media apps, and similar profile-linked apps — cannot be used by other drivers unless they enter your PIN or have your digital key present.

PIN settings are managed in the mobile app via five GraphQL operations on the gateway endpoint.

Typical flow observed in the mobile app:

1. **`GetUserPinAuth`** — read PIN lock settings (`lock_profile`, `always_required`)
2. **`GetUserPinExists`** — check whether a PIN is set
3. **`SetUserPin`** — create or change the PIN (6-digit string)
4. **`SetPinAuth`** — update when the PIN is required (`lock_profile`, `always_required`)
5. **`DeleteUserPin`** — remove the PIN

After `SetUserPin`, `SetPinAuth`, or `DeleteUserPin`, the app re-fetches `GetUserPinAuth` and `GetUserPinExists`.

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
apollographql-client-name: com.rivian.android.consumer
```

## GetUserPinAuth

Returns PIN authentication settings for the current user.

### Request Body

```json
{
  "operationName": "GetUserPinAuth",
  "variables": {},
  "query": "query GetUserPinAuth { currentUser { settings { pinAuth { lock_profile always_required timestamp } } } }"
}
```

### Example Response

```json
{
  "data": {
    "currentUser": {
      "settings": {
        "pinAuth": {
          "lock_profile": true,
          "always_required": false,
          "timestamp": 1700000000000
        }
      }
    }
  }
}
```

| Field | Description |
|-------|-------------|
| `lock_profile` | When `true`, the in-vehicle driver profile is locked behind the PIN (or digital key) |
| `always_required` | When `true`, the PIN is required even when a digital key is present |
| `timestamp` | Last update time (epoch ms) |

## GetUserPinExists

Returns whether the account has a PIN configured.

### Request Body

```json
{
  "operationName": "GetUserPinExists",
  "variables": {},
  "query": "query GetUserPinExists { userPinExists }"
}
```

### Example Response

```json
{
  "data": {
    "userPinExists": true
  }
}
```

## SetUserPin

Creates or updates the 6-digit PIN entered on the vehicle to unlock your driver profile.

### Request Body

```json
{
  "operationName": "SetUserPin",
  "variables": {
    "pin": "<6-digit-pin>"
  },
  "query": "mutation SetUserPin($pin: String!) { setUserPin(pin: $pin) }"
}
```

### Example Response

```json
{
  "data": {
    "setUserPin": true
  }
}
```

## SetPinAuth

Updates profile lock settings without changing the PIN itself.

### Request Body

```json
{
  "operationName": "SetPinAuth",
  "variables": {
    "lock_profile": true,
    "always_required": false
  },
  "query": "mutation SetPinAuth($lock_profile: Boolean!, $always_required: Boolean!) { setPinAuth(lock_profile: $lock_profile, always_required: $always_required) }"
}
```

### Example Response

```json
{
  "data": {
    "setPinAuth": true
  }
}
```

## DeleteUserPin

Removes the profile PIN from the account.

### Request Body

```json
{
  "operationName": "DeleteUserPin",
  "variables": {},
  "query": "mutation DeleteUserPin { deleteUserPin }"
}
```

### Example Response

```json
{
  "data": {
    "deleteUserPin": true
  }
}
```
