---
title: GetProvisionedCampSpeakers
parent: App API
has_children: false
nav_order: 3
---

# GetProvisionedCampSpeakers

## Overview

The `GetProvisionedCampSpeakers` endpoint returns the list of camp speakers that have been provisioned to your account.

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token from the previous request>
```

### Request Body

```json
{
  "operationName": "GetProvisionedCampSpeakers",
  "variables": {},
  "query": "query GetProvisionedCampSpeakers { currentUser { __typename vehicles { __typename id connectedProducts { __typename ... on CampSpeaker { serialNumber id } } } } }"
}
```

### Example Response

```json
{
  "data": {
    "currentUser": {
      "__typename": "User",
      "vehicles": [
        {
          "__typename": "UserVehicle",
          "id": <your-vehicle-id>,
          "connectedProducts": [
            {
              "__typename": "CampSpeaker",
              "serialNumber": <your-camp-speaker-sn>
              "id": <your-camp-speaker-id>
            }
          ]
        }
      ]
    }
  }
}
```
