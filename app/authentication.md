---
title: Authentication
parent: App API
has_children: false
nav_order: 3
---

# Authentication

## Overview

Authentication involves requesting a CSRF token and then using that token to request an access token via your login credentials. The access token is used to authenticate all other API requests.

## Requesting a CSRF Token

A CSRF token, or cross-site request forgery token, is a token that is used to prevent cross-site request forgery attacks. For more information, see [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery).

`POST https://rivian.com/api/gql/gateway/graphql`

### Request Body

```json
{
  "operationName": "CreateCSRFToken",
  "variables": [],
  "query": "mutation CreateCSRFToken { createCsrfToken { __typename csrfToken appSessionToken } }"
}
```

### Example Response

```json
{
  "data": {
    "createCsrfToken": {
      "__typename": "CreateCsrfTokenResponse",
      "csrfToken": "<your csrf token>",
      "appSessionToken": "<your app session token>"
    }
  }
}
```

# Requesting an Access Token

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token from the previous request>
csrf-token: <your CSRF token from the previous request>
apollographql-client-name: com.rivian.android.consumer
```

### Request Body

```json
{
  "operationName": "Login",
  "variables": {
    "email": "<your email>",
    "password": "<your password>"
  },
  "query": "mutation Login($email: String!, $password: String!) { login(email: $email, password: $password) { __typename ... on MobileLoginResponse { accessToken refreshToken userSessionToken } ... on MobileMFALoginResponse { otpToken } } }"
}
```

### Example Response

```json
{
  "data": {
    "loginWithOTP": {
      "__typename": "MobileLoginResponse",
      "accessToken": <your access token>,
      "refreshToken": <your refresh token>,
      "userSessionToken": <your user session token>
    }
  }
}
```

### Example Response (MFA)

```json
{
  "data": {
    "login": {
      "__typename": "MobileMFALoginResponse",
      "otpToken": <some-otp-token>
    }
  }
}
```

# Requesting an Access Token (MFA)

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token from the previous request>
csrf-token: <your CSRF token from the previous request>
apollographql-client-name: com.rivian.android.consumer
```

### Request Body

```json
{
  "operationName": "LoginWithOTP",
  "variables": {
    "email": "<your email>",
    "otpCode": "<your otp code>",
    "otpToken": "<otp token>"
  },
  "query": "mutation LoginWithOTP($email: String!, $otpCode: String!, $otpToken: String!) { loginWithOTP(email: $email, otpCode: $otpCode, otpToken: $otpToken) { __typename accessToken refreshToken userSessionToken } }"
}
```

### Example Response
```json
{
  "data": {
    "loginWithOTP": {
      "__typename": "MobileLoginResponse",
      "accessToken": <your access token>,
      "refreshToken": <your refresh token>,
      "userSessionToken": <your user session token>
    }
  }
}
```