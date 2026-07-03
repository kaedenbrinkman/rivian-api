---
title: Authentication
parent: App API
has_children: false
nav_order: 1
---

# Authentication

## Overview

Authentication uses the gateway GraphQL endpoint. The app first obtains a CSRF token and app session token, then logs in with email and password. If MFA is enabled, an OTP step completes login and returns a user session token (`u-sess`).

`POST https://rivian.com/api/gql/gateway/graphql`

## Requesting a CSRF Token

A CSRF token is required before login. If the app already has valid session headers cached, it may skip this step.

### Request Body

```json
{
  "operationName": "CreateCSRFToken",
  "variables": {},
  "query": "mutation CreateCSRFToken { createCsrfToken { __typename csrfToken appSessionToken } }"
}
```

### Example Response

```json
{
  "data": {
    "createCsrfToken": {
      "__typename": "CreateCsrfTokenResponse",
      "csrfToken": "<your-csrf-token>",
      "appSessionToken": "<your-app-session-token>"
    }
  }
}
```

Use `appSessionToken` as the `a-sess` header and `csrfToken` as the `csrf-token` header on subsequent requests.

## Login

### Required Headers

```text
a-sess: <your app session token>
csrf-token: <your CSRF token>
apollographql-client-name: com.rivian.android.consumer
```

### Request Body

```json
{
  "operationName": "Login",
  "variables": {
    "email": "<your-email>",
    "password": "<your-password>"
  },
  "query": "mutation Login($email: String!, $password: String!) { login(email: $email, password: $password) { __typename ... on MobileLoginResponse { userSessionToken } ... on MobileMFALoginResponse { otpToken targetChannel { __typename ... on MfaEmailChannel { mfaId default email } ... on MfaPhoneChannel { mfaId default phone } ... on MfaAuthenticatorChannel { mfaId nickname authenticatorType default } } channels { __typename ... on MfaEmailChannel { mfaId default email } ... on MfaPhoneChannel { mfaId default phone } ... on MfaAuthenticatorChannel { mfaId nickname default } } } } }"
}
```

### Example Response (no MFA)

```json
{
  "data": {
    "login": {
      "__typename": "MobileLoginResponse",
      "userSessionToken": "<your-user-session-token>"
    }
  }
}
```

### Example Response (MFA required)

```json
{
  "data": {
    "login": {
      "__typename": "MobileMFALoginResponse",
      "otpToken": "<otp-token>",
      "targetChannel": {
        "__typename": "MfaPhoneChannel",
        "mfaId": "<mfa-id>",
        "default": true,
        "phone": "*** *** ****"
      },
      "channels": [
        {
          "__typename": "MfaPhoneChannel",
          "mfaId": "<mfa-id>",
          "default": true,
          "phone": "*** *** ****"
        }
      ]
    }
  }
}
```

## Login with OTP (MFA)

The Apollo operation name is `LoginWithOTP`, but the GraphQL mutation field is `loginWithOTPV2`.

### Required Headers

```text
a-sess: <your app session token>
csrf-token: <your CSRF token>
apollographql-client-name: com.rivian.android.consumer
```

### Request Body

```json
{
  "operationName": "LoginWithOTP",
  "variables": {
    "email": "<your-email>",
    "otpCode": "<otp-code>",
    "otpToken": "<otp-token-from-login-response>"
  },
  "query": "mutation LoginWithOTP($email: String!, $otpCode: String!, $otpToken: String!) { loginWithOTPV2(email: $email, otpCode: $otpCode, otpToken: $otpToken) { __typename ... on MobileLoginResponse { userSessionToken } } }"
}
```

### Example Response

```json
{
  "data": {
    "loginWithOTPV2": {
      "__typename": "MobileLoginResponse",
      "userSessionToken": "<your-user-session-token>"
    }
  }
}
```

Use the returned `userSessionToken` as the `u-sess` header on authenticated requests.

After login, the app calls [`CurrentUserForLogin`](/app/account/current-user-for-login) to load the user profile.

## Logout

See [`Logout`](/app/account/logout).
